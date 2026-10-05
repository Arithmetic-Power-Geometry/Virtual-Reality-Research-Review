# N05 P2R Full Gate — PASS

Workflow run: 37325937407
Head SHA: 05b041fbe215fe7a466d2893871dc0bf53b16a82
Artifact ID: 11352157903
Artifact digest: sha256:d4cc7175e573d4d4d588bfa6a37cdf98232b80a906b384132955db7c018e615e

Design: published P2R steering policy under common R1 benchmark; seeds 1001-1100; four physical geometries; 350 m target; common ARC reset.

Integrity audit:
- rows: 400
- unique seeds: 100 (1001-1100)
- rows per scene: 100
- controller: P2R only
- complete: 400/400
- failures: 0
- stored SHA256 ledger independently matched runs.csv, summary.csv, failures.json and manifest.json.

Full-run means, resets/100 m:
- G01: 7.79896
- G02: 12.29566
- G03: 22.73469
- G04: 17.60613

Reviewer decision: **PASS for common-reset benchmark evidence.**
Claim boundary: this is not a numerical reproduction of Thomas & Suma Rosenberg (2019), because N05 uses the R1 navigation-aware paired paths and common ARC reset. It evaluates the extracted published P2R steering rule under the same benchmark conditions used for Vis.-Poly and S2C.

No controller-superiority conclusion is frozen here; paired multi-controller inference follows in N06/N07.
