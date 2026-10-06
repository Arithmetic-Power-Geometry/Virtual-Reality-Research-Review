# Stage 5 Final Table/Figure/Algorithm Asset Map

## Authority rule
Only assets consistent with the N07 forensic correction and later frozen statistics may appear in the final submission. Earlier N03/N04/N05 figure data that imply 400/400 completion for Vis-Poly or P2R are historical/superseded and must not be plotted in the final paper.

## Final figures to render in Stage 6
1. **Figure 1 — Evidence-library flow.** Source: PRISMA_FINAL_COUNTS.csv. Caption must say registered curated evidence-library flow; it must not imply reconstructed per-database discovery yields.
2. **Figure 2 — Cross-domain evidence/comparability architecture.** Source: A01-A21 codebook + seven-dimension E=(P,I,O,D,C,M,V) operational manual. Conceptual diagram only; no invented frequencies.
3. **Figure 3 — RDW completion by controller and geometry.** Source: Table_N07_corrected_controller_summary.csv. Must show 384/400, 378/400, 381/400 totals consistently.
4. **Figure 4 — Paired conditional reset-burden effects by geometry.** Source: N07 corrected paired effects / Stage-3 PAIRWISE_EFFECT_SIZE_AUDIT.csv; plot mean paired difference with 95% bootstrap CI and zero reference.
5. **Figure 5 — Controller-by-geometry regime reversal.** Source: CONTROLLER_GEOMETRY_REGIME_REVERSAL.csv; emphasize sign changes, not a formal factorial interaction p-value.
6. **Figure 6 — Controller-decision computational cost.** Source: Figure_N09_controller_cost_data.csv / N09 cost pass; label as common-runner decision microbenchmark.

## Final tables
1. Review/evidence-flow counts.
2. Seven-dimension comparability decision rule and Gamma states.
3. Eight-family contradiction/comparability audit.
4. Four RDW geometry descriptors.
5. Corrected controller completion and reset-burden summary.
6. Pairwise effects, bootstrap intervals, Holm-adjusted inference, and completion contrasts.
7. Computational cost and structural complexity.
8. Contribution/prior-art positioning and claim boundary.
9. Reproducibility levels/evidence obligations.

## Algorithm
**Algorithm 1 — Failure-aware paired RDW benchmark and inference workflow.**
Base source: Algorithm_A01_R1_navigation_benchmark.md plus N07/N08 corrections.
Required steps in final pseudocode:
- iterate declared geometry and paired seed;
- execute each admitted controller under common reset/safety semantics;
- store completion separately;
- compute reset burden only for completed runs;
- join controller pairs by seed;
- analyze completion discordance separately from conditional burden;
- apply bootstrap + paired inference + multiplicity control;
- preserve workflow/artifact identifiers.

The algorithm describes the benchmark/evidence procedure. It must not be titled or worded as a novel RDW controller.

## Placement rule
Every table, figure, and algorithm must be introduced and interpreted in prose before placement. Stage 6 may use [H] because the user explicitly requested it, while preserving IEEE two-column readability and using starred floats only when necessary for legibility.

Status: FINAL ASSET CONTENT MAP COMPLETE; RENDERING/TEX PLACEMENT RESERVED FOR STAGE 6.
