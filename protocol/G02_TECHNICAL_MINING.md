# G02 — Technical Algorithm and Benchmark Mining

## Objective
Identify VR problem families in which published computational methods can be compared reproducibly, and distinguish benchmark-ready gaps from literature-only gaps.

## Technical families
T01 Cybersickness prediction/detection
T02 Cybersickness mitigation/adaptation
T03 Locomotion and redirected walking
T04 Foveated rendering and perceptual rendering
T05 Eye/hand/body tracking and pose estimation
T06 Motion prediction and latency compensation
T07 VR streaming, networking, edge/cloud optimization
T08 Privacy/security/authentication
T09 Adaptive and AI-driven VR systems
T10 Accessibility/adaptive interaction algorithms

## Required extraction
Every algorithm record must capture:
- problem definition
- input/output
- algorithm family
- closest baselines
- dataset/environment
- headset/sensors
- train/test protocol
- primary and secondary metrics
- runtime/latency/compute where reported
- human-study outcomes where applicable
- statistical uncertainty
- code/data availability
- reproducibility status
- limitations
- semantic comparability notes

## Benchmark eligibility
Two methods may enter the same numerical benchmark only if their problem formulations, available input information, target output, evaluation environment/data, and metrics are sufficiently compatible. Hardware-dependent runtime results are normalized or kept separate.

## Gap promotion
A technical gap progresses:
C0 author-stated -> C1 candidate -> C2 corroborated -> C3 testable -> C4 benchmark-ready -> C5 evaluated.

C4 requires:
1. at least two defensible existing baselines or a standard baseline plus ablations;
2. accessible data/environment or a reproducible simulator;
3. pre-specified metrics;
4. a missing capability/trade-off that is not already solved by closest work;
5. feasible reproducible implementation.

## Novel algorithm decision
Do not optimize a novelty score. Select a proposed method only when the evidence demonstrates a missing mechanism or unresolved trade-off. A separate technical paper may be preferable if the algorithmic contribution becomes substantial.
