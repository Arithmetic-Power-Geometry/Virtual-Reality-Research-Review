# N06 Frozen Multi-Controller Analysis Design

## Controller set
Executable common-R1 controllers:
1. Vis.-Poly — N02 full, 400/400 complete.
2. S2C — N04 full, 378/400 complete; 22 failures retained.
3. P2R — N05 full, 400/400 complete.

Modern literature comparator APF-S2T is not executed because its exact discretization parameters are unresolved in the recoverable primary-method text. See N05_APFS2T_REPRODUCIBILITY_GATE.md.

## Paired design
- seeds: 1001-1100
- geometries: R1-G01..R1-G04
- target virtual distance: 350 m
- common virtual navigation path per seed
- common ARC reset
- same timing and swept-step safety invariant
- total planned controller-condition cells: 3*4*100 = 1200
- observed complete cells: 1178/1200
- all 22 incomplete cells belong to S2C and remain outcomes.

## Primary outcomes
1. Completion probability / failure class.
2. Resets per 100 m among completed runs, explicitly conditional on completion.

## N07 paired comparisons
Within each geometry:
- P2R vs Vis.-Poly: 100 complete pairs.
- S2C vs Vis.-Poly: complete-pair subset, denominator reported.
- P2R vs S2C: complete-pair subset, denominator reported.
For reset burden compute paired mean/median differences and deterministic bootstrap 95% CIs. Report sign counts and multiplicity-adjusted inference.

## Geometry interaction
Test whether controller effect changes by geometry rather than claiming a single universal ranking. Completion and reset burden are modeled separately. Do not assign an artificial reset score to failed runs.

## N08 confirmatory statistics
Predeclare before inspecting inferential outputs:
- paired bootstrap effect CIs;
- nonparametric paired sensitivity analysis;
- family-wise or FDR multiplicity correction across planned pairwise geometry contrasts;
- failure/completion comparisons using paired binary outcomes where applicable;
- effect sizes alongside p-values.

## Claim boundary
Descriptive N05 means do not establish universal superiority. N06/N07/N08 test controller-by-geometry behavior under the declared R1 benchmark only.
