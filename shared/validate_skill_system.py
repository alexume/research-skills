"""Validate the research skills system as one governed workflow."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "shared"


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8-sig"))


def nested_get(data: dict[str, Any], path: str) -> Any:
    value: Any = data
    for key in path.split("."):
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value


def flatten_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for part in value for item in flatten_strings(part)]
    if isinstance(value, dict):
        return [item for part in value.values() for item in flatten_strings(part)]
    return []


def collect_skill_references(node: Any, parent_key: str = "") -> set[str]:
    references: set[str] = set()
    if isinstance(node, dict):
        for key, value in node.items():
            is_skill_field = (
                key in {"owner", "owner_by_route", "method_override"}
                or key.endswith("_skills")
                or key.startswith("implementation_")
            )
            if is_skill_field:
                references.update(flatten_strings(value))
            references.update(collect_skill_references(value, key))
    elif isinstance(node, list):
        for value in node:
            references.update(collect_skill_references(value, parent_key))
    return references


def main() -> int:
    errors: list[str] = []
    required_shared = {
        "workflow_registry.yaml",
        "project_stages.md",
        "output_contracts.md",
        "stage_gates.md",
        "project_profile_template.yaml",
        "r_code_style.md",
    }
    for name in required_shared:
        if not (SHARED / name).is_file():
            fail(errors, f"Missing shared governance file: shared/{name}")

    skill_dirs = sorted(path.parent for path in ROOT.glob("*/SKILL.md"))
    skill_names: set[str] = set()
    frontmatter_re = re.compile(r"\A---\s*\n(.*?)\n---", re.DOTALL)

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        content = skill_file.read_text(encoding="utf-8-sig")
        match = frontmatter_re.search(content)
        if not match:
            fail(errors, f"Invalid or missing frontmatter: {skill_file.relative_to(ROOT)}")
            continue
        metadata = yaml.safe_load(match.group(1)) or {}
        name = metadata.get("name")
        description = metadata.get("description")
        if name != skill_dir.name:
            fail(errors, f"Skill name mismatch: {skill_dir.name} != {name!r}")
        if not isinstance(description, str) or not description.strip():
            fail(errors, f"Missing description: {skill_file.relative_to(ROOT)}")
        if name:
            skill_names.add(name)
        if not (skill_dir / "agents" / "openai.yaml").is_file():
            fail(errors, f"Missing agents/openai.yaml: {skill_dir.name}")

    registry = load_yaml(SHARED / "workflow_registry.yaml")
    references = collect_skill_references(registry)
    for reference in sorted(references - skill_names):
        fail(errors, f"Registry references unknown skill: {reference}")

    stages = registry.get("stages", [])
    stage_ids = [stage.get("id") for stage in stages]
    if stage_ids != list(range(20)):
        fail(errors, f"Stage IDs must be ordered 0-19, found: {stage_ids}")

    route_names = set(registry.get("routes", {}))
    expected_routes = {"causal", "historical-structural", "hybrid"}
    if route_names != expected_routes:
        fail(errors, f"Routes must be {sorted(expected_routes)}, found {sorted(route_names)}")
    for stage in stages:
        for key in ("owner_by_route", "outputs_by_route", "inputs_by_route"):
            if key in stage and set(stage[key]) != expected_routes:
                fail(errors, f"Stage {stage.get('id')} {key} does not cover all routes")

    gates_text = (SHARED / "stage_gates.md").read_text(encoding="utf-8-sig")
    defined_gates = set(re.findall(r"^## `([^`]+)`", gates_text, re.MULTILINE))
    referenced_gates = {stage["gate"] for stage in stages if stage.get("gate")}
    for gate in sorted(referenced_gates - defined_gates):
        fail(errors, f"Registry references undefined gate: {gate}")

    contract_text = (SHARED / "output_contracts.md").read_text(encoding="utf-8-sig")
    contracted_paths = set(re.findall(r"^## `([^`]+)`", contract_text, re.MULTILINE))
    registry_outputs: set[str] = set()
    for stage in stages:
        registry_outputs.update(flatten_strings(stage.get("outputs", [])))
        registry_outputs.update(flatten_strings(stage.get("outputs_by_route", {})))
    document_outputs = {
        path for path in registry_outputs if Path(path).suffix.lower() in {".md", ".qmd"}
    }
    for path in sorted(document_outputs - contracted_paths):
        fail(errors, f"Registry document output lacks contract: {path}")

    profile = load_yaml(SHARED / "project_profile_template.yaml")
    required_profile_paths = {
        "manuscript.language",
        "manuscript.source_format",
        "manuscript.required_render_formats",
        "manuscript.pdf_engine",
        "figures.generated_with",
        "figures.inclusion_method",
        "tables.inclusion_method",
        "r_code.style",
        "r_code.pipe",
        "r_code.require_styler_check",
        "r_code.require_lintr_check",
        "audit.require_skill_execution_log",
        "audit.require_authorial_revision_log",
    }
    for path in sorted(required_profile_paths):
        if nested_get(profile, path) is None and path != "manuscript.language":
            fail(errors, f"Project profile template lacks required value: {path}")
    if nested_get(profile, "manuscript.source_format") != "qmd":
        fail(errors, "Default manuscript source format must be qmd")
    if "pdf" not in (nested_get(profile, "manuscript.required_render_formats") or []):
        fail(errors, "Default project profile must require PDF")
    if nested_get(profile, "r_code.style") != "tidyverse":
        fail(errors, "Default R style must be tidyverse")
    if nested_get(profile, "r_code.pipe") != "native":
        fail(errors, "Default R pipe must be native")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALIDATION PASSED")
    print(f"skills={len(skill_names)}")
    print(f"stages={len(stages)}")
    print(f"gates={len(defined_gates)}")
    print(f"contracted_document_outputs={len(document_outputs)}")
    print(f"contract_sections={len(contracted_paths)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
