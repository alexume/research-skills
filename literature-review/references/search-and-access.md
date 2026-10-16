# Search, Export, and Access

Use this reference to execute and preserve platform discovery without confusing API return, export, review, metadata verification, and acquisition.

## Contents

1. [Batch contract](#batch-contract)
2. [Raw exports and normalization](#raw-exports-and-normalization)
3. [Platform strategy](#platform-strategy)
4. [OpenAlex](#openalex)
5. [Scopus](#scopus)
6. [Other discovery surfaces](#other-discovery-surfaces)
7. [Full-text states and lawful access](#full-text-states-and-lawful-access)

## Batch contract

For every batch record:

- `search_batch_id`;
- `parent_batch_id`;
- `discovery_track`;
- `search_target_id`;
- `trigger_source_id`;
- `trigger_term`;
- `reason_for_expansion`;
- exact query, citation operation, hand-search range, or persistent ID;
- platform;
- filters and sort order;
- executor and date;
- `results_returned`;
- `results_exported`;
- `results_reviewed`;
- immutable export path;
- reviewed-record exception count/reason;
- new concepts, debates, authors, institutions, venues, sources, datasets, and versions;
- next action.

Do not record a planned batch as executed. Do not use `results_reviewed` for API-returned, downloaded, ranked, or machine-normalized records. Reconcile it through `source_batch_relations.csv`.

Use `parent_batch_id=ROOT` for initial batches. All derived batches identify the source/batch/term that triggered them. If a batch arises from a combined pattern, cite every trigger in `reason_for_expansion` and choose the immediate parent that generated the action.

## Raw exports and normalization

Save each platform response or export under a batch-specific immutable path such as:

```text
literature/raw_results/{search_batch_id}/{platform}_{timestamp}.{ext}
```

Record checksum and export format when feasible. Never overwrite, deduplicate, hand-edit, or silently truncate a raw export.

Normalize retained records into `extended_corpus.csv` and connect each occurrence through `source_batch_relations.csv`. Preserve platform-specific IDs and raw locators.

### Metadata preservation

When offered, retain:

- abstract;
- author keywords;
- platform/index terms;
- source/container and document type;
- language;
- references, citations, and related-work identifiers;
- authors and affiliations;
- access and version information.

Map absence per field:

| Situation | Status |
|---|---|
| Export/API has the field and value | `provided` |
| Chosen platform/export never supplies the field | `not_offered_by_platform` |
| Another endpoint/export may supply it | `pending_retrieval` |
| Platform explicitly reports no value | `verified_absent` |
| Retrieval attempt failed | `access_failure` |

Scopus author keywords and indexed keywords are distinct. OpenAlex `keywords` are platform-generated index terms, not author keywords. Do not merge them.

## Platform strategy

Use both discovery tracks and add source/data and venue-assisted tracks when relevant. Choose platforms by field, geography, period, language, and document type rather than a universal database count.

For historical social science, combine as appropriate:

- OpenAlex and Scopus;
- EconLit, RePEc/IDEAS, NBER, SSRN;
- JSTOR and library catalogues;
- journal/association hand-searching;
- SciELO, Redalyc, Dialnet, CLACSO, national and university repositories;
- theses, books, chapters, edited volumes, working papers, reviews, historical publications;
- archive, census, dataset, institution, producer, and series searches.

Use Google Scholar as complementary discovery for cited-by paths, versions, books, theses, and under-indexed materials. Record who executed it, query/date, reviewed candidates, and reproducibility limitations. Do not scrape around access controls.

## OpenAlex

Official documentation:

- https://developers.openalex.org/api-reference/works
- https://developers.openalex.org/api-reference/works/get-a-single-work
- https://developers.openalex.org/guides/recipes

Use `OPENALEX_API_KEY`; never write it to logs or committed files. Configure interactively on Windows with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File literature-review/scripts/configure_openalex.ps1
```

Use the bundled helper for reproducible raw exports:

```powershell
python literature-review/scripts/openalex_discovery.py `
  --batch-id OA_Q1_20260723 `
  --output literature/raw_results/OA_Q1_20260723/openalex.jsonl `
  search `
  --query "agrarian productivity regional divergence mexico" `
  --from-year 1940 --to-year 1980
```

The helper preserves `abstract_inverted_index`, reconstructs plaintext abstract as a normalization hint, retains OpenAlex keywords/topics and citation IDs, adds batch provenance, refuses to overwrite raw exports, and writes a sidecar metadata file. Use `--dry-run` to inspect requests.

For network traversal:

- `references`: fetch the seed's `referenced_works`, then retrieve those IDs;
- `cited-by`: query works using OpenAlex's `cites:{seed}` filter;
- `related`: fetch and retrieve the seed's `related_works`.

Citation count is discovery metadata only. Never treat it as quality, evidentiary independence, or inclusion.

## Scopus

Use Scopus as a complementary curated index when relevant and accessible.

Construct exact Advanced Search queries such as:

```text
TITLE-ABS-KEY((agrarian OR agricultural) AND productivity AND Mexico)
AND PUBYEAR AFT 1939
AND PUBYEAR BEF 1981
```

Record exact query, date, filters, sort, returned count, exported count, export path, and record-level review.

Preferred routes:

1. authenticated interface export to CSV/RIS/BibTeX;
2. Scopus Search API with valid key and applicable institutional entitlement;
3. exact user-execution request when authenticated access is unavailable.

### Scopus credentials and the entitled abstract lane

Use `SCOPUS_API_KEY_2` as the Scopus API key — this is the correct credential for this environment (a second key, `SCOPUS_API_KEY`, also exists, but key 2 is the one to use). Pair it with the institutional token `SCOPUS_INSTTOKEN`. Read both from the environment; never print or commit them.

Send requests over **HTTPS** with both credentials in **headers** (not as `apiKey` query parameters):

- API key in the header `X-ELS-APIKey`;
- institutional token in the header `X-ELS-Insttoken`.

```text
GET https://api.elsevier.com/content/abstract/scopus_id/{id}?view=META_ABS
X-ELS-APIKey: <SCOPUS_API_KEY_2>
X-ELS-Insttoken: <SCOPUS_INSTTOKEN>
```

`X-ELS-Insttoken` is what unlocks author keywords and abstracts. With the token, Search `view=COMPLETE` and Abstract Retrieval `view=META_ABS` / `FULL` / `ENTITLED` return **200** with `dc:description` (abstract) and `authkeywords` present; without it the same requests fail (401 `AUTHORIZATION_ERROR` / `AUTHENTICATION_ERROR`). The entitlement is bound to the institutional subscription, not to a key count, so a second API key alone does not help. Do not assume a subscription implies API or full-text entitlement.

On import preserve, when present:

- EID and DOI;
- title, authors, year, source/container, type, language;
- abstract;
- author keywords;
- indexed keywords;
- cited references/citation metadata;
- link and access fields;
- exact batch/export provenance.

If the export format omits abstracts or keywords but another authorized export can include them, mark `pending_retrieval`, not `verified_absent`.

## Other discovery surfaces

### EconLit and RePEc/IDEAS

Use EconLit subject descriptors/JEL codes and RePEc series/author links to locate economics and working-paper families. Verify published versions and do not equate working-paper series prestige with evidence quality.

### JSTOR and catalogues

Use for older journals, books, chapters, reviews, and bibliographic verification. A catalogue record may support identity/screening, not a mature content claim.

### Regional platforms and repositories

Search SciELO, Redalyc, Dialnet, CLACSO, national/university repositories, and journal sites using Spanish, Portuguese, English, and historical terminology. Document coverage and interface/export limits.

### Venue hand-searching

Record venue, lane, years/issues, special issues, debates, reviews, source notes, terms used, access limits, and resulting batches in `venue_coverage.csv`. Do not call a venue searched if only a generic platform query happened to return one of its articles.

### Author, institution, and family searches

Trace authors, research projects, institutions, edited volumes, working-paper series, and version families. Keep author/institution discovery separate from claims about intellectual schools.

### Archive and dataset searches

Search archive names, census titles, statistical offices, ministries, producer institutions, dataset acronyms, historical series, and replication repositories. Send verified acquisition needs to `research-evidence-discovery-and-acquisition`.

## Full-text states and lawful access

Use:

- `not_sought`;
- `candidate_url`;
- `access_verified`;
- `downloaded`;
- `local_existing`;
- `user_download_required`;
- `restricted`;
- `unavailable`;
- `rejected`;
- `superseded_version`.

For downloaded/local files record landing page, lawful direct URL when applicable, version, acquisition date, local path, size/checksum when feasible, and reuse limitation.

Prefer publisher OA copies, institutional/disciplinary repositories, author-accepted manuscripts, official working-paper series, and library access under user entitlement. Do not bypass paywalls, CAPTCHAs, authentication, robots restrictions, or license terms.

A candidate URL is not an acquired file; a repository record is not verified full text; and full-text unavailability is not a substantive exclusion unless the protocol explicitly makes it one.
