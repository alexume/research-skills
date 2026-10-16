# Retrieval Order

Use this order unless the user explicitly overrides it.

## 1. Navigation Layer

Open the smallest files that tell you how the wiki is organized:

- `KnowledgeWiki/indexes/` (for hypothesis, debate, or review tasks, open `by_debate.md` first)
- `KnowledgeWiki/vocab/debates.yml` (the controlled list of controversies the corpus speaks to)
- `KnowledgeWiki/dictionaries/`
- `KnowledgeWiki/vocab/`
- glossary files
- overview files

Purpose:
- identify key terms
- discover note clusters and debate positions
- avoid opening too many fichas too early

If both `dictionaries/` and `vocab/` exist, treat them as the same functional layer.

## 2. Historical Source Layer

Inspect:

- `KnowledgeWiki/historical_sources/`
- source registries
- append-ready identified-source files

Purpose:
- identify archives, series, registries, and source collections
- see whether the corpus already points to missing evidence

## 3. Literature Note Layer

Open only the notes with the strongest fit to the question.

Selection criteria:
- direct topic fit
- mechanism fit
- time-period fit
- region fit
- method fit

## 4. Prior Memo Layer

Inspect prior memos only after the navigation and note layers:

- `KnowledgeWiki/hypothesis_tests/`
- memo folders
- prior synthesis notes

Use them to:
- recover previous reasoning
- detect earlier weak links
- avoid duplicating work

Do not use them to:
- replace literature notes
- replace source registries
- claim direct evidence that only exists in the memo

## Hard Exclusions By Default

Do not read:

- raw `.pdf`
- raw `.txt`
- `KnowledgeWiki/extracted_text/`
- `KnowledgeWiki/raw_extracts/`

Exception:
- only if the user explicitly asks for that material
- or if the existing structured notes are demonstrably insufficient and the user agrees
