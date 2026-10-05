# N04-FULL S2C Comparator — QUALIFIED PASS / FAILURE-AWARE ANALYSIS REQUIRED

Workflow run: 37323011397
Head SHA: 2bccc3eb3639f4d4a8297c1c3b797fa590f6d974
Artifact ID: 11351206228
Artifact digest: sha256:8e45e5d30e48e905f1927913a5c0d91e6ce0d5a141243fcbd22ada8c30e32c1e

Design: S2C only, seeds 1001-1100, four physical geometries, 350 m target, paired against frozen N02-FULL Vis.-Poly.

Integrity audit:
- rows: 400
- seeds: 100 (1001-1100)
- rows per scene: 100
- S2C only: yes
- hash ledger independently matched
- complete: 378/400
- geometry_failure: 13
- reset_cap: 9

Completion by scene:
- G01: 100/100
- G02: 97/100
- G03: 86/100
- G04: 95/100

Complete-run means, resets/100 m:
- G01: 10.8952
- G02: 17.2747
- G03: 25.0209
- G04: 20.0708

Failure-aware reviewer decision:
The workflow PASS is not a 400/400 scientific completion PASS. Failures are retained as outcomes and must not be silently excluded. Reset-rate comparisons may be reported only with explicit complete-pair denominators and alongside completion/failure rates. No global controller-superiority claim is permitted.

Complete-pair S2C minus Vis.-Poly reset-rate differences:
- G01 n=100: -2.7236; S2C lower in 92, higher in 6, ties 2.
- G02 n=97: -0.7308; S2C lower in 64, higher in 29, ties 4.
- G03 n=86: +0.7193; S2C lower in 30, higher in 54, ties 2.
- G04 n=95: -0.9557; S2C lower in 55, higher in 35, ties 5.

Interpretation boundary: G03 preserves the controller-order reversal among complete pairs and also has the lowest S2C completion rate. G04 does not preserve the short-gate reset-rate reversal at full scale. Formal N07 inference remains pending.
