# Skills System Architecture

## Status and scope

This document describes the current architecture of the academic research skills system. It is explanatory, not the routing source of truth. Historical migrations and implementation phases belong in `SYSTEM_CHANGELOG.md`; the original inventory remains in `PRECHANGE_INVENTORY.txt`.

The system supports academic research and publication in economic history, environmental history, ecological economics, agrarian studies, and historical political economy.

Current validated state:

- 36 skills;
- 20 ordered stages;
- 16 semantic gates;
- 52 contracted Markdown or Quarto outputs in the registry;
- 74 artifact contract sections across Markdown, Quarto, CSV, YAML, and PDF outputs;
- causal, historical-structural, and hybrid routes.

## Architectural principles

1. **Stage before action.** Diagnose the project's current stage before activating a skill.
2. **Design before implementation.** An estimator, regression, narrative, or visualization cannot substitute for a research design.
3. **Route-specific ownership.** Causal and historical-structural projects share infrastructure but not all analytical artifacts.
4. **Artifacts plus gates.** A file exists only as a draft until it satisfies its output contract and stage gate.
5. **Evidence provenance.** Literature, historical sources, measurements, datasets, transformations, models, and claims remain traceable.
6. **Reproducibility throughout.** Computational reproducibility begins at setup and is verified before submission.
7. **Explicit recovery.** Failed gates return work to the stage that owns the failed decision.
8. **Project-level publication contract.** Language, renders, PDF engine, table/figure inclusion, and R code policy are declared once and consumed by every relevant skill.
9. **Separate intellectual and technical provenance.** Authorial decisions and skill execution use different logs.

## Governance and precedence

| Concern | Authoritative file | Role |
|---|---|---|
| Routing and ownership | `shared/workflow_registry.yaml` | Machine-readable source of truth |
| Stage meaning | `shared/project_stages.md` | Narrative stage definitions |
| Artifact completion | `shared/output_contracts.md` | Minimum content for outputs |
| Quality decisions | `shared/stage_gates.md` | Pass, conditional pass, or fail; not assessed blocks required decisions |
| Machine-local paths | `shared/local_config.yaml` | Non-portable local configuration |
| Journal conventions | `shared/journal_profiles.md` | Venue-specific expectations |
| Output presentation | `shared/output_styles.md` | Shared output conventions |
| Project profile | `shared/project_profile_template.yaml` | Portable publication, rendering, and code defaults |
| R code quality | `shared/r_code_style.md` | Native-pipe, tidyverse, namespace, formatting, and lint policy |
| System validation | `shared/validate_skill_system.py` | Cross-file structural and governance checks |
| Skill discovery | `SKILLS_INDEX.md` | Human-readable intent-to-skill map |
| System history | `SYSTEM_CHANGELOG.md` | Dated migrations and releases |

If documents conflict, routing follows the registry, artifact completion follows output contracts, and quality decisions follow stage gates. The orchestrator must report the conflict instead of silently choosing.

## System layers

### 1. Governance

Shared files define stages, routes, owners, artifacts, gates, presentation, and local configuration. The validator checks skill structure, metadata, registry references, route coverage, gates, and document contracts.

### 2. Orchestration

`orchestration-research-workflow` diagnoses stage and route, dispatches the owner, applies method overrides, activates supporting skills selectively, checks contracts and gates, and routes failures backward.

Dispatch precedence is:

```text
stage owner or owner_by_route
-> method_override when justified by the approved design
-> supporting skills required by inputs and risks
-> route-specific outputs
-> stage gate
```

### 3. Evidence and research formation

Stages 1-9 develop the literature base, hypotheses, source understanding, measurement, route, design, evidence acquisition, and analysis-ready materials. Source criticism and historical measurement are substantive research layers, not cleaning utilities.

### 4. Route-specific analysis

Stages 7 and 10-12 branch by research route. The branches share preparation, figures, tables, reproducibility, interpretation, and claim-evidence auditing where appropriate.

### 5. Writing, review, and publication

Stages 13-19 produce the manuscript, analytical appendix, internal review, revision, journal selection, replication verification, submission package, and response to reviewers.

### 6. Cross-cutting controls

- `research-reproducibility-and-replication` governs environment, pipeline, provenance, manifests, and clean-state verification.
- `research-historical-source-criticism` governs source production, coverage, survival, transformations, and evidentiary limits.
- `research-historical-measurement` governs concept-to-variable fit and historical comparability.
- `research-claim-evidence-mapping` governs claim calibration.
- `implementation-tables-and-appendices` and `implementation-figures` govern traceable presentation outputs.
- `project/project_profile.yaml` governs language, required renders, PDF engine, presentation integration, and R code policy for one project.
- `project/skill_execution_log.csv` records technical skill invocation separately from substantive authorial revision.

## Research routes

### Causal route

```text
strategy choice
-> research-causal-identification
-> implementation-causal-analysis
   or implementation-difference-in-differences
-> research-mechanism-mapping
-> claim-evidence audit
```

The identification skill selects the defensible design and produces the implementation handoff. DiD overrides the general implementation owner at Stages 10-11. Model and specification registries are required analytical records.

### Historical-structural route

```text
strategy choice
-> research-structural-analysis-design
-> implementation-historical-structural-analysis
-> research-mechanism-mapping
-> claim-evidence audit
```

Structural design defines process, periodization, scale, patterns, mechanisms, evidence, and rivals. Structural implementation establishes patterns, tests periodization, compares cases and scales, triangulates evidence, and evaluates mechanisms. Structural evidence and analysis logs replace causal model registries.

### Hybrid route

```text
strategy choice
-> structural design + causal identification
-> structural implementation + selected causal implementation
-> integrated mechanism and claim-evidence analysis
```

The causal component tests bounded claims. It cannot carry more explanatory weight than its estimand and identifying variation permit. Hybrid projects require both causal and structural analytical records.

## Stage ownership

| Stage | Key | Owner | Gate |
|---:|---|---|---|
| 0 | Setup | `orchestration-research-workflow` | None |
| 1 | Literature base | `literature-review` | `G-LITERATURE` |
| 2 | Literature refinement | `literature-review` | `G-LITERATURE` |
| 3 | Hypotheses v1 | `research-hypothesis-generation` | `G-HYPOTHESES` |
| 4 | Exploratory assessment | `data-exploration` | `G-EXPLORATION` |
| 5 | Hypotheses v2 | `research-hypothesis-refinement` | `G-HYPOTHESES` |
| 6 | Strategy choice | `research-strategy-choice` | `G-STRATEGY` |
| 7 | Design | Route-specific design owner | `G-DESIGN` |
| 8 | Requirements and acquisition | `research-evidence-discovery-and-acquisition` | `G-REQUIREMENTS` |
| 9 | Preparation | `data-preparation` | `G-PREPARATION` |
| 10 | Feasibility and design update | Route-specific implementation owner | `G-FEASIBILITY` |
| 11 | Implementation | Route-specific implementation owner | `G-RESULTS` |
| 12 | Interpretation | `research-mechanism-mapping` | `G-INTERPRETATION` |
| 13 | First draft | `writing-paper-draft` | `G-DRAFT` |
| 14 | Internal referee review | `review-reviewer-core` | `G-INTERNAL-REVIEW` |
| 15 | Revision | `writing-paper-draft` | `G-INTERNAL-REVIEW` |
| 16 | Journal fit | `submission-journal-fit` | `G-JOURNAL-FIT` |
| 17 | Pre-submission replication audit | `submission-pre-submission-audit` | `G-REPLICATION` |
| 18 | Submission package | `submission-cover-letter` | `G-SUBMISSION` |
| 19 | Revision and resubmission | `revision-response-to-reviewers` | `G-RESUBMISSION` |

At Stages 7, 10, and 11, exact owners and route-specific outputs are defined in the registry. At Stages 10-11, the DiD method override supersedes the general causal implementation owner.

## Artifact architecture

| Directory | Responsibility |
|---|---|
| `project/` | Setup, project profile, decisions, technical skill log, source inventories, acquisition, reproducibility plan |
| `literature/` | Search strategy, screening, extraction, debates, bibliography |
| `data/raw/` | Immutable provider inputs where lawful |
| `data/interim/` | Replaceable pipeline products |
| `data/clean/` | Validated analysis-ready data |
| `data/metadata/` | Variables, measurement decisions, lineage |
| `analysis/` | Hypotheses, designs, feasibility, results, patterns, interpretation, logs, R code-quality report |
| `tables/` | Registered table data, main/appendix/excluded status, and publication outputs |
| `figures/` | Reproducible publication figures and figure manifest |
| `appendix/` | Analytical appendix and supporting outputs |
| `paper/` | Controlled QMD manuscripts, required PDFs, authorial logs, title and abstract |
| `submission/` | Journal fit, audit, cover letter, submission manifest |
| `replication/` | README, file manifest, run log, verification report |
| `revision/` | Reviewer responses, changes, revised files, resubmission manifest |

## Handoffs and recovery

- Missing or unverified evidence returns to Stage 8.
- Invalid construction, linkage, or harmonization returns to Stage 9 or historical measurement.
- A changed causal estimand or comparison returns to Stage 7 causal identification.
- A changed periodization, scale, pattern, mechanism, or structural scope returns to Stage 7 structural design.
- An indefensible route returns to Stage 6 strategy choice.
- Table, appendix, or manuscript inconsistencies return to the owning analytical stage.
- Replication discrepancies return to the stage that generated the divergent artifact and then repeat Stage 17.

## Architectural invariants

- Raw inputs are immutable.
- A source, dataset, model, table, or figure is not evidence without provenance and scope.
- Fixed effects, TWFE, 2SLS, RDD software, or synthetic controls are not identification strategies by themselves.
- Historical-structural analysis must establish patterns before mechanism claims.
- Causal-only artifacts are not required from a purely historical-structural project, and structural-only artifacts are not required from a purely causal project.
- Generated analytical values are never edited manually in presentation files.
- `G-REPLICATION` precedes `G-SUBMISSION`.
- A conditional pass names the blocking condition, responsible artifact, and verification criterion.
- A required check marked `not assessed` is not a pass.
- QMD is the controlled manuscript source; PDF is mandatory under the default project profile.
- Table and figure integration uses stable Quarto cross-references by default; raw LaTeX requires an explicit profile or journal exception.
- New R code uses `|>` and the shared tidyverse style, with required `styler` and `lintr` evidence.
- `paper/authorial_revision_log.md` cannot substitute for `project/skill_execution_log.csv`.

## Extension rules

Add a new skill only when it owns a distinct decision or repeated operation that existing skills cannot absorb cleanly. Every extension must:

1. define trigger conditions and exclusions;
2. declare workflow position, inputs, outputs, and return paths;
3. update the registry when ownership or routing changes;
4. add or update output contracts and gates;
5. update `SKILLS_INDEX.md`, this architecture document, and `SYSTEM_CHANGELOG.md`;
6. provide `agents/openai.yaml` and only necessary references, scripts, or assets;
7. pass individual and full-system validation.

Do not create a new route merely because a new method or output type is added.
