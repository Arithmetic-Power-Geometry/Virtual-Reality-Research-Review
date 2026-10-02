# G03 Vis.-Poly Component Gate — Pass 3B

## Scope
This pass implements the published controller's geometric slice and gain-selection primitives as independent clean-room functions. It does not yet execute the full redirected-walking simulation.

## Components
- visibility-polygon to triangular slices;
- active virtual slice selection by walking direction;
- physical-slice eligibility within 90 degrees of physical heading;
- physical/virtual slice matching by absolute area difference;
- translation-gain ratio clamped to [0.86, 1.26];
- rotation gain 1.24 when turning toward the optimal direction and 0.67 when turning away;
- 7.5 m curvature-radius rule with steering sign toward the optimal direction.

## Tests
Seven component tests isolate slice geometry, directional selection, matching, translation bounds, rotation behavior and curvature behavior. These are mathematical/component tests, not performance validation.

## Reproduction boundary
The 2021 paper establishes visibility polygons as the free-space representation used to steer toward physically visible regions corresponding to the user's virtual region. The present implementation follows the extracted mathematical description but uses this repository's independently implemented visibility geometry.

An end-to-end reproduction still requires:
1. exact physical/virtual pose update semantics for all gains;
2. integration of the verified ARC reset selector;
3. polygonal static/dynamic benchmark scenes;
4. published or equivalently specified path generation;
5. regression checks against reported qualitative/numerical behavior.

No performance claim is permitted before those gates pass.
