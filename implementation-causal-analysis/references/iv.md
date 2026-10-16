# Instrumental Variables

## 1. Identification handoff

Require:

- endogenous treatment or exposure;
- instrument and assignment process;
- target population and intended parameter;
- relevance, exclusion, independence, and monotonicity assumptions when interpreting LATE;
- treatment, instrument, and outcome timing;
- assignment and clustering level;
- potential direct effects, spillovers, defiers, and heterogeneous compliance.

Distinguish an instrument for treatment from a proxy for treatment. Historical timing or geographic distance is not exogenous by label.

## 2. Estimands

State whether the target is:

- a constant-effect structural coefficient under strong homogeneity assumptions;
- a local average treatment effect for compliers;
- a reduced-form intention-to-treat effect;
- an effect under heterogeneous treatment intensity or multiple instruments.

Describe compliers institutionally and historically. Do not generalize LATE to all treated or all units without additional assumptions.

## 3. Core estimates

Always report:

1. first stage with coefficient, uncertainty, partial fit, and relevant excluded-instrument statistic;
2. reduced form with the instrument's effect on the outcome;
3. 2SLS or selected IV estimate;
4. OLS or descriptive association only as a labeled comparison;
5. sample, fixed effects, controls, weights, and inference for all stages.

For a conventional model, the current `ivreg` interface supports:

```r
fit_iv <- ivreg::ivreg(
  outcome ~ treatment + x1 + x2 | instrument + x1 + x2,
  data = analysis_data
)
```

Exogenous regressors must also enter the instrument set. Use `fixest::feols()` when high-dimensional fixed effects or its supported IV syntax are needed, but preserve separate first-stage and reduced-form outputs.

## 4. Instrument strength

Do not reduce assessment to `F > 10`.

Report diagnostics appropriate to:

- one or multiple endogenous regressors;
- homoskedastic, heteroskedastic, clustered, or serially correlated errors;
- excluded instruments conditional on controls and fixed effects;
- effective sample and assignment-level variation.

Use weak-identification-robust confidence sets or tests, such as Anderson-Rubin or CLR-type procedures, when conventional normal approximations may be unreliable. If the available R implementation cannot provide a diagnostic under the actual clustering structure, report that limitation rather than substituting an incompatible statistic.

## 5. Exclusion and independence

These assumptions are not validated by first-stage strength. Build a threat table covering:

- direct channels from instrument to outcome;
- shared causes of instrument and outcome;
- endogenous instrument timing or location;
- differential measurement or sample selection;
- spillovers and equilibrium effects;
- institutional changes bundled with the instrument.

Use balance, placebo outcomes, pre-period outcomes, alternative samples, and mechanism evidence only as probes. Overidentification tests do not prove that all instruments are valid and can be misleading when violations share direction.

## 6. Multiple instruments and specifications

- Justify each instrument separately.
- Report first stages by endogenous regressor.
- Examine whether instruments identify different complier populations.
- Avoid adding instruments solely to increase the first-stage statistic.
- Report sensitivity to instrument subsets when substantively defensible.
- Diagnose influential observations and instrument leverage.

## 7. Inference and reporting

Cluster at the level generating instrument variation or treatment assignment, as justified by the design. Address few clusters, spatial dependence, and generated instruments explicitly. Report conventional and weak-IV-robust inference when they differ materially.

Interpret the estimate in outcome units per treatment unit for the represented complier population. Keep reduced-form evidence visible even when 2SLS is imprecise.

## Required outputs

- first-stage table;
- reduced-form table;
- IV estimate and weak-identification-robust inference;
- instrument validity threat table;
- complier interpretation;
- influence and instrument-subset sensitivity where relevant.

## Official documentation

- `ivreg`: https://zeileis.github.io/ivreg/
