#!/usr/bin/env python3
"""Validate the curated venue-discovery registry."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path


REQUIRED_COLUMNS = {
    "registry_version",
    "venue_registry_id",
    "venue_name",
    "primary_lane",
    "secondary_lanes",
    "priority_group",
    "disciplinary_fit",
    "geographic_scope",
    "topic_triggers",
    "coverage_mode",
    "metadata_status",
    "metadata_verified_at",
    "metadata_source",
    "jcr_status",
    "jcr_edition",
    "jcr_categories",
    "jcr_quartiles",
    "jcr_verified_at",
    "jcr_source_or_export",
    "active",
    "notes",
}
LANES = {
    "lane_a_disciplinary_core",
    "lane_b_adjacent",
    "lane_c_regional_underindexed",
}
JCR_STATUSES = {
    "verified",
    "verification_required",
    "not_applicable",
    "not_ranked",
}
CORE_GROUP = "core_economic_history_10"
REQUIRED_DISTINCT_TITLES = {
    "Revista de Historia Económica - Journal of Iberian and Latin American Economic History",
    "Journal of Iberian and Latin American Studies",
}
EXCLUDED_GENERIC_TITLES = {
    "Business History",
    "Business History Review",
    "Enterprise & Society",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", type=Path)
    return parser.parse_args()


def value(row: dict[str, str], field: str) -> str:
    return (row.get(field) or "").strip()


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    warnings: list[str] = []

    with args.registry.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        headers = set(reader.fieldnames or [])
        rows = list(reader)

    missing = sorted(REQUIRED_COLUMNS - headers)
    if missing:
        errors.append(f"missing columns: {', '.join(missing)}")

    identifiers = Counter(value(row, "venue_registry_id") for row in rows)
    names = Counter(value(row, "venue_name") for row in rows)
    for label, counts in (("venue_registry_id", identifiers), ("venue_name", names)):
        for item, count in counts.items():
            if not item:
                errors.append(f"blank {label}")
            elif count > 1:
                errors.append(f"duplicate {label}: {item!r}")

    active_rows = [row for row in rows if value(row, "active").lower() == "true"]
    invalid_active = [
        value(row, "venue_registry_id")
        for row in rows
        if value(row, "active").lower() not in {"true", "false"}
    ]
    if invalid_active:
        errors.append(f"invalid active flag: {', '.join(invalid_active)}")

    core_rows = [
        row for row in active_rows if value(row, "priority_group") == CORE_GROUP
    ]
    if len(core_rows) != 10:
        errors.append(f"{CORE_GROUP} must contain 10 active venues, found {len(core_rows)}")
    if any(value(row, "primary_lane") != "lane_a_disciplinary_core" for row in core_rows):
        errors.append(f"every {CORE_GROUP} venue must have lane A as primary lane")

    active_names = {value(row, "venue_name") for row in active_rows}
    missing_titles = sorted(REQUIRED_DISTINCT_TITLES - active_names)
    if missing_titles:
        errors.append(f"missing required distinct titles: {', '.join(missing_titles)}")
    prohibited = sorted(EXCLUDED_GENERIC_TITLES & active_names)
    if prohibited:
        errors.append(f"business-history titles in generic registry: {', '.join(prohibited)}")

    for number, row in enumerate(rows, start=2):
        venue_id = value(row, "venue_registry_id") or f"row {number}"
        primary_lane = value(row, "primary_lane")
        if primary_lane not in LANES:
            errors.append(f"{venue_id}: invalid primary_lane {primary_lane!r}")
        for lane in filter(None, value(row, "secondary_lanes").split(";")):
            if lane not in LANES:
                errors.append(f"{venue_id}: invalid secondary lane {lane!r}")
        jcr_status = value(row, "jcr_status")
        if jcr_status not in JCR_STATUSES:
            errors.append(f"{venue_id}: invalid jcr_status {jcr_status!r}")
        if jcr_status == "verified":
            required_jcr = (
                "jcr_edition",
                "jcr_categories",
                "jcr_quartiles",
                "jcr_verified_at",
                "jcr_source_or_export",
            )
            absent = [field for field in required_jcr if not value(row, field)]
            if absent:
                errors.append(
                    f"{venue_id}: verified JCR row lacks {', '.join(absent)}"
                )
        if not value(row, "topic_triggers"):
            warnings.append(f"{venue_id}: no topic triggers")

    output = {
        "registry": str(args.registry),
        "rows": len(rows),
        "active_rows": len(active_rows),
        "active_core_rows": len(core_rows),
        "errors": errors,
        "warnings": warnings,
        "status": "pass" if not errors else "fail",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
