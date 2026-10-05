# Formal Systematic-Review Pipeline Register

This register converts the verified bibliography into a traceable review corpus. It does **not** treat bibliography membership as automatic study inclusion.

## Stages
1. **Ingestion** — every verified citation receives a stable record ID and normalized metadata.
2. **Deduplication** — DOI is primary key; normalized title is secondary. Duplicate records are retained in the audit trail but only one canonical study proceeds.
3. **Title/abstract screening** — include / exclude / uncertain, with one explicit reason for exclusions.
4. **Full-text assessment** — eligible / excluded / unavailable, with exclusion reason.
5. **Study-family resolution** — multiple papers about the same study/dataset/system are linked rather than double-counted.
6. **Citation chasing** — backward/forward candidates are recorded as separate provenance events.
7. **Corpus freeze** — only after all unresolved records are closed.
8. **PRISMA accounting** — counts are generated from the register, never manually typed into the manuscript.

## Inclusion logic
A study must materially address immersive VR/XR methods, algorithms, systems, interaction, perception, evaluation, applications, reproducibility, or directly relevant enabling infrastructure. Reviews can support landscape/contradiction analysis; primary performance claims should rely on primary studies where available.

## Exclusion logic
Examples: non-immersive visualization without VR/XR relevance; commentary without evidence; inaccessible metadata too incomplete to classify; duplicate reports of the same study when a canonical report is retained.

## Claim boundary
The current verified bibliography is a **candidate evidence library**, not yet the final systematic corpus. PRISMA counts remain provisional until screening/full-text/study-family/citation-chasing stages are complete.
