# Replication Package

## Package classification

Label the release honestly:

- `full`: all lawful inputs and code reproduce reported outputs;
- `partial`: some inputs or outputs cannot be distributed;
- `executable without data`: code and environment are complete but protected inputs require separate access;
- `documentation-only`: materials document the workflow but cannot execute it.

## README contents

`replication/README.md` must include:

- citation, authorship, contact, license, and package version;
- scope and package classification;
- data sources, access conditions, and rights;
- hardware, software, system dependencies, and expected runtime;
- restoration and execution commands in order;
- expected outputs and their locations;
- manual, restricted, licensed, or network-dependent steps;
- known deviations from the published analysis;
- disclosure-control and privacy notes.

## Manifest fields

`replication/manifest.csv` should contain:

- stable file identifier;
- relative path;
- role: input, code, environment, intermediate, output, documentation;
- source or generating command/target;
- version or hash;
- sharing status and license;
- required or optional status;
- corresponding paper table, figure, appendix, or claim;
- verification rule and result.

## Restricted or archival data

Do not redistribute files without rights. Provide persistent catalogue references, lawful access steps, request templates where appropriate, exact variable and extraction descriptions, and transformation code. When disclosure control is required, document how it changes reproducibility and which results an authorized verifier must check.

Synthetic data may verify interfaces and code paths, but cannot verify empirical results unless expressly constructed and validated for that purpose. Label all synthetic outputs clearly.

## Package hygiene

Exclude credentials, caches, user histories, absolute paths, temporary files, undocumented binaries, and personal identifiers. Include only files required to understand, execute, or verify the research.
