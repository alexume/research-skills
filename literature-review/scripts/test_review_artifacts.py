#!/usr/bin/env python3
"""Small fixture tests for validate_review_artifacts.py."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "artifact-schemas.json"
VALIDATOR = ROOT / "scripts" / "validate_review_artifacts.py"


def blank_row(spec: dict) -> dict[str, str]:
    return {column: "" for column in spec["required_columns"]}


def write_table(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def run_validator(literature_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(VALIDATOR),
            "--schema",
            str(SCHEMA),
            "--literature-dir",
            str(literature_dir),
            "--profile",
            "maturation",
        ],
        text=True,
        capture_output=True,
        check=False,
    )


def build_fixture(literature_dir: Path, schema: dict) -> None:
    rows: dict[str, list[dict[str, str]]] = {}
    for name, spec in schema["artifacts"].items():
        rows[name] = [blank_row(spec)]

    rows["query_lineage_log.csv"][0].update(
        {
            "search_batch_id": "B1",
            "parent_batch_id": "ROOT",
            "batch_status": "executed",
            "discovery_track": "question_concept",
            "search_target_id": "Q1",
            "reason_for_expansion": "Initial protocol query",
            "query": "agrarian divergence",
            "platform": "Scopus",
            "executed_by": "fixture",
            "executed_at": "2026-07-23",
            "results_returned": "1",
            "results_exported": "1",
            "results_reviewed": "1",
            "review_exception_count": "0",
            "export_path": "raw_results/B1/export.csv",
            "next_action": "screen",
        }
    )
    rows["source_batch_relations.csv"][0].update(
        {
            "relation_id": "R1",
            "source_id": "SRC000001",
            "search_batch_id": "B1",
            "platform_record_id": "EID1",
            "raw_export_path": "raw_results/B1/export.csv",
            "raw_record_locator": "row:2",
            "result_rank": "1",
            "review_status": "reviewed",
            "reviewed_at": "2026-07-23",
            "screening_decision_id": "D1",
        }
    )
    rows["extended_corpus.csv"][0].update(
        {
            "source_id": "SRC000001",
            "bibkey": "Smith2020",
            "title": "Agrarian Divergence",
            "authors": "Smith, Jane",
            "year": "2020",
            "container_title": "Economic History Review",
            "container_type": "journal",
            "document_type": "article",
            "language": "English",
            "abstract": "A study of regional agricultural divergence.",
            "abstract_status": "provided",
            "abstract_provenance": "Scopus:B1",
            "author_keywords_status": "verified_absent",
            "author_keywords_provenance": "Scopus:B1",
            "index_terms": "agriculture|divergence",
            "index_terms_status": "provided",
            "index_terms_provenance": "Scopus:B1",
            "access_status": "access_verified",
            "full_text_status": "local_existing",
            "references_status": "verified_absent",
            "citations_status": "verified_absent",
            "metadata_verification_status": "verified",
            "screening_status": "analytical_in",
            "inclusion_reason": "Direct question fit",
            "provisional_review_roles": "core_empirical",
            "geographic_fit": "direct_case",
            "question_fit": "direct",
            "source_fit": "same_source_family",
            "period_fit": "direct",
            "scale_fit": "same",
            "disciplinary_tradition": "quantitative_economic_history",
            "canonical_work_id": "WORK1",
            "version_id": "V1",
            "record_origin": "platform_import",
            "record_created_at": "2026-07-23",
            "record_updated_at": "2026-07-23",
        }
    )
    rows["screening_log.csv"][0].update(
        {
            "decision_id": "D1",
            "source_id": "SRC000001",
            "screening_stage": "analytical",
            "decision": "include",
            "primary_reason": "Direct evidence",
            "decision_at": "2026-07-23",
            "decision_by": "fixture",
            "decision_evidence": "full text",
            "full_text_status": "local_existing",
            "next_action": "extract",
        }
    )
    rows["corpus_membership_log.csv"][0].update(
        {
            "membership_event_id": "M1",
            "source_id": "SRC000001",
            "from_layer": "analytical_corpus",
            "to_layer": "core_corpus",
            "decision": "promote",
            "reason": "Carries central claim",
            "evidence": "full text",
            "decided_by": "fixture",
            "decided_at": "2026-07-23",
        }
    )
    rows["analytical_corpus.csv"][0].update(
        {
            "source_id": "SRC000001",
            "bibkey": "Smith2020",
            "current_layer": "core_corpus",
            "geographic_fit": "direct_case",
            "question_fit": "direct",
            "source_fit": "same_source_family",
            "period_fit": "direct",
            "scale_fit": "same",
            "disciplinary_tradition": "quantitative_economic_history",
            "review_roles": "core_empirical",
            "debate_ids": "DEB1",
            "priority": "high",
            "priority_reason": "Central evidence",
            "full_text_status": "local_existing",
            "reading_status": "full",
            "extraction_status": "located",
            "evidence_independence_status": "independent",
        }
    )
    rows["identifier_crosswalk.csv"][0].update(
        {
            "source_id": "SRC000001",
            "bibkey": "Smith2020",
            "pdf_filename": "Smith2020_Agrarian_Divergence.pdf",
            "pdf_path": "pdf/Smith2020_Agrarian_Divergence.pdf",
            "canonical_work_id": "WORK1",
            "version_id": "V1",
            "identity_status": "verified",
            "bibkey_verified_at": "2026-07-23",
            "pdf_verified_at": "2026-07-23",
            "wiki_status": "not_candidate",
        }
    )
    rows["extraction_matrix.csv"][0].update(
        {
            "source_id": "SRC000001",
            "bibkey": "Smith2020",
            "review_role": "core_empirical",
            "geographic_fit": "direct_case",
            "question_fit": "direct",
            "source_fit": "same_source_family",
            "period_fit": "direct",
            "scale_fit": "same",
            "disciplinary_tradition": "quantitative_economic_history",
            "reading_status": "full",
            "extraction_status": "located",
            "question": "Why did regions diverge?",
            "central_claim": "Institutions mediated technology adoption.",
            "evidence_sources": "agricultural census",
            "data_or_corpus": "municipal panel",
            "method": "historical panel analysis",
            "geography": "Mexico",
            "period": "1940-1980",
            "main_finding": "Adoption varied institutionally.",
            "finding_location": "p. 25",
            "evidence_lineage_id": "LIN1",
            "evidence_independence_status": "independent",
            "canonical_work_id": "WORK1",
            "version_id": "V1",
            "dataset_ids": "DATA1",
            "debate_id": "DEB1",
            "wiki_status": "not_candidate",
            "verified_at": "2026-07-23",
        }
    )
    rows["debate_matrix.csv"][0].update(
        {
            "debate_id": "DEB1",
            "research_line": "agrarian_divergence",
            "question": "What explains regional divergence?",
            "position_id": "POS1",
            "position_claim": "Institutions mediate technology.",
            "representative_sources": "SRC000001",
            "core_sources_full_read": "SRC000001",
            "evidence_sources": "census",
            "evidence_lineages": "LIN1",
            "independent_lineage_count": "1",
            "shared_lineage_count": "0",
            "serious_rival_count": "1",
            "position_count": "1",
            "searched_traditions": "economic_history|agrarian_history",
            "searched_venue_lanes": "lane_a|lane_b|lane_c",
            "maturity_status": "developing",
        }
    )
    rows["network_edges.csv"][0].update(
        {
            "edge_id": "E1",
            "network_type": "argument",
            "from_id": "SRC000001",
            "to_id": "POS1",
            "relation_type": "supports",
            "direction": "directed",
            "evidence_source_id": "SRC000001",
            "evidence_location": "p. 25",
            "evidence_basis": "Explicit argument",
            "verification_status": "verified",
        }
    )
    rows["paper_dataset_use.csv"][0].update(
        {
            "use_id": "U1",
            "source_id": "SRC000001",
            "dataset_id": "DATA1",
            "resource_name": "Agricultural Census",
            "producer_or_custodian": "Statistical office",
            "version": "1960",
            "temporal_coverage": "1960",
            "geographic_coverage": "Mexico",
            "unit_of_analysis": "municipality",
            "role_in_study": "outcome",
            "transformation_or_linkage": "harmonized boundaries",
            "access_status": "public",
            "replication_status": "partial",
            "new_contribution": "historical linkage",
            "limitations": "boundary uncertainty",
            "evidence_independence_status": "independent",
            "verification_status": "verified",
        }
    )
    rows["data_source_candidates.csv"][0].update(
        {
            "candidate_id": "C1",
            "source_id": "SRC000001",
            "bibkey": "Smith2020",
            "dataset_id": "DATA1",
            "resource_name": "Agricultural Census",
            "resource_type": "census",
            "creator_or_custodian": "Statistical office",
            "access_status": "candidate",
            "verification_status": "verified",
            "acquisition_status": "not_requested",
            "next_skill": "research-evidence-discovery-and-acquisition",
            "next_action": "verify access",
        }
    )
    venue_rows = []
    for index, lane in enumerate(
        (
            "lane_a_disciplinary_core",
            "lane_b_adjacent",
            "lane_c_regional_underindexed",
        ),
        start=1,
    ):
        row = blank_row(schema["artifacts"]["venue_coverage.csv"])
        row.update(
            {
                "coverage_id": f"VC{index}",
                "research_line_id": "agrarian_divergence",
                "venue_registry_id": "PROJECT_SPECIFIC",
                "registry_version": "fixture-1",
                "venue_name": f"Fixture venue {index}",
                "venue_tier": lane,
                "priority_group": "fixture",
                "venue_priority_basis": "disciplinary fit",
                "jcr_status": "verification_required",
                "disciplinary_fit": "relevant",
                "years_or_issues_reviewed": "1940-1980",
                "terms_or_method": "hand search",
                "venue_search_status": "completed",
                "search_batch_ids": "B1",
                "results_added": "1",
            }
        )
        venue_rows.append(row)
    rows["venue_coverage.csv"] = venue_rows

    (literature_dir / "raw_results" / "B1").mkdir(parents=True, exist_ok=True)
    (literature_dir / "raw_results" / "B1" / "export.csv").write_text(
        "fixture\n", encoding="utf-8"
    )
    for name, spec in schema["artifacts"].items():
        write_table(
            literature_dir / name,
            spec["required_columns"],
            rows[name],
        )


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    literature_dir = ROOT / "tests" / "runtime"
    if not literature_dir.is_dir():
        raise SystemExit(f"fixture directory missing: {literature_dir}")
    try:
        build_fixture(literature_dir, schema)

        valid = run_validator(literature_dir)
        if valid.returncode != 0:
            print(valid.stdout)
            print(valid.stderr)
            raise SystemExit("valid maturation fixture failed")

        query_path = literature_dir / "query_lineage_log.csv"
        headers, query_rows = _read_table(query_path)
        query_rows[0]["results_reviewed"] = "2"
        write_table(query_path, headers, query_rows)
        broken_count = run_validator(literature_dir)
        if broken_count.returncode == 0 or "results_reviewed=2" not in broken_count.stdout:
            raise SystemExit("review-count invariant was not enforced")

        query_rows[0]["results_reviewed"] = "1"
        write_table(query_path, headers, query_rows)
        debate_path = literature_dir / "debate_matrix.csv"
        debate_headers, debate_rows = _read_table(debate_path)
        debate_rows[0]["maturity_status"] = "reconstructed"
        write_table(debate_path, debate_headers, debate_rows)
        broken_debate = run_validator(literature_dir)
        if broken_debate.returncode == 0 or "<2 positions" not in broken_debate.stdout:
            raise SystemExit("debate maturity invariant was not enforced")
    finally:
        for artifact_name in schema["artifacts"]:
            (literature_dir / artifact_name).unlink(missing_ok=True)
        (
            literature_dir / "raw_results" / "B1" / "export.csv"
        ).unlink(missing_ok=True)

    print("review artifact fixture tests passed")
    return 0


def _read_table(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        return list(reader.fieldnames or []), list(reader)


if __name__ == "__main__":
    raise SystemExit(main())
