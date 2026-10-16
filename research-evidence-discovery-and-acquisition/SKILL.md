---
name: research-evidence-discovery-and-acquisition
description: "Identify, search for, verify, acquire, and document missing datasets, archival sources, maps, administrative records, and contextual evidence required by an approved research design. Use when available materials do not satisfy documented data or source requirements, when access and licensing must be assessed, or when Codex must produce a reproducible discovery log, acquisition manifest, fallback strategy, and evidence-coverage decision."
---

# Evidence Discovery and Acquisition

Find only the evidence required by the design, verify what has actually been found, and preserve a traceable path from requirement to acquired or unavailable source. Do not turn evidence acquisition into an open-ended web search.

## Workflow position

Use this skill primarily at Stage 8 after causal, historical-structural, or hybrid design. It may be activated earlier from `literature-review` when a paper identifies a dataset, archive, code repository, official series, supplement, or replication package that is material to question refinement, hypothesis plausibility, or feasibility. Early acquisition verifies and preserves a candidate; it does not approve a design or make the resource analysis-ready. The skill may also be reactivated after failed feasibility, source criticism, measurement, or replication reveals a material evidence gap.

Recover or create from the approved design:

- route-specific causal, structural, or hybrid design outputs;
- `analysis/data_requirements.qmd`;
- `analysis/source_requirements.qmd`;
- `project/source_inventory.csv`;
- `project/historical_source_registry.csv` when available;
- `literature/data_source_candidates.csv` when literature discovery produced it;
- route-specific design and measurement outputs;
- access, budget, language, time, and rights constraints.

When the two requirement files do not yet exist at Stage 8, formalize them before searching. For early literature-stage acquisition, create a provisional requirement identifier linked to the refined question, hypothesis candidate, mechanism, or measurement problem and state that design status is provisional. Do not infer search targets only from a broad research topic.

If existing evidence satisfies the requirements, record that decision and stop. Use `literature-review` for scholarly publication searches; use this skill to verify and acquire empirical, historical, replication, and supplementary resources found through those publications.

## Step 1: Convert requirements into search targets

For every requirement, assign a stable identifier and specify:

- variable, source type, mechanism, or claim served;
- unit, population, geography, period, frequency, and resolution;
- preferred format and minimum acceptable coverage;
- provenance, production-context, and measurement requirements;
- access, rights, privacy, cost, and deadline constraints;
- acceptable fallback and consequence of non-acquisition.

Classify priority as `blocking`, `important`, or `contextual`. Do not search for contextual enrichment while a blocking requirement remains undefined.

## Step 2: Search in a controlled sequence

Search from the most authoritative and source-proximate location outward:

1. known provider, archive, statistical office, repository, or collection;
2. official catalogues and documented APIs;
3. disciplinary, national, regional, or institutional repositories;
4. citation and provenance chains from verified sources;
5. broad web discovery only to locate a provider or catalogue record.

Record exact query, filters, platform, date, result identifier, and stopping decision. Search multilingual variants and historical names when relevant. Do not treat a search-engine result, AI summary, or aggregator record as the acquired source.

Read `references/discovery-strategy.md` before designing a substantial search.

## Step 3: Verify each candidate

Before acquisition, verify:

- title, creator, custodian, edition, release, and stable identifier;
- source type and production purpose;
- geographic, temporal, population, variable, and file coverage;
- file format, schema, documentation, and update history;
- original versus derivative, transcription, aggregation, or mirror status;
- license, terms, privacy, confidentiality, and redistribution rights;
- authenticity, completeness, checksum or version information when available;
- fit with the requirement and known limitations.

Open the provider record or documentation. Never infer coverage from a filename or search snippet. Route acquired historical material to `research-historical-source-criticism` before analytical use.

Read `references/source-verification.md` for candidate and file-level checks.

## Step 4: Acquire lawfully and immutably

- Store provider files in `data/raw/` without modifying their contents.
- Preserve accompanying codebooks, metadata, licenses, readme files, and catalogue citations.
- Record acquisition date, access route, version, size, format, and checksum where feasible.
- Keep credentials, request correspondence, and confidential access details outside public artifacts.
- Do not bypass access controls, automate prohibited collection, or redistribute protected files.
- For archives requiring visits or formal requests, create a concrete request or visit plan rather than claiming acquisition.

An access URL is not proof that the file was acquired. Distinguish `discovered`, `verified`, `requested`, `acquired`, `restricted`, `unavailable`, and `rejected`.

## Step 5: Assess requirement coverage

For each acquired or unavailable item, classify:

- `satisfied`: meets the minimum requirement;
- `partial`: usable only for a restricted period, geography, population, variable, or claim;
- `substitute`: changes measurement or evidentiary strategy;
- `failed`: inaccessible, invalid, incompatible, or insufficient.

State whether a partial or substitute source changes the estimand, concept, comparison, mechanism test, target population, or allowable claim. Return to design or measurement rather than silently accepting a convenient proxy.

## Step 6: Apply the acquisition gate

Return:

- `pass`: every blocking requirement is satisfied and acquired evidence is verified;
- `conditional pass`: named restrictions or pending access steps permit only a narrower design or claim;
- `fail`: a blocking requirement remains unmet and no defensible fallback exists.

Search exhaustion is not established by the number of queries. State the repositories, languages, dates, collections, and citation chains covered and why further searching is unlikely to change the decision.

## Outputs

- updated `analysis/data_requirements.qmd` and `analysis/source_requirements.qmd`;
- `project/evidence_discovery_log.csv`;
- `project/acquisition_log.csv`;
- `project/acquisition_manifest.md`;
- acquired provider files and documentation in `data/raw/` where lawful;
- updated `project/source_inventory.csv` and historical source registry where applicable.

Read `references/examples.md` for archival and quantitative-data examples.

## Rules

- Never search without a requirement identifier.
- Never confuse discovery, verification, request, and acquisition.
- Never claim that inaccessible or snippet-level material has been reviewed.
- Never accept a derivative dataset without tracing its source and transformations.
- Never download or redistribute material contrary to its terms.
- Never let a convenient source silently redefine the research question.
- Preserve failed searches and rejected candidates; they are part of the acquisition record.
