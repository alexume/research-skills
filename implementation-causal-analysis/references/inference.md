# Causal Inference and Reporting

## 1. Start from assignment and dependence

Choose uncertainty procedures from:

- treatment or instrument assignment level;
- sampling design and weights;
- repeated observations within units;
- common time shocks;
- spatial, network, market, watershed, or institutional dependence;
- number and balance of clusters;
- estimator-specific asymptotics.

Do not choose heteroskedastic, clustered, two-way, spatial, bootstrap, or randomization inference solely because a package makes it easy.

## 2. Few clusters and finite samples

Always report cluster count and cluster-size imbalance. With few assignment-level clusters, conventional cluster-robust normal approximations may be unreliable. Consider method-compatible small-sample corrections, wild cluster bootstrap, randomization inference, or explicitly limited inference. Do not substitute clustering at a lower level to manufacture many clusters.

## 3. Spatial and common-shock dependence

Historical economic and environmental data often share markets, weather, policies, watersheds, borders, or measurement systems. Time fixed effects absorb common means, not arbitrary cross-sectional dependence. Justify spatial cutoffs, multiway clustering, or aggregation using the mechanism and data-generating process.

## 4. Multiplicity and researcher decisions

Prespecify the main outcome, estimand, horizon, subgroup, and specification. Distinguish confirmatory, supporting, and exploratory families. Use family-wise, false-discovery, or simultaneous inference when the claim depends on multiple comparisons. Do not correct mechanically across unrelated descriptive outputs.

## 5. Missing and generated quantities

Inference must account for estimated weights, imputation, crosswalks, generated instruments, first-stage models, or reconstructed outcomes when these affect uncertainty. When full propagation is infeasible, use sensitivity scenarios and state that conventional intervals are conditional on measurement decisions.

## 6. Reporting minimum

Report:

- point estimate, confidence interval, units, and estimand;
- sample and target population;
- assignment and cluster levels with counts;
- weights and dependence assumptions;
- finite-sample or asymptotic basis;
- multiplicity family when relevant;
- measurement uncertainty included or omitted;
- failed, undefined, or incompatible inference procedures.

Prefer effect magnitudes and confidence intervals to star-centered tables. A null result can be informative, underpowered, weakly identified, or inconsistent with a meaningful effect; distinguish these cases.
