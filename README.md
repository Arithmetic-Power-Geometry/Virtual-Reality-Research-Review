# Evidence in Virtual Reality Research

This repository contains the software, frozen evidence records, reproducible workflows, benchmark outputs, statistical analyses, and provenance artifacts supporting the study **Evidence in Virtual Reality Research: Comparability, Reproducibility, and Geometry-Dependent Redirected Walking**.

## Study

Virtual-reality evidence is difficult to compare when studies differ in problem definition, intervention, outcome, environment, constraints, measurement, and validation design. The study addresses this problem with a seven-dimension comparability model, a six-level reproducibility taxonomy, an eight-family contradiction audit, and a controlled failure-aware redirected-walking benchmark.

The frozen evidence library contains 174 verified records, 173 canonical reports, 171 retrieved and assessed reports, 165 direct eligible VR/XR reports, six supporting/context reports, and two reports not retrieved. The earliest exploratory per-database yields were not preserved in reconstructible form and are not retroactively reconstructed.

### Comparability model

A study or claim is represented by:

`E = (P, I, O, D, C, M, V)`

where:

- **P** — problem or population
- **I** — intervention or input
- **O** — outcome
- **D** — data or environment
- **C** — constraints
- **M** — metric or measurement
- **V** — validation design

For each dimension, pairwise compatibility is coded as compatible, incompatible, or uncertain. Direct comparison is supported only when all seven dimensions are compatible.

### Reproducibility taxonomy

The project distinguishes six reproducibility states:

- **R0 — Specified:** protocol and parameters are sufficiently specified.
- **R1 — Artifact available:** required code, data, or materials are available.
- **R2 — Executable:** the artifact runs in its documented environment.
- **R3 — Regenerates:** execution regenerates the reported output.
- **R4 — Semantic match:** regenerated output measures the claimed construct or estimand.
- **R5 — Independent result:** an independent compatible implementation or study reproduces the substantive result.

## Evidence audit

Eight pre-specified contradiction families cover interaction, embodiment, avatars, security, evaluation/education, reproducibility, health, and redirected walking. Seven were classified as comparability-limited and one as a genuine controlled regime effect.

An independent second coder recoded all seven comparability dimensions, overall Γ, and family classification for CM01–CM08. Agreement was 8/8 for every coded field, with Cohen's κ = 1.00 for P, I, O, D, C, M, V, overall Γ, and contradiction class. This reliability result applies to the eight pre-specified contradiction families and is not generalized to the complete evidence corpus.

## Redirected-walking benchmark

The controlled benchmark evaluates three executable redirected-walking controllers:

- **Vis.-Poly**
- **S2C**
- **P2R**

Four declared physical geometries are evaluated with 100 paired seeds per geometry and approximately 350 m target virtual travel per run. Completion/failure is retained as a first-class outcome, while reset burden is analyzed only for paired runs in which both controllers complete.

Authoritative completion totals are:

| Controller | Completed runs |
| --- | ---: |
| Vis.-Poly | 384/400 |
| S2C | 378/400 |
| P2R | 381/400 |

Every controller pair changes the sign of its conditional reset-burden difference at least once across the four declared geometries. The result demonstrates geometry-dependent ordering within the declared benchmark; it is not a universal ranking of redirected-walking controllers.

Median controller-decision cost on the common runner was:

| Controller | Median decision cost |
| --- | ---: |
| Vis.-Poly | 251.448 μs |
| S2C | 2.022 μs |
| P2R | 3.938 μs |

These measurements are implementation-specific controller-decision microbenchmarks, not end-to-end VR frame times.

## Research artifacts

The repository preserves the research chain connecting software, configuration, workflow execution, immutable outputs, transformation scripts, and reported results. GitHub workflow artifacts and run-level outputs take precedence over stale derivative summaries when discrepancies occur.

The repository contains:

- frozen evidence-library and screening records
- contradiction-audit and independent-coding artifacts
- redirected-walking implementations and benchmark configurations
- workflow and provenance records
- corrected completion and paired-effect results
- multiplicity-adjusted statistical analyses
- controller-decision microbenchmarks
- figures, tables, and machine-readable research outputs

The redirected-walking experiment is computational. It does not claim live-user evidence for cybersickness, presence, comfort, perceptual detectability, preference, workload, or usability. No new redirected-walking controller is claimed.

## Data and code

The software, data, evidence records, workflow outputs, and provenance artifacts are maintained in this repository:

https://github.com/Arithmetic-Power-Geometry/Virtual-Reality-Research-Review


## License

Software and code in this repository are licensed under the **Apache License 2.0**. See [LICENSE](LICENSE).

Research papers, manuscripts, and other scholarly text retain their respective publication or archive terms and are not relicensed merely by being referenced from this repository.

Copyright © 2026 Mohammad Amir Khusru Akhtar
