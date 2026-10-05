# TVCG Completion and Sequential Execution Plan

This is the master execution order for the Virtual Reality Research Review project. Future "do next" instructions start at the first unfinished blocker.

## Completed
- Review protocol and RQ1-RQ10.
- A01-A21 workstream architecture.
- Controlled review universe and evidence strata.
- C0-C5 gap evidence ladder.
- Seed-review registry and preliminary synthesis.
- Technical mining and RDW prioritization.
- Published RDW controller registry and provenance.
- Vis.-Poly method/parameter extraction.
- ARC reset extraction and clean-room selector.
- 2-D geometry engine.
- Vis.-Poly controller primitives.
- RDW motion semantics.
- End-to-end Vis.-Poly simulator.
- Seeded waypoint generator and reset continuation.
- Batch experiment harness with CI/provenance.
- Published-condition ledger and R0-R3 reproduction tiers.
- Four declared R1 substitute geometries.
- R1 paired geometry-sensitivity harness.
- Paper-readiness gate.

## Remaining work in exact order

| Seq | Task | Required output | Gate |
|---|---|---|---|
| N01 | Pre-R1 semantic correctness audit | verified definitions + patches/tests if needed | BLOCKER |
| N02 | Run and freeze R1 geometry sensitivity | raw CSV + summary + manifest + SHA256 + workflow provenance | BLOCKER |
| N03 | Analyze R1 results | paired geometry metrics + uncertainty + analysis | REQUIRED |
| N04 | Implement first faithful comparator | primary-source ledger + clean-room code + tests | BLOCKER |
| N05 | Add compatible baselines | target 4-6 families where semantic assumptions match | REQUIRED |
| N06 | Controller x geometry x seed experiment | common paired experiment matrix + hashes | CORE RESULT |
| N07 | Ranking/failure-regime analysis | crossover/stability/failure results + figures | CORE RESULT |
| N08 | Statistical analysis | paired effects + CI/uncertainty + suitable tests | CORE RESULT |
| N09 | Computational-cost analysis | cost artifact + table | REQUIRED |
| N10 | C4 gap decision | promote/reject documented gap | NOVELTY GATE |
| N11 | Novel method only if C4 passes | algorithm specification + implementation | CONDITIONAL |
| N12 | Novel-method evaluation | closest baselines + ablation + robustness + cost | CONDITIONAL |
| N13 | Finish A01-A21 study extraction | >=90-95% evidence extraction; technical debt cleaned | PAPER 1 GATE |
| N14 | Complete contradiction/reproducibility/gap maps | quantitative maps + generated figures | PAPER 1 GATE |
| N15 | Reference/reporting freeze | verified references + PRISMA/reporting + evidence matrix | PAPER 1 GATE |
| N16 | Final artifact freeze | CI green + figures/tables from machine outputs + hashes | WRITING GATE |
| N17 | Start manuscript writing | submission-ready TVCG paper(s) from frozen evidence | FINAL |

## Run/commit rule
Every scientific run saves raw machine-readable output, summary, configuration/manifest and hashes where applicable. Each completed unit is committed with a descriptive message. Workflow provenance records run ID, head SHA, status, artifact identity/hash where available, and interpretation boundaries.

## Claim boundaries
R1 is protocol-compatible reproduction with declared substitutes, not numerical replication. Engineering substitute geometries are not the original published scenes. Passing CI is software evidence, not controller superiority. No novel algorithm is claimed before N10 reaches C4. Geometry-aware/adaptive wording alone is not sufficient novelty.

## Paper start gates
Paper 1 starts after N13-N16. Paper 2 starts after N01-N10 and N16. Paper 3 exists only if N10 supports a C4 gap and N11-N12 succeed.

## Immediate next task
**N01: Pre-R1 semantic correctness audit.**
