# G03 Published-Condition Reconstruction — Pass 5B

## Objective
Reconstruct only the Vis.-Poly simulation conditions that are supported by primary-source extraction. Missing experimental details remain explicit rather than being filled with convenient benchmark choices.

## Reconstructable conditions
The current evidence ledger supports:
- 0.05 s simulation timestep;
- 1.0 m/s walking speed;
- 90 degrees/s turning speed;
- 0.5 m user radius;
- published Vis.-Poly rotation, translation and curvature bounds;
- 100 static simulated paths with approximately 350 m average length;
- 100 dynamic paths with approximately 136 m average length;
- ORCA path generation for the dynamic condition.

ARC-derived reset/path parameters are separately provenance-tagged because Vis.-Poly explicitly reuses ARC resetting, but a reused reset method does not automatically prove that every ARC path-generation detail was identical in every Vis.-Poly experiment.

## Unresolved variables
The exact static environment geometry and exact 100 static waypoint sequences/seeds have not been established from the currently verified text extraction. They are therefore marked unavailable and must not be reconstructed by guesswork.

## Reproduction tiers
- R0: software/component regression.
- R1: protocol-compatible reproduction using exact published parameters plus explicitly substituted environment/path details.
- R2: condition-faithful reproduction with reconstructed published geometry and path generation.
- R3: numerical replication against author artifacts/code or fully specified original inputs.

The repository is currently eligible to proceed from R0 toward R1 only.

## Consequence
Reset counts from the engineering obstacle scene cannot be compared numerically to the paper. The next experiment should instead test whether controller behavior is stable under multiple declared substitute geometries while preserving all exact parameters.

This converts unavailable geometry from a hidden confound into an explicit sensitivity factor.
