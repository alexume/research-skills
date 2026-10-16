# Identifiers and Source Lineage

Use this reference to prevent identity, version, and evidence reuse from being conflated.

## Contents

1. [Identifier contract](#identifier-contract)
2. [Deduplication and versions](#deduplication-and-versions)
3. [Networks](#networks)
4. [Paper–dataset/source use](#paperdatasetsource-use)
5. [Evidence independence](#evidence-independence)
6. [Bibliography and KnowledgeWiki promotion](#bibliography-and-knowledgewiki-promotion)

## Identifier contract

### `source_id`

Assign once at first normalization. Use a project-local immutable sequence such as `SRC000001`. Do not derive it from DOI, title, author, keyword, or mutable metadata. Merging duplicates selects one surviving `source_id` and records all merged IDs; never recycle an ID.

### `bibkey`

Assign only after canonical identity is verified against the publication, DOI registry, authoritative catalogue, or equivalent source. Use `PENDING` until then. The authoritative `.bib` contains only promoted verified records, not the entire extended corpus.

### `pdf_filename`

After a verified bibkey exists, use:

```text
Bibkey_Short_Title.pdf
```

Make `Short_Title` deterministic: ASCII transliteration when feasible, title case removed, spaces/punctuation replaced by single underscores, unsafe filesystem characters removed, and length capped by the project convention. Example: `Solbrig1970_Green_Revolution_Latin_America.pdf`.

Never rename a file to a fabricated key. Record version (`submitted`, `accepted`, `published`, edition) in the crosswalk, not through ad hoc filename suffixes unless two distinct files must coexist.

### `wiki_note_slug`

Use the KnowledgeWiki note identifier independently of citation and file names. The crosswalk must connect it to `source_id` and `bibkey`.

Quarto and manuscript citations use `@bibkey`, never `@source_id`, filename, keyword, or wiki slug.

## Deduplication and versions

Deduplicate in this order:

1. exact persistent identifiers;
2. normalized DOI or catalogue/work ID;
3. normalized title plus author/year;
4. edition, translation, container, and version inspection;
5. full-text or publisher verification for ambiguous cases.

Do not merge:

- a chapter and its parent book;
- a translated edition when pagination or content matters;
- a working paper and published article before checking substantive revision;
- an article later incorporated into a book when arguments or evidence changed;
- two works that reuse the same title or dataset.

Create a canonical work family with distinct version IDs. Record `is_version_of`, `supersedes`, `translation_of`, `chapter_in`, and `substantially_revised_as` relations with evidence.

## Networks

Use `network_edges.csv` with a separate `network_type`.

### Citation network

Record directed `cites`, `cited_by`, `reviews`, `critiques`, and `replies_to` edges. A citation alone does not prove agreement, influence, or lineage.

### Author and institution network

Record authorship, coauthorship, affiliation at publication, supervision or project membership only when evidenced. Do not infer a school from coauthorship or institutional proximity.

### Version network

Connect working papers, conference papers, journal articles, chapters, books, translations, editions, and replication updates. Select the citable version deliberately and preserve the earlier path.

### Argument and position network

Record `supports`, `extends`, `qualifies`, `contradicts`, `reframes`, `borrows_concept_from`, or `does_not_engage`. Require explicit textual or source-level evidence and a location when possible. Coauthorship, citation, or shared data is insufficient.

### Dataset, archive, and historical-source genealogy

Use the many-to-many use matrix in addition to edges. Record producers, versions, transformations, inherited constructions, and replication access.

## Paper–dataset/source use

For each work–resource relation record:

- `source_id`;
- `dataset_id`;
- resource name and producer/custodian;
- version;
- temporal and geographic coverage;
- unit of analysis;
- role: `outcome`, `treatment`, `exposure`, `control`, `instrument`, `validation`, `descriptive`, `primary_source`, or `context`;
- transformation, coding, deflation, harmonization, geocoding, aggregation, or linkage;
- `inherited_from_source_id` when construction was reused;
- access and replication status;
- claimed new contribution;
- limitations;
- shared or independent evidence status.

Use one row per role when the same resource has materially different uses.

Distinguish:

- common upstream archive with independently collected/coded evidence;
- identical downloaded dataset;
- inherited cleaned panel or variable;
- reproduced table or series;
- linked extension with partially new evidence;
- nominally different datasets built from the same underlying census or archive.

## Evidence independence

Classify:

- `independent`: distinct underlying evidence and construction for the claim;
- `partially_independent`: some new evidence or transformation, but material lineage is shared;
- `shared`: same dataset, series, archive extraction, sample, or inherited construction carries the result;
- `uncertain`: lineage cannot yet be resolved;
- `not_applicable`: theoretical/contextual work not making an empirical confirmation claim.

Never count the number of papers as the number of independent confirmations. Synthesize by evidence lineage and state where several publications are versions or reuses of one evidentiary base.

## Bibliography and KnowledgeWiki promotion

Promote to the authoritative `.bib` only when:

- identity and document type are verified;
- the source is cited or is a committed core/contextual source;
- `bibkey` conflicts are resolved;
- required citation fields are verified rather than inferred.

Promote to KnowledgeWiki only when:

- used claims are checked against full text at the required depth;
- `source_id` and `bibkey` crosswalk is stable;
- the note depth and status match its review role;
- debate vocabulary is supported by more than discovery metadata.

Keep rejected, duplicate, inaccessible, abstract-only, and discovery-only records in review artifacts, not in authoritative bibliography or wiki indexes.
