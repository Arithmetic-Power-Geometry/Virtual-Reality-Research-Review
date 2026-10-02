# G03 ARC Reset Gate — Pass 2C

## Primary-source extraction

The ARC reset policy is now implementation-resolved.

A reset is triggered when the user comes within 0.7 m of an obstacle. Twenty equally spaced directions are sampled around the physical user position. The chosen reset direction minimizes the mismatch between physical clearance in that sampled direction and virtual clearance along the user's virtual heading, subject to facing away from the obstacle that triggered the reset and, when possible, providing physical clearance at least as large as the virtual forward clearance. If that clearance constraint is infeasible, ARC minimizes the clearance mismatch among directions that still face away from the obstacle.

The user then turns in place toward the selected reset direction while the virtual turn is scaled to a full 360-degree turn. The published method chooses the larger angular route for the physical turn to reduce the required rotational distortion.

## Clean-room implementation

The repository now contains a small independent implementation of the reset-direction selector. It was written from the published mathematical/textual specification. No code from the unlicensed third-party pasumi repository was copied.

The implementation deliberately separates ray/clearance geometry from reset-direction selection so that the rule can be unit-tested independently.

## Vis.-Poly consequence

The Visibility-Polygon paper states that it uses the ARC reset function. This removes the principal reset-policy dependency identified in Pass 2B.

However, a full Vis.-Poly reproduction still requires benchmark geometry capable of visibility polygons and ray-obstacle distances. The existing rectangular scaffold is too simple to claim reproduction in complex polygonal scenes.

## Next gate

1. add polygonal environment geometry and ray casting;
2. add visibility-polygon construction;
3. validate geometry on hand-checkable scenes;
4. integrate the verified Vis.-Poly slice/gain rules;
5. run literature baseline tests;
6. only then compare against engineering controls.

Status: ARC reset rule **implementation-ready and clean-room coded**. Full ARC steering is not yet reproduced.
