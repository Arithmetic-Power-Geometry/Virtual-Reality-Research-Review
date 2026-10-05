# N05 APF-S2T Primary-Source Reproducibility Gate

Primary source: Chen, Hung, Sun & Chuang, IEEE TVCG 30(5), 2464-2473 (2024), DOI 10.1109/TVCG.2024.3372052. Author/lab-hosted manuscript indexed and inspected.

## Verified core method
- APF at sample p is the sum over uniformly sampled rays of reciprocal distance to the first environment intersection.
- Physical/virtual walkable cells are visibility-polygon-bounded forward regions with included angle 104 degrees.
- The virtual cell is rigidly embedded into PE by aligning virtual user position/heading with physical user position/heading.
- Candidate samples lie in the overlap of physical and embedded virtual cells and must satisfy the reset-safety clearance condition.
- score(p_i) = APF(p_i)/(1 + c(p_i,Pp)); choose the candidate with minimum score.
- Steering direction is from physical user position to the selected target sample.
- With signed steering error theta* and movement d=1.0*0.05=0.05 m:
  curvature gain = theta*/d if achievable, otherwise sign(theta*)/7.5.
- Rotation gain = 0.67 when theta* and signed virtual rotation r have the same sign; 1.24 when signs differ.
- Translation gain = 1.26 when |theta*| exceeds the maximum curvature rotation for d; otherwise clamp(ev/ep,0.86,1.26), where ep and ev are forward clearances in PE and VE.

## Reproducibility issue
The indexed primary-method text establishes uniform spatial samples and n uniformly sampled APF rays, but the currently recoverable method text does not unambiguously expose the exact spatial sample spacing and numerical ray count n. These discretization choices can change target selection and therefore controller behavior.

## Decision
**CORE METHOD: VERIFIED.**
**N06 NUMERICAL ADMISSION: BLOCKED pending exact discretization parameters or an author/code source.**

No arbitrary grid spacing or ray count will be invented. APF-S2T remains a literature comparator and discussion reference, but is not executed in the common R1 benchmark at this gate.

This is a reproducibility limitation, not evidence that APF-S2T is invalid or inferior. The published paper reports APF-S2T outperforming the compared controllers in its own simulation design.

N05 controller set therefore closes with three executable common-benchmark controllers: Vis.-Poly, S2C, and P2R. N06 may proceed with these three while APF-S2T remains a documented non-executable modern comparator.
