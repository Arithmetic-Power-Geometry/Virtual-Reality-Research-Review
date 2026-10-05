# N02 Path-Model Reproducibility Finding

## Evidence
The Vis.-Poly paper states that static experiments used 100 paths from the Azmandian et al. motion model, averaging roughly 350 m, with random physical/virtual starts and headings reused across controllers. It also frames the redirection problem as maintaining collision-free physical and virtual paths.

Azmandian et al. (2015) define the Exploration (small) virtual-path family with distance ~ Uniform(2,6) m, angle ~ Uniform(-pi,pi), and waypoint count 250 for an expected 1000 m path. The original RDW Toolkit source implements path generation as WALK THEN TURN: the next waypoint is placed along the current forward direction, then the forward vector is rotated for the following segment.

## Reproduction issue discovered
Our earlier harness used TURN THEN WALK and was corrected. After correction, diagnostic failures remain because unconstrained generated virtual trajectories can leave the bounded virtual environment used by the visibility controller. Instrumented failures show virtual coordinates beyond the substitute 14x14 VE boundary and physical boundary crossings before "no eligible physical slice" errors.

The cited path-model description/source does not, in the inspected material, specify an obstacle/boundary rejection or resampling rule for static cluttered VEs. Therefore we must not silently invent one and call it condition-faithful reproduction.

## Reviewer decision
- R3 numerical replication: BLOCKED.
- R2 condition-faithful reproduction: BLOCKED pending explicit resolution of static path validity/obstacle handling.
- R1 protocol-compatible sensitivity: may proceed only with an explicitly declared collision-free path-admission rule, treated as our benchmark condition rather than the published exact protocol.

## Scientific significance
This is itself a reproducibility/evidence finding: controller performance depends on path shape, and the Vis.-Poly paper explicitly identifies path-model effects as an open question. Any benchmark paper should report path-generation semantics as a first-class experimental factor rather than a hidden implementation detail.
