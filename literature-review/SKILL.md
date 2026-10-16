---
name: literature-review
description: "Design and conduct systematic, scoping, rapid, update, or historiographic literature reviews through an iterative, traceable corpus workflow. Use when Codex must register and amend a review protocol; expand verified seeds into a normalized corpus with abstracts and query lineage; deduplicate and screen articles, books, chapters, theses, and working papers; reconstruct citation, version, argument, author, institution, dataset, archive, and historical-source relations; audit disciplinary and venue coverage; distinguish direct evidence, theory, rivals, methods, and context; assess saturation; promote validated sources into a bibliography or KnowledgeWiki; or position a contribution in economic history, political economy, agrarian or environmental history, and related historical social sciences."
---

# Literature Review

Build a traceable corpus and an evidence-bounded interpretation. A returned result is not a reviewed record; an abstract is not a mature finding; shared data are not independent evidence; and a seed map is not a reconstructed debate.

## Load the right reference

Read:

- [references/iterative-discovery-and-corpus-layers.md](references/iterative-discovery-and-corpus-layers.md) before creating or changing corpus layers, query loops, or screening flows;
- [references/search-and-access.md](references/search-and-access.md) before external discovery, citation chasing, export import, or full-text acquisition;
- [references/identifiers-and-source-lineage.md](references/identifiers-and-source-lineage.md) before assigning identifiers, naming PDFs, resolving versions, or mapping datasets and evidence independence;
- [references/economic-history-and-social-science.md](references/economic-history-and-social-science.md) and its machine-readable [curated venue registry](references/venue-priority-registry.csv) when the review touches economic history or historical social science, or when planning venue-assisted discovery and JCR checks;
- [references/maturity-gates-and-schemas.md](references/maturity-gates-and-schemas.md) before creating artifacts, validating schemas, or declaring a gate;
- [references/synthesis-and-question-refinement.md](references/synthesis-and-question-refinement.md) before refining the question, reconstructing debates, synthesizing, or positioning a contribution;
- [references/external-patterns-and-provenance.md](references/external-patterns-and-provenance.md) only when auditing this protocol or adapting external agent-skill patterns.

Machine-readable schemas live in [schemas/artifact-schemas.json](schemas/artifact-schemas.json).

## Operating principles

- Choose `systematic`, `scoping`, `historiographic`, `rapid`, or `update`; state why. Systematic search may support historiography without turning interpretation into vote counting.
- Treat `orientation` and `maturation` as maturity states, not shortcuts. Orientation may refine scope provisionally; maturation requires documented discovery, screening, full reading, extraction, rivals, and lineage analysis.
- Keep the protocol append-only in substance. Record dated amendments and their triggers; never rewrite the initial question or search retrospectively.
- Use platform-appropriate and discipline-appropriate sources. Do not impose PubMed, arXiv, PRISMA, journal articles, figures, citation thresholds, or fixed paper counts universally.
- Never synthesize a mature claim from abstracts, snippets, catalogue descriptions, or central works not read in full.

## Iterative funnel

Execute this funnel with documented returns rather than as a rigid line:

1. **Initial protocol** — register the initial question, review type, boundaries, criteria, platforms, languages, document types, venue lanes, screening procedure, intended synthesis, access constraints, and stopping rule, together with the conversation map below.
2. **Verified seeds (optional)** — inspect local files and a `Seed Pack for Literature Review` from `wiki-consult` when available. Verify identity and record why each seed matters. When the reviewer does not know the field, or seeds are weak, absent, or only adjacent, record that and build the seed core from anchor venues in step 3: seeds become an output of discovery, not its precondition.
3. **Initial queries** — run both question/concept discovery and seed/network discovery unless an explicit amendment makes one inapplicable. Without adequate seeds, the default entry is the **anchor-venue core**, not broad platform searches: run topic-only `venue_assisted` `ROOT` batches in the anchor venues (see «Anchor venues and the debate frame»), use their book reviews as a route to monographs, give priority to review articles, syntheses, handbook chapters and historiographic essays, shape provisional debates from that core, and select seeds from it. Then extend: seed/network discovery from the core (references and citing works), and question/concept batches derived from the debates to fill gaps, confirm positions and find rivals. Broad platform searches are derived, targeted batches, not the entry point.
4. **Extended corpus** — preserve immutable raw exports, normalize every retained platform record, keep abstracts and vocabulary with provenance, deduplicate identities, and retain retrieval many-to-many relations.
5. **Discovery from records** — extract new concepts, historical terms, authors, institutions, debates, sources, archives, datasets, venues, versions, and rival formulations.
6. **Derived queries and networks** — open child batches linked to their parent batch and trigger; chase citations, authors, venues, versions, arguments, datasets, and archives separately.
7. **Deduplication and screening** — preserve duplicates, exclusions, unavailable texts, and decisions at record level.
8. **Analytical corpus** — promote included works with multidimensional fit and review roles; place useful non-direct works in the contextual/comparative layer.
9. **Full-reading core** — prioritize, acquire, read fully, and extract location-level evidence for sources carrying central claims or debate positions.
10. **Debates and evidence genealogies** — reconstruct positions, relations, versions, sources, datasets, reuse, and evidence independence.
11. **Directed rival searches** — search for contradictions, nulls, alternative mechanisms, boundary conditions, measurement disputes, source critiques, and neglected traditions.
12. **Saturation** — test whether successive batches change concepts, positions, evidence lineages, methods, regions, periods, languages, or conclusions.
13. **Synthesis and contribution** — write only to the maturity actually achieved; state residual gaps and unsupported claims.

Reopen earlier steps when a record reveals a material synonym, historical category, source name, dataset, archive, author cluster, version, venue, rival, or coverage gap. Log the return as a child batch and, if scope or criteria change, append a protocol amendment.

## Conversation map

A case question speaks to literatures larger than its case. Before searching, decompose the question into the conversations the review must enter, and plan `question_concept` batches for each:

- `case`: the topic in the case's place and period;
- `component`: each main process or concept of the question studied in its own right, in any place;
- `relational`: work on the relations the question posits between those components, in any place;
- `field`: the broader disciplinary conversations that frame the problem, its mechanisms and its consequences.

Example: violence and agro-export intensification in Colombia enters violence in Colombia and the Colombian agro-export model (`case`); factors and consequences of political violence, and foreign trade in developing countries (`component`); and the relations between violence and trade (`relational`). Livestock modernization in twentieth-century Mexico enters Mexican livestock history (`case`); technical change in twentieth-century livestock (`component`); the social, political and economic conditions of livestock modernization, and its environmental effects (`relational`).

Place restricts only `case` batches. Elsewhere geography is a tag (`geographic_fit`), never a filter. Record each batch's `conversation` in the query lineage, report coverage by conversation, and do not let the case literature stand in for the others: non-case works carry mechanisms, measures, methods and rivals, not evidence about the case.

## Anchor venues and the debate frame

The reviewer's disciplinary conversation defines where the debates of a review are framed. The default **anchor base** is every active row of the [venue registry](references/venue-priority-registry.csv). It is built from:

- the author's quality whitelist ("Beyond the top five": JCR Q1–Q2 or SJR Q1 journals in history, development studies, area studies and economic history, plus its proposed additions), with the quartile reported by the whitelist kept in `notes` and verified for the current edition before it is cited, recorded with edition, category, date and source in `venue_coverage.csv`;
- the journal families in [../shared/journal_profiles.md](../shared/journal_profiles.md);
- named exceptions (notes `anchor exception`), central to the conversation whatever their quartile: Latin American economic and agrarian history (*Revista de Historia Económica - Journal of Iberian and Latin American Economic History*, *Investigaciones de Historia Económica*, *América Latina en la Historia Económica*, *Historia Agraria de América Latina*) and environmental history (*Global Environment*, *Historia Ambiental Latinoamericana y Caribeña*, *International Review of Environmental History*, *Journal for the History of Environment and Society*).

Inactive rows (for example *Journal of Cleaner Production*) and the business-history titles excluded from the generic registry enter only by protocol amendment. The protocol declares the anchor venues of the review as the active base, or as a subset with a reason; add or drop venues for the project with a reason. Rivals internal to a discipline usually publish in its anchor venues; rivals from other disciplines usually do not, which is why the extension step searches beyond them.

- **Search:** run a `venue_assisted` `ROOT` batch in every anchor venue with the topic terms only. The venue already supplies the disciplinary filter, so do not add historical or geographic anchors.
- **Frame:** seed the provisional debate map from anchor-venue works first, then attach works from elsewhere to those debates or to `other_debate`.
- **Screen:** a work that bears on none of the review's debates and has low relevance to any other may be excluded as `outside_review_debates`, with its reason logged. Never exclude a work for its venue alone, and keep works that challenge the frame (rivals, other disciplines, regional or non-indexed literature) even when they come from outside the anchor venues.

Anchor venues define the frame and the filter of relevance; they do not grade a work's quality or evidence.

## Mandatory discovery tracks

Run and distinguish:

- `question_concept`: questions, mechanisms, actors, outcomes, concepts, rivals, measurements, periods, scales, and multilingual or historical terminology;
- `seed_network`: backward references, forward citations, related works, authors, institutions, venues, editions, working-paper/publication versions, reviews, replies, and critiques;
- `source_data`: archives, censuses, datasets, official series, institutional producers, replication packages, and inherited constructions;
- `venue_assisted`: deliberate coverage of disciplinary-core, adjacent-field, and regional/non-indexed lanes.

Every batch needs a parent or an explicit `ROOT`, an exact query or seed operation, a trigger, a reason, returned/exported/reviewed counts, an immutable export path, discoveries, and a next action.

`results_reviewed` must equal individually reconciled reviewed records plus a quantified, justified exception. API return, download, ranking, or scrolling does not count as review.

## Corpus and identifier invariants

Maintain:

- immutable `raw_results`;
- deduplicated `extended_corpus` with metadata, abstracts, controlled absence states, and retrieval provenance;
- screened `analytical_corpus`;
- fully read and located `core_corpus`;
- separate `contextual_or_comparative_corpus`.

Promote and demote only through logged decisions. An abstract may support discovery, classification, and priority; it cannot close a mature claim.

Keep these identifiers distinct:

- `source_id`: internal, stable, immutable from first discovery;
- `bibkey`: canonical citation key after identity verification, otherwise `PENDING`;
- `pdf_filename`: deterministic `Bibkey_Short_Title.pdf` after `bibkey` verification;
- `wiki_note_slug`: independent KnowledgeWiki identifier.

Use `@bibkey` in Quarto and drafts. Connect corpus, `.bib`, PDF, extraction, and wiki note through `identifier_crosswalk.csv`. Do not use keywords as identifiers, invent a final key, or export the whole extended corpus automatically to the authoritative bibliography or KnowledgeWiki.

## Classification and evidence

Do not collapse relevance into one score. Record at least:

- `geographic_fit`;
- `question_fit`;
- `source_fit`;
- `period_fit`;
- `scale_fit`;
- `disciplinary_tradition`;
- one or more `review_role`.

Allow a work to be direct by geography but adjacent by question, external by geography but direct by mechanism, theoretical, methodological, contextual, a rival, or a reuser of the same source.

Reconstruct separately:

- citation links;
- author and institution links;
- version families;
- argument and position links;
- dataset, archive, and historical-source genealogies.

Coauthorship or shared data does not prove an intellectual school. Require an explicit argumentative relation. Shared sources or inherited constructions default to `shared_or_uncertain`, not independent evidence.

## Core outputs

Create or update as applicable:

- `literature/search_strategy.qmd` with amendment log;
- `literature/query_lineage_log.csv`;
- immutable exports under `literature/raw_results/`;
- `literature/source_batch_relations.csv`;
- `literature/extended_corpus.csv`;
- `literature/screening_log.csv`;
- `literature/corpus_membership_log.csv`;
- `literature/analytical_corpus.csv`;
- `literature/identifier_crosswalk.csv`;
- `literature/extraction_matrix.csv`;
- `literature/debate_matrix.csv`;
- `literature/network_edges.csv`;
- `literature/paper_dataset_use.csv`;
- `literature/data_source_candidates.csv`;
- `literature/venue_coverage.csv`;
- `literature/research_question_handoff.qmd`;
- `literature/literature-review.qmd`;
- `literature/recent_literature.qmd` for updates;
- `literature/references.bib`.

Seed `venue_coverage.csv` selectively from the curated registry; do not copy every venue into every project. Preserve the registry version and venue ID so later coverage remains reproducible.

Legacy `source_discovery_log.csv`, `search_execution_log.csv`, and `corpus_crosswalk.csv` may remain as views during migration; do not silently reinterpret their old rows.

## Gates and handoffs

Apply `G-LITERATURE-ORIENTATION` before passing a provisional question to `research-hypothesis-generation`. Refine conservatively: preserve the initial question and explain every change. Do not let early convenience narrow the project before the extended corpus and major traditions are visible.

Apply `G-LITERATURE` before presenting mature synthesis. A debate cannot be `reconstructed` when a central source is unread, only one position is evidenced, or no serious rival was sought.

Promote to KnowledgeWiki only after identity and used claims are verified:

- contextual source: `knowledge-ingestion` at `quick` depth;
- core source: `full` depth;
- central interpretive source: verified or enriched note as required.

Consume and return `source_id`, `bibkey`, and `wiki_note_slug` separately so the handoff remains compatible with `wiki-consult`.

Validate artifacts with:

```powershell
python literature-review/scripts/validate_review_artifacts.py `
  --schema literature-review/schemas/artifact-schemas.json `
  --literature-dir literature `
  --profile maturation
```

After editing the curated journal list, validate it with:

```powershell
python literature-review/scripts/validate_venue_registry.py `
  literature-review/references/venue-priority-registry.csv
```

## Non-negotiable failures

- Synthesis jumps from seeds or raw results past the extended and analytical corpora.
- Abstracts or keywords supplied by a platform are discarded, or blanks have no absence state.
- A derived query lacks parentage and trigger.
- Reviewed totals do not reconcile to record decisions or a justified exception.
- Exclusions or duplicate/version relations disappear.
- `source_id`, `bibkey`, PDF, and wiki slug are conflated.
- Venue prestige, JCR quartile, citation count, language, format, or indexation determines inclusion or evidentiary quality.
- A central line is covered through only one venue lane.
- Shared data are counted automatically as independent confirmation.
- A reconstructed debate depends on central unread texts.
- The mature synthesis precedes required screening, full reading, and extraction.
