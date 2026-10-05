# N01 — Pre-R1 Semantic Correctness Audit and Adversarial Review

## Decision
**REJECT AS PREVIOUSLY IMPLEMENTED; CORRECTION IN PROGRESS.**

The audit found two reject-level issues before any R1 result was frozen.

## Finding N01-R1 — published geometry was incorrectly marked unavailable
**Severity: CRITICAL.** The Vis.-Poly supplementary material publishes explicit environment coordinates for Experiments 1–4. The prior protocol row VP-SIM-017 therefore understated available evidence.

**Resolution:** register the published static environment coordinates and change the protocol status from unresolved to exact geometry available. R1 substitute geometries remain useful for sensitivity analysis, but they are no longer sufficient as the only geometry evidence.

## Finding N01-R2 — reset trigger used heading-ray clearance
**Severity: CRITICAL.** The implementation checked only forward heading clearance. The published simulator represents the user as a 0.5 m radius circle and incurs a reset within 0.2 m of any physical obstacle, i.e. a 0.7 m center-to-obstacle boundary threshold.

**Resolution:** reset detection now uses Euclidean distance to the nearest physical segment.

## Finding N01-R3 — obstacle normal was estimated by 360 sampled rays
**Severity: HIGH.** ARC specifies the normal of the closest obstacle face that triggered the reset. Angular ray sampling can select a different direction and introduces an unnecessary discretization.

**Resolution:** compute the closest point on the nearest segment and use the normalized vector from that face to the user as the away-facing normal. Segment-endpoint ties remain a declared geometric convention.

## Finding N01-R4 — active slice and average slice length
**Severity: PASS.** Primary text defines active slice by argmin angular distance between slice bisector and virtual heading. The repository implementation matches this rule. Average slice length is the mean of the two kernel-to-boundary radial segment lengths; repository implementation matches Eq. (2).

## Finding N01-R5 — physical-slice eligibility and area matching
**Severity: PASS.** Primary text restricts physical slices to bisector offset < pi/2 and chooses the eligible slice with area closest to the active virtual slice. Repository implementation matches the equations. The deterministic secondary tie-breaker is an implementation convention and must be documented because the paper does not specify ties.

## Finding N01-R6 — gain selection
**Severity: CONDITIONAL PASS.** Translation ratio and bounds, rotation bounds/toward-away rule, and curvature direction/radius match the primary equations. The simulator-level convention mapping gain values to physical/virtual pose increments remains an implementation convention to validate against canonical RDW gain definitions before numerical-replication claims.

## Finding N01-R7 — static path generator
**Severity: CRITICAL FOR R2/R3, NOT R1.** The paper states that static paths use the Azmandian et al. motion model, 100 paths, random physical/virtual starts and headings shared across controllers, with mean path length about 350 m. Exact path instances/seeds are not published in the paper. The cited path model must be reconstructed before condition-faithful comparison.

## Revised gate
N01 does **not** authorize the large scientific R1 run until the corrected geometry/reset tests are green. After those tests, R1 sensitivity may proceed as a declared sensitivity study. In parallel, published static environments should be used to advance R2 condition-faithful reconstruction.

## Reviewer recommendation
**MAJOR REVISION / REJECT current scientific run; accept corrected infrastructure for re-review after CI.**
