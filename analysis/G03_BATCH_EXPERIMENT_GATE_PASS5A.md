# G03 Seeded Batch Experiment Gate — Pass 5A

## Purpose
Create the first machine-readable multi-path experiment artifact after all component and integration gates passed.

## Harness
The batch harness combines:
- deterministic physical and virtual segment environments;
- seeded 2–6 m waypoint distances and random relative turns;
- 0.05 s timing at 1 m/s and 90 degrees/s;
- Vis.-Poly visibility/slice/gain selection;
- physical pose updates;
- ARC reset detection, direction selection and trajectory continuation.

Ten default seeds (121–130) are executed. Outputs are CSV, JSON summary and SHA-256 hashes.

## Metrics
The harness records path distance, reset count, simulation steps, completion status and aggregate resets per 100 m.

## Evidence boundary
The physical obstacle scene is an engineering stress scene constructed for this repository, not a reconstructed scene from the primary paper. Therefore the resulting reset rate is NOT compared directly with a published reset count. This pass validates deterministic batch execution and artifact provenance.

## Next gate
After CI passes:
1. archive the exact batch artifact and hashes;
2. extract/reconstruct the paper's static environment geometry and path protocol where sufficiently specified;
3. run paired controller seeds;
4. compare semantically aligned metrics;
5. only then decide whether Vis.-Poly reproduction is sufficiently faithful for algorithm comparison.
