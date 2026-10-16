# Maturity Gates and Schemas

Use this reference to test whether artifacts evidence the work claimed. The canonical machine-readable column contract is `../schemas/artifact-schemas.json`.

## Contents

1. [Maturity dimensions](#maturity-dimensions)
2. [Artifact contracts](#artifact-contracts)
3. [Count reconciliation](#count-reconciliation)
4. [Orientation gate](#orientation-gate)
5. [Maturation gate](#maturation-gate)
6. [Migration](#migration)

## Maturity dimensions

Track separately:

- `metadata_verification_status`;
- `screening_status`;
- `full_text_status`;
- `reading_status`;
- `extraction_status`;
- `corpus_layer`;
- `wiki_status`;
- `data_status`;
- `evidence_independence_status`;
- `debate_maturity_status`.

Never compress these into a single relevance, inclusion, or quality score.

## Artifact contracts

### `query_lineage_log.csv`

One row per executed or explicitly planned batch. Required lineage fields include:

`search_batch_id`, `parent_batch_id`, `discovery_track`, `search_target_id`, `trigger_source_id`, `trigger_term`, `reason_for_expansion`, exact `query`, `platform`, `filters`, `sort_order`, `executed_at`, `results_returned`, `results_exported`, `results_reviewed`, `review_exception_count`, `review_exception_reason`, `export_path`, discoveries, and `next_action`.

Use `parent_batch_id=ROOT` only for initial protocol batches. A planned batch has blank execution counts and `batch_status=planned`; never present it as executed.

### `source_batch_relations.csv`

This is the auditable bridge between queries and works. One source may appear in many batches. Record its platform record ID, raw export locator, rank when available, and whether it was individually reviewed.

### `extended_corpus.csv`

One canonical row per `source_id`, after deduplication. Preserve all persistent identifiers, document identity, container and document types, language, abstract, author keywords, index terms, platform/query/batch provenance, reference and citation IDs when supplied, access, verification, screening, provisional roles, and multidimensional fit. `source_batch_relations.csv` remains the normalized authority for the many-to-many retrieval relation; the extended row carries an auditable summary.

For `abstract`, `author_keywords`, `index_terms`, references, and citations, use an explicit status:

- `provided`;
- `not_offered_by_platform`;
- `pending_retrieval`;
- `verified_absent`;
- `access_failure`.

If status is `provided`, the value cannot be empty. If another status is used, the value must be empty or explicitly marked as a platform transcription. Never use blank, `NA`, or `unknown` without a state.

### `screening_log.csv`

Preserve stage-specific decisions and a primary exclusion reason. Do not overwrite an earlier decision; append a new row with `supersedes_decision_id` if a decision changes.

### `corpus_membership_log.csv`

Record every promotion, demotion, contextual reassignment, or removal from active analysis. Raw results are never deleted; exclusion changes analytical membership, not historical provenance.

### `analytical_corpus.csv`

Materialize included analytical and contextual/comparative works with their orthogonal fit dimensions and review roles. It is a screened view, not a second identity registry.

### `identifier_crosswalk.csv`

Connect `source_id`, verified `bibkey` or `PENDING`, deterministic PDF filename/path, wiki slug, persistent identifiers, canonical work family, and version ID. Conflicts require an explicit note.

### `extraction_matrix.csv`

Retain the previous fields and add:

- multidimensional fit;
- location of each principal finding;
- `evidence_lineage_id`;
- `evidence_independence_status`;
- shared-source IDs;
- version and dataset/source relations;
- core-reading priority and status.

Abstract-only extraction is `discovery_only`, never `located`.

### `debate_matrix.csv`

Use multiple rows per debate position. In addition to the earlier conceptual fields, record:

- core sources fully read;
- central unread sources;
- number of distinct positions;
- serious rivals;
- independent and shared evidence lineages;
- contradictions and boundary conditions;
- searched traditions and venue lanes.

`reconstructed` requires zero central unread sources, at least two evidenced positions, a serious rival, and fully read/location-extracted core evidence unless a documented sparse-literature exception narrows the claim.

### `network_edges.csv`

Use `network_type` to keep citation, author, institution, version, argument, and source/data relations separate. Every inferred intellectual relation needs an evidence basis and, where possible, a location. Do not project an argument edge from a coauthor or shared-dataset edge.

### `paper_dataset_use.csv`

Use one row per work–dataset/source use. This is distinct from `data_source_candidates.csv`, which records resources the project may acquire. The use matrix records how an existing work used or inherited evidence.

### `venue_coverage.csv`

One row per research line, venue, and coverage action. When a row derives from the skill's curated registry, retain `venue_registry_id` and `registry_version`; use `PROJECT_SPECIFIC` for a venue added by the review protocol. Retain venue priority, JCR verification metadata when used, lane, years/issues/terms covered, search status, and access constraints. Venue priority is not article quality.

## Count reconciliation

For every executed batch:

```text
results_reviewed
= count(source_batch_relations.review_status == "reviewed")
+ review_exception_count
```

Require a non-empty, quantified `review_exception_reason` when `review_exception_count > 0`. An exception may document a legacy import or a platform failure that prevented record retention; it cannot relabel API returns, exports, rankings, or automated retrieval as human/agent screening.

Also require:

- `results_exported <= results_returned` when both counts are observed;
- every individually reviewed relation to resolve to an `extended_corpus.source_id`;
- every screening decision to resolve to the extended corpus;
- exclusions to retain stage, reason, actor, and date;
- deduplicated records to retain all batch relations.

## Orientation gate

Return `G-LITERATURE-ORIENTATION`:

- `pass`: the protocol exists; verified seeds and initial batches in required tracks have been executed; a normalized extended corpus exists; major concepts, traditions, venue lanes, and provisional rivals are visible; question changes are conservative and reasoned; required next searches are named.
- `conditional pass`: the question is defensible but specified platforms, languages, full texts, traditions, or lane checks remain and the handoff explains how they could alter it.
- `fail`: the output is a seed list, generic query plan, unreconciled result claim, early synthesis, unsupported gap claim, or one-tradition framing.
- `not assessed`: the evidence required to apply the gate was not inspected.

Orientation permits hypothesis generation. It never certifies comprehensive coverage or mature claims.

## Maturation gate

Return `G-LITERATURE`:

- `pass`: the layered corpus, query genealogy, screening, core full reading, location-level extraction, debate/argument/source genealogies, directed rival searches, three-lane venue coverage, saturation test, bibliography crosswalk, and synthesis satisfy their contracts.
- `conditional pass`: bounded named gaps remain, but they do not undermine the central synthesis or are explicitly excluded from its scope.
- `fail`: a central claim rests on abstracts, central unread works, one position, unreconciled screening, shared evidence presented as independent, missing rivals, or a single venue lane.
- `not assessed`: mandatory artifacts or checks were not inspected.

For each core research line require:

- at least two fully read, location-extracted core sources where the literature permits;
- at least two distinguishable positions or interpretations;
- at least one serious rival;
- explicit evidence-lineage comparison;
- one contradiction, uncertainty, boundary, or documented search finding none;
- coverage in disciplinary-core, adjacent-field, and regional/non-indexed lanes, or a justified inapplicability amendment;
- a concrete unresolved problem tied to concept, scale, period, mechanism, source, measurement, or method.

## Migration

Preserve old files and add, do not silently recode:

| Legacy artifact | New artifact | Migration rule |
|---|---|---|
| `search_execution_log.csv` | `query_lineage_log.csv` | Copy observable values; set new lineage fields to `PENDING_REVIEW`; reconcile old reviewed counts before reuse. |
| `source_discovery_log.csv` | `extended_corpus.csv` + `source_batch_relations.csv` | Split identity from retrieval relations; retrieve abstracts/keywords when possible; assign absence states. |
| `corpus_crosswalk.csv` | `identifier_crosswalk.csv` | Preserve IDs and paths; verify that bibkeys were not assigned provisionally without identity checks. |
| `extraction_matrix.csv` | expanded `extraction_matrix.csv` | Add fit, lineage, independence, version, and core-reading fields; retain old values verbatim. |
| `data_source_candidates.csv` | unchanged plus `paper_dataset_use.csv` | Do not confuse acquisition candidates with evidence actually used by reviewed works. |
| prior `venue_coverage.csv` | expanded `venue_coverage.csv` | Add `venue_registry_id`, `registry_version`, and `priority_group`; use `LEGACY_UNMAPPED` until the old venue is reconciled to the registry or marked project-specific. |

Mark migrated rows with `record_origin=legacy_migration` and preserve the original files until reconciliation passes.
