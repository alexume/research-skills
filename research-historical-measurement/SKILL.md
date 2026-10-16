---
name: research-historical-measurement
description: "Design and audit historical measures by translating concepts into indicators while documenting source definitions, units, populations, classifications, prices, boundaries, aggregation, uncertainty, and comparability over time and space. Use when Codex must construct or evaluate variables from historical or environmental sources, harmonize series, build a measurement strategy or variable dictionary, assess proxies, or determine whether an empirical measure matches a causal, structural, or socioecological concept."
---

# Historical Measurement

Design measurements that preserve the relationship between concept, historical source, transformation, analytical variable, and claim. A clean number is not necessarily a valid or comparable measure.

## Workflow position

Use this skill at:

- Stage 4 to diagnose available measures and comparability risks;
- Stage 7 to define the measurement strategy before implementation;
- Stages 8-9 to specify requirements and approve harmonization rules;
- Stage 10 to audit whether feasible measures still match the target estimand or structural claim;
- Stages 11-12 to interpret measurement sensitivity.

Coordinate with `research-historical-source-criticism` for source production and coverage, `research-causal-identification` or `research-structural-analysis-design` for the target concept, and `data-preparation` for execution.

## Required inputs

Recover or request:

- concept, mechanism, estimand, or historical pattern;
- target population, unit, geography, period, and frequency;
- candidate sources and their source-criticism status;
- original categories, units, prices, boundaries, and aggregation level;
- intended comparisons across time, place, groups, or sources;
- known transformations and uncertainty.

Do not begin harmonization without an explicit target comparison.

## Step 1: Define the measurement target

Write:

- conceptual definition;
- empirical object actually observable;
- target population and unit;
- temporal and spatial scale;
- desired interpretation and excluded interpretations;
- mechanism linking the measure to the research claim.

Distinguish outcomes, treatments, exposures, mechanisms, confounders, contextual indicators, and proxies.

## Step 2: Build the measurement chain

Document:

```text
concept
→ observable implication
→ source field or category
→ extraction rule
→ correction or harmonization
→ aggregation
→ analytical variable
→ permitted claim
```

Assign a stable identifier to each source variable and derived variable. Preserve original values and categories alongside transformed versions.

## Step 3: Audit validity

Assess separately:

- **construct validity:** whether the variable represents the intended concept;
- **content validity:** which dimensions are included or omitted;
- **comparability:** whether meaning is stable across observations;
- **coverage:** which population, territory, period, or ecological flow is observed;
- **resolution:** whether aggregation matches the mechanism and claim;
- **reliability:** whether repeated measurement would be consistent;
- **measurement error:** likely direction, structure, and consequences.

Do not label a proxy valid merely because it is correlated with the concept.

## Step 4: Design harmonization

Specify rules for relevant dimensions:

- physical units and conversion factors;
- nominal currencies, exchange rates, price bases, and deflators;
- quantities versus values and current versus constant prices;
- population denominators and exposure time;
- occupational, commodity, land-use, disease, or social classifications;
- administrative and ecological boundary changes;
- calendar, fiscal, agricultural, or hydrological years;
- stocks versus flows and gross versus net measures;
- missing, zero, censored, bounded, estimated, or imputed observations.

Never apply a conversion or crosswalk without recording source, formula, domain, and uncertainty.

## Step 5: Address scale and aggregation

Evaluate:

- whether aggregation hides distribution or heterogeneity;
- whether denominators change with treatment or historical process;
- ecological fallacy and modifiable areal-unit risks;
- consistency between source geography and analytical geography;
- whether annualization or interpolation invents temporal precision;
- whether material-flow boundaries avoid double counting.

Use crosswalks with explicit weights and residual unmatched shares. Report sensitivity to defensible alternative crosswalks.

## Step 6: Represent uncertainty

Classify uncertainty from:

- source coverage;
- transcription or OCR;
- category mapping;
- conversion factor;
- boundary allocation;
- deflator or benchmark choice;
- imputation or interpolation;
- model-based reconstruction.

Preserve flags at observation level where possible. Use ranges, alternative series, scenarios, or probabilistic propagation when a single corrected value would conceal material uncertainty.

## Step 7: Validate and stress-test

Check:

- arithmetic identities and plausible ranges;
- totals against components and independent benchmarks;
- breaks aligned with definition or institutional changes;
- alternative denominators, deflators, crosswalks, and category mappings;
- heaping, rounding, censoring, and suspicious repetition;
- consequences for the target estimand, trend, ranking, or mechanism.

A robustness check should vary a defensible measurement decision, not an arbitrary coding choice.

## Outputs

Produce or update:

- `analysis/measurement_strategy.qmd`;
- `data/metadata/variable_dictionary.csv`;
- `data/metadata/measurement_decisions.csv`;
- `analysis/preparation_manifest.md` with approved transformations;
- `analysis/feasibility.qmd` with measurement-related limits.

Use this report structure:

```markdown
## Concept and Measurement Target
## Source Variables and Provenance
## Measurement Chain
## Validity and Coverage
## Units, Prices, Categories, and Boundaries
## Harmonization Rules
## Uncertainty and Flags
## Validation and Alternative Measures
## Claims Supported and Not Supported
## Measurement Gate
```

## References

- Read `references/harmonization-guide.md` for common historical and socioecological measurement problems.
- Read `references/examples.md` for worked land and material-flow examples.

## Rules

- Define the intended comparison before harmonizing.
- Preserve original, corrected, harmonized, and derived values separately.
- Never mix quantities and values or stocks and flows without explicit definitions.
- Never hide changing boundaries, categories, or denominators behind a stable variable name.
- Never use post-treatment information to construct a baseline causal variable without justification.
- Record every nontrivial transformation in the measurement decision log.
- Return to research design when the feasible measure changes the concept, estimand, population, scale, or period.
