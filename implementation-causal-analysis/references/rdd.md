# Regression Discontinuity

## 1. Identification handoff

Require:

- running variable and its measurement process;
- binding cutoff and assignment rule;
- sharp, fuzzy, or kink design;
- local target population and estimand;
- treatment timing and no-anticipation logic;
- continuity assumptions and manipulation risks;
- clustering, mass points, and geographic or temporal dependence.

Do not call a design RDD merely because treatment probability changes near a threshold. Verify that the threshold actually governed assignment in the study period.

## 2. Data audit

Before estimation:

- plot treatment probability and outcome against the running variable;
- report observations and unique running-variable values on each side;
- inspect heaping, rounding, censoring, missingness, and support gaps;
- verify cutoff coding and treatment compliance;
- identify institutional exceptions, appeals, or discretionary assignment;
- assess whether observations can sort precisely around the cutoff.

Activate `research-historical-measurement` when the running variable or cutoff was reconstructed, rounded, converted, or administratively revised.

## 3. Main estimation

Use local polynomial methods with data-driven bandwidth selection and robust bias-corrected inference. Local linear estimation is the usual starting point; do not default to global high-order polynomials.

The current `rdrobust` ecosystem provides:

```r
fit_rd <- rdrobust::rdrobust(
  y = analysis_data$outcome,
  x = analysis_data$running,
  c = cutoff
)

bw <- rdrobust::rdbwselect(
  y = analysis_data$outcome,
  x = analysis_data$running,
  c = cutoff
)
```

For fuzzy RDD, specify treatment take-up according to the documented package interface and interpret the local complier effect. Record kernel, polynomial order, bandwidth selector, bias order, covariate adjustment, weights, clustering, and mass-point handling.

## 4. Graphical evidence

Use binned means and local fits for visualization, but do not estimate from the visual bin choice. Show raw support, cutoff, uncertainty, and bandwidth used. Avoid plotting conventions that manufacture or conceal a discontinuity.

## 5. Design diagnostics

Assess:

- treatment discontinuity and compliance;
- running-variable density or manipulation evidence with `rddensity` or an appropriate alternative;
- continuity of predetermined covariates and pre-treatment outcomes;
- other policies or institutional thresholds at the same cutoff;
- donor or comparison observations close enough to the cutoff;
- sensitivity to discrete running variables and few support points.

Covariate continuity tests are diagnostics, not a procedure for selecting only favorable covariates. Multiple diagnostic tests require cautious interpretation.

## 6. Sensitivity

Report:

- alternative bandwidth selectors and transparent bandwidth ranges;
- local polynomial order choices, normally keeping low order;
- kernel sensitivity when material;
- estimates excluding observations extremely close to the cutoff only when a donut design has substantive justification;
- local-randomization analysis when its window and assumptions are defensible;
- placebo cutoffs chosen before examining favorable results;
- influence of mass points, clusters, or boundary observations.

Do not use bandwidth sensitivity as a search for statistical significance.

## 7. Inference and interpretation

Use robust bias-corrected intervals for continuity-based estimation. Respect clustering and discrete support. With few clusters or few mass points, qualify asymptotic inference and consider design-appropriate finite-sample alternatives.

Interpret the effect at the cutoff for units near the threshold. Do not generalize to distant units, other historical periods, or a different assignment regime without evidence.

## Required outputs

- institutional assignment-rule audit;
- support and treatment-probability figures;
- main robust bias-corrected estimate;
- bandwidth and mass-point diagnostics;
- manipulation and predetermined-variable evidence;
- sensitivity and local external-validity statement.

## Official documentation

- `rdrobust`, `rdbwselect`, and `rdplot`: https://rdpackages.github.io/rdrobust/
