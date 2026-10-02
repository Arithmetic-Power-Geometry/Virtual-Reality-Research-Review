# G03 Published-Controller Resolution — Pass 1

## Verified comparison neighborhood

The first primary-literature pass establishes a coherent RDW lineage rather than an arbitrary collection of algorithms:

P2R/APF family (2019) -> RL steering (2020) -> ARC and Visibility-Polygon alignment (2021) -> Adaptive Redirection (2022) -> optimized alignment/APF variants (2023) -> APF-S2T (2024).

### Key evidence

- P2R was introduced as a reactive artificial-potential-function controller for complex spaces.
- APF-RDW extends potential-field ideas to multi-user redirected walking/resetting.
- Strauss et al. formulate RDW steering as continuous-control reinforcement learning, directly prescribing rotation, translation and curvature gains and comparing against Steer-to-Center.
- ARC aligns physical and virtual obstacle proximity and introduces Complexity Ratio for environment-complexity characterization.
- Vis.-Poly. computes physical and virtual visibility polygons, identifies corresponding slices, and derives gains from their alignment; its open manuscript exposes frame-level pseudocode.
- Adaptive Redirection formalizes a context-aware meta-strategy and includes COPPER for pre-planned paths.
- The 2023 optimized-alignment/APF work introduces optimization-driven alignment, APF and integrated controllers.
- APF-S2T (2024) explicitly compares APF-S2G, APF-RDW, Vis.-Poly. and Alignment-Optimized using reset count and average distance between resets.

## Benchmark strata

To avoid invalid comparisons, controllers are divided before implementation.

### R1 — Reactive single-user steering
Candidate methods: engineering controls, P2R/APF variants, ARC, Vis.-Poly., optimized alignment, APF-S2T.

### R2 — Learned steering
RL-Steering is retained as a distinct stratum until its state/action/reward/training assumptions can be reproduced fairly.

### R3 — Meta-strategy/pre-planned
Adaptive Redirection/COPPER is not pooled automatically with frame-reactive controllers.

### R4 — Multi-user
Multi-user APF and later predictive/interaction-aware controllers require separate scenarios and cannot be judged by single-user results alone.

## Immediate implementation order

1. **Vis.-Poly.** — highest priority because open manuscript evidence includes explicit frame-level pseudocode and the method appears in later comparison sets.
2. **ARC** — high priority for obstacle-rich/complex environments.
3. **Alignment-Optimized** — high priority because it is a direct APF-S2T comparator.
4. **APF-S2T** — high priority as the newest verified comparison hub.
5. **APF-RDW/P2R** — extract exact potential equations and parameters.
6. **RL-Steering** — reproduce only if training protocol/state/action/reward can be matched.

## Scientific rule

No literature controller will be coded from its abstract. Implementation begins only after equations/pseudocode, parameter choices, reset logic, gain limits, and scenario assumptions are extracted from a primary full-text source.

## Gap status

The literature already contains sophisticated obstacle-aware, optimization-driven, potential-field, learning-based and adaptive controllers. Therefore a generic claim such as "existing RDW methods do not adapt to the environment" is false or at least materially incomplete.

The remaining novelty search must be narrower and empirical: identify conditions in which these verified families fail under a common benchmark.

## Next gate

G03-Pass-2 will perform method-level extraction for Vis.-Poly., ARC, Alignment-Optimized and APF-S2T, including pseudocode/equations, parameters, gain constraints, reset definitions and original evaluation scenarios. Only then will literature-derived implementations enter the executable benchmark.
