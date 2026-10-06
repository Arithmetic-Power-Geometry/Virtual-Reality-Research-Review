# Stage 1 Screening and Disposition Codebook

## Unit of accounting
The canonical unit is a unique report after exact-identifier deduplication. Reviews, taxonomies, software/toolkit papers, and primary empirical papers remain separate reports but must not be interpreted as independent replications of the same primary evidence.

## Deduplication
1. Exact DOI match -> retain one canonical record and log the duplicate.
2. If DOI is absent, exact/near-exact title plus author/year metadata requires manual verification before merging.
3. Reviews that cite a primary study are not duplicates of that primary study.
4. A duplicate is excluded before full-text disposition and is not counted among the 173 canonical reports.

## Title/abstract screening
INCLUDE: directly addresses VR/XR methods, algorithms, systems, interaction, perception, evaluation, applications, reproducibility, or a directly enabling technical component used in the synthesis.
SUPPORTING: not direct VR/XR evidence but materially supports infrastructure, measurement, methodological, or contextual interpretation.
EXCLUDE: duplicate or demonstrably outside the evidence scope.
Uncertainty is resolved at full text where available; absence of full text is not converted into an exclusion reason.

## Full-text disposition
ELIGIBLE: report is in scope and enough authoritative report content was retrieved to assess it.
SUPPORTING: retained only as contextual/enabling evidence and excluded from direct-eligible prevalence claims.
AWAITING_FULL_TEXT / REPORT_NOT_RETRIEVED: targeted retrieval did not yield a legitimate complete report; no eligibility inference is made from abstract alone.

## Inclusion criteria
A report may be direct eligible when it contributes evidence about at least one of the review's VR/XR workstreams, including rendering/display, tracking/sensing, interaction, locomotion/RDW, haptics, audio/multisensory experience, presence/embodiment, cybersickness, avatars, social/multiuser VR, intelligent agents, networking/streaming, privacy/security, accessibility, evaluation/statistics, reproducibility/tooling, healthcare, education/training, or industrial/digital-twin use.

## Exclusion criteria
- exact duplicate;
- clearly non-VR/XR with no enabling/context role;
- non-scholarly item without evidentiary value for the synthesis;
- record whose available information is insufficient for full-text eligibility is **not** labeled excluded solely because retrieval failed.

## Reviewer/coding status
The current corpus coding is author-led. Stage 1 does not claim independent dual-reviewer agreement. Independent validation of workstreams, comparability, C0-C5, reproducibility levels, and contradiction classifications belongs to Stage 2.

## Disagreement policy for Stage 2
Independent coders must code before adjudication. Pre-adjudication values are retained; disagreement is resolved by a documented rule or consensus, never overwritten without provenance.

## Study-family counting rule
Distinct primary studies remain distinct when algorithms, participants, environments, datasets, or experiments differ. Reviews/taxonomies are secondary evidence and do not add independent primary replications. Toolkits support method/reproducibility claims rather than effect-size claims. Foundational instruments are separated from reviews of those instruments.

## Corpus freeze rule
Stage-1 numerical claims use only FROZEN_CANONICAL_CORPUS_173.csv plus DUPLICATE_RESOLUTION.csv.
