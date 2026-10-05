# N05 P2R Primary-Source Extraction Gate

Primary source: Thomas & Suma Rosenberg, IEEE VR 2019, DOI 10.1109/VR.2019.8797983. Author-hosted manuscript inspected.

## Frozen steering semantics
- P2R is reactive and does not require intended virtual-path knowledge.
- The evaluated P2R uses only the repulsive component of an artificial potential function; the attractive component is not used in the P2R-vs-S2C evaluation.
- Obstacles in the evaluated implementation are convex; environment boundaries are modeled as four rectangular obstacles.
- Each frame, the negative gradient of the potential at the physical user position is computed using centered finite differences.
- Translating: apply maximum signed curvature toward the negative-gradient direction. If dot(negative-gradient, physical-forward) < 0, apply minimum translation gain; otherwise no extra minimum-translation rule is specified.
- Rotating: maximum rotation gain if the turn decreases angular error to the negative gradient; minimum rotation gain if it increases angular error.
- Translation and rotation gains are bounded by Steinicke et al. thresholds; the paper states 0.86/1.26 translation and 0.67/1.24 rotation.
- Maximum curvature in the simulation is radius 7.5 m.
- Simulated speed: 1 m/s; turn rate: pi/2 rad/s; fixed 90 fps.

## Published reset/evaluation semantics
- Three proposed reset strategies: MR2C, R2G, SFR2G.
- Experiment 2 P2R-vs-S2C used MR2C for both controllers to provide a fair reset-controlled comparison.
- Published paths: 100 trials, 100 random waypoints, step distance Uniform[2,6] m, relative rotation Uniform[-pi,pi], same 100 paths per permutation; TURN to waypoint then WALK.
- Published physical environments A/B/C are 10 m or 20 m squares; B has a boundary-adjacent square obstacle; C has a centered square obstacle; obstacle side is 40% of environment side.

## R1 benchmark compatibility decision
**Steering implementation: ADMIT after unit/semantic tests.**
**Direct numerical reproduction: NO.**
Our benchmark uses declared R1 geometries, navigation-aware 350 m paired paths and a common ARC reset. Therefore P2R in N06 will test the published P2R steering policy under a common-reset/common-path benchmark. It must not be described as reproducing Thomas & Rosenberg's reported numerical results.

## Remaining implementation detail
The paper specifies centered finite differences but does not expose a finite-difference step size in the extracted method text. The implementation must therefore either (a) use an analytically equivalent gradient for the stated reciprocal-distance repulsive potential, or (b) register a benchmark numerical step as an implementation parameter and demonstrate sensitivity. No hidden arbitrary epsilon is permitted.

Reviewer decision: **P2R steering semantics PASS; implementation allowed with explicit gradient-computation provenance.**
