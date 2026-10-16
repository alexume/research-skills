---
name: research-reproducibility-and-replication
description: "Design, audit, and verify reproducible academic research workflows and replication packages in R and Quarto. Use from project setup through preparation, estimation, submission, and resubmission when Codex must define computational environments, executable pipelines, data and model provenance, deterministic randomness, output manifests, restricted-data alternatives, or clean-room verification."
---

# Research Reproducibility and Replication

Make every reported result traceable from a documented source through code, environment, analytical decisions, and generated outputs. Treat reproducibility as a project-wide design constraint, not a package assembled after the paper is written.

## Workflow position

Use this skill across:

- Stage 0 to design the reproducibility architecture;
- Stage 9 to freeze data lineage and the computational environment;
- Stages 10-11 to register models and specifications or structural evidence and decisions, plus seeds and generated outputs;
- Stage 17 to assemble and independently verify the replication package;
- Stages 18-19 to publish or revise the verified package consistently.

This skill supports every research route. It does not choose the research strategy, validate identification, or replace source criticism and measurement design.

## Required inputs

Recover or request:

- `project/project_profile.yaml` and `project/skill_execution_log.csv`;
- project root and intended public or restricted-data package;
- raw, interim, clean, and analytical data locations;
- software, system dependencies, and rendering requirements;
- scripts, notebooks, functions, targets, and manual steps;
- model, table, figure, appendix, and manuscript outputs;
- data licenses, confidentiality, privacy, and archival restrictions;
- random procedures, seeds, and nondeterministic external services;
- target journal or repository requirements when known.

Read `../shared/r_code_style.md` and the relevant contracts in `../shared/output_contracts.md`. A missing or incomplete project profile is a setup defect that must be resolved before final verification.

Never expose restricted data, credentials, machine-specific secrets, or absolute local paths in a public package.

## Step 1: Define the reproducibility plan

Create `project/reproducibility_plan.md` before substantive analysis. Define:

1. the executable entry point;
2. project-relative paths and directory roles;
3. raw-data immutability and acquisition boundaries;
4. environment capture and restoration;
5. pipeline architecture and dependency order;
6. seed policy and nondeterministic steps;
7. generated versus manually curated artifacts;
8. restricted-data and disclosure strategy;
9. verification responsibility and completion criteria.

Also initialize `project/skill_execution_log.csv` and ensure the project profile declares language, required manuscript renders, PDF engine, figure/table inclusion, and R code-quality requirements.

Read `references/r-environment-and-pipeline.md` for `renv`, `targets`, Quarto, and small-project alternatives.

## Step 2: Capture the computational environment

Create or update `analysis/computational_environment.md`. Record:

- R, Quarto, operating system, locale, and external program versions;
- package restoration method and lockfile status;
- system libraries or external dependencies not captured by the R lockfile;
- environment variables by name and purpose, never secret values;
- expected runtime and resource constraints;
- exact commands for restoration, execution, rendering, and validation.
- `styler`, `lintr`, TeX engine, and any figure or table rendering dependency versions and commands.

For R projects, prefer an explicit `renv` lockfile and record the result of `renv::status()`. A lockfile does not capture the operating system, system libraries, external binaries, or inaccessible data; document those separately.

## Step 3: Build an executable pipeline

Use `targets` when the project has multiple dependency branches, costly intermediate objects, or repeatedly generated tables and figures. A small project may use numbered scripts only when one documented entry point executes them in dependency order.

Require:

- functions separated from orchestration where complexity warrants it;
- no undocumented working-directory changes or machine-specific paths;
- no manual edits to generated tables, figures, or analytical datasets;
- explicit inputs and outputs for every stage;
- deterministic seeds for bootstrap, imputation, simulation, permutation, cross-fitting, or stochastic optimization;
- fail-fast checks for schemas, keys, required files, and package restoration.

Read `references/project-structure.md` for a minimal project layout and dependency rules.

## Step 4: Record data and analytical provenance

Maintain:

- hashes or stable version identifiers for immutable raw inputs;
- `analysis/preparation_manifest.md` for transformations and clean-data outputs;
- `analysis/model_registry.csv` for all estimands and estimators;
- `analysis/specification_log.csv` for material analytical deviations;
- `analysis/structural_evidence_matrix.csv` and `analysis/structural_analysis_log.csv` for historical-structural work;
- `tables/table_manifest.csv` for displayed analytical outputs;
- `figures/figure_manifest.csv` for displayed visual outputs;
- `analysis/r_code_quality.md` for required style and lint checks;
- `project/skill_execution_log.csv` for technical workflow provenance;
- provenance from fitted objects to every table, figure, and manuscript claim.

The model registry must distinguish `main`, `diagnostic`, `sensitivity`, `exploratory`, and `invalid` analyses. Never overwrite an earlier result without retaining its decision history.

## Step 5: Assemble the replication package

Create:

- `replication/README.md` as the human entry point;
- `replication/manifest.csv` as the file and provenance inventory;
- `replication/run_log.md` as the execution record;
- `replication/verification_report.md` as the independent verification decision.

The package must state whether it is full, partial, executable without data, or documentation-only. When data cannot be shared, provide lawful access instructions, data-construction code where permitted, metadata, schemas, and synthetic or mock data sufficient to test the pipeline without implying that mock outputs reproduce the published estimates.

Read `references/replication-package.md` before assembly.

## Step 6: Verify from a clean state

Verification must use a fresh checkout or clean copy, a restored environment, and only documented inputs. Record:

- verifier and date;
- platform and environment restoration result;
- commands executed and elapsed time;
- missing, manual, network, or restricted-data steps;
- hashes or tolerances used to compare outputs;
- discrepancies in estimates, tables, figures, appendices, or manuscript numbers;
- required-format render results, including the current PDF, citations, and cross-references;
- table and figure manifest coverage and R code-quality status;
- final decision: `pass`, `conditional pass`, or `fail`.

Use exact comparison for stable text and data artifacts; use justified numeric or image tolerances where platform variation is unavoidable. A script that runs but does not reproduce reported values fails verification.

Read `references/verification-checklist.md` for the clean-room protocol.

## Outputs

- `project/reproducibility_plan.md`.
- `analysis/computational_environment.md`.
- `analysis/model_registry.csv`.
- `analysis/specification_log.csv`.
- structural evidence and analysis logs when applicable.
- `tables/table_manifest.csv`.
- `figures/figure_manifest.csv`.
- `analysis/r_code_quality.md`.
- `project/skill_execution_log.csv`.
- `appendix/analytical_appendix.qmd`.
- `replication/README.md`.
- `replication/manifest.csv`.
- `replication/run_log.md`.
- `replication/verification_report.md`.
- environment lockfile and executable pipeline files appropriate to the project.

## Rules

- Never equate reproducibility with code availability alone.
- Never modify raw inputs in place.
- Never depend on an undocumented manual step for a reported result.
- Never place credentials, personal data, or restricted source material in the package.
- Never treat `renv` as a substitute for documenting system dependencies.
- Never label a package verified when it was run only in the author's working environment.
- Never allow revised estimates to diverge from tables, figures, appendices, or manuscript claims.
- Never accept HTML as a substitute for a profile-required PDF.
- Never treat a required check marked `not assessed` as a pass.
