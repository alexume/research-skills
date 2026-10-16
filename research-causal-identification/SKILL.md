---
name: research-causal-identification
description: Select and formalize a causal identification strategy by comparing candidate designs, defining the estimand and counterfactual, stating assumptions, mapping threats, and producing a method-specific implementation handoff. Use when a project has chosen or is considering a causal or hybrid route but has not yet established whether DiD, IV, RDD, synthetic control, selection on observables, shift-share, or another design provides the most defensible identifying variation.
---

# Causal Identification

Select the most defensible identification strategy for the causal question. Choose a design family from the assignment process, available variation, counterfactual, and assumptions; do not choose it from the regression or package the researcher prefers.

This skill operates at Stage 7, design. It precedes method-specific implementation and can be revisited after the Stage 10 feasibility audit.

## Workflow

### Step 1: Define the causal target

- State the causal question in plain language.
- Define treatment, outcome, target population, unit, time, and exposure window.
- Define the estimand using potential outcomes.
- Describe the ideal experiment and its assignment mechanism.
- State the counterfactual comparison required by the question.

### Step 2: Reconstruct treatment assignment

Identify:

- who assigns or adopts treatment;
- the institutional rule or historical process generating exposure;
- the timing and level of assignment;
- whether treatment is anticipated, reversible, continuous, or subject to spillovers;
- which observed units could credibly represent untreated potential outcomes.

Do not treat the existence of panel data, fixed effects, a cutoff, or a candidate instrument as sufficient identification.

### Step 3: Map threats

Assess at minimum:

1. omitted confounding and selection;
2. reverse causality and endogenous timing;
3. anticipation and behavioral responses;
4. measurement error in treatment, outcome, or assignment variables;
5. spillovers and interference;
6. attrition, migration, and changing composition;
7. scale, timing, and variable-mechanism mismatch;
8. functional-form or support dependence.

### Step 4: Compare candidate design families

| Design family | Identifying variation | Core assumption |
|---|---|---|
| DiD | Comparative outcome changes | Parallel untreated trends for the actual comparison |
| IV | Treatment variation induced by an instrument | Relevance, exclusion, independence, and monotonicity when interpreting LATE |
| RDD | Local treatment discontinuity at a binding cutoff | Continuity of untreated potential outcomes and no precise manipulation |
| Selection on observables | Exposure variation conditional on measured covariates | Conditional exchangeability and overlap |
| Synthetic control | Pre-treatment outcome path and donor combination | Donors approximate the treated unit's untreated path and are uncontaminated |
| Shift-share | Differential exposure to common shocks | Exogeneity conditions appropriate to shares, shocks, and inference |
| Experiment or randomized rollout | Known random assignment | Correct implementation, compliance, and no interference |

Treat OLS, 2SLS, panel fixed effects, TWFE, matching, and weighting as estimators or specifications, not automatically as identification strategies.

For each plausible family, state what variation identifies the effect, why the assumptions may hold historically, what evidence can probe them, and what claim would remain if they fail.

### Step 5: Select, reject, or defer

Return one of:

- `pass`: one design has a defensible estimand, comparison, assumptions, and data path;
- `conditional pass`: one design is preferred but requires explicit data or design checks;
- `fail`: no available design supports the intended causal claim.

Explain why rejected alternatives are weaker. A failed causal design should trigger a narrower causal question, additional data acquisition, or reconsideration of a hybrid or historical-structural route.

### Step 6: Formalize the design

For the selected family, provide:

- formal estimand;
- identifying variation and comparison units;
- identifying assumptions in plain language and notation;
- method-relevant equations or moment conditions;
- variable definitions and sources;
- role of fixed effects, controls, and remaining variation;
- inference level implied by assignment;
- falsification, diagnostic, and sensitivity plan;
- required data and feasibility checks;
- limits on interpretation and external validity.

Activate `research-historical-measurement` when the treatment, outcome, instrument, running variable, exposure, denominator, or comparison requires historical construction or harmonization. Activate `research-historical-source-criticism` when identification depends on archival or administratively produced records whose coverage or production process may affect the design.

### Step 7: Produce the implementation handoff

Name the implementation skill and pass only design decisions that have been justified. For a DiD design, activate `implementation-difference-in-differences` and provide:

```markdown
## DiD Implementation Handoff
- Target estimand and population:
- Treatment timing and adoption structure:
- Proposed comparison group:
- Parallel-trends assumption: unconditional or conditional
- Pre-treatment covariates and timing:
- Anticipation window:
- Treatment reversibility:
- Spillovers or interference:
- Assignment and clustering level:
- Required cohort and panel coverage:
- Required measurement strategy and alternative measures:
- Source-production and coverage risks:
- Historically plausible effect lags:
- Gate result and unresolved risks:
```

Do not choose `att_gt()`, DRDID, TWFE, bootstrap settings, or reporting formats here unless a design property makes an option mandatory. Those are implementation decisions.

For IV, RDD, panel, or synthetic-control designs, activate `implementation-causal-analysis` and pass:

```markdown
## Causal Implementation Handoff
- Selected design family and identifying variation:
- Target estimand, population, and comparison:
- Assignment process, timing, and institutional rule:
- Core assumptions and strongest threats:
- Required variables, sources, measurement, and sample:
- Fixed effects, controls, or predictors justified by the design:
- Assignment, clustering, spatial, and finite-sample structure:
- Prespecified diagnostics, falsification, and sensitivity:
- Historically plausible effect timing and mechanism:
- Gate result, unresolved risks, and claims not allowed:
```

Add method-specific content: instrument and complier population for IV; running variable, cutoff, and manipulation risks for RDD; remaining within-unit variation and exogeneity for panel models; treated unit, donor criteria, intervention date, and pre-fit requirements for synthetic control. Do not choose software defaults in the handoff unless the identification argument requires them.

## Output structure

```markdown
## Causal Question and Estimand
## Assignment Process and Counterfactual
## Candidate Strategies
## Recommended Identification Strategy
## Rejected Alternatives
## Assumptions
## Threats and Evidence
## Formal Design
## Data and Feasibility Requirements
## Implementation Handoff
## Claims Allowed and Not Allowed
## Design Gate
```

## Rules

- Define the estimand before selecting a design or estimator.
- Always state what variation identifies the effect.
- State each identifying assumption in plain language and formally.
- Distinguish design families from estimators and regression specifications.
- Prefer the strongest defensible claim, not the most elaborate method.
- Treat historical and institutional plausibility as part of identification.
- Never present IV without a first-stage, weak-identification, and reduced-form plan.
- Never validate DiD solely because pre-treatment coefficients are insignificant.
- Return to strategy choice when no causal design passes.
