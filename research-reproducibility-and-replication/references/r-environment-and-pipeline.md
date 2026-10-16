# R Environment and Pipeline

## Environment capture

For an R project:

1. initialize or activate `renv` at the project root;
2. use `renv::snapshot()` after reviewing project dependencies;
3. commit `renv.lock`, the activation files, and project configuration;
4. run `renv::status()` before release;
5. test `renv::restore()` in a clean library;
6. document system libraries, external programs, Quarto extensions, and private repositories separately.

Do not update the lockfile merely because a package exists in the user library. Review whether it is a declared project dependency and whether the chosen snapshot mode discovers it.

## Pipeline selection

Use `targets` when the analysis has branching dependencies, expensive computations, many generated outputs, or a meaningful need for incremental rebuilds. Declare files and other dependencies so changes invalidate the correct downstream targets.

A numbered-script pipeline is acceptable for a small linear project when:

- a single entry point runs all required scripts;
- each script declares its inputs and outputs;
- scripts fail on missing dependencies;
- generated artifacts are never edited manually;
- rerunning from a clean state yields the reported outputs.

Do not combine a nominal pipeline with undocumented notebook cells or console commands.

## Quarto and external tools

Record:

- Quarto version and extensions;
- TeX distribution and nonstandard packages for PDF output;
- Pandoc filters, fonts, geospatial libraries, Java, Python, or command-line tools;
- locale, encoding, and time-zone assumptions when they affect parsing or rendering.

## Randomness

Set seeds at reproducible boundaries. Record the RNG kind when relevant. Parallel random generation must use a reproducible stream supported by the selected framework. Do not reuse one arbitrary seed invisibly across unrelated procedures; register the procedure, seed, and purpose.

## Official documentation

- `renv`: https://rstudio.github.io/renv/
- `targets`: https://docs.ropensci.org/targets/
