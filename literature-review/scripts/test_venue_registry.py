#!/usr/bin/env python3
"""Fixture tests for validate_venue_registry.py."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "references" / "venue-priority-registry.csv"
VALIDATOR = ROOT / "scripts" / "validate_venue_registry.py"


def run_validator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        text=True,
        capture_output=True,
        check=False,
    )


def write_rows(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    with REGISTRY.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        headers = list(reader.fieldnames or [])
        rows = list(reader)

    valid = run_validator(REGISTRY)
    if valid.returncode != 0:
        print(valid.stdout)
        raise SystemExit("curated registry failed its positive fixture")

    broken_path = ROOT / "tests" / "runtime" / "venue_registry_broken.csv"
    try:
        broken_rows = [dict(row) for row in rows]
        broken_rows[0]["venue_registry_id"] = broken_rows[1]["venue_registry_id"]
        write_rows(broken_path, headers, broken_rows)
        duplicate = run_validator(broken_path)
        duplicate_output = json.loads(duplicate.stdout)
        if duplicate.returncode == 0 or not any(
            "duplicate venue_registry_id" in error
            for error in duplicate_output["errors"]
        ):
            raise SystemExit("duplicate venue ID invariant was not enforced")

        broken_rows = [
            dict(row)
            for row in rows
            if row["venue_name"] != "Journal of Iberian and Latin American Studies"
        ]
        write_rows(broken_path, headers, broken_rows)
        missing_title = run_validator(broken_path)
        missing_output = json.loads(missing_title.stdout)
        if missing_title.returncode == 0 or not any(
            "missing required distinct titles" in error
            for error in missing_output["errors"]
        ):
            raise SystemExit("distinct Ibero-American title invariant was not enforced")
    finally:
        broken_path.unlink(missing_ok=True)

    print("venue registry fixture tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
