#!/usr/bin/env python3
"""Reproducible OpenAlex discovery for literature-review search logs.

Uses only the Python standard library. The API key is read from
OPENALEX_API_KEY and is never written to output.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path


BASE_URL = "https://api.openalex.org/works"
SELECT_FIELDS = ",".join(
    [
        "id",
        "ids",
        "doi",
        "display_name",
        "publication_year",
        "publication_date",
        "updated_date",
        "type",
        "language",
        "authorships",
        "biblio",
        "primary_location",
        "locations",
        "best_oa_location",
        "open_access",
        "abstract_inverted_index",
        "keywords",
        "topics",
        "primary_topic",
        "cited_by_count",
        "referenced_works",
        "related_works",
        "is_retracted",
    ]
)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        description="Search OpenAlex or traverse a seed work's citation network."
    )
    root.add_argument("--dry-run", action="store_true", help="Print a redacted URL only.")
    root.add_argument(
        "--batch-id",
        help="Stable search_batch_id; required for non-dry-run exports.",
    )
    root.add_argument(
        "--output",
        type=Path,
        help="Write an immutable JSONL export and .meta.json sidecar.",
    )
    root.add_argument("--per-page", type=int, default=100, choices=range(1, 101))
    root.add_argument("--pages", type=int, default=1, help="Number of pages to request.")

    sub = root.add_subparsers(dest="command", required=True)

    search = sub.add_parser("search", help="Full-text work search.")
    search.add_argument("--query", required=True)
    search.add_argument("--from-year", type=int)
    search.add_argument("--to-year", type=int)
    search.add_argument("--language")
    search.add_argument("--type")
    search.add_argument(
        "--sort",
        default="relevance_score:desc",
        choices=["relevance_score:desc", "cited_by_count:desc", "publication_date:desc"],
    )

    for name, help_text in [
        ("references", "Works referenced by the seed."),
        ("cited-by", "Works that cite the seed."),
        ("related", "Works OpenAlex marks as related to the seed."),
    ]:
        child = sub.add_parser(name, help=help_text)
        child.add_argument("--work-id", required=True, help="OpenAlex W identifier or URL.")

    return root


def normalize_work_id(value: str) -> str:
    value = value.rstrip("/").split("/")[-1]
    if not value.startswith("W"):
        raise ValueError("work-id must be an OpenAlex W identifier or URL")
    return value


def build_params(args: argparse.Namespace, api_key: str) -> dict[str, str]:
    params: dict[str, str] = {
        "api_key": api_key,
        "per_page": str(args.per_page),
        "select": SELECT_FIELDS,
    }
    filters: list[str] = []

    if args.command == "search":
        params["search"] = args.query
        params["sort"] = args.sort
        if args.from_year:
            filters.append(f"from_publication_date:{args.from_year}-01-01")
        if args.to_year:
            filters.append(f"to_publication_date:{args.to_year}-12-31")
        if args.language:
            filters.append(f"language:{args.language}")
        if args.type:
            filters.append(f"type:{args.type}")
    else:
        work_id = normalize_work_id(args.work_id)
        if args.command == "cited-by":
            filters.append(f"cites:{work_id}")
        elif args.command in {"references", "related"}:
            pass
        else:
            raise ValueError(f"unsupported command: {args.command}")

    if filters:
        params["filter"] = ",".join(filters)
    return params


def related_ids(seed: dict) -> list[str]:
    return [normalize_work_id(item) for item in seed.get("related_works", [])]


def referenced_ids(seed: dict) -> list[str]:
    return [normalize_work_id(item) for item in seed.get("referenced_works", [])]


def request_json(url: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "literature-review-skill/1.0"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def redact(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    safe = [("api_key", "REDACTED") if key == "api_key" else (key, value) for key, value in query]
    return urllib.parse.urlunsplit(
        (parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(safe), parsed.fragment)
    )


def reconstruct_abstract(inverted_index: dict | None) -> str:
    if not inverted_index:
        return ""
    positioned: list[tuple[int, str]] = []
    for token, positions in inverted_index.items():
        positioned.extend((int(position), token) for position in positions)
    return " ".join(token for _, token in sorted(positioned))


def annotate_row(
    row: dict,
    args: argparse.Namespace,
    retrieved_at: str,
) -> dict:
    abstract = reconstruct_abstract(row.get("abstract_inverted_index"))
    keywords = [
        item.get("display_name", "")
        for item in row.get("keywords", [])
        if item.get("display_name")
    ]
    enriched = dict(row)
    enriched["_review_provenance"] = {
        "search_batch_id": args.batch_id,
        "platform": "OpenAlex",
        "command": args.command,
        "query": getattr(args, "query", ""),
        "trigger_work_id": getattr(args, "work_id", ""),
        "retrieved_at": retrieved_at,
    }
    enriched["_normalized_hints"] = {
        "abstract": abstract,
        "abstract_status": "provided" if abstract else "verified_absent",
        "author_keywords": "",
        "author_keywords_status": "not_offered_by_platform",
        "index_terms": keywords,
        "index_terms_status": "provided" if keywords else "verified_absent",
        "index_terms_provenance": "OpenAlex keywords",
    }
    return enriched


def emit(rows: list[dict], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    stream = output.open("x", encoding="utf-8", newline="\n")
    try:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    finally:
        stream.close()


def emit_metadata(metadata: dict, output: Path) -> None:
    sidecar = output.with_suffix(output.suffix + ".meta.json")
    with sidecar.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(metadata, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def main() -> int:
    args = parser().parse_args()
    if args.pages < 1:
        raise SystemExit("--pages must be at least 1")
    if not args.dry_run and not args.batch_id:
        raise SystemExit("--batch-id is required for an executed export.")
    if not args.dry_run and not args.output:
        raise SystemExit("--output is required for an executed immutable export.")
    if args.output and args.output.exists():
        raise SystemExit(f"Refusing to overwrite raw export: {args.output}")
    if args.output:
        sidecar = args.output.with_suffix(args.output.suffix + ".meta.json")
        if sidecar.exists():
            raise SystemExit(f"Refusing to overwrite metadata sidecar: {sidecar}")

    api_key = os.environ.get("OPENALEX_API_KEY", "")
    if not api_key and not args.dry_run:
        raise SystemExit("Set OPENALEX_API_KEY or use --dry-run.")

    params = build_params(args, api_key or "REDACTED")
    base_url = BASE_URL

    if args.command in {"references", "related"}:
        seed_url = f"{BASE_URL}/{normalize_work_id(args.work_id)}?" + urllib.parse.urlencode(
            {
                "api_key": api_key or "REDACTED",
                "select": "id,referenced_works,related_works",
            }
        )
        if args.dry_run:
            print(redact(seed_url))
            field = "referenced_works" if args.command == "references" else "related_works"
            print(f"Then batch-fetch IDs returned in {field} using filter=openalex:W1|W2|...")
            return 0
        seed = request_json(seed_url)
        ids = referenced_ids(seed) if args.command == "references" else related_ids(seed)
        if not ids:
            retrieved_at = dt.datetime.now(dt.timezone.utc).isoformat()
            emit([], args.output)
            emit_metadata(
                {
                    "search_batch_id": args.batch_id,
                    "platform": "OpenAlex",
                    "command": args.command,
                    "trigger_work_id": normalize_work_id(args.work_id),
                    "retrieved_at": retrieved_at,
                    "results_returned": 0,
                    "results_exported": 0,
                },
                args.output,
            )
            return 0

    first_url = base_url + "?" + urllib.parse.urlencode(params)
    if args.dry_run:
        print(redact(first_url))
        return 0

    rows: list[dict] = []
    results_returned = 0
    retrieved_at = dt.datetime.now(dt.timezone.utc).isoformat()
    if args.command in {"references", "related"}:
        results_returned = len(ids)
        for start in range(0, len(ids), 100):
            chunk_params = dict(params)
            chunk_params["filter"] = "openalex:" + "|".join(ids[start : start + 100])
            chunk_params["per_page"] = "100"
            payload = request_json(base_url + "?" + urllib.parse.urlencode(chunk_params))
            rows.extend(payload.get("results", []))
    else:
        cursor = "*"
        for page_number in range(args.pages):
            page_params = dict(params)
            page_params["cursor"] = cursor
            url = base_url + "?" + urllib.parse.urlencode(page_params)
            payload = request_json(url)
            if page_number == 0:
                results_returned = int(payload.get("meta", {}).get("count", 0))
            rows.extend(payload.get("results", []))
            cursor = payload.get("meta", {}).get("next_cursor")
            if not cursor:
                break

    enriched_rows = [annotate_row(row, args, retrieved_at) for row in rows]
    emit(enriched_rows, args.output)
    emit_metadata(
        {
            "search_batch_id": args.batch_id,
            "platform": "OpenAlex",
            "command": args.command,
            "query": getattr(args, "query", ""),
            "trigger_work_id": getattr(args, "work_id", ""),
            "filters": params.get("filter", ""),
            "sort_order": params.get("sort", ""),
            "retrieved_at": retrieved_at,
            "results_returned": results_returned,
            "results_exported": len(enriched_rows),
            "pages_requested": args.pages,
            "raw_export": str(args.output),
        },
        args.output,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
