# Stage 3 Failure-Aware Two-Part RDW Analysis

## Estimand
The benchmark produces two linked but distinct outcomes:

1. **Completion**: binary success/failure for each controller-seed-geometry run.
2. **Reset burden conditional on completion**: resets per 100 m among seeds for which both controllers in a pair complete.

These outcomes are not collapsed into a single synthetic score. A failed run is never assigned an artificial reset count.

## Part A — completion
For every controller pair within each geometry, the analysis uses paired completion discordance and an exact paired test. With 100 common seeds per geometry, the completion-rate difference in percentage points is (A-only complete - B-only complete).

The strongest completion contrasts are:
- G01 Vis-Poly versus S2C: -8 pp, exact p=0.007812.
- G01 Vis-Poly versus P2R: -8 pp, exact p=0.007812.
- G03 Vis-Poly versus P2R: +13 pp, exact p=0.010622.

Other pairwise completion tests do not cross 0.05.

## Part B — reset burden conditional on paired completion
For seeds on which both compared controllers complete, the estimand is the paired difference in resets/100 m. Stage 3 adds standardized paired effect size d_z = mean(paired difference)/SD(paired difference) to the already frozen mean difference, deterministic 95% bootstrap interval, Wilcoxon test, BH adjustment, and Holm adjustment.

Large absolute paired standardized effects occur in G01:
- Vis-Poly - S2C: d_z=1.403.
- Vis-Poly - P2R: d_z=0.773.
- S2C - P2R: d_z=-0.977.

The effect changes sign across geometry for every controller pair. This is the central regime result.

## Omnibus within-geometry evidence
The triple-complete Friedman tests reject equal controller distributions in all four geometries:
- G01: chi2=100.778, n=92, p=1.31e-22.
- G02: chi2=14.683, n=96, p=6.48e-4.
- G03: chi2=6.059, n=62, p=0.0483.
- G04: chi2=9.531, n=94, p=0.00852.

These are within-geometry omnibus tests; they are not a factorial controller-by-geometry interaction test.

## Controller-by-geometry claim
A formal mixed/factorial interaction p-value is **not** reconstructed from marginal summaries because that would require the joint seed-level cross-geometry covariance. Instead, Stage 3 reports an auditable regime-reversal criterion:

A controller pair has a geometry-dependent regime reversal when its paired reset-burden difference changes sign across the declared geometries and the completion contrast is reported alongside it.

All three pairs satisfy the sign-reversal criterion.

This supports the bounded statement: **within the tested simulation benchmark, controller ordering is geometry-dependent and no universal winner is supported.**

It does not establish perceptual superiority, cybersickness effects, presence effects, usability, or live-user benefit.
