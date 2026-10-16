# Minimal R transformation examples

Use these examples with [the shared R standard](r_code_style.md). Each block is
self-contained and produces an inspectable table in memory. In a project, replace
the toy inputs with declared file reads and write the required output to its
project-relative path. Do not add a runner, configuration layer, or helper library
to reproduce these patterns.

All values, years, territories, products, and factors below are synthetic. The
energy factors illustrate units and joins, not scientifically valid coefficients.
Approved measurement decisions must establish the product and moisture basis
before applying real factors. These examples are not a census analysis design.

## 1. Join factors and preserve unmatched production

Purpose: calculate a derived variable without losing source quantities or rows
without a factor. Inputs: synthetic production and a factor lookup. Outputs:
`production_energy` and `unmapped_products` in memory. Requires `dplyr` >= 1.1.1
and `tibble`.

```r
# Inputs: production in tonnes; factors on the same product basis, in MJ/t.
production <- tibble::tribble(
  ~territory, ~item_code, ~production_t,
  "A", "crop_a", 10,
  "B", "crop_a", 20,
  "A", "crop_b", 5
)
energy_factors <- tibble::tribble(
  ~item_code, ~energy_mj_per_t,
  "crop_a", 1000
)

# A lookup must have unique keys and finite positive factors.
stopifnot(
  !anyNA(energy_factors$item_code),
  anyDuplicated(energy_factors$item_code) == 0L,
  all(is.finite(energy_factors$energy_mj_per_t)),
  all(energy_factors$energy_mj_per_t > 0)
)

# Keep physical production and identify products awaiting a factor.
production_energy <- production |>
  dplyr::left_join(
    energy_factors,
    by = "item_code",
    relationship = "many-to-one"
  ) |>
  dplyr::mutate(
    factor_status = dplyr::if_else(
      is.na(energy_mj_per_t), "unmapped", "matched"
    ),
    energy_mj = production_t * energy_mj_per_t
  )

unmapped_products <- production_energy |>
  dplyr::filter(factor_status == "unmapped") |>
  dplyr::distinct(item_code)

stopifnot(nrow(production_energy) == nrow(production))
production_energy
```

The unmatched product remains in the result with missing energy. Do not discard
it or assign zero energy. Add source and quantity checks when the real inputs
require them; the example assumes its declared toy quantities are valid.

## 2. Aggregate paired quantities on common territorial support

Purpose: compare one crop over two periods using the same territories, with
production and harvested area paired. Inputs: a synthetic one-crop, one-universe,
one-cycle panel and the declared expected support. Outputs: `coverage`,
`excluded_cells`, and `yield_table` in memory. Requires `dplyr` >= 1.1.1,
`tidyr`, and `tibble`.

```r
# The comparison's expected territories and years are explicitly declared.
years <- c(2020L, 2021L)
territories <- c("A", "B", "C")
observed <- tibble::tribble(
  ~territory, ~year, ~production_t, ~area_harvested_ha,
  "A", 2020L, 20, 10,
  "A", 2021L, 30, 10,
  "B", 2020L, 15, 5,
  "B", 2021L, 20, 5,
  "C", 2020L, 8, 4
)
stopifnot(
  anyDuplicated(observed[c("territory", "year")]) == 0L,
  all(observed$territory %in% territories),
  all(observed$year %in% years)
)

# Materialize absent cells as missing, then identify paired observations.
coverage <- tidyr::expand_grid(territory = territories, year = years) |>
  dplyr::left_join(
    observed,
    by = c("territory", "year"),
    relationship = "one-to-one"
  ) |>
  dplyr::mutate(
    paired = is.finite(production_t) & production_t >= 0 &
      is.finite(area_harvested_ha) & area_harvested_ha > 0
  ) |>
  dplyr::group_by(territory) |>
  dplyr::mutate(common_support = all(paired)) |>
  dplyr::ungroup()

# Keep exclusions visible, including valid cells outside common support.
excluded_cells <- coverage |>
  dplyr::filter(!common_support) |>
  dplyr::mutate(
    exclusion_reason = dplyr::if_else(
      paired, "outside_common_support", "missing_or_invalid_pair"
    )
  )
paired_panel <- coverage |>
  dplyr::filter(common_support)
stopifnot(nrow(paired_panel) > 0L, all(paired_panel$paired))

# Ratio of matched sums: the denominator is harvested area, not unique land.
yield_table <- paired_panel |>
  dplyr::group_by(year) |>
  dplyr::summarise(
    production_t = sum(production_t),
    area_harvested_ha = sum(area_harvested_ha),
    n_territories = dplyr::n_distinct(territory),
    .groups = "drop"
  ) |>
  dplyr::mutate(yield_t_per_ha = production_t / area_harvested_ha)

yield_table
```

Common support is a declared choice for this comparison, not a universal rule for
all analyses. For multiple crops, universes, cycles, or source regimes, establish
the appropriate full key and comparability decisions first. The resulting tidy
table can feed a presentation table or `ggplot2` expression without a new layer
of calculation hidden in formatting helpers.
