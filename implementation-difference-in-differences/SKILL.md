---
name: implementation-difference-in-differences
description: Implement and assess modern difference-in-differences designs in R, including canonical 2x2 DiD, multiple periods, staggered treatment adoption, conditional parallel trends, and event studies. Use after research-causal-identification selects a DiD strategy, or when Codex must implement, diagnose, compare, or interpret DiD estimates using methods such as DRDID or Callaway-Sant'Anna. Do not use to choose the project's primary research route or to treat TWFE as automatically causal.
---

# Modern Difference-in-Differences

Implement a DiD design only after its causal question and identifying variation have been defined. Separate the target estimand, identification assumptions, estimation, aggregation, inference, and interpretation.

## Workflow position

Use this skill at:

- Stage 10, feasibility and design update: audit whether the proposed DiD is estimable.
- Stage 11, implementation: estimate, diagnose, aggregate, and report effects.

Consume the DiD handoff from `research-causal-identification`. Return to that skill when the proposed comparison does not identify the target effect. Use `review-causal-historical-logic` after estimation to assess temporal, institutional, and mechanism coherence.

Activate `research-reproducibility-and-replication` to register models and analytical deviations, capture the environment and seeds, connect outputs to the execution pipeline, and prepare later verification.

Read `project/project_profile.yaml` and `../shared/r_code_style.md`. Use the native `|>`, tidyverse style, explicit namespaces in reusable code, and project-relative paths. Use `did`, `DRDID`, `HonestDiD`, `fixest`, or other specialized packages when required by the approved estimator; the shared style standard does not determine identification or estimator choice.

## Required inputs

Before estimating, recover or request:

- causal question and target population;
- outcome, treatment, unit, and time frequency;
- treatment-assignment process and first treatment date;
- adoption structure and whether treatment is absorbing;
- target estimand;
- proposed comparison group;
- unconditional or conditional parallel-trends assumption;
- anticipation window;
- pre-treatment covariates, if required;
- treatment-assignment and inference level;
- plausible spillovers, attrition, or composition changes;
- historically grounded mechanism and relevant lags.

Do not silently invent a missing estimand or comparison group. If either is unavailable, stop implementation and return a failed design handoff.

## Step 1: Classify the design

Classify before selecting an estimator:

| Structure | Primary route |
|---|---|
| Two groups and two periods | Canonical DiD; use `DRDID` when conditioning on covariates |
| Multiple periods with common adoption | Multiperiod DiD with explicit pre-period use |
| Staggered absorbing adoption | Group-time effects with `did::att_gt()` |
| Repeated cross-sections | Use a repeated-cross-section-compatible estimator |
| Reversible or intermittent treatment | Do not apply absorbing-treatment methods automatically |
| Continuous or multivalued treatment | Treat as a specialized extension; read `references/methodology.md` |
| One or very few treated units | Reconsider whether synthetic-control methods are more credible |

Treat TWFE as an estimator or benchmark, not as a standalone identification strategy.

## Step 2: Apply the feasibility gate

Audit:

1. uniqueness of unit-time observations;
2. construction of first-treatment cohort;
3. units treated before the observed panel;
4. never-treated and not-yet-treated availability;
5. treatment reversals or intermittent exposure;
6. pre- and post-treatment coverage by cohort;
7. identifiable group-time cells and comparison-group size;
8. attrition and changing sample composition;
9. covariate overlap and extreme weights when conditioning;
10. anticipation, spillovers, and treatment-timing ambiguity;
11. number of assignment-level clusters and inference feasibility.

Classify the gate:

- `pass`: the target effects and required comparisons are identified and estimable;
- `conditional pass`: proceed only with explicit restrictions or a revised estimand;
- `fail`: return to causal identification or data preparation.

Do not estimate the main model after a failed gate.

## Step 3: Define effects and aggregations

For staggered adoption, use the group-time effect as the building block:

$$ATT(g,t)=E[Y_t(1)-Y_t(0)\mid G=g].$$

Choose aggregations before examining preferred results:

- overall ATT for treated units;
- cohort-specific effects;
- calendar-time effects;
- dynamic effects by exposure length;
- dynamic effects over a common exposure window.

State the target population and weighting induced by each aggregation. Do not describe different aggregations as estimates of the same parameter when their cohort composition or weights differ.

## Step 4: Select and implement the estimator

Prefer:

- `DRDID` for a conditional two-group, two-period design;
- `did::att_gt()` for binary staggered absorbing adoption;
- `did::aggte()` for prespecified group, calendar, dynamic, or overall aggregations.

Use doubly robust estimation as a reasoned default when conditional parallel trends and adequate overlap are plausible. Compare regression adjustment or IPW when that comparison diagnoses nuisance-model dependence.

Set explicitly:

- panel versus repeated cross-section;
- never-treated versus not-yet-treated controls;
- anticipation window;
- pre-treatment covariates and their timing;
- sampling weights;
- clustering level;
- bootstrap and simultaneous confidence bands;
- base-period convention.

Register every main, diagnostic, sensitivity, exploratory, and invalid specification in `analysis/model_registry.csv`. Record material changes to comparison groups, covariates, anticipation, aggregation, sample, estimator, or inference in `analysis/specification_log.csv`.

Use TWFE only when its identifying restrictions match the design or as a labeled benchmark. Never use a conventional staggered TWFE event study as the sole main estimator when treatment effects may vary across cohorts or exposure time.

## Step 5: Diagnose assumptions and inference

Report:

- group-time estimates and simultaneous confidence bands;
- joint evidence from pre-treatment pseudo-effects;
- the power limitation of pretrend tests;
- overlap and extreme-weight diagnostics;
- attrition and composition checks;
- sensitivity to comparison group and anticipation window;
- sensitivity to aggregation and cohort influence;
- cluster count and inference limitations;
- sensitivity to plausible violations of parallel trends when material.

Do not interpret failure to reject a pretrend test as proof of parallel trends. Use `HonestDiD` or an equivalent sensitivity analysis when conclusions depend materially on small deviations from parallel trends.

## Step 6: Report and interpret

Produce or update `analysis/feasibility.qmd` at Stage 10 and `analysis/results.qmd` at Stage 11. Use this structure:

```markdown
## DiD Design Classification
## Target Estimand and Population
## Identification Handoff
## Feasibility Gate
## Estimator and Comparison Group
## Group-Time Effects and Aggregation
## Diagnostics and Inference
## Sensitivity
## Historical Interpretation
## Limits of Inference
## Gate Result
```

Connect estimates to the proposed mechanism without treating statistical identification as a complete historical explanation. Distinguish short-run exposure effects from longer-run transformations and respect the spatial and institutional scale of the identifying variation.

Also produce or update `analysis/inference_plan.qmd`, `analysis/model_registry.csv`, and `analysis/specification_log.csv`; store fitted objects separately from presentation outputs and connect all generated tables and figures to the reproducible pipeline.

Update `analysis/r_code_quality.md`, `tables/table_manifest.csv`, and `figures/figure_manifest.csv`. A DiD results gate cannot pass when required code checks or generated-output manifests are missing or not assessed.

Use `implementation-tables-and-appendices` to separate the prespecified main aggregation from cohort, calendar, dynamic, diagnostic, and sensitivity evidence while preserving group-time support, comparison groups, weights, uncertainty, and simultaneous-band information.

## References

- Read `references/methodology.md` for assumptions, estimator selection, aggregation, diagnostics, and extensions.
- Read `references/examples.md` for a conditional 2x2 design and a staggered-adoption design.

## Rules

- Define the estimand before selecting the estimator.
- Separate identification, estimation, aggregation, and inference.
- Never treat panel structure, fixed effects, or statistical significance as causal identification.
- Never control for variables affected by treatment.
- Never pool already-treated units into the comparison group without an explicit valid design.
- Report uniform bands for an event-study path when supported by the estimator.
- Preserve a reproducible record of estimator arguments, package versions, seeds, and sample restrictions.
- Return to `research-causal-identification` when the feasible comparison or estimand changes materially.
