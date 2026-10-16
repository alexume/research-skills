---
name: wiki-consult
description: Consult, synthesize, and reason over a KnowledgeWiki built from structured research notes. Use when Codex needs to refine hypotheses, brainstorm or connect mechanisms, support a manuscript argument, map claims to evidence, identify exact source needs, prepare a retrieval pack, or draft a memo from KnowledgeWiki indexes, dictionaries, historical source registries, literature notes, and prior research memos. Prefer this skill when the workflow must avoid reading raw PDFs, TXT files, or extracted-text dumps unless the user explicitly asks for them.
---

# Wiki Consult

Use this skill as the entry point for KnowledgeWiki-based reasoning. This skill does not replace specialized research skills; it orchestrates them after building context from the wiki.

## Core Rules

- Treat the KnowledgeWiki as the primary knowledge layer.
- Prefer structured notes over raw library files.
- Do not read `.pdf`, `.txt`, or `extracted_text/` unless the user explicitly asks for that.
- Do not assume a fixed output directory for reports.
- If the user requests a Markdown file and does not provide a destination, ask before creating the file.
- If no output destination is provided, default to chat output only.
- Treat prior memos as secondary synthesis, not as substitutes for literature notes or source registries.
- Resolve the KnowledgeWiki root explicitly before opening fichas.
- Retrieve safely available project and wiki evidence before asking the user to supply it.
- Do not treat repeated qualification as a solution to a missing central bridge.
- Do not treat narrowing as resolution when it removes a central contribution that a specific source or author decision could preserve.

## Locate The KnowledgeWiki

Resolve the root in this order:

1. Use a root path explicitly provided by the user.
2. Use an environment or project variable such as `KNOWLEDGEWIKI_ROOT` if one exists.
3. Search upward from the current working directory for `KnowledgeWiki/`.
4. Read `../shared/local_config.yaml` and use `paths.knowledge_wiki_root` when configured.
5. If none of the above works, ask the user for the root path before proceeding.

Once the root is resolved:
- treat that path as the base for all fiche lookups
- prefer opening navigation files before note files
- do not guess alternative wiki roots if the intended one is missing

## Retrieval Order

Follow the retrieval order in [references/retrieval-order.md](references/retrieval-order.md).

In short:
- Start with indexes and vocabularies or dictionaries. For hypothesis, debate, or review tasks, open `indexes/by_debate.md` and `vocab/debates.yml` first: they map who argues what.
- Then inspect historical-source registries.
- Then open literature notes.
- Then consult prior memos only if they are relevant.

Notes carry a `bibkey` (BibTeX key in the master bibliography). When recommending or citing fichas, reference both the note slug and its bibkey so downstream writing and review skills can cite without re-resolving identities.

## Choose A Mode

### `frontier`

Use when the task is conceptual, diagnostic, or strategic:
- brainstorming
- hypothesis generation
- hypothesis refinement
- mechanism design
- claim-evidence arbitration
- deciding what to read next

This mode should usually produce a `Research Brief`, not a long report.

See:
- [references/mode-frontier.md](references/mode-frontier.md)
- [references/research-brief-template.md](references/research-brief-template.md)
- [references/example-research-brief.md](references/example-research-brief.md)

### `report`

Use when the task is synthetic and output-heavy:
- long memo drafting
- hypothesis-test writeups
- evidence summaries
- structured research notes that integrate several existing fichas

This mode should preferentially consume a prior `Research Brief` or retrieval pack when one exists.

See:
- [references/mode-report.md](references/mode-report.md)
- [references/memo-template.md](references/memo-template.md)
- [references/example-hypothesis-memo.md](references/example-hypothesis-memo.md)

### `argument_support`

Use when an introduction, discussion, conclusion, or interpretation map contains a consequential bridge that needs literature, historical-source support, a rival interpretation, or an author decision.

Read and apply [references/argument-support.md](references/argument-support.md).
Produce an `Argument Support Pack`, not a generic literature summary. Return exact evidence actions and block finalization only for the affected central bridge.

## Orchestrate Other Skills

Use auxiliary skills selectively. Do not load all of them by default.

### Preferred skills in `frontier`

- `research-mechanism-mapping` for actors, institutions, timing, scale, and alternative explanations.
- `research-hypothesis-generation` when the user has a topic but no clear hypothesis.
- `research-hypothesis-refinement` when the user already has a working hypothesis.
- `research-claim-evidence-mapping` when claims need to be separated from support.
- `research-strategy-choice` when it is unclear whether the question is causal, historical-structural, or hybrid.
- `research-causal-identification` when the user wants an empirical test design.
- `research-structural-analysis-design` when the task is processual and historical rather than econometric.

### Preferred skills in `report`

- `research-claim-evidence-mapping` to keep claim-evidence discipline.
- `research-mechanism-mapping` when the memo has a causal or process-tracing core.
- `scientific-writing` when the output needs tighter prose.
- `review-causal-historical-logic` as a final coherence check for temporal or causal claims.

If those skills are unavailable in the environment, continue with the best equivalent workflow inside `wiki-consult`.

### Preferred skills in `argument_support`

- `research-claim-evidence-mapping` to define the burden of each bridge.
- `research-mechanism-mapping` to identify mediation, timing, scale, and rivals.
- `writing-paper-draft` only after the support status and author decisions are explicit.

## Frontier Output Contract

When operating in `frontier`, end with a compact handoff artifact for a cheaper long-context model. Call it `Research Brief` by default.

The brief must contain:
- working question or problem
- refined hypothesis
- subclaims
- mechanism map
- weak links
- evidence gaps
- debate positioning: which debates from `vocab/debates.yml` the question sits in, and which notes occupy each position (from `indexes/by_debate.md`)
- recommended literature notes (slug + bibkey)
- recommended historical-source notes
- recommended prior memos
- next-step instructions for `report` mode

This handoff is mandatory unless the user explicitly asks for a different output.

When the declared goal is a literature review, close the brief with a `Seed Pack for Literature Review`: the list of note slugs + bibkeys that form the seed corpus, the debates already mapped in the wiki, and the gaps the wiki could not fill. The `literature-review` skill consumes this pack in its seed-corpus step instead of re-reading PDFs.

## Report Output Contract

When operating in `report`:
- consume the `Research Brief` first if it exists
- open only the notes needed to complete the assignment
- distinguish direct evidence, inferred synthesis, and open gaps
- preserve temporal and scalar discipline
- avoid turning prior memos into primary evidence

If writing to file:
- use the user-specified path
- if no path was specified, ask before creating files

## Argument Support Output Contract

When operating in `argument_support`, return:

- the bridge or relation being evaluated;
- its evidentiary burden;
- notes and source registries consulted;
- direct support, inferred synthesis, and rivals;
- the strongest warranted formulation;
- material boundary;
- exact next action;
- a user-facing source or author request only when retrieval cannot resolve the gap.

Before returning `narrow`, `park`, or no request for a central bridge, state whether that action preserves the paper's promised contribution. If it does not, return an exact source or author request and mark the affected architecture provisional or blocked.

Do not ask the user merely because the first note is insufficient. Expand within the structured wiki according to the retrieval order first.

## Quality Bar

- Cite which notes support each important claim.
- Separate what the notes say from what you infer.
- Mark speculative bridges explicitly.
- Preserve uncertainty when the corpus is thin.
- Prefer a smaller, higher-fit reading pack over a broad unfocused bibliography.
- When useful, recommend which exact fichas a cheaper model should read next and why.
- Distinguish a missing citation from a missing interpretive decision.
- Mark central unresolved bridges as blocking for the affected section; use precise placeholders for noncentral gaps.
- Treat provisional notes, missing page or section locators, and unverified source summaries as discovery aids rather than sufficient closure when a central historical or interpretive bridge depends on them.
