# DiD Methodology Reference

## Contents

1. Design handoff
2. Assumptions
3. Estimator selection
4. Aggregation
5. Diagnostics and sensitivity
6. Extensions and boundaries

## 1. Design handoff

Keep three objects distinct:

- **Causal design:** why a comparison identifies a potential-outcome contrast.
- **Estimator:** how sample observations estimate that contrast.
- **Regression specification:** one possible computational representation, not an identification argument.

For staggered adoption, record the cohort $G=g$, calendar period $t$, untreated comparison set available for that cell, and the population represented by $ATT(g,t)$.

## 2. Assumptions

### Parallel trends

State parallel trends for the untreated potential outcome and for the actual comparison used. Distinguish:

- unconditional from covariate-conditional parallel trends;
- never-treated from not-yet-treated comparisons;
- assumptions using one pre-period from assumptions exploiting multiple pre-periods.

Covariates should be determined before treatment and motivated by why trends would otherwise differ. Adding controls mechanically does not repair a failed design.

### No anticipation

Define when units can first respond to treatment. If anticipation is plausible, move the effective treatment boundary back by a prespecified number of periods and revise the comparison set accordingly.

### Treatment path

Callaway-Sant'Anna's standard staggered design treats adoption as absorbing. Detect exits, reversals, dose changes, and intermittent exposure before applying it.

### SUTVA and composition

Assess spillovers across neighboring or linked units, changes in administrative boundaries, migration, attrition, and changing repeated-cross-section composition. These problems may alter the estimand or invalidate the comparison.

### Overlap

Under conditional parallel trends, examine whether treated cohorts and their controls share covariate support. Document trimming and recognize that it changes the target population.

## 3. Estimator selection

### Canonical 2x2

For an unconditional design, the difference in mean outcome changes estimates the ATT under parallel trends and no anticipation. Under conditional parallel trends, prefer a doubly robust estimator from `DRDID`; it remains consistent if either the propensity-score working model or the outcome-regression working model is correctly specified, subject to the remaining design assumptions.

### Staggered adoption

Use `did::att_gt()` to estimate cohort-time effects. Make explicit:

```r
did::att_gt(
  yname = "outcome",
  tname = "period",
  idname = "unit_id",
  gname = "first_treat",
  xformla = ~ x1 + x2,
  data = df,
  panel = TRUE,
  control_group = "nevertreated",
  anticipation = 0,
  est_method = "dr",
  bstrap = TRUE,
  cband = TRUE
)
```

Use not-yet-treated units only when their untreated outcomes provide a defensible comparison and anticipation is handled. Never-treated and not-yet-treated specifications can answer the same target question under different maintained assumptions but may use different support.

### TWFE

A two-group, two-period TWFE regression reproduces the canonical DiD contrast. With staggered timing and heterogeneous effects, conventional TWFE and lead-lag regressions can combine inappropriate comparisons and obscure their weights. Use them only under defended homogeneity restrictions or as clearly labeled benchmarks.

## 4. Aggregation

Use `did::aggte()` only after deciding which summary matches the research question:

- `type = "simple"`: weighted overall effect across available post-treatment cells;
- `type = "group"`: effects summarized by adoption cohort;
- `type = "calendar"`: effects summarized by calendar period;
- `type = "dynamic"`: effects summarized by exposure length.

Dynamic aggregation can change cohort composition at long event times. Prefer a common exposure window when comparing dynamics, and report which cohorts contribute to each event time.

## 5. Diagnostics and sensitivity

### Pre-treatment evidence

Use pseudo-effects and joint tests as evidence about the plausibility of the design, not as proof. Report simultaneous bands for paths with multiple coefficients. Discuss whether the design has enough pre-periods and power to detect violations of substantive concern.

### Required sensitivity checks

Select checks tied to actual threats:

- never-treated versus not-yet-treated controls;
- alternative defensible anticipation windows;
- unconditional versus justified conditional trends;
- doubly robust, regression, and IPW nuisance estimators;
- leave-one-cohort-out or cohort influence;
- balanced versus available panel when attrition matters;
- common event-time windows;
- sensitivity to smooth deviations from parallel trends using `HonestDiD` when appropriate.

Avoid long lists of untargeted robustness regressions.

### Inference

Cluster at the level of treatment assignment or the level implied by the dependence structure. Report the number of clusters. Use multiplier bootstrap and simultaneous confidence bands when supported. With few clusters, explicitly consider finite-cluster methods and qualify inference.

## 6. Extensions and boundaries

Do not force the binary absorbing-treatment workflow onto:

- continuous doses;
- repeated switching or treatment exit;
- triple differences;
- one treated unit with a small donor pool;
- strong spatial or network interference;
- settings with no credible untreated comparison.

Treat `contdid`, specialized switching estimators, triple-difference estimators, or synthetic-control approaches as separate extensions. Re-open causal identification before selecting one.
