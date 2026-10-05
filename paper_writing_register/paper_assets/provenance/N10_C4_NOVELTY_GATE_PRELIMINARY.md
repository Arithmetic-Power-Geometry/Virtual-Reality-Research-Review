# N10 C4 Novelty Gate — Preliminary Decision

## Question
Does the corrected benchmark evidence justify a new geometry-conditioned redirected-walking controller/selector that is not already substantially occupied by existing adaptive, predictive, learned, switching, or APF-based work?

## Evidence now available
- N07/N08 show controller ranking and completion change with geometry; no universal winner.
- N09 shows materially different controller decision costs: S2C and P2R are far cheaper than Vis.-Poly in the current implementation.
- Therefore a practical selector would need to trade off at least robustness, reset burden, geometry regime, and controller overhead.

## Prior-art pressure
The literature already includes:
- selective redirection / strategy switching for dynamic-environment adaptation;
- predictive future-position RDW;
- APF-S2T target steering;
- DRL methods using spatial walkability representations;
- predictive reset strategies;
- other adaptive/predictive and multiuser RDW methods.

## Decision
**C4 NOT YET GRANTED.**

The empirical regime dependence is real and benchmark-ready, but the concept “select controller according to environment state” is not sufficiently novel by itself because strategy-switching/adaptive RDW already exists.

## What would be needed for C4
A defensible new contribution would need a sharper gap, for example:
1. a formally defined geometry/regime representation tied to measurable controller failure/reset/cost surfaces;
2. evidence that existing switching/adaptive methods do not optimize this joint failure-reset-cost objective or cannot operate under the same reproducible benchmark assumptions;
3. a pre-registered selector or policy whose decision rule is derived from the identified separation rather than hand-tuned after observing test outcomes;
4. held-out geometries and paths demonstrating generalization;
5. direct comparison against at least one modern adaptive/switching baseline where exact reproduction is possible, or a transparent reproducibility block if not.

Until those conditions are met, the manuscript should foreground the **empirical separation and reproducibility finding**, not claim a novel controller.

Status: C3 strong / C4 pending.
