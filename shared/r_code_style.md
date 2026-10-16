# Shared R Code Standard

Apply this standard to project R scripts, functions, Quarto chunks, and generated analytical outputs. A project may tighten it in `AGENTS.md` or `project/project_profile.yaml`. Document exceptions in the existing task closure; consolidate relevant exceptions in `analysis/r_code_quality.md` when closing a milestone that requires it.

## Syntax and organization

- Use the native pipe `|>` in new code. Retain `%>%` only when a required API or documented legacy module cannot be migrated safely.
- Follow the tidyverse style guide for naming, spacing, indentation, and line breaks. Use `snake_case` for objects and functions.
- Prefer `dplyr`, `tidyr`, `readr`, `stringr`, `purrr`, `forcats`, and `lubridate` for data transformation when appropriate. Use specialized packages for estimators, spatial work, tables, or figures when they are methodologically preferable.
- Use explicit package namespaces in reusable functions and pipeline code, for example `dplyr::mutate()` and `fixest::feols()`.
- Separate genuinely reusable functions from orchestration when that makes the transformation easier to follow. Multiple stages alone do not justify helper files.
- Use project-relative paths. Do not use `setwd()`, absolute machine paths, `attach()`, or hidden global-state dependencies.

## Readable transformations and proportional complexity

The author should be able to follow the empirical reasoning from input to output
by reading the main script from top to bottom.

- Write the main transformation as a visible linear pipeline. Prefer `|>` to
  nested transformation calls when it makes the sequence clearer.
- Name intermediate objects after meaningful analytical stages or results worth
  inspecting. Do not create an object for every verb or force everything into one
  long pipeline.
- Introduce meaningful blocks with a short purpose comment. Keep formulas near
  their application; keep authoritative measurement decisions in the project's
  decision records or curated mappings and reference them where applied.
- Prefer vectorized operations, explicit joins, grouped operations, `across()`,
  and reshaping to row-by-row iteration. Use a loop when it is clearer or needed,
  with a short explanation. Do not replace a clear loop with nested `map()` calls
  merely to avoid loops.
- Create functions for repeated logic or substantive rules that benefit from
  independent checking. Do not wrap a one-off short transformation in a helper.
- Use one data-manipulation grammar per script where practical. Default to
  tidyverse; use `data.table` when measured scale or performance justifies it,
  with an explicit boundary if both are needed.
- Add configurable frameworks, wrappers, classes, execution modes, logging
  layers, or check registries only for an observed need. Prefer one or two
  blocking checks next to a simple transformation; add checks for additional
  concrete risks, not to meet a quota.
- Split scripts by responsibilities and products. Do not spread a simple
  transformation across many files or create abstractions for hypothetical reuse.
- Length is a guideline, not a cap. As an orientation, a script stays around
  150 lines after normal formatting; a project may set its own figure. A longer
  script is right when it implements one conceptual process that would be
  harder to follow if split: state that reason in the script's header comment.
  Never compress multiple operations onto one line, or fragment one process
  across files, to meet the number.

During review, locate the inputs, joins, exclusions, formula, and output without
reconstructing a chain of helpers. If this is difficult, simplify the organization
before adding infrastructure.

Consult [minimal transformation examples](r_code_examples.md) when writing or
reviewing joins, derived variables, or supported aggregations. Adapt only the
relevant example; it is not a framework to install in each project.

## Analytical integrity

- Make joins, exclusions, missing-value handling, weights, grouping, and ordering explicit.
- Validate join keys and cardinality where multiplicity could change results;
  account for exclusions and expected row-count changes. Do not deduplicate or
  drop unmatched rows merely to make a check pass.
- Set and record seeds for stochastic procedures.
- Preserve unrounded values for computation and round only at presentation.
- Generate analytical data, tables, and figures through one documented script or pipeline target; do not repair generated outputs manually.
- Keep estimator choices in the appropriate implementation skill. Tidyverse style does not imply that causal estimators must come from tidyverse packages.

## Automated checks

For a bounded change, format and lint the changed files and relevant Quarto R
chunks. Replace the example path with the file in scope:

```r
styler::style_file("scripts/03_transform.R")
lintr::lint("scripts/03_transform.R")
```

Review the diff after `styler`; do not accept a mechanical rewrite that changes executable strings or generated code. Configure justified exclusions in project lint settings rather than ignoring failures silently.

Do not reformat entire directories as a side effect of a small task. At a
reproducibility milestone, broaden checks to the maintained analytical chain and
relevant Quarto chunks; broaden formatting only within the authorized scope.
Reuse valid check results unless changes or failures justify repeating them.

For a small task, report checked paths, results, and any exceptions or unavailable
tools in its existing closure. Do not create a separate report merely to prove
that checks ran. Required checks remain required; unavailable tools are
`not assessed`, not an implicit pass.

At a milestone requiring a code-quality report, update the existing
`analysis/r_code_quality.md` with:

- paths checked and paths excluded;
- `styler` and `lintr` versions;
- commands and date;
- warnings or errors;
- documented exceptions with file, location, reason, and owner;
- result: `pass`, `conditional pass`, `fail`, or `not assessed`.

`not assessed` is an audit state, not a pass. It blocks any gate that requires code-quality verification.
