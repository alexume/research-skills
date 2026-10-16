# Panel Models

## 1. Identification handoff

Panel data and fixed effects do not constitute an identification strategy by themselves. Require:

- causal question and estimand;
- source of within-unit variation;
- timing of treatment, exposure, outcome, and covariates;
- strict, sequential, or other exogeneity assumptions;
- unit entry, exit, attrition, and composition;
- relevant fixed effects and what variation remains;
- serial, spatial, and cross-sectional dependence.

Route staggered binary policy adoption and event studies to `implementation-difference-in-differences`.

## 2. Select the panel specification

Distinguish:

- unit fixed effects for time-invariant unit heterogeneity;
- time fixed effects for common period shocks;
- first differences for changes between periods;
- correlated random-effects or Mundlak formulations when between-unit information is substantively useful;
- unit-specific trends only when their identifying restrictions and loss of signal are defensible;
- distributed-lag models for prespecified dynamic exposure;
- dynamic panels with lagged outcomes, which require explicit treatment of short-panel bias and stronger assumptions.

Do not add fixed effects or trends as generic robustness controls. State what each absorbs and what identifies the coefficient afterward.

## 3. Data and variation audit

Report:

- unit and time counts, panel balance, entry, exit, and gaps;
- within- and between-unit variation for each key variable;
- number of units that actually switch or change exposure;
- timing, persistence, and reversals;
- support after fixed effects and controls;
- missingness and attrition by exposure and outcome history;
- influential units and periods.

A precisely estimated coefficient based on few switchers should not be presented as broad panel evidence.

## 4. Implementation

For a standard two-way FE specification:

```r
fit_fe <- fixest::feols(
  outcome ~ exposure + x1 + x2 | unit_id + period,
  data = analysis_data,
  vcov = ~ assignment_cluster
)
```

Record formula, fixed effects, weights, panel restrictions, missing-value sample, clustering, and absorbed variation. Compare first differences or correlated random effects when those target the same parameter under defensible assumptions.

## 5. Threats and diagnostics

Assess:

- time-varying confounding;
- reverse causality and feedback;
- treatment anticipation and lag structure;
- measurement error amplified by differencing;
- serial correlation and common shocks;
- cross-sectional or spatial dependence;
- heterogeneous effects and weighting of within-unit changes;
- endogenous attrition and changing unit definitions.

Residual plots or significance tests do not validate strict exogeneity. Use timing, institutional evidence, negative controls, alternative lags, and design-specific falsification where meaningful.

## 6. Dynamic and lagged models

Choose lags from the mechanism and observation frequency, not fit alone. Report the contemporaneous and cumulative estimand clearly. Avoid conditioning on post-treatment mediators.

Lagged dependent variables with unit fixed effects can be biased in short panels. Do not use them automatically; justify an appropriate estimator and its instrument or moment assumptions, and report sensitivity to panel length and instrument proliferation when relevant.

## 7. Inference

Cluster according to treatment assignment and error dependence, not automatically by unit. Consider two-way, spatial, or common-shock dependence where justified. Report cluster counts and finite-cluster limitations. Time fixed effects do not eliminate all cross-sectional dependence.

## 8. Reporting

Report within-unit variation, switcher population, fixed effects, sample changes, cluster count, effect timing, and the remaining identifying assumption. Separate descriptive panel associations from bounded causal estimates.

## Required outputs

- panel and variation audit;
- fixed-effect absorption and identifying-variation statement;
- main and compatible alternative specifications;
- timing, attrition, and dependence diagnostics;
- effect heterogeneity and influential-unit sensitivity;
- bounded causal interpretation.
