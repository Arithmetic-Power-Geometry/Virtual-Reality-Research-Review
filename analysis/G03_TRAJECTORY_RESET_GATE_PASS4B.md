# G03 Trajectory and Reset Continuation Gate — Pass 4B

## Added
This pass adds two missing capabilities needed before seeded multi-path experiments.

### Seeded waypoint generator
Relative waypoint instructions are generated reproducibly from a fixed seed. Distances are sampled uniformly from 2–6 m and heading changes from -pi to pi, matching the extracted ARC simulation specification. Motion is discretized at 1 m/s walking speed, 90 degrees/s turning speed and 0.05 s timestep.

### ARC reset continuation
The verified ARC reset-direction selector is now wrapped by an execution endpoint: after reset, physical heading equals the selected safe reset direction, virtual heading is preserved, and the reset counter increments.

The wrapper estimates the nearest obstacle direction numerically from physical ray clearance and uses its opposite as the obstacle normal for the selector.

## Evidence boundary
The primary paper specifies reset direction selection and describes the physical/virtual reset turn. The present implementation uses the post-reset endpoint invariant to resume trajectory. It does not claim that its intermediate reset animation exactly reproduces the authors' simulator. Reset-turn duration and intermediate visual rotation are therefore excluded from scientific comparison until independently resolved.

## Next gate
1. integrate waypoint turns/walks with reset continuation;
2. add polygonal obstacle scenes;
3. run fixed-seed batches;
4. emit machine-readable trajectory/reset summaries and hashes;
5. compare only metrics semantically aligned with the primary paper.
