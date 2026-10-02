# G03 Vis.-Poly Reproduction Gate — Pass 2B

## Resolved from primary full text

The Visibility-Polygon controller is now resolved at the gain-selection level.

- Eligible physical slices have bisectors within 90 degrees of physical heading.
- The target physical slice minimizes absolute area difference from the active virtual slice.
- The optimal steering direction is the matched physical slice bisector.
- Rotation gains are 0.67 when turning away and 1.24 when turning toward the optimal direction.
- Curvature follows the signed angular error toward the optimal direction with a 7.5 m curvature-radius threshold.
- Translation gain is the physical/virtual average-slice-length ratio clamped to [0.86, 1.26].

The published simulation uses a 0.5 m-radius simulated user, reset proximity 0.2 m, walking speed 1 m/s, turning speed 90 degrees/s, and timestep 0.05 s. Static experiments use 100 paired paths averaging roughly 350 m; the dynamic experiment uses 100 paired ORCA-generated paths averaging 136 m.

## Remaining dependency

The Vis.-Poly paper states that its reset function is the same as ARC. Therefore Vis.-Poly is not yet marked as a complete faithful reproduction until the ARC reset policy is extracted and encoded.

## Reproducibility lead audit

The third-party pasumi/pasumi repository is public C++ code and cites both ARC and Visibility-Polygon. GitHub reports no repository license metadata. Code from it must not be copied into this project unless licensing is clarified. It may be inspected as independent corroboration of algorithm interpretation.

## Decision

**Gain-selection gate: PASS.**

**Complete-controller gate: HOLD — ARC reset dependency remains.**

The next extraction target is the ARC reset policy and implementation-critical ARC constants. Once resolved, a clean-room Vis.-Poly implementation can be added from the published mathematical description.
