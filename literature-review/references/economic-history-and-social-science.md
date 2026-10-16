# Economic History and Historical Social Science

Use this reference as disciplinary calibration, not as a universal hierarchy.

## Contents

1. [Traditions are not interchangeable](#traditions-are-not-interchangeable)
2. [Platform and format coverage](#platform-and-format-coverage)
3. [Venue-assisted discovery](#venue-assisted-discovery)
4. [Curated venue registry](#curated-venue-registry)
5. [Responsible JCR use](#responsible-jcr-use)
6. [Coverage control](#coverage-control)

## Traditions are not interchangeable

Identify how each research line reasons and what it treats as evidence:

- **quantitative economic history**: constructed historical data, identification, measurement comparability, robustness, and economic mechanisms;
- **qualitative economic history**: archival interpretation, institutions, actors, chronology, representativeness, and source criticism;
- **political economy**: strategic actors, institutions, distribution, state capacity, conflict, and causal or comparative designs;
- **agrarian history**: land, labor, tenancy, rural institutions, technology, production relations, and territorial differentiation;
- **environmental history**: socioecological change, landscapes, resources, nonhuman processes, environmental knowledge, and scale;
- **historiography**: changing questions, concepts, archives, periodizations, schools, and interpretive stakes.

Integrate these traditions through explicit questions, mechanisms, scales, source bases, and argumentative relations. Do not treat a difference in method as a rank ordering or infer agreement from shared terminology.

## Platform and format coverage

Select platforms by question and document ecology. Consider:

- Scopus and OpenAlex for broad indexed discovery and citation graphs;
- EconLit for economics subject/JEL indexing;
- RePEc/IDEAS, NBER and discipline-specific working-paper series;
- SSRN for working papers where relevant;
- JSTOR, library catalogues, WorldCat or national catalogues for older journals, books, and chapters;
- disciplinary journal sites and hand-searching;
- SciELO, Redalyc, Dialnet, CLACSO, and national or university repositories;
- theses and dissertations;
- books, edited volumes, chapters, reviews, source notes, institutional publications, and historical publications;
- archival catalogues, census names, dataset producers, official series, ministries, statistical offices, research institutes, and replication repositories;
- multilingual searches in contemporary, historical, and translated vocabulary.

Expect weak indexation of books, chapters, regional journals, older scholarship, and literature in Spanish or Portuguese. Search authors, bibliographies, associations, journal runs, edited volumes, archives, datasets, and institutional series directly.

## Venue-assisted discovery

Venue priority structures deliberate searching. Anchor venues (see `SKILL.md`, «Anchor venues and the debate frame») also frame the review's debates, and a work's relevance to those debates may justify its exclusion. Venue alone never determines article inclusion, quality, evidence strength, or argumentative importance.

### Lane A — disciplinary core

Deliberately search:

- the approximately ten journals in the registry group `core_economic_history_10`;
- journals verified as Q1 or Q2 in the current JCR edition for the protocol-relevant categories; by default *History*, *Development Studies*, and *Area Studies*, with other categories added by protocol amendment;
- central disciplinary journals that are not Q1–Q2, not in JCR, or whose position changed; named exceptions for Latin American economic and agrarian history include *Investigaciones de Historia Económica*, *América Latina en la Historia Económica* and *Historia Agraria de América Latina* (registry rows; verify scope and indexing);
- special issues, debates, review essays, source notes, and classic articles.

`core_economic_history_10` is a curated search set, not an objective league table or a claim that the venues are the ten highest by JIF. Revise it when disciplinary practice, the question, or venue scope changes. Do not call it `JCR top 10`.

The registry carries the author's anchor base (see `SKILL.md`, «Anchor venues and the debate frame»), built from a curated quality whitelist. Quartiles reported by that whitelist are kept in `notes` as orientation only; verify them for the current edition before citing them. Build any further JCR-derived extension from current verification, seed bibliographies, associations, and disciplinary expertise.

### Lane B — adjacent fields

Search in parallel across relevant:

- development economics;
- political economy;
- area and Latin American studies;
- agrarian and environmental history;
- history of science and technology;
- peasant and rural studies;
- historical geography;
- agricultural economics;
- historical sociology and historical political science.

Do not subordinate these fields when they contribute mechanisms, sources, regional evidence, methods, or interpretations absent from the core.

### Lane C — regional and under-indexed literature

Include:

- national and Latin American journals;
- journals outside JCR or in any quartile;
- books, chapters, theses, working papers, institutional documents, historical publications, repositories, and Spanish/Portuguese literature.

Never exclude solely because of quartile, format, language, low citation, or missing indexation.

## Curated venue registry

Use [`venue-priority-registry.csv`](venue-priority-registry.csv) as an editable discovery aid. Its default economic-history core contains:

1. *Journal of Economic History*;
2. *Economic History Review*;
3. *Explorations in Economic History*;
4. *European Review of Economic History*;
5. *Cliometrica*;
6. *Revista de Historia Económica - Journal of Iberian and Latin American Economic History*;
7. *Investigaciones de Historia Económica - Economic History Research*;
8. *Economic History of Developing Regions*;
9. *Australian Economic History Review*;
10. *Scandinavian Economic History Review*.

Keep *Journal of Iberian and Latin American Studies* separately in the adjacent area-studies lane. It is not an alternate title for *Revista de Historia Económica - Journal of Iberian and Latin American Economic History*. Retain both when Iberian or Latin American coverage is relevant.

The registry also carries priority sets for development and agrarian studies, general and comparative history, and Latin American/area studies. *Historia Agraria* belongs to the agrarian bridge; it may also satisfy regional/non-indexed coverage when its language, geography, or source base performs that role. Treat lane assignment as a search function, not an immutable property of the journal.

Do not include *Business History*, *Business History Review*, or *Enterprise & Society* in the generic priority set. Add any of them through a dated project amendment when firms, corporate organization, entrepreneurship, or business archives are substantively relevant. Likewise, treat history-of-economic-thought and specialized labor/slavery venues as conditional rather than mandatory for every project.

For each project:

1. copy only relevant active registry rows into `venue_coverage.csv`;
2. preserve `venue_registry_id` and `registry_version`;
3. record why each venue covers a research line and the years, issues, or terms searched;
4. add project-specific venues rather than forcing the registry to be exhaustive;
5. retain omitted priority venues as `planned`, `inapplicable`, or covered through another source, with a reason;
6. never infer article relevance or evidentiary strength from registry membership.

Article counts, JIFs, quartiles, and category assignments are intentionally absent until verified for the relevant edition. They are volatile metadata, not stable properties of the registry.

## Responsible JCR use

When JCR is used, record in `venue_coverage.csv`:

- `venue_registry_id` and `registry_version` when the venue came from the curated registry;
- `venue_name` and `issn`;
- `venue_tier` as search lane, not quality grade;
- `venue_priority_basis`;
- `jcr_edition`;
- every protocol-relevant `jcr_category`;
- quartile observed in each relevant category;
- `jcr_verified_at`;
- authorized source/export;
- disciplinary fit and search status.

JCR is an annual snapshot; categories and quartiles can change. Do not choose only the category yielding the most favorable quartile. Record all relevant categories and distinguish `not_ranked` from `not_verified`.

If verified access is unavailable:

- set `jcr_status=verification_required`;
- do not guess a quartile;
- create an exact user/library verification action;
- continue through disciplinary fit, seed venues, associations, bibliographies, and specialized databases.

Keep separate:

- venue search priority;
- article relevance;
- design quality;
- evidence quality and originality;
- importance to the debate.

## Coverage control

For every core research line document:

1. disciplinary-core venues searched;
2. adjacent fields/venues searched;
3. regional and under-indexed sources covered;
4. years, issues, terms, and hand-search procedure;
5. access restrictions and incomplete runs;
6. results added and concepts or source leads found from each lane.

A line cannot be sufficiently covered through only one lane. If a lane is genuinely inapplicable, append a protocol amendment explaining why and how the remaining search compensates.

Use the disciplinary core to structure the economic-history conversation while keeping adjacent and regional lanes active throughout rival, mechanism, and source discovery.
