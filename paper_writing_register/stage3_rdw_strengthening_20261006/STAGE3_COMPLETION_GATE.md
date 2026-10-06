# Stage 3 Completion Gate — RDW Experimental and Statistical Strengthening

## User constraint
**No live-user validation will be added.** The RDW contribution is computational/simulation-based and all claims are bounded accordingly.

## Completed
- [x] Frozen explicit descriptors for G01-G04: dimensions, area, perimeter, aspect ratio, internal-segment count/length, and structural description.
- [x] Preserved N07 forensic authority: Vis-Poly 384/400, S2C 378/400, P2R 381/400.
- [x] Added standardized paired effect size d_z for all 12 controller-by-geometry contrasts.
- [x] Retained deterministic bootstrap 95% intervals.
- [x] Retained Wilcoxon inference with BH and Holm multiplicity correction.
- [x] Retained exact paired completion inference.
- [x] Expressed completion contrasts in percentage points.
- [x] Formalized a two-part outcome analysis: completion + reset burden conditional on paired completion.
- [x] Retained Friedman omnibus tests for each geometry.
- [x] Added explicit controller-by-geometry regime-reversal audit.
- [x] Verified all three controller pairs change reset-burden ordering across G01-G04.
- [x] Added multiplicity-sensitivity interpretation using Holm for conservative declarations.
- [x] Added geometry-generalization boundary.
- [x] Frozen N09 computational-cost provenance and complexity interpretation.
- [x] Explicitly separated controller-decision cost from end-to-end VR latency.
- [x] Added manuscript-ready strengthened Methods, Results, and Discussion text.
- [x] Explicitly excluded live-user/perceptual/cybersickness/presence/usability claims.

## Deliberately not fabricated
A factorial controller x geometry interaction p-value is not reconstructed from marginal summaries. Such a model requires the joint seed-level cross-geometry data/covariance. The Stage-3 claim is instead a directly auditable sign-reversal/regime result backed by paired effects, completion discordance, and within-geometry omnibus tests.

A new held-out generated-geometry experiment is not claimed because no separately frozen prospective held-out experiment is available in the authoritative Stage-3 artifacts.

Detailed CPU model/runner OS is not invented where the preserved manuscript-facing N09 provenance does not specify it.

## Stage-3 scientific conclusion
Within the tested deterministic simulation benchmark:
1. no universal controller winner is supported;
2. every pair changes conditional reset-burden ordering across geometry;
3. completion and conditional reset burden can disagree and must be reported separately;
4. geometry G03 exposes the strongest completion-regime reversal;
5. controller computational cost differs sharply in the tested implementation.

These conclusions are computational, not human-subject conclusions.

## Gate
STAGE_3 = COMPLETE
LIVE_USER_VALIDATION = OUT_OF_SCOPE_BY_DESIGN
STAGE_4 = NOT_STARTED
