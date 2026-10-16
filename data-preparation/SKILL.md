---
name: data-preparation
description: "Create analysis-ready research data in R through immutable raw-input handling, schema and key validation, traceable cleaning, controlled historical harmonization, variable construction, linkage, quality checks, and preparation manifests. Use when Codex must import and normalize source files, execute approved measurement decisions, merge datasets, construct variables, preserve lineage, diagnose failed joins, or produce validated clean and interim data without silently changing the research population or source evidence."
---

# Data Preparation

Transform source data into analysis-ready datasets while preserving provenance, original values, measurement decisions, and the ability to reconstruct every derived variable.

## Required inputs

Recover or create:

- source inventory and immutable raw files;
- acquisition manifest with verified provider, version, rights, and requirement coverage;
- acquisition version and access conditions;
- expected unit of observation, keys, and coverage;
- source-criticism report when historical records are involved;
- measurement strategy and variable dictionary;
- design-specific population, period, geography, and support requirements;
- approved exclusions, crosswalks, conversion factors, and derived-variable rules.

Return to `research-historical-source-criticism` or `research-historical-measurement` rather than inventing substantive corrections during cleaning.

Return to `research-evidence-discovery-and-acquisition` when an acquired file is missing, corrupted, undocumented, the wrong version, or materially different from the verified requirement.

## Step 1: Protect and inventory raw inputs

- Never overwrite files in `data/raw/`.
- Record filename, source identifier, acquisition date, version, size, encoding, format, and sheet or table structure.
- Preserve original compressed files, images, and metadata where permitted.
- Distinguish provider files from locally transcribed or manually entered files.
- Record access, licensing, privacy, and redistribution restrictions.

Create stable names without changing file content. If a source is replaced, retain or explicitly version the prior input.

## Step 2: Define schema and keys

For each input and intended output, specify:

- unit of observation;
- primary and candidate keys;
- expected row cardinality;
- variable names, types, units, labels, and allowed values;
- geographic, temporal, and population coverage;
- missing-value codes;
- uniqueness, range, and relational constraints.

Check whether the observed file conforms before transforming it. Do not resolve duplicate keys by arbitrary row deletion.

## Step 3: Import and preserve source values

- Detect format, delimiter, decimal mark, encoding, headers, footnotes, merged cells, and formulas.
- Import source columns with lossless types where possible.
- Retain original text fields and create parsed versions separately.
- Preserve source row, page, table, image, or record identifiers.
- Distinguish blank, zero, not applicable, illegible, censored, suppressed, and unrecorded values when the source permits.

Do not convert ambiguous source codes to `NA` before recording their original meaning.

## Step 4: Normalize structure

Apply documented rules for:

- column names and stable identifiers;
- dates and reference periods;
- character normalization without erasing historical categories;
- wide-to-long or long-to-wide reshaping;
- repeated headers, notes, subtotals, and totals;
- duplicates and conflicting records;
- obvious transcription corrections supported by source evidence.

Keep source values, corrected values, and correction flags separate.

## Step 5: Execute approved harmonization

Use `analysis/measurement_strategy.qmd` and the measurement decision log for:

- currencies, deflators, and price bases;
- physical units and conversion factors;
- classifications and category crosswalks;
- boundary and geographic crosswalks;
- population denominators and exposure time;
- fiscal, agricultural, hydrological, and calendar periods;
- stocks, flows, gross values, and net values.

For every transformation, retain formula, source, valid domain, uncertainty flag, and alternative version when required. Do not hide definition changes behind one continuous series.

## Step 6: Construct variables with lineage

For each derived variable, record:

- stable name and definition;
- conceptual role;
- source variables and datasets;
- formula and temporal ordering;
- missing-value propagation;
- unit, denominator, price basis, geography, and population;
- flags, assumptions, and responsible measurement decision;
- claims or models for which it is intended.

Prevent post-treatment or future information from entering baseline causal variables unless the design explicitly justifies it.

## Step 7: Link and merge

Before joining:

1. declare key and expected cardinality: one-to-one, one-to-many, many-to-one, or intentionally many-to-many;
2. standardize keys through documented crosswalks;
3. test key uniqueness on the required side;
4. report matched, left-only, right-only, ambiguous, and duplicate matches;
5. inspect match rates by time, place, group, and source regime;
6. verify row counts, coverage, and totals after the join.

Do not accept a high aggregate match rate when unmatched observations are concentrated in analytically important populations.

## Step 8: Validate outputs

Run and report:

- schema, type, key, and allowed-value checks;
- row, unit, period, geography, and group coverage;
- arithmetic identities and total conservation;
- range, monotonicity, and temporal-ordering rules;
- merge cardinality and unmatched shares;
- source-to-clean spot checks;
- sensitivity versions required by measurement decisions;
- comparison of written and in-memory objects.

Classify failures as blocking, material but non-blocking, or informational. Do not write a final clean dataset with unresolved blocking failures.

## Outputs

- Raw inputs: `data/raw/`, immutable.
- Intermediate data: `data/interim/`.
- Validated analysis data: `data/clean/`.
- Metadata: `data/metadata/variable_dictionary.csv` and `data/metadata/measurement_decisions.csv`.
- Scripts: `scripts/{NN}_{descriptive_name}.R`.
- Add a manifest, validation report, or code-quality report only when the task,
  project contract, or material risk requires it. Do not create them for a
  simple import, selection, renaming, normalization, or export.

Use CSV for transparent exchange and RDS or Parquet when types, size, or performance justify them. Document the authoritative format and do not allow multiple unsynchronized final versions.

## Script requirements

State purpose, inputs, and output in a short header. Add dependencies,
assumptions, execution order, or a validation summary only when they are not
obvious from the code or are necessary to use the result safely. Keep
substantive measurement decisions in shared artifacts rather than only in code
comments.

## Minimal code first

Start with the shortest readable transformation that satisfies the requested
contract. Apply the readable-transformation and complexity rules in
`../shared/r_code_style.md`; consult `../shared/r_code_examples.md` for a minimal
join and derived variable or an aggregation over declared support. Preserve
source labels unless an approved mapping requires normalization.

## R conventions

- Read `project/project_profile.yaml` and `../shared/r_code_style.md`.
- Default to `readr`, `dplyr`, `tidyr`, `stringr`, `lubridate`, and `janitor`
  with the native pipe `|>`.
- Normalize output names to `snake_case`. Use explicit namespaces consistently
  in reusable code and avoid combining `library()` calls with fully qualified
  calls for the same package.
- Make missing-value handling and join relationships explicit.
- Avoid working-directory side effects and machine-specific paths.
- Stop execution on failed blocking assertions.
- Run required `styler` and `lintr` checks with the scope and reporting defined
  in `../shared/r_code_style.md`. A small task uses its existing closure; a
  reproducibility milestone consolidates the required code-quality report.

## Rules

- Never overwrite raw inputs.
- Never drop duplicates, missing values, unmatched rows, or outliers silently.
- Never change source values without retaining the original and a correction flag.
- Never invent a harmonization rule during implementation.
- Never let joins change the analytical population without reporting it.
- Preserve lineage from every clean variable to sources and decisions.
