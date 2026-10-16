# Mode `frontier`

Use `frontier` for high-value reasoning tasks where conceptual quality matters more than long output volume.

## Best Use Cases

- formulate a hypothesis from a loose topic
- refine a draft hypothesis
- break a large claim into subclaims
- identify mechanisms, mediations, and omitted steps
- decide which fichas a cheaper model should read next
- arbitrate between competing explanations
- decide whether the next step should be historical, causal, or hybrid

## Workflow

1. Reconstruct the user's question in one or two lines.
2. Build context from indexes and dictionaries first.
3. Select a small, high-fit note set.
4. Invoke auxiliary research skills selectively.
5. Produce a `Research Brief`.

## Required Output Sections

- Working Question
- Provisional Hypothesis
- Refined Hypothesis
- Subclaims
- Mechanism Map
- Weak Links
- Evidence Gaps
- Debate Positioning (debates from `vocab/debates.yml` the question sits in, with the notes on each side per `indexes/by_debate.md`)
- Retrieval Pack
- Next Step For Report Mode

## Retrieval Pack Rules

The retrieval pack is the handoff to the cheaper model.

For each recommended file, include:
- path or identifier (for literature notes: slug + bibkey)
- fit
- what it should be used for
- priority: high, medium, or low

Prefer:
- 4 to 10 high-fit notes
- 1 to 5 source-registry entries
- 0 to 3 prior memos

If prior memos are included, label them as:
- `secondary synthesis`

## Frontier Failure Modes

Avoid:
- opening too many fichas before identifying the conceptual target
- giving broad reading lists without fit labels
- collapsing direct evidence and inference
- producing a long memo instead of a brief
