#!/usr/bin/env python3
"""Fixture tests for OpenAlex raw export, normalization hints, and traversal."""

from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "openalex_discovery.py"
RUNTIME = ROOT / "tests" / "runtime"


def load_module():
    spec = importlib.util.spec_from_file_location("openalex_discovery", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def work(work_id: str) -> dict:
    return {
        "id": f"https://openalex.org/{work_id}",
        "ids": {"openalex": f"https://openalex.org/{work_id}"},
        "doi": "https://doi.org/10.1000/fixture",
        "display_name": "Agrarian History Fixture",
        "publication_year": 2020,
        "publication_date": "2020-01-01",
        "updated_date": "2026-01-01",
        "type": "article",
        "language": "en",
        "authorships": [],
        "biblio": {},
        "primary_location": None,
        "locations": [],
        "best_oa_location": None,
        "open_access": {"is_oa": False},
        "abstract_inverted_index": {"Agrarian": [0], "history": [1]},
        "keywords": [{"display_name": "Agrarian history", "score": 0.9}],
        "topics": [],
        "primary_topic": None,
        "cited_by_count": 0,
        "referenced_works": [],
        "related_works": [],
        "is_retracted": False,
    }


def run_search(module, output: Path) -> None:
    payload = {
        "meta": {"count": 1, "next_cursor": None},
        "results": [work("W1")],
    }
    argv = [
        "openalex_discovery.py",
        "--batch-id",
        "OA_FIXTURE_SEARCH",
        "--output",
        str(output),
        "search",
        "--query",
        "agrarian history",
    ]
    with patch.object(module, "request_json", return_value=payload), patch.object(
        sys, "argv", argv
    ), patch.dict(os.environ, {"OPENALEX_API_KEY": "fixture-key"}):
        assert module.main() == 0

    row = json.loads(output.read_text(encoding="utf-8").splitlines()[0])
    assert row["_normalized_hints"]["abstract"] == "Agrarian history"
    assert row["_normalized_hints"]["abstract_status"] == "provided"
    assert row["_normalized_hints"]["author_keywords_status"] == "not_offered_by_platform"
    assert row["_normalized_hints"]["index_terms"] == ["Agrarian history"]
    metadata = json.loads(
        output.with_suffix(output.suffix + ".meta.json").read_text(encoding="utf-8")
    )
    assert metadata["results_returned"] == 1
    assert metadata["results_exported"] == 1


def run_references(module, output: Path) -> None:
    seed = {
        "id": "https://openalex.org/WSEED",
        "referenced_works": ["https://openalex.org/W2"],
        "related_works": ["https://openalex.org/W3"],
    }
    fetched = {"meta": {"count": 1}, "results": [work("W2")]}
    argv = [
        "openalex_discovery.py",
        "--batch-id",
        "OA_FIXTURE_REFS",
        "--output",
        str(output),
        "references",
        "--work-id",
        "WSEED",
    ]
    with patch.object(module, "request_json", side_effect=[seed, fetched]), patch.object(
        sys, "argv", argv
    ), patch.dict(os.environ, {"OPENALEX_API_KEY": "fixture-key"}):
        assert module.main() == 0
    metadata = json.loads(
        output.with_suffix(output.suffix + ".meta.json").read_text(encoding="utf-8")
    )
    assert metadata["command"] == "references"
    assert metadata["results_returned"] == 1
    assert metadata["results_exported"] == 1


def main() -> int:
    module = load_module()
    outputs = [RUNTIME / "openalex_search.jsonl", RUNTIME / "openalex_refs.jsonl"]
    try:
        run_search(module, outputs[0])
        run_references(module, outputs[1])
    finally:
        for output in outputs:
            output.unlink(missing_ok=True)
            output.with_suffix(output.suffix + ".meta.json").unlink(missing_ok=True)
    print("OpenAlex fixture tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
