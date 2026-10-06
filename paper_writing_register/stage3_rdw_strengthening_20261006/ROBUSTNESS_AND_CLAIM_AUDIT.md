# Stage 3 Robustness, Sensitivity, and Claim Audit

## 1. Artifact-authority sensitivity
Authoritative values are the immutable workflow artifacts/job logs audited in N07, not superseded manuscript summaries.

Corrected totals:
- Vis-Poly: 384/400 complete.
- S2C: 378/400 complete.
- P2R: 381/400 complete.

Any analysis using earlier 400/400 Vis-Poly or 400/400 P2R summaries is invalid for the final paper.

## 2. Multiplicity sensitivity
Pairwise reset-burden inference is reported with both Benjamini-Hochberg and Holm corrections. The conservative manuscript interpretation uses Holm when declaring familywise-significant pairwise differences.

Holm-significant reset-burden contrasts:
- G01: all three pairs.
- G02: Vis-Poly/S2C and S2C/P2R.
- G03: Vis-Poly/S2C only.
- G04: S2C/P2R only.

This avoids treating nominal or BH-only findings as equally strong confirmatory evidence.

## 3. Completion-versus-burden sensitivity
Completion and conditional reset burden can point in different directions. The analysis therefore never ranks a controller using reset burden alone when completion differs materially.

Examples:
- G01: S2C and P2R both complete more seeds than Vis-Poly; their conditional burden is also lower than Vis-Poly.
- G03: Vis-Poly completes more seeds than P2R (+13 pp, exact p=0.010622) while its paired-complete reset burden is lower descriptively; the Holm-adjusted reset-burden test does not cross 0.05.
- G04: S2C has lower paired-complete reset burden than P2R, while its completion is 5 pp lower; the completion test is p=0.0625.

These cases justify two-part reporting instead of a scalar leaderboard.

## 4. Geometry sensitivity
The physical scenes differ structurally:
- G01 open 10x10 square;
- G02 same square plus one 5 m internal segment;
- G03 same square plus two 5 m internal segments;
- G04 12x8 rectangle plus one 4 m internal segment.

All three pairwise reset-burden contrasts change sign across these four scenes. This is robust evidence that the tested controller ordering is not invariant to geometry.

## 5. Generalization boundary
The four scenes are deterministic declared benchmark geometries, not a random sample from all possible tracked spaces. The study therefore supports **geometry dependence within the tested benchmark family**, not a population-level estimate over arbitrary geometries.

No held-out generated-geometry claim is added because Stage 3 does not have a separately frozen, prospectively defined held-out geometry experiment with authoritative artifacts.

## 6. Human-validation boundary
Per user decision, no live-user validation is part of this study. Consequently:
- no claim about perceptual detectability of applied gains;
- no claim about cybersickness, comfort, presence, embodiment, preference, or usability;
- no claim that lower simulated reset burden necessarily produces better human experience;
- no claim of clinical/behavioral effectiveness.

The RDW case study is a computational benchmark demonstrating controller-by-geometry regime dependence and reproducibility/provenance lessons.
