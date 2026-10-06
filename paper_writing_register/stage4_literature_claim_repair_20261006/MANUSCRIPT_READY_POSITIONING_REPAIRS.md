# Stage 4 Manuscript-Ready Literature Positioning and Claim Repair

## Replacement paragraph — end of Introduction

The contribution of this review is therefore not breadth alone. Virtual-reality scholarship already contains mature domain reviews of locomotion, cybersickness, interaction, education, haptics, security, accessibility, rendering, and other subfields. The unresolved problem addressed here is how evidence from those lanes should be compared when studies differ in problem definition, input, output, environment or data, constraints, metrics, populations, and validation level. We operationalize those obligations in a cross-domain evidence architecture and then test their practical consequence through a controlled redirected-walking case study. The case study is intentionally not presented as a new controller: adaptive, predictive, learned, and strategy-switching redirected-walking approaches already occupy that design space. Instead, it asks whether common simulation semantics are sufficient to produce a stable controller ranking once geometry, execution failure, reset burden, and decision cost are considered together.

## Replacement contributions

The paper makes the following bounded contributions.

1. It organizes the frozen VR/XR evidence library through a 21-workstream architecture connecting methods, applications, evaluation, reproducibility, contradictions, and testable gaps.
2. It operationalizes semantic comparability through six fields—problem, input, output, environment or data, constraints, and metric—so that numerical results are not treated as commensurate merely because they share a topic label.
3. It audits eight pre-specified contradiction families. Seven are limited by construct or protocol incompatibility, while the RDW family supplies a controlled regime effect; the resulting 7/8 split is reported only for these audited families and not as a prevalence estimate for VR as a whole.
4. It applies a six-level operational reproducibility taxonomy separating specification, artifact, execution, regeneration, semantic, and independent-result failures.
5. It provides a failure-aware RDW benchmark that reports completion separately from reset burden conditional on paired completion, rather than assigning synthetic performance scores to failed runs.
6. It shows that all three tested controller pairs reverse their conditional reset-burden ordering across the four declared geometries, while completion behavior also changes, so no universal winner is supported within the benchmark.
7. It adds a common-runner controller-decision cost comparison and preserves the distinction between algorithmic overhead and end-to-end VR latency.
8. It demonstrates provenance-first correction in practice: immutable workflow artifacts were used to identify and supersede stale manuscript summaries before confirmatory inference.
9. It records a negative algorithm-novelty decision. The present paper claims no new RDW controller, adaptive selector, or predictive switching mechanism.

## Replacement Related-Work subsection — Position of the RDW case study

### Redirected walking: from controller taxonomies to regime-aware comparison

Redirected walking has progressed from fixed steering and reset techniques toward constrained-environment methods, visibility-based redirection, prediction, learning, multi-user control, and adaptive strategy selection. This progression matters for the present paper in two ways. First, earlier constrained-environment and tracking-area studies already establish that physical-space configuration can influence redirected-walking performance. Geometry dependence is therefore not introduced here as a new concept. Second, recent adaptive and predictive methods—including learned walkability, future-position conditioning, predictive reset, and strategy switching—make a generic claim of "geometry-aware adaptation" insufficient for algorithmic novelty.

The present case study occupies a different position. It fixes three executable controllers, common simulation semantics, common seeds, common reset logic, and four declared physical geometries, then asks whether the resulting evidence supports a context-free ranking. The answer is negative. Every controller pair changes the sign of its paired reset-burden difference somewhere across the four geometries, and completion differences do not always move in the same direction as conditional reset burden. The contribution is therefore an empirical comparison result and an evidence-design lesson: controller evaluation should expose operating regime and failure behavior instead of compressing heterogeneous conditions into a single leaderboard.

This interpretation is deliberately narrower than a new-controller claim. The prior-art audit shows that adaptive, predictive, learned, and switching mechanisms are already represented in the RDW literature. A future algorithmic study would need a sharper objective—such as jointly reasoning about failure probability, conditional reset burden, computational cost, uncertainty, and held-out geometry—and would require its own prior-art audit and prospective evaluation. That future problem is not claimed as a contribution of this review.

## Replacement Discussion subsection — What is actually new

### Evidence contribution rather than controller invention

The broad VR literature already documents heterogeneity. Presence instruments differ, cybersickness protocols differ, interaction techniques are task dependent, educational comparisons can be confounded, security proposals vary in validation strength, and open-source tools do not automatically produce reproducible studies. The present paper's contribution is to make those differences operational at comparison time. A result enters a direct comparison only when its problem, input, output, environment or data, constraints, and metric are sufficiently aligned for the intended claim.

The contradiction audit illustrates why this matters. Seven of eight pre-specified families that initially appear to contain disagreement are better explained by differences in constructs, interventions, populations, tasks, metrics, or validation level. This 87.5% figure describes the audited set only. It should not be read as an estimate that 87.5% of contradictions in VR are spurious. The eighth family—the RDW case study—is valuable precisely because the competing controllers are placed under common simulation semantics and paired seeds. The resulting change in controller ordering can therefore be interpreted as a regime effect rather than dismissed as cross-study incompatibility.

The RDW result also clarifies what the simulation can and cannot establish. It can show that completion, reset burden, geometry, and controller-decision cost jointly complicate algorithm ranking. It cannot establish perceptual gain detectability, cybersickness, presence, comfort, preference, or usability because no live-user experiment is included. Human-facing RDW studies remain important literature context, but their outcomes are not inferred from the computational benchmark.

## Replacement limitation paragraph — review provenance

The evidence flow is frozen for the registered curated library: 174 verified records were reduced to 173 canonical reports, 171 reports were retrieved and assessed, 165 were directly eligible, six were retained as supporting/context evidence, and two reports were not retrieved. The project does not preserve reconstructible raw yield counts for every original bibliographic database/source query. Those early identification counts are therefore not recreated retrospectively. The PRISMA-style counts in this paper describe the registered evidence-library flow and should not be interpreted as a fully reconstructible database-identification history.

## Replacement conclusion paragraph

The review does not identify a single technology, interface, metric, or controller that can be ranked independently of its operating regime. Its stronger conclusion is methodological: comparison itself has evidence obligations. Across the reviewed VR domains, construct definitions, tasks, environments, populations, metrics, and validation levels determine whether two results can legitimately be placed on the same scale. The controlled RDW case study makes that principle concrete: under common simulation semantics, all three controller pairs change conditional reset-burden ordering across geometry, completion behavior can tell a different story, and computational overhead differs sharply. These findings support regime-aware, failure-aware, and provenance-preserving evaluation. They do not constitute a new RDW controller and, without live-user validation, they do not imply human perceptual or experiential benefit.
