---
name: research-historical-source-criticism
description: "Critically assess historical sources by reconstructing provenance, production purpose, survival, coverage, categories, silences, transformations, representativeness, and evidentiary limits. Use when Codex must evaluate archival, administrative, statistical, cartographic, corporate, press, or environmental records; build a historical source registry; triangulate conflicting evidence; or determine which descriptive, causal, structural, or interpretive claims a source can support."
---

# Historical Source Criticism

Evaluate historical evidence before treating it as data or support for a claim. A source is produced by actors and institutions for particular purposes; bias is an object of analysis, not a generic reason to accept or discard it.

## Workflow position

Use this skill at:

- Stage 4 to assess the available source base;
- Stage 8 to define source requirements and acquisition priorities;
- Stage 9 to document acquired sources before extraction or coding;
- Stage 12 to calibrate interpretation and triangulate claims.

Coordinate with `knowledge-ingestion` for secondary literature and fiche creation, `research-evidence-discovery-and-acquisition` for locating and verifying missing empirical sources, `research-historical-measurement` for concept-to-variable decisions, `data-preparation` for transformation, and `research-claim-evidence-mapping` for manuscript claims.

## Required inputs

Recover or request:

- source or collection identifier and location;
- creator, custodian, and chain of transmission;
- date, place, language, and material or digital form;
- stated or inferred production purpose;
- project question, period, geography, and intended claim;
- known selection, digitization, transcription, or aggregation steps.

If the source itself is unavailable, distinguish catalog-level assessment from content-level criticism.

## Step 1: Identify the source and provenance

Record:

- source type and archival hierarchy;
- creator, commissioner, collector, and intended audience;
- original production date versus later copy, edition, or transcription;
- custody, preservation, cataloging, and access history;
- authenticity, completeness, version, and stable identifier;
- access, copyright, privacy, and permission constraints.

Do not collapse a collection, series, volume, document, table, and extracted observation into one source level.

## Step 2: Reconstruct production context

Ask:

- Why was the record created?
- Which administrative, fiscal, scientific, commercial, colonial, or political practice generated it?
- Who had incentives or capacity to report, conceal, classify, or omit information?
- Which categories mattered to the producer, and how did they change?
- What was never intended to be observed?

Treat official status as information about production, not proof of accuracy.

## Step 3: Audit coverage, selection, and survival

Assess:

- target and observed populations;
- geographic, temporal, social, sectoral, and ecological coverage;
- inclusion, exemption, nonresponse, under-registration, and missing volumes;
- survival and preservation bias;
- boundary, jurisdiction, institutional, or classification changes;
- whether absence means zero, not applicable, unrecorded, lost, or inaccessible.

Describe representativeness dimension by dimension rather than assigning one global quality score.

## Step 4: Conduct internal criticism

Evaluate:

- terminology and contemporary meanings;
- units, categories, counting rules, and aggregation levels;
- internal consistency and arithmetic plausibility;
- rhetoric, standard formulas, retrospective accounts, and strategic reporting;
- contradictions within the source;
- distinction between observation, estimate, opinion, and administrative decision.

Never translate historical categories into modern concepts without documenting the interpretive step.

## Step 5: Audit the transformation chain

Trace:

```text
original record
→ catalog or image
→ transcription or OCR
→ extraction
→ coding
→ aggregation
→ analytical variable
→ claim
```

At each step, record actor or tool, rule, uncertainty, correction, and retained link to the original. Keep source values separate from corrected or harmonized values.

## Step 6: Triangulate

Compare independent or differently produced evidence. For agreements and conflicts, distinguish:

- genuinely independent corroboration;
- sources derived from the same administrative series;
- differences in definitions, populations, boundaries, or dates;
- strategic or institutional disagreement;
- uncertainty that cannot be resolved.

Triangulation should explain disagreement, not average incompatible numbers mechanically.

## Step 7: Determine evidentiary use

For each intended claim, classify source support as:

- `direct`: the source observes the relevant object with adequate fit;
- `indirect`: the source supports a proxy, mechanism, or contextual condition;
- `contrastive`: the source helps evaluate a rival interpretation;
- `illustrative`: the source provides texture but cannot establish prevalence;
- `insufficient`: coverage or production prevents the claim.

State whether the source can support descriptive, causal, structural, interpretive, historiographic, or methodological claims, and at what temporal and spatial scale.

## Outputs

Produce or update:

- `analysis/source_criticism.qmd`;
- `project/historical_source_registry.csv`;
- `analysis/data_source_quality.md` when the source becomes data;
- source-specific entries in `analysis/claim_evidence_map.qmd` when interpreting results.

Use this report structure:

```markdown
## Source Identity and Provenance
## Production Context and Purpose
## Coverage, Selection, and Survival
## Categories, Units, and Internal Consistency
## Transformation Chain
## Triangulation
## Claims Supported and Not Supported
## Access, Ethics, and Rights
## Uncertainties and Required Follow-up
## Source-Criticism Gate
```

## References

- Read `references/source-type-guide.md` for source-specific questions.
- Read `references/examples.md` for worked administrative and environmental-history examples.

## Rules

- Preserve stable links from claims and variables to original source locations.
- Cite folio, page, table, image, box, folder, or record identifiers when available.
- Distinguish absence, zero, missing, illegible, and not applicable.
- Never call a source representative without specifying population, place, period, and dimension.
- Never treat precision in a historical table as proof of measurement accuracy.
- Never allow transcription or cleaning to erase original categories or values.
- Record unresolved contradictions rather than forcing agreement.
