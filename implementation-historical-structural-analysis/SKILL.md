---
name: implementation-historical-structural-analysis
description: "Implement an approved historical-structural or hybrid research design by establishing temporal, spatial, compositional, institutional, and socioecological patterns; testing periodization; triangulating heterogeneous evidence; evaluating mechanisms and rival interpretations; and producing reproducible structural-analysis outputs. Use after research-structural-analysis-design, source criticism, measurement, and preparation have defined what evidence can support."
---

# Historical-Structural Analysis Implementation

Execute a historical-structural design as a disciplined empirical explanation. Establish patterns before interpreting them, preserve contradictions and uncertainty, and distinguish evidence for sequence and mechanism from causal identification in a narrow econometric sense.

## Workflow position

Use this skill at:

- Stage 10 to assess whether the prepared evidence can establish the proposed patterns and evaluate the mechanisms;
- Stage 11 to implement the historical-structural analysis;
- the structural component of a hybrid route alongside its selected causal implementation skill.

Consume:

- `analysis/structural_analysis_design.qmd`;
- `analysis/mechanism_map.qmd`;
- `analysis/source_criticism.qmd` and the historical source registry;
- `analysis/measurement_strategy.qmd` and variable dictionary;
- `analysis/preparation_manifest.md` and data validation;
- prepared quantitative, documentary, spatial, and environmental evidence;
- hypotheses or propositions and competing interpretations.

Return to structural design when feasible evidence changes the process, periodization, scale, core pattern, or intended explanatory claim.

Read `project/project_profile.yaml` and `../shared/r_code_style.md` for all computational components. The shared R standard applies to quantitative, spatial, textual-processing, table, figure, and map code; it does not force a quantitative operation where source-based analysis is more appropriate.

## Step 1: Build the structural evidence matrix

Create `analysis/structural_evidence_matrix.csv` with one row per pattern, mechanism step, rival interpretation, or limit. Record:

- stable analytical object and claim identifiers;
- period, geography, population, sector, actor, and scale;
- source and exact locator;
- measurement or coding decision;
- evidentiary role: direct, indirect, contrastive, illustrative, or insufficient;
- independence from other evidence;
- uncertainty and known contradiction;
- output in which the evidence appears.

Do not count multiple derivatives of one administrative series as independent corroboration.

## Step 2: Apply structural feasibility

Audit whether the available evidence can:

1. establish every core pattern across its claimed period and scale;
2. distinguish a real transition from changes in source coverage, categories, boundaries, or measurement;
3. observe the actors, institutions, mediations, and sequence required by each mechanism;
4. evaluate at least one serious rival interpretation;
5. support comparisons without forcing incompatible cases or sources into one metric;
6. disclose unresolved gaps without making the central explanation circular.

Return `pass`, `conditional pass`, or `fail` in `analysis/feasibility.qmd`. A conditional pass must narrow a period, scale, population, pattern, mechanism, or claim.

## Step 3: Establish empirical patterns

Analyze separately before synthesis:

- temporal levels, rates, cycles, breaks, lags, and persistence;
- spatial concentration, diffusion, frontiers, networks, and boundary effects;
- compositional change among sectors, groups, commodities, land uses, or material flows;
- distribution across classes, regions, institutions, or ecological systems;
- institutional rules, organizational capacities, and state or market practices;
- material and socioecological stocks, flows, pressures, and transformations.

Use appropriate descriptive uncertainty, denominators, weights, price bases, spatial units, and source-regime flags. Never infer a structural break solely from a visually convenient date or a change in documentation.

## Step 4: Evaluate periodization

Treat the design periodization as a proposition to assess. For each proposed boundary:

- state which indicators, events, institutional changes, or actor strategies change;
- identify anticipatory developments and delayed effects;
- test whether different dimensions change simultaneously or asynchronously;
- compare with plausible alternative boundaries;
- distinguish historical turning points from data-availability boundaries.

Revise periodization explicitly in `analysis/structural_analysis_log.csv`; do not retrofit periods to preferred results.

## Step 5: Compare cases and scales

Choose comparisons for analytical leverage, not convenience. Use as appropriate:

- within-case comparison across periods;
- subnational or cross-case comparison;
- positive, negative, deviant, or shadow cases;
- nested comparison across local, regional, national, commodity-chain, or ecological scales.

For every comparison, state what is held comparable, what differs, and which inference it permits. Absence of an outcome or mechanism step may be informative only when evidence could have observed it.

## Step 6: Triangulate heterogeneous evidence

Integrate quantitative series, archival records, maps, administrative reports, material-flow evidence, and literature without flattening their different production processes. Classify convergence as:

- independent corroboration;
- complementary evidence for different mechanism steps;
- apparent agreement from a shared source;
- unresolved contradiction;
- incommensurable evidence.

Investigate contradiction through definitions, timing, scale, incentives, survival, and transformation before choosing one source. Retain unresolved disagreement in the results.

## Step 7: Evaluate mechanisms and rival interpretations

For each mechanism, reconstruct:

```text
initial conditions -> actors and capacities -> institutional or material change
-> mediating processes -> observed structural pattern -> feedback or persistence
```

Assess temporal order, actor evidence, institutional plausibility, scale fit, intermediate traces, and counterevidence. Use `research-mechanism-mapping` to update the mechanism map. A pattern consistent with a mechanism is not by itself evidence that the mechanism operated.

Evaluate rival explanations against the same evidence matrix. State what evidence discriminates, what remains observationally equivalent, and whether the final explanation is established, supported, plausible, or unresolved.

Read `references/analytical-operations.md` and `references/evidence-and-inference.md` for detailed implementation decisions.

## Step 8: Produce reproducible outputs

Update:

- `analysis/structural_patterns.qmd`;
- `analysis/structural_evidence_matrix.csv`;
- `analysis/structural_analysis_log.csv`;
- `analysis/mechanism_map.qmd`;
- `analysis/claim_evidence_map.qmd` when claims are ready;
- scripts, analytical objects, tables, figures, and maps.
- `analysis/r_code_quality.md`, `tables/table_manifest.csv`, and `figures/figure_manifest.csv` for computational and presentation outputs.

Use this report structure:

```markdown
## Structural Question and Design Handoff
## Feasibility Gate
## Evidence Base and Comparability
## Periodization Assessment
## Temporal Patterns
## Spatial and Compositional Patterns
## Institutional and Socioecological Patterns
## Comparative Analysis
## Triangulation and Contradictions
## Mechanisms and Rival Interpretations
## Uncertainty and Limits of Inference
## Results Gate
```

Activate `implementation-tables-and-appendices`, `implementation-figures`, and `research-reproducibility-and-replication` for presentation and execution. Read `references/examples.md` for agrarian and environmental examples.

## Rules

- Never treat chronology as explanation.
- Never equate a trend, correlation, or break with a mechanism.
- Never hide source-regime, classification, boundary, or coverage changes.
- Never average incompatible evidence to manufacture agreement.
- Never make a causal claim stronger than the design and evidence permit.
- Never let one vivid source establish prevalence or representativeness.
- Preserve negative, contradictory, missing, and mechanism-inconsistent evidence.
- Never pass `G-RESULTS` when required code-quality or generated-output checks are missing or not assessed.
