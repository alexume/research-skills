# Table and Appendix Audit

## Numerical consistency

- Regenerate from a clean pipeline state.
- Compare unrounded displayed inputs with registered analytical objects.
- Match estimates, intervals, sample sizes, cluster counts, and test statistics.
- Confirm transformations such as percentages, indexes, elasticities, and cumulative effects.
- Confirm manuscript numbers after table regeneration.

## Design consistency

- Match estimand, comparison, sample, weights, fixed effects, controls, and inference.
- Match period, geography, denominator, source regime, and measurement basis.
- Confirm that main, diagnostic, sensitivity, exploratory, and invalid status is respected.
- Confirm that appendix alternatives do not silently replace the main specification.

## Presentation consistency

- Title states the table's object rather than its conclusion.
- Headers identify units and periods.
- Notes define symbols and abbreviations.
- Source statement identifies provider and transformation when relevant.
- Empty cells distinguish missing, not applicable, suppressed, and unavailable.
- Panels and continued tables preserve identifiers and notes.

## Replication consistency

- Every output has a manifest entry and generating command or target.
- No generated value was edited outside code.
- Main and appendix files are included or intentionally excluded with a reason.
- Verification rules account for expected format-dependent variation.
