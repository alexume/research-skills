# External Patterns and Conceptual Provenance

This file records inspected public implementations and the patterns adapted during the 2026-07 audit. It is provenance, not an instruction to copy their text or assumptions.

## Inspected implementations

### K-Dense-AI — `scientific-agent-skills/literature-review`

- Source: https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/literature-review/SKILL.md
- License: MIT at https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/LICENSE.md
- Adopted patterns: staged planning/search/screening/extraction/synthesis; multi-database intent; deduplication; explicit citation verification; thematic rather than source-by-source synthesis.
- Rejected: biomedical defaults as universal; PICO/Cochrane/AMSTAR hierarchies outside their valid domains; PRISMA and figures as mandatory for every review; fixed database minima; citation, h-index, institution, impact factor, and journal tier as quality proxies.

### ByteDance — `deer-flow/systematic-literature-review`

- Source: https://github.com/bytedance/deer-flow/blob/main/skills/public/systematic-literature-review/SKILL.md
- License: MIT at https://github.com/bytedance/deer-flow/blob/main/LICENSE
- Adopted patterns: explicit phase boundaries; deterministic retrieval helper; structured per-record extraction; transparent failure states; no fabrication or padding; cross-paper synthesis.
- Rejected: arXiv-only universe; one-shot search; retaining results only in agent context; fixed 10/20/30 or 50-paper caps; mandatory subagents; abstract-derived “findings” as mature extraction.

### WenyuChiou — `research-hub/literature-triage-matrix`

- Source: https://github.com/WenyuChiou/research-hub/blob/master/skills/literature-triage-matrix/SKILL.md
- License: MIT at https://github.com/WenyuChiou/research-hub/blob/master/LICENSE
- Adopted patterns: compare known works in a matrix; prefer structured notes before repeated PDF reading; use stable identifiers; leave unknown cells explicit; separate literature comparison from manuscript-claim memory.
- Rejected: a single high/medium/low relevance field; limited PDF reading as a general rule; a known-paper matrix as a substitute for search, screening, full extraction, or debate reconstruction.

### Huangwb8 — `ChineseResearchLaTeX/research-literature-review`

- Source: https://github.com/huangwb8/ChineseResearchLaTeX/blob/main/skills/research-literature-review/SKILL.md
- Repository/registry described as MIT during audit, but no root `LICENSE` file was found through the GitHub contents API; treat license verification as incomplete before textual reuse.
- Adopted patterns: resumable intermediate artifacts; multi-query OpenAlex search; deduplication mapping; explicit abstract coverage warning; validation reports; isolation of raw/intermediate outputs.
- Rejected: fixed word/reference quotas; 1–10 semantic relevance scoring as substantive selection; distribution targets for scores; forced PDF/Word output; high-score-first selection; fixed section structures.

### Awesome Econ AI — `lit-review-assistant`

- Source: https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/literature/lit-review-assistant/SKILL.md
- License: CC0-1.0 at https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/LICENSE
- Adopted patterns: include EconLit, RePEc/IDEAS, NBER, SSRN, method terms, contradictory findings, and working-paper awareness.
- Rejected: summary-card workflow as a complete review; “seminal” discovery through a 1,000-citation threshold; causal-identification focus as universal economics or history standard.

## Finding on field-specific skills

Searches of public GitHub repositories and skill indexes found general scientific, computing, and thin economics-review helpers, but no robust public agent skill specifically implementing economic-history or historical-social-science review with iterative corpus layers, multilingual/regional coverage, version networks, and historical-source/dataset genealogies. The disciplinary calibration in this skill is therefore an original synthesis of workflow requirements and established research practice, not an adaptation of a single external implementation.

## General rejection rules

Do not import:

- PubMed, arXiv, or journal articles as the sole document universe;
- PRISMA as mandatory for historiographic work;
- obligatory figures;
- fixed paper-count ceilings or targets;
- citation count, venue prestige, JCR quartile, author reputation, or institutional affiliation as evidence quality;
- biomedical evidence hierarchies applied mechanically to historical research;
- automatic relevance scores as screening decisions;
- prose synthesis before record-level screening and full-text extraction.

Use external repositories for transferable engineering patterns only. Preserve conceptual provenance and re-implement in language fitted to this protocol.
