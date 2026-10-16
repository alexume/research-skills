---
name: implementation-figures
description: "Create and revise publication-quality academic figures in R with ggplot2, including time series, distributions, comparisons, panels, event annotations, accessible palettes, labeling, and manuscript export. Use when Codex must produce, standardize, diagnose, or export figures for papers, reports, or presentations."
---

# Skill: Publication-Quality Figures

You produce figures suitable for academic journals using ggplot2 in R.

Read `project/project_profile.yaml`, `../shared/r_code_style.md`, and the figure contract in `../shared/output_contracts.md` before generating project figures. If the profile is missing, do not infer export or inclusion requirements from existing files.

Assign each figure a stable identifier and register it in `figures/figure_manifest.csv` before manuscript integration. Record its claim or analytical purpose, source object, generation target, caption, export paths, Quarto cross-reference, status (`main`, `appendix`, or `excluded`), and audit result.

## Cedric Scherer as input

Treat [cedric-scherer-aesthetics.qm](cedric-scherer-aesthetics.qm) as an input to this skill, not as a separate style system.

The operational synthesis is backed by two source artifacts:

- `references/cedric_content.txt`: extracted tutorial and blog content used to derive detailed plotting guidance;
- `references/cedric_scraped.html`: the preserved raw site scrape used for provenance and link verification.

Use the `.qm` synthesis by default. Read the source artifacts only when auditing provenance, checking whether the synthesis omitted relevant guidance, or updating it from the preserved scrape. Do not load the raw HTML for ordinary figure work.

Some of its principles should live directly inside this skill as defaults because they improve figure quality consistently:

- Prefer direct labels and clear annotation hierarchy when they reduce legend dependence.
- Use small multiples or highlight-one-vs-rest strategies when color categories become too numerous.
- Reorder categories by value when that improves interpretability and does not violate substantive ordering.
- Keep panel spacing, margins, grid lines, and axis styling intentional rather than default.
- Use color strategically, including contrast, accessibility, and contextual meaning.

Other elements should remain modular inside the `.qm` file and be consulted only when the task calls for them:

- Advanced labeling patterns for bars, facets, and dense plots.
- More specialized chart forms such as raincloud plots, lollipop charts, or composition-heavy layouts.
- Extended guidance on typography, palette-building resources, and multi-panel composition.
- Automation patterns for repeated figure generation across subgroups.

Absorb the general principles above by default and consult the `.qm` module selectively when a plot needs additional aesthetic development beyond the core publication workflow below.

## Base theme

Always start with this custom theme unless the user specifies otherwise:

```r
theme_paper <- function(base_size = 12) {
  theme_minimal(base_size = base_size) +
    theme(
      # Text
      plot.title = element_text(face = "bold", size = rel(1.15), hjust = 0.5),
      plot.subtitle = element_text(color = "grey40", size = rel(0.9), hjust = 0.5),
      plot.caption = element_text(color = "grey50", size = rel(0.7), hjust = 1),
      axis.title = element_text(size = rel(0.9)),
      axis.text = element_text(size = rel(0.8)),
      legend.title = element_text(size = rel(0.85), face = "bold"),
      legend.text = element_text(size = rel(0.8)),
      # Grid
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "grey90", linewidth = 0.3),
      # Legend
      legend.position = "bottom",
      legend.key.width = unit(1.2, "cm"),
      # Margins
      plot.margin = margin(10, 15, 10, 10)
    )
}
```

## Color palettes

- **Categorical (<=5 groups)**: `scale_color_brewer(palette = "Set2")`
- **Categorical (6-8 groups)**: `scale_color_brewer(palette = "Dark2")`
- **Sequential**: `scale_fill_viridis_c(option = "C")`
- **Diverging**: `scale_fill_distiller(palette = "RdBu", direction = 1)`
- **Binary**: `scale_color_manual(values = c("#2c7bb6", "#d7191c"))`

## Figure types and conventions

| Type | Geometry | Notes |
|------|----------|-------|
| Time series | `geom_line()` + `geom_point(size = 1)` | Points help show data density |
| Distribution | `geom_histogram()` or `geom_density()` | Never both overlaid |
| Comparison | `geom_col()` (not `geom_bar`) | Horizontal if >5 categories |
| Scatter | `geom_point(alpha = 0.6)` | No smooth unless requested |
| Panel | `facet_wrap(~var, scales = "free_y")` | Free y-axis by default |
| Event overlay | `geom_vline(linetype = "dashed", alpha = 0.5)` | Annotate with `geom_text` |

## Labeling rules

- Always include `labs(title, x, y)` and never leave axes unlabeled.
- Use sentence case for titles ("Baptism counts by year"), not title case.
- Units in axis labels: "Body mass (g)", "Trade volume (captives)".
- No legends when color or shape is obvious from facets.
- Use `annotate()` for key events, not `geom_text` on data.
- Prefer direct labels over legends when that materially improves readability.

## Saving

```r
ggplot2::ggsave(
  filename = "figures/{figure_id}_{descriptive_name}.png",
  plot = figure_object,
  width = 13,
  height = 9,
  dpi = 300
)
```

Export figures as 300 dpi PNG files by default. Do not generate standalone PDF figure files: the manuscript PDF is produced by Quarto and is a separate artifact. If an author or target journal explicitly requires another figure format, treat it as a documented exception, update the project profile, and generate only the requested format. If an existing profile requires standalone PDF figures without an explicit author or journal decision, stop and surface the conflict instead of creating them.

Follow `../shared/r_code_style.md`, including its readable-transformation rules
and proportional check scope. Keep figure data preparation visible and separate
from the plotting expression. Adapt only the examples needed for the requested
figure; they do not require a configurable figure-generation framework. A theme
or export helper is appropriate when actually reused. Do not create wrappers or
extra files merely to generate one figure.

## Manuscript embedding

- For paper figures, avoid embedding global titles, subtitles, or long notes inside the exported file when the figure will be included with Quarto. Put the figure title, interpretive subtitle, and notes in the caption instead.
- Keep only panel titles, axis labels, legends, and annotations needed to read the visual evidence.
- Use publication-size text: panel titles should remain readable when the figure is scaled to `\textwidth`; for two-panel paper figures, prefer approximately `width = 13`, `height = 9`, `dpi = 300`.
- Center panel titles unless there is a specific journal or design reason to left-align them.
- Use Quarto figure labels and cross-references by default, for example `#| label: fig-event-study` and `@fig-event-study`. Use raw LaTeX such as `\includegraphics` only when the project profile or target journal explicitly requires it.
- Render all required manuscript formats and inspect figure presence, order, caption, cross-reference, legibility, and clipping. A file that exists but is absent or unreadable in the rendered PDF fails the audit.

## Rules

- Never use the default ggplot2 theme.
- Never truncate the y-axis unless explicitly justified.
- Always start bar charts at zero.
- Use colorblind-friendly palettes.
- Figures should be interpretable in greyscale, using shape or linetype as backup.
- Keep it minimal: remove elements that do not carry information.
- Reorder categories by value unless a substantive ordering should be preserved.
- If categories exceed the effective color limit, prefer faceting or highlight-one-vs-rest instead of adding more hues.
- Never edit a generated figure manually to repair analytical content.
- Never generate standalone PDF figure files by default.
- Never declare a figure integrated without a manifest entry and a successful required-format render check.
