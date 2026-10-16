# Synthesis and Question Refinement

Use this reference after the extended corpus exists and before question handoff, debate reconstruction, or contribution positioning.

## Contents

1. [Conservative question refinement](#conservative-question-refinement)
2. [Research-line reconstruction](#research-line-reconstruction)
3. [Debates and genealogies](#debates-and-genealogies)
4. [Provisional hypotheses](#provisional-hypotheses)
5. [Contribution positioning](#contribution-positioning)
6. [KnowledgeWiki handoff](#knowledgewiki-handoff)

## Conservative question refinement

Compare the initial and refined question across:

| Dimension | Initial | Extended-corpus finding | Refined |
|---|---|---|---|
| Outcome or process | | | |
| Explanatory focus | | | |
| Unit and scale | | | |
| Geography | | | |
| Period | | | |
| Concepts and historical terms | | | |
| Mechanisms and actors | | | |
| Rivals | | | |
| Sources/data required | | | |
| Claim type | | | |

Do not refine materially from seeds or one convenient tradition. Before narrowing, verify that major disciplinary traditions, venue lanes, document formats, and languages have at least orientation-level representation.

Record each change as:

- confirmed clarification;
- literature-driven expansion;
- literature-driven narrowing;
- feasibility constraint;
- provisional decision pending coverage.

If the initial question survives, explain what the corpus confirmed. Preserve the initial wording and dated rationale.

## Research-line reconstruction

For every core line answer:

1. What question and concept does it organize?
2. What mechanism or historical process does it propose?
3. Which actors, institutions, environments, periods, and scales matter?
4. Which positions and serious rivals exist?
5. What primary sources, datasets, archives, or evidence families support them?
6. Which works reuse the same evidence or construction?
7. Which methods or modes of inference are used?
8. What findings are established, localized, contradicted, or unresolved?
9. Which versions, replies, reviews, or reinterpretations changed the line?
10. What design, source, measurement, access, and transfer limits remain?
11. Which traditions or venue lanes are missing?
12. What exact problem remains unresolved?

Keep quantitative economic history, qualitative economic history, political economy, agrarian history, environmental history, and historiography distinct when their questions and evidentiary standards differ. Connect them through explicit mechanisms, scales, and sources.

## Debates and genealogies

Reconstruct a debate only from position-level rows backed by fully read core sources. A debate is:

- `seeded`: one or more candidate positions, central reading incomplete;
- `developing`: at least two positions identified, but core reading, rivals, or lineages incomplete;
- `reconstructed`: central works read and located; at least two positions and a serious rival; argument relations evidenced; source/data reuse and independence evaluated;
- `sparse_documented`: searches show genuinely sparse literature and the allowable claim is narrowed.

Build five linked but separate views:

1. citation network;
2. author/institution network;
3. version network;
4. argument/position network;
5. dataset/archive/historical-source genealogy.

Do not infer a position from citation alone or a school from coauthorship/shared data. Read the passages that establish agreement, critique, extension, or reframing.

Map each debate as points of agreement and points of tension, not only as a list of positions. In `debate_matrix.csv`, add `agreement_points` (what the positions share: facts, chronology, measures, mechanisms) and `tension_points` (what they dispute and which evidence would discriminate), alongside `contradictions` and `rival_position`. In a `seeded` debate these are provisional and come from abstracts; they become claims only after the central sources are read.

Synthesize evidence by lineage:

- independent sources/constructions;
- partially shared constructions;
- repeated publications or versions;
- direct reuse of the same dataset/series/archive extraction;
- uncertain lineage requiring further verification.

## Provisional hypotheses

Generate candidates only after recognizable debates and mechanisms exist. For each record:

- motivating debate and fully read sources;
- expected pattern or sequence;
- mechanism, actors, institutions, and ecological conditions;
- timing and scale;
- observable implication;
- serious rival;
- discriminating evidence;
- relevant source/dataset candidates;
- uncertainty and coverage status.

Label all candidates provisional. `research-hypothesis-generation` owns formal hypotheses; `research-hypothesis-refinement` owns later triage.

## Contribution positioning

Distinguish:

- relatively established knowledge backed by independent lineages;
- repeated claims resting on shared evidence;
- localized evidence;
- unresolved interpretive disputes;
- version or measurement changes;
- source silences and access limits;
- scale, period, geography, and language gaps;
- mechanisms not discriminated;
- what the project can and cannot answer.

State contribution as a positive operation:

- introduce or reconstruct evidence;
- correct, validate, or historicize measurement;
- compare scales, periods, territories, or institutions;
- test or arbitrate mechanisms;
- reinterpret a known pattern;
- connect separate evidence bases;
- establish a boundary condition;
- replicate, extend, or reassess a result.

Absence, a new place, or a prestigious venue gap alone is not a contribution.

## KnowledgeWiki handoff

Consume a `Seed Pack for Literature Review` from `wiki-consult` when available. It should contain note slugs + bibkeys, debates already mapped, and gaps the wiki could not fill.

Return validated sources only:

| Review role | Ingestion depth | Minimum state |
|---|---|---|
| discovery candidate | none | review artifacts only |
| contextual/comparative | quick | claims used verified |
| core | full | verified |
| central interpretive | full | enriched when interpretation depends on it |

Before promotion:

1. verify identity;
2. resolve authoritative `bibkey`;
3. preserve `source_id`;
4. update `identifier_crosswalk.csv`;
5. ingest through `knowledge-ingestion`;
6. update debate/source indexes only after note validation.

KnowledgeWiki is a durable knowledge layer, not a substitute for the extended corpus, screening log, or raw exports.
