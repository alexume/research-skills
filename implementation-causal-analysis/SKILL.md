---
name: implementation-causal-analysis
description: "Implement and diagnose causal analyses in R after a design has been selected, with method-specific workflows for instrumental variables, regression discontinuity, panel fixed-effects or first-difference models, and synthetic-control methods. Use at feasibility or implementation stages when Codex must translate an identification handoff into estimable specifications, inference, diagnostics, sensitivity analysis, model registries, tables, and reproducible outputs. Use implementation-difference-in-differences instead for DiD, event studies, multiple periods, or staggered treatment adoption."
---

# Causal Analysis Implementation

Implement a selected causal design without allowing software or a preferred regression to redefine the estimand, comparison, assumptions, or target population.

## Workflow position

Use this skill at:

- Stage 10 to audit estimability and update the design;
- Stage 11 to estimate, diagnose, stress-test, and report results.

Consume the method-specific handoff from `research-causal-identification`. Return to identification when feasible data, comparison, treatment, instrument, cutoff, donor pool, or estimand changes materially. Delegate all DiD and event-study implementations to `implementation-difference-in-differences`.

Read `project/project_profile.yaml` and `../shared/r_code_style.md`. Apply the shared R standard to estimation, diagnostic, table, and figure code without substituting tidyverse packages for methodologically appropriate estimators.

## Required inputs

Recover or request:

- causal question, estimand, and target population;
- treatment-assignment process and identifying variation;
- outcome, treatment, unit, time, and relevant scale;
- method-specific assumptions and comparison units;
- measurement strategy and source limitations;
- final analysis sample and exclusion rules;
- assignment level, dependence structure, and cluster count;
- prespecified main model, outcomes, heterogeneity, and sensitivity plan;
- historically plausible mechanism and effect timing.

Do not silently reconstruct a missing identification argument from the proposed code.

## Step 1: Select the method workflow

| Selected design | Required reference |
|---|---|
| Instrumental variables or 2SLS | `references/iv.md` |
| Sharp, fuzzy, or kink RDD | `references/rdd.md` |
| Panel FE, first differences, or related panel model | `references/panel.md` |
| Synthetic control, augmented SCM, or synthetic DiD | `references/synthetic-control.md` |
| DiD or event study | Use `implementation-difference-in-differences` |

Also read `references/inference.md`. Read `references/examples.md` when a concrete implementation pattern is helpful.

## Step 2: Apply the feasibility gate

Before estimating, verify:

1. the data preserve the identifying variation;
2. the feasible sample represents the stated target population;
3. treatment, outcome, instrument, running variable, panel structure, or donor pool pass method-specific checks;
4. measurement and source uncertainty do not change the design object;
5. cluster count and dependence permit defensible inference;
6. the proposed specification is estimable without undocumented exclusions;
7. diagnostics and sensitivity analyses can be computed.

Return `pass`, `conditional pass`, or `fail`. A conditional pass must state the restricted estimand or claim. Do not continue to a preferred main estimate after a failed gate.

## Step 3: Register the analysis before comparison

Create or update:

- `analysis/model_registry.csv` for estimand, sample, estimator, formula, fixed effects, weights, inference, and status;
- `analysis/specification_log.csv` for every material deviation, reason, timing, and result status;
- `analysis/inference_plan.qmd` for dependence, clustering, small-sample issues, multiplicity, and confidence intervals.

Classify models as:

- `main`: prespecified estimate of the target estimand;
- `diagnostic`: probes a design assumption or data problem;
- `sensitivity`: varies a defensible assumption or implementation decision;
- `exploratory`: generates a new question and cannot silently replace the main model;
- `invalid`: retained for audit but excluded from inference.

Do not select the main model by statistical significance, preferred sign, or visual fit.

## Step 4: Implement transparently

For every model:

- use the same stable variable and sample definitions recorded upstream;
- state the estimand and identifying comparison;
- record package, function, version-relevant arguments, formula, weights, and sample filters;
- store fitted objects and tidy estimates separately from presentation tables;
- keep first-stage, reduced-form, assignment, balance, fit, and placebo objects when required;
- set and record random seeds for bootstrap, permutation, simulation, or cross-fitting;
- route all code and outputs through `research-reproducibility-and-replication` requirements.
- route final result tables and analytical appendices through `implementation-tables-and-appendices`.

Package defaults are not methodological justifications. Override or retain them explicitly.

## Step 5: Diagnose the design

Use diagnostics tied to identifying assumptions, not a generic robustness checklist. At minimum:

- inspect effective variation and influential observations or units;
- evaluate support, overlap, leverage, and sample composition where relevant;
- test observable implications without calling them proof of untestable assumptions;
- compare only estimators that target compatible parameters;
- identify diagnostics that are underpowered or invalid under the dependence structure;
- document failed or undefined diagnostics.

Do not interpret passing a test as validation of exclusion, continuity, no interference, strict exogeneity, or donor validity.

## Step 6: Conduct sensitivity analysis

Vary assumptions or defensible implementation choices that threaten the claim:

- sample and comparison definitions;
- measurement, outcome, treatment, instrument, or running-variable construction;
- bandwidth, polynomial, lag, trend, predictor, donor, or weight choices as method-appropriate;
- cluster, spatial, or finite-sample inference;
- influential units, periods, instruments, cutoffs, or donors;
- alternative estimands or target populations, labeled as such.

Explain what each sensitivity result changes: estimate, uncertainty, estimand, population, or interpretation.

## Step 7: Report

Update `analysis/results.qmd` with:

```markdown
## Causal Question and Estimand
## Identification Handoff
## Feasibility Gate
## Data, Sample, and Measurement
## Estimator and Inference
## Main Estimate
## Design Diagnostics
## Sensitivity and Alternative Estimands
## Mechanism and Historical Interpretation
## Limits of Inference
## Results Gate
```

Report point estimates with uncertainty, units, sample size, assignment-level clusters, and the population represented. Prefer confidence intervals and substantive magnitudes over star-centered reporting. Keep null, imprecise, failed, and specification-sensitive results visible.

## Outputs

- `analysis/feasibility.qmd` at Stage 10.
- `analysis/inference_plan.qmd`.
- `analysis/model_registry.csv`.
- `analysis/specification_log.csv`.
- `analysis/results.qmd`.
- fitted objects in `data/interim/models/`.
- final tables and figures in their project directories.
- scripts connected to the reproducible execution pipeline.
- `analysis/r_code_quality.md` covering maintained analytical code.
- `tables/table_manifest.csv` and `figures/figure_manifest.csv` for generated presentation outputs.

## Rules

- Never confuse an estimator with an identification strategy.
- Never let feasibility changes remain implicit.
- Never treat fixed effects as automatically causal.
- Never use an arbitrary first-stage threshold as the sole weak-IV assessment.
- Never use global high-order polynomials as the default RDD specification.
- Never choose synthetic-control donors or predictors using post-treatment fit.
- Never hide failed models, diagnostics, or sample changes.
- Never interpret statistical significance as mechanism or historical explanation.
- Never pass `G-RESULTS` when required code-quality, table-manifest, or figure-manifest checks are not assessed.
