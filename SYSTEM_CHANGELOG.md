# Skills System Changelog

This file records dated migrations and material changes to the skills system. See `ARCHITECTURE_REPORT.md` for the current architecture and `PRECHANGE_INVENTORY.txt` for the original inventory.

## 2026-10-16 - Self-contained README

- `README.md`: where the system lives, contents, installation on a new machine,
  daily use and pending migration steps (second computer, research projects in
  OneDrive). The system no longer depends on notes kept in any project.

## 2026-10-16 - Orchestration in eight gated phases

- `orchestration-research-workflow` rewritten: eight phases (0 setup · 1 question
  and literature · 2 sources and hypotheses · 3 strategy and design · 4 data ·
  5 analysis and interpretation · 6 drafting and internal review · 7 submission
  and resubmission), each closed by an author gate recorded in `BITACORA.md`,
  committed and tagged `fase-N`. Stages 0–19 stay as the detailed map other
  skills cite.
- New-project mode (commit 0): minimal skeleton, logbook, brief index, source
  inventory with rights, private repository from day one.
- Precedence: `GLOBAL_INSTRUCTIONS.md` > this skill > `shared/`. Shared
  contracts are a menu, not a checklist; `BITACORA.md` and git replace
  `project/skill_execution_log.csv`.
- `G-LITERATURE-ORIENTATION`: read a small core before any search or screening
  at scale; extension starts from what was read (a literature review in October 2026 screened about
  10,000 records before reading and made little progress on its question).

## 2026-10-16 - Back to local disk, fully versioned; global instructions

- The core moves from OneDrive (`AlexF/SKILLS_IA/codex/skills`) back to
  `~/.codex/skills`, a real folder; `~/.claude/skills` and `~/.agents/skills`
  (Cline) are junctions to it. Copy verified by sha256 (714 files).
- The whole system is versioned for the first time (until now only
  `SKILLS_INDEX.md`) and pushed to the private repository `research-skills`.
  Tool-managed folders (`.system/`, `synced/`, `.cache/`, `.vscode/`) and the
  2026-06-21 backup are ignored.
- `GLOBAL_INSTRUCTIONS.md`: one source of global instructions for Claude Code
  (imported from `~/.claude/CLAUDE.md`), Codex (`~/.codex/AGENTS.md`) and Cline
  (`Documents/Cline/Rules/`), the last two as copies.
- `setup.ps1` replaces `install_instructions.ps1` and the old
  `SKILLS_IA/bootstrap_symlinks.ps1`: junctions, CLAUDE.md import and copies.
- `shared/r_code_style.md`: script length is a guideline (about 150 lines), not
  a cap; a longer script is right when it is one conceptual process.
- The OneDrive copy stays frozen as the source for other machines until each one
  clones the repository and runs `setup.ps1`. `agent/skills` (`skills_bridge`,
  `ds_flash_review_adapter`) stays archived there.
- Next: rewrite `orchestration-research-workflow` as eight gated phases.

## 2026-07-14 - Manuscript, rendering, and R-code calibration

- Added `shared/project_profile_template.yaml` to declare manuscript language, QMD source, required PDF render, PDF engine, table/figure inclusion, and audit policy per project.
- Added `shared/r_code_style.md` with native `|>`, tidyverse style, explicit namespace, project-relative path, `styler`, and `lintr` requirements.
- Separated intellectual provenance in `paper/authorial_revision_log.md` from technical invocation evidence in `project/skill_execution_log.csv`.
- Added contracts and routing for `analysis/r_code_quality.md`, `figures/figure_manifest.csv`, and draft, revised, and resubmission PDFs.
- Required stable Quarto table and figure cross-references by default; raw LaTeX now requires an explicit project-profile or journal exception.
- Calibrated writing, scientific style, figures, tables, exploration, preparation, causal, DiD, and historical-structural implementation skills.
- Calibrated journal-fit and response-to-reviewers transitions so venue or revision requirements propagate into the project profile and regenerated PDF.
- Updated orchestration, reproducibility, and pre-submission audit to treat missing or `not assessed` checks as non-passing.
- Added `shared/validate_skill_system.py` for full-system governance validation and corrected the index's validator path.

## 2026-07-13 - Documentation separation and orchestrator audit

- Rewrote `ARCHITECTURE_REPORT.md` as a current-state architecture document.
- Moved chronological implementation history into this changelog.
- Audited `orchestration-research-workflow` against the workflow registry.
- Made dispatch precedence explicit: stage owner, method override, supporting skills, route-specific outputs, then gate.
- Corrected analytical record requirements by route: model/specification registries for causal work; structural evidence/analysis logs for historical-structural work; both for hybrid work.
- Added explicit failed-gate recovery paths and distinguished `G-REPLICATION` at Stage 17 from `G-SUBMISSION` at Stage 18.
- Updated `SKILLS_INDEX.md` as the documentation and intent-to-skill entry point.

## 2026-07-13 - Figure source normalization

- Confirmed `implementation-figures/cedric-scherer-aesthetics.qm` as the operational aesthetic synthesis.
- Moved `cedric_content.txt` to `implementation-figures/references/cedric_content.txt`.
- Moved `cedric_scraped.html` to `implementation-figures/references/cedric_scraped.html`.
- Documented that raw source artifacts are used for provenance and selective updates, not ordinary figure generation.

## 2026-07-13 - Phase 4: acquisition and historical-structural implementation

- Added `research-evidence-discovery-and-acquisition` for requirement-driven search, verification, lawful acquisition, and failed-search documentation.
- Added `implementation-historical-structural-analysis` to separate structural design from empirical implementation.
- Added `implementation-tables-and-appendices` for traceable tables, diagnostics, sensitivity evidence, and analytical appendices.
- Split Stage 10-12 inputs and outputs across causal, historical-structural, and hybrid routes.
- Removed the final declared capability gap from the workflow registry.

## 2026-07-13 - Phase 3: causal implementation and reproducibility

- Refactored `implementation-causal-analysis` into explicit IV, RDD, panel, and synthetic-control workflows with method-specific references and examples.
- Preserved `implementation-difference-in-differences` as the specialized DiD and event-study implementation skill.
- Added `research-reproducibility-and-replication` for environment capture, executable pipelines, analytical provenance, replication packages, and clean-state verification.
- Added `G-REPLICATION` as a gate distinct from submission readiness.
- Added model and specification registries and replication output contracts.

## 2026-07-13 - Phase 2: evidence, measurement, and data foundations

- Added `research-historical-source-criticism` and `research-historical-measurement`.
- Strengthened `literature-review`, `data-exploration`, and `data-preparation`.
- Integrated source production, coverage, historical comparability, measurement uncertainty, lineage, and validation into contracts and gates.

## 2026-07-13 - Phase 1: governance and routing

- Established `shared/workflow_registry.yaml` as the routing source of truth.
- Completed project-stage definitions, output contracts, semantic gates, and local configuration.
- Standardized skill metadata and `agents/openai.yaml` files.
- Added full-system validation for skill references, route coverage, stages, gates, and document contracts.

## 2026-06-01 - Hyphen-case migration

- Renamed 27 skill folders from `snake_case` to canonical `hyphen-case`.
- Updated frontmatter names, self-references, cross-skill references, presets, and the skills index.
- Retained historical snake-case names only in migration records.
- Validated all affected skills after UTF-8 normalization.

Representative migrations included:

- `implementation_causal_analysis` to `implementation-causal-analysis`;
- `research_causal_identification` to `research-causal-identification`;
- `research_structural_analysis_design` to `research-structural-analysis-design`;
- `submission_pre_submission_audit` to `submission-pre-submission-audit`;
- `writing_paper_draft` to `writing-paper-draft`.

## 2026-05-14 - Editorial and doctoral extensions

- Repaired frontmatter placement in the four original review skills.
- Added `writing-title-abstract-keywords`, `submission-cover-letter`, and `revision-response-to-reviewers`.
- Added `review-doctoral-proposal`.
- Expanded journal profiles and submission/resubmission output contracts.

## 2026-05-14 - Professional workflow extension

- Added the first end-to-end workflow from setup through submission.
- Added orchestration, strategy choice, structural design, mechanism mapping, claim-evidence mapping, journal fit, and pre-submission audit.
- Introduced shared project stages, output contracts, and stage gates.
- Established causal, historical-structural, and hybrid route concepts.

## 2026-05-14 - Initial reorganization

- Created backup `C:\Users\alex.urrego.mesa\.codex\skills_backup_20260514_180348`.
- Converted loose research prompts into skill folders with `SKILL.md`.
- Renamed the original reviewer folders into flat prefixed skill names.
- Preserved existing causal-historical review examples.
- Added shared journal, review-label, and output-style resources.
- Retained `PRECHANGE_INVENTORY.txt` as the authoritative pre-change file list.

No filename conflicts or unclassified files were reported during the initial reorganization.
