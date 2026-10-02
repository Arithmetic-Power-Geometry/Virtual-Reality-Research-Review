# G03 R1 Paired Geometry-Sensitivity Experiment — Pass 5C

## Question
Does the Vis.-Poly reproduction candidate's reset behavior remain stable when the same seeded virtual waypoint instructions are replayed across declared substitute physical geometries?

## Design
A paired design uses identical seeds and waypoint instructions in four physical scenes: open convex, single occluder, two occluders, and asymmetric rectangular. The virtual environment and controller implementation are held fixed.

Default batch: 10 seeds x 4 scenes = 40 paired runs, eight waypoints per seed.

## Outputs
The workflow-ready harness emits run-level CSV, scene summary CSV, a manifest, and SHA-256 hashes. Scene summaries report mean and sample standard deviation of resets per 100 m.

## Interpretation rule
This is an R1 protocol-compatible sensitivity experiment. A geometry effect may establish that benchmark geometry materially affects controller outcomes. It does not by itself establish a weakness unique to Vis.-Poly, because comparator controllers have not yet been run under the same paired design.

Therefore:
- no superiority claim;
- no novel-controller claim;
- no direct numerical comparison with the original paper;
- no C4 gap promotion from this experiment alone.

## Paper timing
The paper is intentionally deferred. After R1, the project must add comparator baselines, promote only corroborated/testable gaps, evaluate any justified new method with ablations/robustness/cost, freeze all workflow artifacts, and then write the paper from the frozen evidence.
