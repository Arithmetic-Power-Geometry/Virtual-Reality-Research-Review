# G03 Motion-Semantics Gate — Pass 3C

## Purpose
Separate redirected-walking kinematics from controller selection so pose-update errors cannot be mistaken for controller behavior.

## Explicit conventions
- translation gain maps virtual displacement to physical displacement;
- rotation gain maps virtual angular displacement to physical angular displacement;
- curvature introduces physical heading change according to travelled physical arc length divided by curvature radius;
- walking integration uses midpoint heading over the short arc.

These conventions are isolated in a small module and covered by identity, gain, curvature and invalid-input tests.

## Literature boundary
The Vis.-Poly primary paper defines the three gain types and supplies its gain-selection rules. This benchmark module makes the numerical pose-update convention explicit for reproducibility. Any discrepancy between this convention and a subsequently verified original simulator convention will be recorded and corrected before performance comparison.

## Closest-current-method audit
DGM-RDW (IEEE TVCG, 2026; DOI 10.1109/TVCG.2026.3660749) is now registered. It dynamically constructs dense mappings between physical and virtual geometry and reports extensive comparison with existing RDW controllers. Consequently, geometry-aware alignment by itself cannot support a new novelty claim.

## Next gate
After CI:
1. integrate geometry + Vis.-Poly primitives + motion semantics + ARC reset;
2. create deterministic static polygonal scenes;
3. add trajectory replay and reset accounting;
4. run smoke/regression tests;
5. label the result a reproduction candidate, not validated reproduction, until behavior is checked against published experiment patterns.
