# Reproducible Table Generation

## Analytical and presentation layers

Keep three layers distinct:

1. fitted models, evidence objects, or source summaries;
2. tidy table data with full precision and stable identifiers;
3. formatted outputs for HTML, PDF/LaTeX, DOCX, or other submission formats.

Presentation labels and rounding belong in layer 3. Sample definitions, estimands, statistics, and exclusions belong upstream.

## R tools

Select tools by project needs and verify their current documentation:

- `modelsummary` for model summaries and compatible data-frame tables: https://modelsummary.com/
- `tinytable` for multi-format table rendering: https://vincentarelbundock.github.io/tinytable/
- `gt` for structured presentation tables: https://gt.rstudio.com/
- estimator-specific extraction only when it preserves the required statistics and metadata.

Do not combine packages merely for decorative effects. Store the table data independently when package upgrades could change rendering.

## Precision

- calculate with unrounded values;
- define display precision by substantive scale;
- keep consistent precision within comparable rows or columns;
- distinguish true zero from rounded zero;
- never infer exact equality from rounded display values.

## Stable labels

Maintain a label dictionary for variables, estimands, periods, samples, and source regimes. Avoid changing analytical variable names for presentation. Use stable table and panel identifiers so manuscript references survive reordering.

## Output formats

Generate every required format through the pipeline. Format-specific corrections must live in code and remain bounded to presentation. Verify pagination, repeated headers, footnotes, special characters, decimal alignment, and accessible text alternatives where required.
