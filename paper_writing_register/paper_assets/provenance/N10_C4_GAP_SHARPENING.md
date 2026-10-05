# N10 C4 Gap Sharpening — Joint Failure–Reset–Cost Regimes

## Prior-art boundary confirmed
Adaptive Redirection (2022) already formalizes context-dependent switching among multiple redirection strategies and learns partitions of the context space according to which strategy performs best.
SRC (2024) explicitly uses reinforcement learning to switch dynamically among S2C, TAPF, ARC and SRL based on the user's physical and virtual environment.
F-RDW (2025) injects forecast future-position information into multiple existing RDW controllers.
APF-S2T (2024), optimized alignment/APF controllers, predictive reset, DRL walkability, and DGM-RDW further occupy geometry-aware, predictive, learned, and adaptive territory.

Therefore none of the following is novel enough:
- geometry-aware switching;
- controller selection from environment state;
- RL-based selector;
- future-position-conditioned controller adaptation;
- generic combination of several existing controllers.

## Candidate unresolved gap
The corrected benchmark reveals a different question:
**Can controller choice be learned or certified from a jointly modeled regime surface that includes failure probability, reset burden conditional on completion, and controller decision cost, with uncertainty and held-out-geometry generalization?**

This differs from choosing a controller solely to minimize reset count because:
1. failed runs are retained as first-class outcomes rather than assigned synthetic reset penalties;
2. reset burden is modeled conditionally on successful completion;
3. computational overhead is explicitly part of utility;
4. uncertainty across seeds/geometry is retained;
5. the selector would be evaluated on held-out geometries/paths, not merely on contexts used to derive the selection rule.

## C4 gate requirements
C4 is granted only if the review establishes that no prior method already optimizes this joint objective with the same failure-aware decomposition and held-out regime validation.

Required evidence before C4:
- exact review of Adaptive Redirection, SRC, F-RDW, APF-S2T, DGM-RDW, DRL walkability and predictive-reset objectives;
- code/artifact availability audit;
- objective-function comparison table;
- reproducibility/comparability map;
- held-out benchmark protocol pre-registration.

Current decision: **C3 strong; C4 pending literature exhaustion.**
