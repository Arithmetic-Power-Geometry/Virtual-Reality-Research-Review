# Redirected-Walking Benchmark

This benchmark evaluates redirected-walking (RDW) controllers under identical simulated conditions before any proposed controller is introduced.

## Principle

The simulator separates:
- virtual user motion;
- physical tracked-space geometry;
- controller decisions;
- redirection application;
- boundary/reset events;
- metrics.

This prevents controller-specific environment logic from contaminating comparisons.

## Baseline families

The first implementation stage uses transparent baseline families:
1. No-redirection control.
2. Center-steering heuristic.
3. Boundary-aware steering heuristic.

These are engineering baselines, not claims of faithful reproduction of a named published controller. Exact literature controllers are added only after their equations, thresholds, and assumptions are verified from primary sources.

## Initial metrics

- reset count
- boundary violations
- minimum boundary clearance
- physical distance travelled
- virtual distance travelled
- mean absolute injected rotation
- maximum absolute injected rotation

Later literature-aligned metrics will be added only after primary-controller extraction is frozen.

## Determinism

Every stochastic scenario uses an explicit seed. A controller must receive the same virtual trajectory in each paired comparison.

## Research gate

Baseline infrastructure does not establish novelty. A new controller may be formulated only after verified published baselines are reproduced and failure modes remain unresolved.
