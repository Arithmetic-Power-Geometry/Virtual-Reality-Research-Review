# N02 R1 Path Admission Design Review

## Reviewer decision
**REJECTED:** segment-wise resampling and whole-path rejection are not accepted as the R1 benchmark generator.

## Evidence from tests
1. Segment-wise distance resampling dead-ends when the current heading points toward a boundary because RDWT semantics are WALK THEN TURN.
2. Whole-path rejection preserves those semantics but becomes impractical for long paths in a bounded VE: 40-100 segment candidate paths repeatedly failed admission even after 100,000 attempts.
3. Therefore neither method is a defensible route to the published-scale ~350 m benchmark.

## Correct next design
Use a separately declared **navigation-aware collision-free R1 benchmark path family**. This does not claim to reproduce the unpublished/static-scene path-validity procedure of Williams et al. The random Azmandian Exploration-small model remains relevant as a reproducibility boundary and distributional comparison, not as the generator forced into bounded cluttered substitute VEs.

## Literature basis
- Azmandian et al. published navigation-mesh-based path prediction for redirected walking (3DUI 2016, DOI 10.1109/3DUI.2016.7460032).
- Vis.-Poly explicitly distinguishes static Azmandian-model paths from dynamic ORCA collision-free trajectories and states that path-model effects warrant future investigation.
- Simulation-validation work shows that virtual walking paths are an experimental factor in RDW evaluation.

## Gate
No full R1 experiment until the navigation-aware generator has:
- deterministic tests;
- collision-free/boundary-safe tests;
- path-length target tests;
- common path reuse across controller conditions;
- provenance manifest;
- adversarial reviewer PASS.
