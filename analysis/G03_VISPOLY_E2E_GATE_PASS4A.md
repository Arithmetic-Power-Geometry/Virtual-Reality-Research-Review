# G03 End-to-End Vis.-Poly Integration Gate — Pass 4A

## Objective
Connect the independently validated components into the first deterministic end-to-end Vis.-Poly reproduction candidate.

## Integrated pipeline
physical/virtual segment geometry → visibility polygons → triangular slices → active virtual slice → eligible physical slices → area-based slice match → published gain selection → physical pose update → ARC reset trigger.

## Regression scenarios
Three deliberately simple scenes are registered. They test deterministic replay, gain bounds and reset triggering. They are not used for scientific performance claims.

## Important limitation
The current integration detects when the ARC reset threshold is reached but stops at that event. The already-tested ARC reset-direction selector is not yet used to execute the reset turn inside the trajectory. This prevents an accidental partial reset implementation from contaminating controller comparisons.

The virtual path is also a deterministic straight-step replay rather than the original paper's random waypoint/ORCA experiment generator.

## Interpretation
Passing this gate means the software components interoperate coherently. It does not mean the published reset-count results have been reproduced.

## Next gate
1. execute the complete ARC reset turn and resume trajectory;
2. add deterministic waypoint turns;
3. create polygonal obstacle scenes;
4. reproduce the paper's 0.05 s / 1 m/s stepping and 2–6 m waypoint generator;
5. run seeded multi-path experiments;
6. compare qualitative patterns with the published Vis.-Poly/ARC/APF/S2C results before calling the baseline reproduced.
