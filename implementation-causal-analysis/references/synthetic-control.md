# Synthetic-Control Methods

## 1. Select the design family

Distinguish:

- classical synthetic control for one or few treated units;
- augmented synthetic control when outcome modeling is used to reduce imbalance bias;
- synthetic difference-in-differences for supported block-treatment panels;
- generalized or staggered extensions, which require their own assumptions and software checks.

Do not treat these estimators as interchangeable. Define the treatment-effect target and treatment-timing structure first.

## 2. Identification handoff

Require:

- treated unit or treated block and intervention date;
- donor-pool construction before outcome inspection;
- no anticipation and no donor contamination or spillovers;
- sufficiently long and relevant pre-treatment period;
- outcome and predictor comparability;
- stable measurement and boundaries;
- target post-treatment horizon;
- inference population and placebo logic.

Re-open identification when no convex or substantively credible donor combination approximates the untreated trajectory.

## 3. Donor and predictor design

Document:

- inclusion and exclusion criteria for donors;
- exposure to related policies, shocks, migration, trade, or ecological spillovers;
- predictor choice and temporal aggregation;
- outcome lags used for fit;
- unit and time weights;
- whether negative weights or extrapolation are permitted by the method;
- historical comparability of institutional and measurement regimes.

Never choose donors, predictors, or pre-period windows using post-treatment fit.

## 4. Pre-treatment fit

Report:

- treated and synthetic trajectories;
- pre-treatment RMSPE or method-appropriate loss;
- predictor and outcome balance;
- donor weights and concentration;
- leave-one-donor-out sensitivity;
- placebo pre-fit distribution.

Poor pre-fit changes the credibility or estimand; it is not repaired by a visually large post-treatment gap.

## 5. Estimator implementation

Use a package whose maintained method matches the selected design. Record its version and interface because synthetic-control packages differ materially.

For the currently documented block-treatment interface in `synthdid`:

```r
setup <- synthdid::panel.matrices(panel_data)
fit_sdid <- synthdid::synthdid_estimate(setup$Y, setup$N0, setup$T0)
```

The package documentation currently describes `synthdid` as beta and requires all treated units to begin simultaneously for this interface. Do not apply it mechanically to staggered adoption. Use classical or augmented SCM packages only after checking their current documentation and assumptions.

## 6. Inference and placebo evidence

Use design-compatible procedures:

- in-space placebo reassignment;
- in-time placebo only when anticipation and structural stability make it meaningful;
- RMSPE-scaled placebo comparisons;
- jackknife, bootstrap, conformal, or method-provided variance only under their documented conditions;
- exact or randomization-style inference when the assignment interpretation supports it.

Report the number of credible placebo units and exclude placebos with unacceptable pre-fit using a prespecified rule. A rank or pseudo-p value based on a tiny donor pool requires strong qualification.

## 7. Sensitivity

Assess:

- donor exclusions and leave-one-out results;
- predictor and pre-period choices fixed without post-treatment tuning;
- alternative measurement and boundary harmonization;
- anticipation and post-treatment horizon;
- spillover-contaminated donors;
- classical, augmented, and SDID estimates only when they target compatible effects;
- influential donor or time weights.

## 8. Interpretation

The estimate concerns the treated unit or treated block under the constructed counterfactual. Do not generalize from one country, region, watershed, firm, or historical episode without a separate external-validity argument.

## Required outputs

- donor-pool and contamination audit;
- pre-treatment fit and balance report;
- donor and time weights;
- treated-versus-synthetic figure;
- placebo and sensitivity evidence;
- local historical interpretation and generalization limits.

## Official documentation

- `synthdid`: https://synth-inference.github.io/synthdid/
