# Final Manuscript Closing Sections — Abstract, Contributions, Discussion, Conclusion

## Abstract

Virtual-reality (VR) research spans tightly coupled technical and human factors, making cross-study comparison difficult when hardware, tasks, populations, environments, metrics, and validation procedures differ. This systematic evidence review organizes a verified library of 174 records into 173 canonical reports; 171 complete reports were retrieved and assessed, yielding 165 direct eligible VR/XR reports and six supporting/context reports, with two reports not retrieved. We introduce a comparability framework that separates genuine contradiction from semantic incompatibility and a six-level reproducibility taxonomy spanning specification, artifact, execution, regeneration, semantic, and independent-result failure. Among eight pre-specified contradiction families, seven (87.5%) were limited by construct or protocol incompatibility, whereas one (12.5%) represented a controlled regime effect. A redirected-walking case study evaluated Visibility-Polygon, Steer-to-Center, and Potential-to-Redirect controllers across four geometries and 1,200 planned controller-condition cells. Completion was 384/400, 378/400, and 381/400, respectively; paired analyses showed geometry-dependent rank changes rather than a universal winner. Controller-decision medians were 251.448, 2.022, and 3.938 microseconds on the common runner. The synthesis argues that VR evidence should be interpreted through operating regimes, explicit comparability obligations, failure-aware outcomes, and reproducible provenance rather than universal rankings derived from heterogeneous experiments.

**Keywords:** virtual reality; systematic evidence review; reproducibility; redirected walking; comparability; contradiction analysis; cybersickness; presence; interaction.

## Final Contributions

1. A 21-workstream VR evidence architecture linking methods, applications, evaluation, reproducibility, contradictions, and testable gaps.
2. A semantic comparability rule based on problem, input, output, environment/data, constraints, and metric, preventing invalid cross-study rankings.
3. A contradiction framework that distinguishes genuine disagreement from differences caused by task, construct, population, intervention, or validation level.
4. A six-level reproducibility taxonomy separating missing specification/artifacts from execution, regeneration, semantic, and independent-result failures.
5. A failure-aware RDW benchmark in which completion is separated from reset burden and unsuccessful runs are not assigned synthetic performance scores.
6. Controlled evidence that RDW controller ordering changes with geometry, supported by paired inference across four geometries rather than a universal-controller claim.
7. A provenance-first workflow in which immutable workflow artifacts corrected stale summary results before confirmatory inference.
8. A negative novelty result: generic geometry-aware/adaptive controller selection is already occupied by prior art, so the paper does not claim a new RDW controller.

## 8. Discussion

### 8.1 What the evidence supports

The principal result of this review is not a universal ordering of VR technologies. It is that the validity of a comparison depends on the operating regime and on whether the compared evidence answers materially compatible questions. Across interaction, embodiment, avatars, security, education, reproducibility, healthcare, and locomotion, apparently conflicting results often become coherent once task, construct, population, intervention, hardware, metric, and validation level are made explicit. In the eight audited contradiction families, seven were comparability-limited rather than controlled contradictions. This 87.5% proportion should not be interpreted as corpus-wide prevalence; it quantifies the deliberately selected contradiction audit and demonstrates the practical importance of semantic screening before synthesis.

The RDW case study provides the complementary result. Here the comparison is controlled: controllers share geometries, paired seeds, path-generation logic, reset policy, safety rules, and metrics. Under these conditions, controller ordering still changes with geometry. S2C has the lowest reset burden in G01, G02, and G04 among the strongest pairwise contrasts, whereas Vis.-Poly becomes favorable in the difficult G03 geometry and also completes more G03 runs than P2R. The appropriate conclusion is therefore a controller-by-geometry regime effect. This is stronger than an apparent cross-paper contradiction because the relevant nuisance factors are controlled, but narrower than a claim that geometry alone determines performance in all RDW settings.

### 8.2 Robustness and burden are different outcomes

The corrected RDW evidence also shows why failed runs must remain visible. Across all geometries, completion was 384/400 for Vis.-Poly, 378/400 for S2C, and 381/400 for P2R, but the relative completion pattern changes by geometry. Reset burden is computed only on paired completed runs. Combining failure and burden through an arbitrary penalty would change the estimand and could manufacture a ranking. Separating them exposes the actual decision problem: a practical controller must balance failure probability, burden conditional on success, and computational overhead.

The N09 microbenchmark adds a third dimension. Vis.-Poly's median controller-decision time was 251.448 microseconds, compared with 2.022 microseconds for S2C and 3.938 microseconds for P2R on the common runner. These are not end-to-end VR latencies, but they show that methods with different geometric reasoning can have substantially different computational costs. A meaningful future controller-selection problem therefore cannot be reduced to reset count alone.

### 8.3 Reproducibility as a layered claim

The review's reproducibility synthesis separates six failure levels because code availability, executability, numerical regeneration, semantic fidelity, and independent reproduction answer different questions. Public artifacts can improve inspection while still failing to regenerate a published result; conversely, missing public code does not prove that a result is false or irreproducible. The strongest claims should identify exactly which level has been demonstrated.

The RDW workflow illustrates this principle internally. Earlier summary artifacts overstated completion for two controllers. Re-examination of immutable workflow artifacts and job logs corrected the values before confirmatory analysis. The important lesson is not merely that an error occurred, but that provenance made the error detectable and correctable. Reproducibility infrastructure should therefore preserve raw execution evidence and transformations rather than only final tables.

### 8.4 Implications across VR domains

For presence and embodiment, the framework argues against treating questionnaires, physiological signals, neurophysiological measures, agency, ownership, and self-location as interchangeable observations of one latent quantity without validation. For avatars and social VR, human resemblance, animation quality, customization, identity, and behavioral realism should be modeled as distinct factors. For cybersickness, exposure duration, locomotion, display characteristics, individual susceptibility, and measurement instrument are potential moderators rather than noise to be ignored.

Networking and rendering evidence similarly requires end-to-end interpretation. A rendering optimization that reduces computational work may shift cost to communication or sensing; an edge-assisted streaming method may improve bandwidth efficiency while introducing dependency on latency, prediction, or network topology. Healthcare and education evidence requires equivalent caution because intervention content, instructional design, population, comparator, and outcome instrument can dominate the nominal fact that VR was used.

### 8.5 What remains a research opportunity

The N10 prior-art audit rules out a simple novelty claim based on switching controllers according to geometry or context. Adaptive, predictive, reinforcement-learning, APF, and strategy-switching approaches already occupy that space. A narrower future problem remains: jointly model failure probability, reset burden conditional on completion, controller decision cost, and uncertainty, then test a pre-specified policy on held-out geometries and paths. This is retained as future work rather than presented as a contribution of the current paper.

More broadly, the most productive VR gaps may be failure-boundary questions: where an interaction technique becomes inaccessible, where a network/rendering pipeline crosses an unacceptable latency threshold, where avatar fidelity ceases to improve social experience, where cybersickness offsets task benefit, or where a controller changes rank. Such questions are more falsifiable than generic calls for “more realistic,” “more immersive,” or “more adaptive” systems.

### 8.6 Review limitations

The final registered evidence-library flow contains 174 verified records, one exact duplicate, 173 canonical reports, 171 retrieved reports, 165 direct eligible reports, six supporting/context reports, and two reports not retrieved. The two inaccessible reports remain explicit rather than being classified from abstracts alone.

A further limitation concerns identification provenance. The repository preserves the verified evidence library and its subsequent formal screening, but it does not preserve reliable raw yield counts for every database query used during the earlier discovery phase. We therefore do not reconstruct database-specific counts retrospectively. The reported flow is a reproducible accounting of the registered curated evidence library, not a claim that the original database-identification stage can be recreated record-for-record. This distinction should remain visible in submission.

Finally, the RDW benchmark is simulation-based, uses four geometries, and evaluates three executable controllers under one common implementation environment. The observed regime effect is internally controlled but requires live-user and broader-geometry validation before being generalized to deployed VR systems.

## 11. Conclusion

VR evidence is most informative when the conditions under which a result holds are treated as part of the result itself. Across the reviewed domains, many apparent contradictions arise because studies use different tasks, constructs, populations, interventions, hardware, metrics, or validation levels. The eight-family contradiction audit demonstrates this directly: seven families were comparability-limited, while the controlled RDW family exposed a genuine regime effect.

The redirected-walking benchmark reinforces the same conclusion experimentally. Visibility-Polygon, S2C, and P2R controllers showed different completion, reset-burden, and computational-cost profiles, and their ordering changed with geometry. No controller was universally best. The paper therefore rejects a new-controller novelty claim and instead contributes a failure-aware, provenance-backed way to reason about conditional performance.

The broader methodological implication is that VR reviews should move beyond inventories of techniques toward explicit evidence obligations. Comparability should precede ranking; failure should remain distinct from conditional performance; reproducibility should identify the level actually demonstrated; and research gaps should progress from observation to corroboration, testability, benchmark readiness, and experimental evaluation. Under this view, the most useful open problems are not unsupported absences in the literature but reproducible boundaries where existing methods change behavior, fail, or cease to generalize.
