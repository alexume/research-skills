#!/usr/bin/env python3
"""Validate literature-review artifacts against schemas and cross-file invariants."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


PDF_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*_[A-Za-z0-9][A-Za-z0-9._-]*\.pdf$")
ABSENCE_STATES = {
    "provided",
    "not_offered_by_platform",
    "pending_retrieval",
    "verified_absent",
    "access_failure",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--literature-dir", type=Path, required=True)
    parser.add_argument(
        "--profile",
        choices=("orientation", "maturation"),
        default="orientation",
    )
    parser.add_argument(
        "--allow-missing",
        action="store_true",
        help="Report missing profile artifacts as warnings instead of errors.",
    )
    return parser.parse_args()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        return list(reader.fieldnames or []), list(reader)


def value(row: dict[str, str], field: str) -> str:
    return (row.get(field) or "").strip()


def integer(raw: str, label: str, errors: list[str], allow_blank: bool = False) -> int:
    raw = raw.strip()
    if not raw and allow_blank:
        return 0
    try:
        parsed = int(raw)
    except ValueError:
        errors.append(f"{label}: expected integer, found {raw!r}")
        return 0
    if parsed < 0:
        errors.append(f"{label}: negative counts are not allowed")
    return parsed


def count_list(raw: str) -> int:
    raw = raw.strip()
    if not raw or raw == "0":
        return 0
    return len([item for item in re.split(r"[;|]", raw) if item.strip()])


def validate_headers_and_rows(
    artifact_name: str,
    spec: dict,
    headers: list[str],
    rows: list[dict[str, str]],
    errors: list[str],
) -> None:
    missing = [column for column in spec["required_columns"] if column not in headers]
    if missing:
        errors.append(f"{artifact_name}: missing columns: {', '.join(missing)}")
        return

    primary_key = spec.get("primary_key", [])
    seen: set[tuple[str, ...]] = set()
    for number, row in enumerate(rows, start=2):
        key = tuple(value(row, field) for field in primary_key)
        if any(not item for item in key):
            errors.append(f"{artifact_name}:{number}: blank primary key {primary_key}")
        elif key in seen:
            errors.append(f"{artifact_name}:{number}: duplicate primary key {key}")
        seen.add(key)

        for field, allowed in spec.get("enums", {}).items():
            current = value(row, field)
            if not current:
                continue
            if "__NONEMPTY_OTHER__" in allowed:
                continue
            if current not in allowed:
                errors.append(
                    f"{artifact_name}:{number}: {field}={current!r} not in {allowed}"
                )


def validate_metadata_states(
    rows: list[dict[str, str]], errors: list[str]
) -> None:
    pairs = (
        ("abstract", "abstract_status"),
        ("author_keywords", "author_keywords_status"),
        ("index_terms", "index_terms_status"),
    )
    for number, row in enumerate(rows, start=2):
        source_id = value(row, "source_id") or f"row {number}"
        if not value(row, "bibkey"):
            errors.append(
                f"extended_corpus.csv:{number} {source_id}: bibkey must be PENDING "
                "or a verified canonical key"
            )
        for data_field, status_field in pairs:
            data = value(row, data_field)
            status = value(row, status_field)
            if status not in ABSENCE_STATES:
                errors.append(
                    f"extended_corpus.csv:{number} {source_id}: invalid/blank "
                    f"{status_field}={status!r}"
                )
            elif status == "provided" and not data:
                errors.append(
                    f"extended_corpus.csv:{number} {source_id}: {data_field} is blank "
                    "while status is provided"
                )
            elif status != "provided" and data:
                errors.append(
                    f"extended_corpus.csv:{number} {source_id}: {data_field} has a value "
                    f"while status is {status}"
                )


def validate_query_lineage(
    batches: list[dict[str, str]],
    relations: list[dict[str, str]],
    errors: list[str],
) -> None:
    batch_ids = {value(row, "search_batch_id") for row in batches}
    reviewed_by_batch = Counter(
        value(row, "search_batch_id")
        for row in relations
        if value(row, "review_status") == "reviewed"
    )

    for number, row in enumerate(batches, start=2):
        batch_id = value(row, "search_batch_id")
        parent = value(row, "parent_batch_id")
        status = value(row, "batch_status")
        if parent != "ROOT" and parent not in batch_ids:
            errors.append(
                f"query_lineage_log.csv:{number} {batch_id}: unresolved parent {parent!r}"
            )
        if parent != "ROOT" and not value(row, "reason_for_expansion"):
            errors.append(
                f"query_lineage_log.csv:{number} {batch_id}: derived batch lacks reason"
            )
        if status != "executed":
            continue

        reviewed = integer(
            value(row, "results_reviewed"),
            f"query_lineage_log.csv:{number} {batch_id}.results_reviewed",
            errors,
        )
        exception = integer(
            value(row, "review_exception_count") or "0",
            f"query_lineage_log.csv:{number} {batch_id}.review_exception_count",
            errors,
        )
        if exception and not value(row, "review_exception_reason"):
            errors.append(
                f"query_lineage_log.csv:{number} {batch_id}: review exception lacks reason"
            )
        reconciled = reviewed_by_batch[batch_id] + exception
        if reviewed != reconciled:
            errors.append(
                f"query_lineage_log.csv:{number} {batch_id}: results_reviewed={reviewed} "
                f"but individual_reviewed={reviewed_by_batch[batch_id]} "
                f"+ exception={exception}"
            )

        returned_raw = value(row, "results_returned")
        exported_raw = value(row, "results_exported")
        if returned_raw and exported_raw:
            returned = integer(
                returned_raw,
                f"query_lineage_log.csv:{number} {batch_id}.results_returned",
                errors,
            )
            exported = integer(
                exported_raw,
                f"query_lineage_log.csv:{number} {batch_id}.results_exported",
                errors,
            )
            if exported > returned:
                errors.append(
                    f"query_lineage_log.csv:{number} {batch_id}: "
                    "results_exported exceeds results_returned"
                )


def validate_references(
    tables: dict[str, list[dict[str, str]]],
    errors: list[str],
) -> None:
    sources = {value(row, "source_id") for row in tables.get("extended_corpus.csv", [])}
    batches = {
        value(row, "search_batch_id")
        for row in tables.get("query_lineage_log.csv", [])
    }

    source_tables = (
        "source_batch_relations.csv",
        "screening_log.csv",
        "corpus_membership_log.csv",
        "analytical_corpus.csv",
        "identifier_crosswalk.csv",
        "extraction_matrix.csv",
        "paper_dataset_use.csv",
    )
    for name in source_tables:
        for number, row in enumerate(tables.get(name, []), start=2):
            source_id = value(row, "source_id")
            if source_id and source_id not in sources:
                errors.append(f"{name}:{number}: unresolved source_id {source_id!r}")

    for number, row in enumerate(
        tables.get("source_batch_relations.csv", []), start=2
    ):
        batch_id = value(row, "search_batch_id")
        if batch_id and batch_id not in batches:
            errors.append(
                f"source_batch_relations.csv:{number}: unresolved batch {batch_id!r}"
            )


def validate_crosswalk(
    rows: list[dict[str, str]], errors: list[str], warnings: list[str]
) -> None:
    bibkeys: dict[str, str] = {}
    for number, row in enumerate(rows, start=2):
        source_id = value(row, "source_id")
        bibkey = value(row, "bibkey")
        identity = value(row, "identity_status")
        filename = value(row, "pdf_filename")
        if not bibkey:
            errors.append(
                f"identifier_crosswalk.csv:{number} {source_id}: bibkey must be PENDING "
                "or a verified canonical key"
            )
            continue
        if bibkey != "PENDING":
            if identity != "verified":
                errors.append(
                    f"identifier_crosswalk.csv:{number} {source_id}: final bibkey "
                    "requires verified identity"
                )
            if bibkey in bibkeys and bibkeys[bibkey] != source_id:
                errors.append(
                    f"identifier_crosswalk.csv:{number}: bibkey {bibkey!r} reused by "
                    f"{bibkeys[bibkey]} and {source_id}"
                )
            bibkeys[bibkey] = source_id
        if filename:
            if bibkey == "PENDING":
                errors.append(
                    f"identifier_crosswalk.csv:{number} {source_id}: PDF named before "
                    "bibkey verification"
                )
            elif not filename.startswith(f"{bibkey}_") or not PDF_NAME.match(filename):
                errors.append(
                    f"identifier_crosswalk.csv:{number} {source_id}: unsafe or "
                    f"non-deterministic pdf_filename {filename!r}"
                )
        elif value(row, "pdf_path"):
            warnings.append(
                f"identifier_crosswalk.csv:{number} {source_id}: pdf_path without filename"
            )


def validate_maturation(
    tables: dict[str, list[dict[str, str]]],
    errors: list[str],
    warnings: list[str],
) -> None:
    extraction = {
        value(row, "source_id"): row
        for row in tables.get("extraction_matrix.csv", [])
    }
    for number, row in enumerate(tables.get("analytical_corpus.csv", []), start=2):
        if value(row, "current_layer") != "core_corpus":
            continue
        source_id = value(row, "source_id")
        extracted = extraction.get(source_id)
        if not extracted:
            errors.append(
                f"analytical_corpus.csv:{number} {source_id}: core source lacks extraction"
            )
        elif value(extracted, "reading_status") != "full" or value(
            extracted, "extraction_status"
        ) != "located":
            errors.append(
                f"analytical_corpus.csv:{number} {source_id}: core source is not "
                "fully read and location-extracted"
            )

    for number, row in enumerate(tables.get("debate_matrix.csv", []), start=2):
        if value(row, "maturity_status") != "reconstructed":
            continue
        if count_list(value(row, "central_sources_unread")):
            errors.append(
                f"debate_matrix.csv:{number}: reconstructed debate has central unread sources"
            )
        positions = integer(
            value(row, "position_count"),
            f"debate_matrix.csv:{number}.position_count",
            errors,
        )
        rivals = integer(
            value(row, "serious_rival_count"),
            f"debate_matrix.csv:{number}.serious_rival_count",
            errors,
        )
        if positions < 2:
            errors.append(
                f"debate_matrix.csv:{number}: reconstructed debate has <2 positions"
            )
        if rivals < 1:
            errors.append(
                f"debate_matrix.csv:{number}: reconstructed debate lacks a serious rival"
            )
        if count_list(value(row, "core_sources_full_read")) < 2:
            errors.append(
                f"debate_matrix.csv:{number}: reconstructed debate has <2 full-read core sources"
            )

    for number, row in enumerate(tables.get("network_edges.csv", []), start=2):
        if value(row, "network_type") == "argument" and not value(
            row, "evidence_basis"
        ):
            errors.append(
                f"network_edges.csv:{number}: argument edge lacks evidence_basis"
            )

    lanes_by_line: dict[str, set[str]] = defaultdict(set)
    for row in tables.get("venue_coverage.csv", []):
        if value(row, "venue_search_status") in {"partial", "completed"}:
            lanes_by_line[value(row, "research_line_id")].add(value(row, "venue_tier"))
    for line, lanes in lanes_by_line.items():
        if len(lanes) < 3:
            warnings.append(
                f"venue_coverage.csv: research line {line!r} covers {len(lanes)}/3 lanes"
            )


def main() -> int:
    args = parse_args()
    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    literature_dir = args.literature_dir
    errors: list[str] = []
    warnings: list[str] = []
    tables: dict[str, list[dict[str, str]]] = {}

    for artifact_name, spec in schema["artifacts"].items():
        required = args.profile in spec.get("profiles", [])
        path = literature_dir / artifact_name
        if not path.exists():
            if required:
                message = f"missing required {args.profile} artifact: {artifact_name}"
                (warnings if args.allow_missing else errors).append(message)
            continue
        headers, rows = read_csv(path)
        tables[artifact_name] = rows
        validate_headers_and_rows(
            artifact_name, spec, headers, rows, errors
        )
        if required and not rows:
            warnings.append(f"{artifact_name}: required artifact has no records")

    raw_results = literature_dir / "raw_results"
    if not raw_results.is_dir():
        message = "missing raw_results directory"
        (warnings if args.allow_missing else errors).append(message)

    validate_metadata_states(tables.get("extended_corpus.csv", []), errors)
    validate_query_lineage(
        tables.get("query_lineage_log.csv", []),
        tables.get("source_batch_relations.csv", []),
        errors,
    )
    validate_references(tables, errors)
    validate_crosswalk(
        tables.get("identifier_crosswalk.csv", []), errors, warnings
    )
    if args.profile == "maturation":
        validate_maturation(tables, errors, warnings)

    print(
        json.dumps(
            {
                "profile": args.profile,
                "literature_dir": str(literature_dir),
                "errors": errors,
                "warnings": warnings,
                "status": "pass" if not errors else "fail",
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
