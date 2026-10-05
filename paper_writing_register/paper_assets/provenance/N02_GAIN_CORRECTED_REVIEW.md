# N02 adversarial review after canonical gain correction

## Decision
**REJECT FOR PAPER CLAIMS — diagnostic value only.**

Workflow 37264391612, head SHA 321be9a846b0c1fb172657afadac09cf4faedb77, passed CI and generated R1 artifacts after correcting the canonical gain convention to virtual/physical.

## Why the reviewer still rejects the numerical result
- One short run still reaches the 100-reset cap and several runs have unusually high reset density.
- The experiment is 10 seeds x 4 substitute geometries with only 8 waypoints; it is not the published 100-path, ~350 m static protocol.
- The summary excludes the reset-cap run, so the displayed mean for R1-G02 is not an admissible unbiased performance estimate.
- Rotation-gain application must be audited at the simulator transformation level. The Vis.-Poly paper specifies minRotationGain when turning away and maxRotationGain when turning toward the optimal vector, while canonical gain definitions are virtual/physical. The exact virtual-to-physical update semantics must be reconciled before scientific performance claims.
- Published-condition experiments should use the exact Experiment 1-3 geometries now reconstructed, while substitute geometries remain sensitivity tests.

## Positive result
The diagnostic demonstrates that geometry/path interactions can produce large variation, but this is not yet evidence of a scientific geometry effect because implementation and censoring concerns remain.

## Next correction
Audit frame-level rotation/translation application against the primary controller and canonical RDW formulation; eliminate censoring bias; then rerun a short gate before scaling to 100 paths.
