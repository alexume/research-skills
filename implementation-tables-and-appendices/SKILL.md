---
name: implementation-tables-and-appendices
description: "Create, standardize, and audit publication-ready academic tables and analytical appendices from registered models, structural evidence, diagnostics, and sensitivity analyses. Use when Codex must turn analytical objects into traceable R and Quarto outputs, organize main versus appendix evidence, produce consistent notes and uncertainty reporting, or verify that manuscript tables and appendices match the reproducible analysis."
---

# Tables and Analytical Appendices

Turn analytical evidence into compact, auditable outputs without allowing presentation code or manual editing to redefine results. Every displayed value must trace to a registered analytical object, source, or reproducible transformation.

## Workflow position

Use this skill at Stage 11 for analytical output production, Stage 13 for manuscript integration, Stage 17 for replication and consistency audit, and Stage 19 after analytical revision.

Consume as applicable:

- `project/project_profile.yaml`;
- `analysis/model_registry.csv` and `analysis/specification_log.csv`;
- `analysis/results.qmd` or `analysis/structural_patterns.qmd`;
- fitted model and diagnostic objects;
- structural evidence and source registries;
- measurement and inference plans;
- target journal and manuscript argument;
- `shared/output_styles.md`, `shared/r_code_style.md`, `shared/output_contracts.md`, and replication requirements.

## Step 1: Design the output architecture

Assign every proposed table a stable identifier and one primary purpose:

- data and source coverage;
- descriptive pattern;
- main causal estimate or structural comparison;
- design diagnostic;
- mechanism or heterogeneity evidence;
- sensitivity or alternative construction;
- source, measurement, or harmonization audit;
- appendix documentation.

Decide main text versus appendix using argumentative necessity, not statistical significance. A main table should support a central claim or required design assessment. The appendix should preserve diagnostic and sensitivity evidence, not bury failures.

Create `tables/table_manifest.csv` before final formatting.
Assign one status to every registered item: `main`, `appendix`, or `excluded`. Retain excluded or failed outputs when they document a material analytical decision.

## Step 2: Define the table contract

For each table record:

- title, purpose, and linked claim;
- source datasets or evidence identifiers;
- model, specification, comparison, or transformation identifiers;
- sample, population, period, geography, and unit;
- displayed statistics, uncertainty, and precision;
- row and column order;
- notes, abbreviations, source statement, and limitations;
- generation script or pipeline target;
- output formats and manuscript location.
- stable Quarto label and every manuscript or appendix cross-reference.

Do not build a table from values copied out of console output or a manuscript draft.

## Step 3: Generate from analytical objects

Generate tables in R through a maintained package or explicit data-frame transformation appropriate to the output. `modelsummary`, `tinytable`, `gt`, or estimator-specific extractors may be used when their current interface fits the project. Preserve a tidy analytical table before styling.

Follow `../shared/r_code_style.md`, including its readable-transformation rules
and proportional check scope. Keep the calculation of the tidy analytical table
visible before presentation formatting. Consult `../shared/r_code_examples.md`
for a supported aggregation. Adapt examples to the requested output; do not build
a configurable table framework for a single table. Reuse formatting functions
only when there is actual repetition.

Require:

- deterministic row and column ordering;
- explicit coefficient or statistic selection;
- stable labels separated from source variable names;
- declared missing, suppressed, unavailable, and not-applicable values;
- no hidden rounding before calculations;
- explicit format-specific rendering;
- one pipeline target or script owning each output.

Read `references/table-generation.md` before implementation.

## Step 4: Report uncertainty and design information

For causal tables include, where applicable:

- estimand, estimate, confidence interval, and units;
- sample size, treated or comparison counts, cohorts, and periods;
- assignment and cluster levels with cluster counts;
- fixed effects, controls, weights, bandwidth, instrument, donor, or aggregation choices;
- weak-identification, simultaneous-band, finite-sample, or sensitivity status.

For historical-structural tables include, where applicable:

- pattern or comparison and its periodization;
- geography, population, denominator, price or physical basis;
- source regime, coverage, and comparability flags;
- evidence role and independence;
- uncertainty, contradiction, or missing-source status;
- mechanism or rival-interpretation linkage.

Do not communicate evidentiary strength through significance stars alone.

## Step 5: Build the analytical appendix

Create or update `appendix/analytical_appendix.qmd` with a navigable sequence:

```markdown
# Data, Sources, and Measurement
# Design and Estimator Details
# Additional Descriptive or Structural Evidence
# Diagnostics and Falsification
# Sensitivity and Alternative Specifications
# Heterogeneity and Mechanism Evidence
# Additional Tables and Figures
# Reproducibility and Access Notes
```

Include only sections relevant to the route. Each appendix item must be called from the text, support a registered claim or design decision, or document a material limitation. Do not use the appendix as an unstructured output dump.

## Step 6: Write complete notes

Table notes must define:

- outcome, exposure, treatment, comparison, or pattern;
- unit, sample, geography, period, and exclusions;
- estimator or calculation;
- uncertainty and clustering;
- weights, fixed effects, controls, or measurement basis;
- source and transformation provenance;
- symbols, abbreviations, and rounding;
- relevant limitations and appendix cross-references.

Notes should make the table interpretable without duplicating the full methods section.

## Step 7: Audit consistency and accessibility

Check:

- displayed values against underlying objects before formatting;
- manuscript numbers, signs, units, sample sizes, and labels against tables;
- main and appendix specifications against the model and specification registries;
- notes against actual inference and sample definitions;
- table width, pagination, font size, contrast, and grayscale legibility;
- HTML, PDF/LaTeX, or DOCX outputs required by the journal;
- every format required by `project/project_profile.yaml`, with PDF mandatory under the default profile;
- generated files against `replication/manifest.csv`.

Use stable Quarto labels and cross-references by default, for example `#| label: tbl-main-results` and `@tbl-main-results`. Use raw LaTeX only when the project profile or target journal explicitly requires it. A table that exists but is missing, clipped, stale, or uncited in the required PDF fails the audit.

Use exact comparisons before rounding and declared tolerances after rendering. A visually correct table with stale values fails the audit.

Read `references/audit-checklist.md` and `references/examples.md` for implementation patterns.

## Outputs

- `tables/table_manifest.csv`;
- machine-readable table data in `tables/data/` where useful;
- publication outputs in `tables/`;
- `appendix/analytical_appendix.qmd`;
- appendix tables and figures;
- updated replication manifest and manuscript cross-references.
- updated `analysis/r_code_quality.md` status for table-generation code.

## Rules

- Never edit generated numerical values manually.
- Never select table content by significance or preferred sign.
- Never hide a failed diagnostic or material sensitivity only because it complicates presentation.
- Never mix estimates of different parameters under one unlabeled coefficient row.
- Never omit units, samples, uncertainty, or source provenance needed for interpretation.
- Never allow main text, appendix, and replication outputs to disagree.
- Never declare a table integrated without a manifest status, stable cross-reference, and successful required-format render check.
- Prefer a small number of purpose-driven tables to wide specification grids.
