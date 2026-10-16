# Worked DiD Examples

## Contents

1. Conditional 2x2 DiD
2. Staggered policy adoption

## 1. Conditional 2x2 DiD

### Request

> Estimate the effect of a land reform introduced in treated districts in 1950 using district outcomes observed in 1945 and 1955. Baseline land concentration and population differ between treated and comparison districts.

### Identification handoff

- Target: ATT for districts treated in 1950.
- Comparison: districts untreated through 1955.
- Assumption: untreated outcome changes would be parallel conditional on 1945 land concentration and population.
- No anticipation: districts could not adjust before 1950.
- Inference: cluster at the district level unless assignment occurred at a higher level.

### Feasibility decisions

Confirm one row per district-period, both periods for each retained district, no treatment contamination among controls, overlap in baseline covariates, and no post-treatment covariates in adjustment.

### Implementation pattern

```r
library(DRDID)

fit_dr <- drdid(
  yname = "outcome",
  tname = "post",
  idname = "district_id",
  dname = "treated",
  xformla = ~ land_concentration_1945 + population_1945,
  data = district_panel,
  panel = TRUE
)
```

Compare the doubly robust estimate with regression-adjustment and IPW variants to diagnose dependence on nuisance-model specification. Inspect propensity-score overlap before interpreting the ATT.

### Reporting

Report the ATT for treated districts, its confidence interval, overlap restrictions, cluster count, and the conditional parallel-trends assumption. Do not generalize the estimate to untreated districts or later reforms.

## 2. Staggered policy adoption

### Request

> Estimate the effect of railway connection on municipal agricultural output when municipalities first received a railway between 1900 and 1930, while some remained unconnected through 1940.

### Identification handoff

- Building block: $ATT(g,t)$ for municipalities first connected in year $g$.
- Primary comparison: never-connected municipalities.
- Secondary sensitivity: not-yet-connected municipalities.
- Assumption: untreated output trends are parallel for each cohort and its comparison group, conditional on prespecified baseline covariates if required.
- Anticipation: allow one period if construction was announced and economically relevant before opening.
- Treatment path: connection is absorbing.

### Feasibility decisions

Construct `first_treat = 0` for never-connected municipalities and the first connection period otherwise. Detect municipalities connected before the panel, duplicate municipality-years, boundary changes, missing cohort coverage, and spillovers to neighboring municipalities.

### Implementation pattern

```r
library(did)

att_gt_fit <- att_gt(
  yname = "agricultural_output",
  tname = "year",
  idname = "municipality_id",
  gname = "first_treat",
  xformla = ~ output_1890 + population_1890,
  data = municipality_panel,
  panel = TRUE,
  control_group = "nevertreated",
  anticipation = 1,
  est_method = "dr",
  bstrap = TRUE,
  cband = TRUE
)

dynamic_fit <- aggte(att_gt_fit, type = "dynamic", min_e = 0, max_e = 10)
cohort_fit <- aggte(att_gt_fit, type = "group")
```

Prespecify the 0-to-10 exposure window because long event times otherwise draw on a changing set of early cohorts. Report group-time effects or their support table before relying on the dynamic summary.

### Diagnostics

- Plot pre-treatment pseudo-effects with simultaneous bands.
- State that failure to reject does not validate parallel trends.
- Compare never-treated with defensible not-yet-treated controls.
- Re-estimate with alternative anticipation windows justified by railway planning history.
- Inspect cohort influence, overlap, attrition, and cluster count.
- Use parallel-trends sensitivity analysis if modest deviations would overturn the conclusion.

### TWFE benchmark

A conventional TWFE event study may be reported only as a benchmark. Label its additional homogeneity restrictions and do not use agreement or disagreement with it as the sole validity criterion.

### Reporting

Interpret the dynamic aggregation as effects by time since connection for the contributing cohorts. Separate the identified effect of railway access from the broader historical transformation of agrarian markets, which requires mechanism and contextual evidence.
