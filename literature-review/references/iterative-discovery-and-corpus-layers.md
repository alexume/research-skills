# Iterative Discovery and Corpus Layers

Use this reference to operate the review funnel without jumping from search results to synthesis.

## Contents

1. [The funnel and its returns](#the-funnel-and-its-returns)
2. [Corpus layers](#corpus-layers)
3. [Promotion and demotion](#promotion-and-demotion)
4. [Extended corpus normalization](#extended-corpus-normalization)
5. [Screening and prioritization](#screening-and-prioritization)
6. [Saturation](#saturation)

## The funnel and its returns

Treat the thirteen stages in `SKILL.md` as states connected by evidence-triggered returns.

Open a derived batch when a source reveals a material:

- concept, synonym, historical label, translation, or obsolete classification;
- author, institution, association, edited volume, special issue, or venue;
- archive, census, administrative series, dataset, producer, or replication package;
- working-paper, article, chapter, book, translation, or revised edition;
- critique, reply, rival mechanism, contradictory result, boundary condition, or measurement dispute;
- geographic, temporal, scalar, linguistic, disciplinary, or document-type coverage gap.

Each return must:

1. append a child row to `query_lineage_log.csv`;
2. retain `parent_batch_id`, trigger, reason, exact operation, and next action;
3. append a protocol amendment if boundaries, eligibility, or stopping rules change;
4. preserve the earlier protocol and failed queries unchanged.

Finding a useful source does not by itself justify narrowing the question. Delay substantive refinement until the extended corpus exposes the principal traditions and plausible rivals.

## Corpus layers

### `raw_results`

Immutable platform exports, API responses, RIS/BibTeX/CSV/JSON, catalogue captures, and user-provided seed lists. Save one batch per path. Record checksums when feasible. Never clean, deduplicate, or overwrite these files.

### `extended_corpus`

The canonical deduplicated identity layer. It contains every retained candidate identity from raw results, including excluded records, with normalized metadata, abstracts, vocabulary, retrieval relations, access state, and provisional classification. Keep one active survivor per canonical identity. When two already-assigned `source_id` values merge, retain the losing ID as a duplicate tombstone with `duplicate_of`; never promote that tombstone analytically or erase its provenance.

This layer must exist before analytical inclusion or synthesis.

### `analytical_corpus`

Works included after screening because they bear directly on a question, mechanism, rival, source, measurement, method, or historiographic position. Analytical inclusion does not imply full reading or evidentiary strength.

### `core_corpus`

Priority works read in full and extracted at page/section/location level because they carry a central claim, position, source genealogy, method, or project comparison.

### `contextual_or_comparative_corpus`

Works useful for background, external comparison, theory, analogous methods, broad historiography, or institutional context but not direct support for the case claim. Keep them accessible without allowing them to inflate direct-evidence coverage.

## Promotion and demotion

Log every layer change in `corpus_membership_log.csv`.

Promote:

- raw result → extended: a record is normalized and assigned stable `source_id`;
- extended → analytical: screening criteria are satisfied and fit/role dimensions are recorded;
- analytical → core: the work is priority, full text is available or an acquisition action exists, and the reason for full reading is explicit;
- extended/analytical → contextual: useful but not direct to the claim or case.

Demote or reassign when:

- identity resolves to a duplicate or different version;
- full text contradicts the abstract-based classification;
- the work is direct by place but answers another question;
- evidence is inherited rather than independently produced;
- a stronger published version supersedes a working paper;
- a claimed central relation cannot be verified.

Demotion never deletes the record or its earlier decisions. Append a new membership event.

## Extended corpus normalization

Preserve when offered:

- internal and platform identifiers;
- title, authors, year, container, type, language;
- abstract;
- author keywords and platform/index terms separately;
- all retrieving batches and raw locators;
- an auditable summary of retrieving platforms, query IDs, and batch IDs;
- URL and access/full-text state;
- available reference and citation IDs;
- metadata verification and screening state;
- inclusion/exclusion reason;
- provisional debates, roles, and fit dimensions.

Normalize identity before enrichment, but do not erase platform strings. When values conflict, retain the conflicting value and record verification status and source.

### No ambiguous blanks

For abstracts, author keywords, index terms, references, and citations distinguish:

- `not_offered_by_platform`: this platform/export does not expose the field;
- `pending_retrieval`: another endpoint/export may provide it but retrieval has not occurred;
- `verified_absent`: the platform explicitly has no value for this record;
- `access_failure`: retrieval was attempted but failed;
- `provided`: value preserved.

For a record found on multiple platforms, store per-platform provenance in `source_batch_relations.csv`; the canonical extended row may use the best verified value while preserving its origin.

### Abstract boundary

An abstract may:

- create new search terms;
- support title/abstract screening;
- assign provisional fit and review role;
- determine acquisition priority.

It may not:

- establish a mature finding;
- close a central claim;
- certify a method, limitation, data construction, or argument not stated clearly;
- make a debate reconstructed.

## Screening and prioritization

Screen title/catalogue, then abstract/description, then full text, then analytical inclusion. Record one primary exclusion reason at each stage and preserve all earlier stages.

Use multidimensional classification, not a single relevance score:

| Dimension | Example values |
|---|---|
| `geographic_fit` | `direct_case`, `regional_comparison`, `external_case`, `not_applicable` |
| `question_fit` | `direct`, `adjacent_mechanism`, `rival`, `theory`, `method`, `context` |
| `source_fit` | `same_dataset`, `same_source_family`, `comparable_source`, `different_source`, `none` |
| `period_fit` | `direct`, `overlap`, `preceding`, `subsequent`, `external`, `not_applicable` |
| `scale_fit` | `same`, `nested`, `broader`, `different`, `not_applicable` |
| `disciplinary_tradition` | protocol-defined controlled list |
| `review_role` | `core_empirical`, `direct_evidence`, `context`, `theory`, `method_analogue`, `measurement`, `rival`, `historiography` |

Allow multiple roles. Priority should reflect the burden the work may carry, not venue prestige.

## Saturation

Run at least one derived-search cycle after the first analytical corpus. Then compare successive batches for new:

- concepts or definitions;
- positions or rival mechanisms;
- authors, institutions, venues, or traditions;
- source/dataset lineages and versions;
- methods, measurements, geographies, periods, scales, or languages;
- contradictions and boundary conditions.

Declare saturation by research line and discovery track, never from total counts alone. A line is not saturated if one venue lane, central language, source genealogy, or known rival remains unsearched.

Record:

- batches compared;
- genuinely new categories found;
- repeated categories;
- unresolved access and platform limits;
- why additional searching is unlikely to alter the bounded synthesis;
- exact triggers that would reopen the review.
