# Project Structure and Dependency Rules

## Minimal structure

```text
project/
  project/
  analysis/
  data/raw/
  data/interim/
  data/clean/
  data/metadata/
  R/
  scripts/
  tables/
  figures/
  paper/
  replication/
  renv.lock
  _targets.R or run.R
```

Adapt names to the existing project, but keep roles stable:

- raw inputs are immutable;
- interim data are replaceable pipeline products;
- clean data satisfy the preparation contract;
- analytical objects are distinct from presentation outputs;
- manuscript tables and figures are generated from registered analytical objects.

## Dependency direction

Use this default direction:

```text
raw sources -> preparation -> clean data -> models/analysis
-> tables and figures -> manuscript and supplements
```

Configuration and functions may feed multiple stages. Manuscript files must not feed values back into analytical data. Manual corrections belong upstream as explicit source or measurement decisions.

## Paths and configuration

Use paths relative to the project root. Keep machine-local source locations, credentials, and private repository tokens outside versioned research code. A versioned example configuration may document required keys without exposing values.

## Generated artifacts

Every generated artifact should have:

- an owning script or target;
- declared inputs;
- a stable destination;
- a manifest entry;
- a comparison rule for verification.
