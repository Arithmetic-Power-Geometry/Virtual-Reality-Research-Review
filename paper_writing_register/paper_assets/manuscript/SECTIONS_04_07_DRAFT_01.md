# Virtual Reality Research: A Systematic Review of Methods, Algorithms, Evaluation, and Open Research Problems

> Draft 03 — Sections 4 and 7. This block synthesizes currently verified evidence without freezing corpus prevalence, final PRISMA values, or N10 novelty.

## 4. Cross-Domain Evidence Synthesis

### 4.1 From component technologies to coupled VR systems

Across the reviewed workstreams, VR performance is rarely attributable to a single component in isolation. Display and rendering choices interact with sensing and eye tracking; interaction techniques depend on task demands and ergonomics; locomotion depends on available physical space and perceptual manipulation; presence and embodiment depend on both system properties and measurement choices; cybersickness depends on motion, display, exposure, and participant factors; social and avatar effects depend on identity, fidelity, behavior, and context; and application outcomes depend on instructional, clinical, or operational design. The evidence therefore favors a coupled-system interpretation in which hardware, software, algorithms, users, environments, and evaluation protocols jointly determine the observed outcome.

This observation changes how broad VR evidence should be synthesized. A method that improves one metric under one task is not automatically superior at the system level, and evidence from one population or application cannot be transferred without checking the intervention and outcome semantics. The synthesis below consequently emphasizes stable patterns, recurrent trade-offs, and evidence boundaries rather than a single cross-domain ranking.

### 4.2 Locomotion, navigation, and redirected walking

Locomotion is one of the most mature technical lanes in the current evidence map. The literature spans natural walking, walking-in-place, teleportation, redirected walking, hybrid techniques, predictive approaches, multi-user methods, reinforcement-learning strategies, resets, and perceptual manipulations. Existing taxonomies show that locomotion techniques differ not only in input mechanism but also in physical-space requirements, navigation fidelity, embodiment, usability, safety, and susceptibility to perceptual side effects.

Redirected walking illustrates why method labels alone are insufficient for comparison. Physical tracking-area size and shape, obstacle layout, virtual path, gain limits, reset policy, prediction horizon, user interaction, and whether evaluation is simulated or live can all alter performance. Prior studies already motivate environment-dependent and prediction-aware control, while the controlled case study in Sections 5 and 6 provides within-benchmark evidence that controller ordering changes across geometry. The appropriate synthesis is therefore conditional: locomotion algorithms should be evaluated over explicit operating regimes rather than summarized by a single best-controller claim.

The same literature also shows an evolution from fixed steering heuristics toward predictive, context-aware, multi-user, and learning-assisted methods. That evolution narrows the space for novelty claims based merely on switching between existing strategies. A defensible algorithmic gap must identify an unresolved decision variable or trade-off and show that it is not already handled by prior adaptive or predictive methods.

### 4.3 Presence, embodiment, and perceptual experience

Presence and embodiment remain central constructs in VR, but their measurement is heterogeneous. Foundational work distinguishes technological immersion from the psychological experience of presence, while subsequent studies employ multiple questionnaires, behavioral measures, physiological measures, and increasingly neurophysiological signals. Meta-analytic evidence supports an association between immersive system features and presence, yet the magnitude and interpretation of effects depend on the feature manipulated and the instrument used.

Embodiment adds further complexity because body ownership, agency, self-location, perspective, avatar appearance, sensorimotor congruence, and social affordance are related but non-identical constructs. Objective or physiological markers can complement subjective reports, but they do not make those constructs interchangeable. Consequently, an apparent disagreement between an EEG-based embodiment result and a questionnaire-based perspective-taking result is not necessarily a contradiction.

Perceptual manipulation also creates an ethical and methodological boundary. Techniques that improve spatial use or redirect behavior may influence awareness, agency, comfort, or trust. The evidence therefore supports reporting both technical effectiveness and experiential consequences when the system intentionally alters perception.

### 4.4 Cybersickness and comfort

Cybersickness research has a comparatively large evidence base but remains difficult to aggregate because studies vary in display hardware, motion profiles, locomotion techniques, exposure duration, participant susceptibility, symptom instruments, timing of measurement, and mitigation strategy. The Simulator Sickness Questionnaire remains influential, but recent syntheses document a broader and fragmented instrument landscape.

The cross-domain implication is that cybersickness should not be treated as a single binary property of a VR technique. It is an outcome conditioned by system, task, exposure, and participant characteristics. Comparisons are strongest when the same symptom construct, instrument, measurement timing, and exposure conditions are preserved. This also affects education, healthcare, and training studies: a positive learning or clinical outcome does not eliminate the need to report adverse effects and attrition.

### 4.5 Interaction, sensing, haptics, and multisensory design

Interaction evidence spans controllers, hand tracking, hands-free interfaces, eye tracking, gesture and wearable sensing, vibrotactile feedback, force and kinesthetic feedback, ultrasound-based sensing, and multimodal combinations. Current evidence does not support a universal input interface. Performance depends on task, required precision, fatigue, learnability, accessibility, sensing reliability, and the metric being optimized.

Hand tracking can remove a physical controller and increase directness, but controller-based input may remain advantageous for particular precision or feedback requirements. Hands-free interfaces broaden the design space but are evaluated with diverse tasks and metrics. Eye tracking serves both interaction and sensing roles and is increasingly coupled to foveated rendering, attention analysis, prediction, and authentication; this coupling creates dependencies between sensing quality and downstream system claims.

Haptics similarly spans distinct mechanisms rather than one intervention class. Vibrotactile, wearable, kinesthetic, passive, mid-air, and application-specific interfaces impose different trade-offs in fidelity, encumbrance, workspace, calibration, and accessibility. Evidence from surgical training, social touch, accessibility, and general interaction should therefore be synthesized by mechanism and task rather than collapsed into a generic claim that haptics improves VR.

Spatial audio and multisensory redirection provide another example of conditional evidence. Audio can support spatial orientation, immersion, communication, and perceptual redirection, but implementation details, acoustic rendering, task, and multimodal congruence determine the outcome. The current evidence lane remains less saturated than locomotion or education, so strong prevalence claims are deferred until corpus closure.

### 4.6 Avatars, virtual humans, social VR, and intelligent agents

Avatar and virtual-human research shows that realism is multidimensional. Visual human likeness, animation fidelity, behavioral responsiveness, personalization, identity representation, and social appropriateness can affect outcomes differently. Greater human resemblance alone is therefore not a reliable proxy for better user experience or social effectiveness.

Social and multi-user VR adds synchronization, proxemics, identity, privacy, communication, shared-space, and embodiment constraints. Multi-user locomotion and redirected-walking research further demonstrates that algorithms designed for a single user may require additional collision, coordination, or prediction logic when several users share physical or virtual space.

AI and embodied-agent research is expanding the system from pre-scripted behavior toward prediction, adaptation, language-mediated interaction, reinforcement learning, scene synthesis, and intelligent virtual agents. These capabilities increase flexibility but also introduce new evidence obligations: training data and model identity, inference latency, failure behavior, controllability, reproducibility, and the separation of agent intelligence from interface or content effects. The existence of AI in a VR system should therefore not be treated as an explanatory variable by itself.

### 4.7 Networking, streaming, rendering, and distributed delivery

High-quality immersive delivery couples rendering cost, visual quality, field of view, sensing, bandwidth, latency, and edge/cloud resources. Foveated rendering and foveated streaming exploit nonuniform visual sensitivity to reduce computation or transmission, often using gaze or predicted gaze as an input. Edge-assisted and cloud-assisted approaches move parts of the rendering or streaming pipeline away from the local device, creating a trade-off between device workload and communication dependency.

The current evidence supports bandwidth- and computation-saving potential, but networking and streaming remain a comparatively under-saturated workstream in this review. Results from generic edge/fog video streaming are useful infrastructure evidence but are not automatically VR evidence because immersive systems impose additional motion-to-photon, viewpoint, stereoscopic, interaction, and quality-of-experience constraints. Final synthesis in this lane will therefore distinguish direct immersive-system evidence from enabling networking literature.

### 4.8 Security, privacy, accessibility, and inclusion

VR systems collect unusually rich behavioral and biometric signals, including head and hand motion, gaze, body configuration, voice, spatial context, and interaction patterns. Security and authentication studies propose biometric and behavioral mechanisms, but the existence of many proposals should not be confused with mature validation. Threat models, sensors, participant scale, spoofing assumptions, and real-world deployment conditions differ substantially.

Privacy extends beyond account authentication. Avatars and digital bodies can expose identity, behavior, social relationships, and inferred attributes. Eye tracking and other sensors may simultaneously improve interaction while creating additional sensitive data streams. Security and privacy should therefore be evaluated as system properties rather than isolated login mechanisms.

Accessibility evidence likewise argues against designing for a nominal average user. Motor, sensory, cognitive, developmental, age-related, and ergonomic differences can alter whether an interaction method is usable at all. Haptic and multimodal interfaces may improve accessibility in some contexts while increasing device burden or excluding users in others. Inclusive VR evaluation consequently requires participant diversity, accessibility-specific outcomes, and reporting of who could not use or complete the system.

### 4.9 Healthcare, education, training, and transfer

Healthcare and education are among the stronger application lanes in the current evidence map. Reviews and meta-analyses report promising outcomes in nursing, medical education, anatomy, procedural training, mental-health training, and broader immersive learning. However, these findings are accompanied by substantial variation in instructional design, comparator equivalence, population, exposure, outcome measurement, and methodological quality.

A recurring problem is confounding between medium and content. A VR condition may differ from its comparator not only in immersion but also in instructional sequence, feedback, interaction, practice time, novelty, or facilitator involvement. Positive outcomes therefore require equivalence auditing before they are attributed specifically to immersion.

Transfer is a particularly important evidence boundary. Improved performance inside a virtual task does not automatically establish improvement in real-world clinical, educational, or operational practice. Evidence that explicitly tests transfer should be distinguished from evidence that measures only immediate in-VR performance, knowledge, presence, or satisfaction. This distinction is essential for claims about training effectiveness.

### 4.10 Industrial VR and digital twins

Industrial and digital-twin applications connect immersive interfaces with simulation, manufacturing, planning, teleoperation, monitoring, and distributed decision support. The literature demonstrates broad potential but also exposes conceptual inconsistency in what is called a digital twin, differences in synchronization and data architecture, interoperability problems, and challenges in translating simulation models into operational systems.

For review purposes, a visualization of a physical asset, a simulation model, and a continuously synchronized digital twin should not be treated as equivalent evidence. Claims should specify the direction and frequency of data exchange, model update mechanism, decision role, and degree of coupling to the physical system.

### 4.11 Evaluation as the cross-domain bottleneck

Across the workstreams, the most consistent cross-domain finding is methodological rather than technological: evaluation choices determine what can legitimately be concluded. Questionnaires for presence, embodiment, workload, usability, and cybersickness are not interchangeable; objective task metrics may capture only one aspect of experience; and positive application outcomes may be confounded by unequal treatments.

The evidence therefore supports a minimum comparison description comprising the problem, input, output, environment or dataset, constraints, metric, population where applicable, hardware/software context, and uncertainty. Without these fields, numerical results may be individually valid yet unsuitable for synthesis.

The current cross-domain synthesis should be interpreted as a structured evidence map, not as a final prevalence analysis. The final corpus size, workstream proportions, and frequency of specific gaps remain intentionally unfrozen until full-text assessment, study-family resolution, formal-source execution, and citation-chasing closure are complete.

## 7. Contradictions, Reproducibility, and Failure Regimes

### 7.1 Apparent contradiction versus valid contradiction

A central objective of the review is to avoid labeling heterogeneous results as contradictions merely because their conclusions differ. Two claims constitute a strong contradiction only when they address sufficiently compatible problems, inputs, outputs, environments, constraints, metrics, populations, and validation conditions. If one or more of these dimensions changes materially, the correct diagnosis may be incompatibility, conditionality, or a regime boundary.

The current contradiction map contains eight audited claim families. Seven primarily illustrate cross-study heterogeneity, whereas the RDW case study provides a controlled within-benchmark reversal. This distinction is important because the evidential meaning is different: cross-study disagreement often identifies missing comparability, while a reversal under paired conditions is direct evidence that performance depends on an experimental factor.

### 7.2 Interaction: task dependence rather than a universal interface

Hands-free interaction reviews and direct hand-tracking/controller comparisons can appear to disagree about which interface is preferable. The underlying tasks, interfaces, performance measures, and evaluation goals differ. The safe synthesis is therefore not that one result invalidates the other, but that interaction performance is task- and metric-dependent. A universal interface ranking is unsupported without a common benchmark that preserves task requirements and outcome definitions.

This pattern generalizes to multimodal input: directness, precision, fatigue, accessibility, feedback, and learnability can trade off. Contradiction analysis should expose the optimized dimension rather than collapse those dimensions into a single notion of performance.

### 7.3 Embodiment: measurement constructs are not interchangeable

Embodiment research combines subjective ownership and agency reports with behavioral, physiological, and neurophysiological measures. An EEG-associated marker and a self-report affordance measure can both be valid while answering different questions. Treating disagreement between them as replication failure would conflate construct validity with result direction.

The reproducibility obligation is therefore twofold: the technical protocol must be repeatable, and the construct being measured must be explicitly defined. Reusing the same hardware or avatar does not reproduce an embodiment result if the outcome construct changes.

### 7.4 Avatars: realism is a bundle of interventions

Evidence on avatar customization, identity, human likeness, animation fidelity, and social behavior can produce apparently inconsistent conclusions about realism. The inconsistency weakens when realism is decomposed. Increased human likeness is not the same intervention as personalization, expressive animation, behavioral contingency, or identity congruence.

A failure regime emerges when a study or system treats visual resemblance as a sufficient proxy for social effectiveness. Future comparisons should manipulate and report realism dimensions separately whenever the research question permits.

### 7.5 Security: proposal volume is not validation strength

VR security and biometric-authentication literature contains many mechanisms, but evidence strength varies from conceptual threat analysis to small controlled studies and practical attack evaluation. A large literature therefore does not imply that authentication effectiveness is well established under realistic adversarial conditions.

The failure regime here is evidential: mechanisms may appear mature because they are numerous, while practical validation remains sparse or heterogeneous. Reproducibility requires more than code availability; threat model, sensor configuration, enrollment protocol, attack assumptions, population, and evaluation metric must also be recoverable.

### 7.6 Education and evaluation: positive outcomes can coexist with methodological confounding

Immersive-learning studies frequently report positive outcomes, while methodological reviews identify comparator inequivalence, confounding, inconsistent quality criteria, and limited repeated validation. These findings are not inherently contradictory. A positive result can be genuine within a study while the causal attribution to immersion remains uncertain.

This produces a recurring failure regime: the VR condition and control condition differ simultaneously in medium, content, feedback, interaction, duration, or novelty. Under such designs, the study may establish effectiveness of the complete treatment package but not the isolated effect of immersion. Cross-study synthesis should therefore distinguish treatment effectiveness from medium-specific causality.

### 7.7 Tool availability versus reproducibility

Open-source toolkits, online experiment frameworks, datasets, and standardized components lower the cost of executing VR studies. However, tool availability alone does not guarantee reproducibility. Experiments may still depend on undocumented engine versions, hardware, calibration, scene assets, timing assumptions, parameter defaults, data-cleaning rules, or proprietary services.

The current A17 evidence therefore supports a layered model. **Availability** asks whether code, data, and materials can be accessed. **Executability** asks whether they can be run. **Regenerability** asks whether the published outputs can be recreated from the supplied artifacts. **Independent reproducibility** asks whether a separate team can obtain sufficiently compatible results under documented conditions. These states should not be collapsed.

The project's own RDW artifact correction illustrates this distinction. Executable workflows and stored summaries existed, yet a later raw-artifact audit found that two manuscript-facing summaries disagreed with immutable workflow outputs. Reproducibility consequently requires provenance and consistency checking in addition to source-code release.

### 7.8 Healthcare: application heterogeneity limits broad claims

Healthcare VR evidence spans education, rehabilitation, assessment, procedural practice, mental health, and professional training. Populations, interventions, outcome measures, exposure schedules, and clinical relevance differ substantially. Promising results in one application therefore do not establish a domain-wide treatment effect.

The corresponding failure regime is overgeneralization across incompatible clinical or educational contexts. Synthesis should preserve the population-intervention-comparator-outcome structure and distinguish clinical outcomes, learning outcomes, usability, presence, and feasibility.

### 7.9 RDW: a genuine controlled regime reversal

The RDW case differs from the preceding examples because controller comparisons were performed under the same benchmark infrastructure with paired seeds, common geometries, a common reset policy, and common outcome definitions. Controller ordering nevertheless changed across geometry.

In G01, S2C had lower reset burden than P2R and Vis.-Poly among complete pairs. In G03, Vis.-Poly had lower reset burden than both S2C and P2R, while completion also separated the controllers. Because the benchmark and pairing are held constant, this is not readily explained by cross-study incompatibility. It is evidence of a genuine controller-by-geometry regime effect within the declared benchmark.

The result also illustrates why failures and successful-run burden must remain separate. A controller can look favorable on conditional reset burden while completing fewer seeds. Any future selector or regime model must therefore reason jointly about failure risk, reset burden, computational cost, and uncertainty rather than optimize only the mean reset count of successful runs.

This does not itself establish a novel algorithm. Adaptive, predictive, and strategy-switching RDW methods already exist. The remaining N10 question is narrower: whether the literature lacks a method that explicitly models the joint failure-reset-cost regime with uncertainty and demonstrates held-out generalization under compatible evaluation.

### 7.10 Reproducibility failure taxonomy

Across domains, reproducibility problems can be organized into at least six failure classes:

1. **Specification failure:** essential parameters, hardware, software versions, calibration, preprocessing, or procedural details are absent.
2. **Artifact failure:** code, data, scenes, models, or study materials are unavailable or incomplete.
3. **Execution failure:** artifacts exist but cannot be executed under the documented environment.
4. **Regeneration failure:** execution succeeds but the reported tables, figures, or statistics cannot be regenerated.
5. **Semantic failure:** regenerated outputs use a different task, metric, construct, or comparator than the claimed result.
6. **Independent-result failure:** a sufficiently faithful independent reproduction produces materially different findings.

These classes should not be assigned when evidence is merely unavailable. For example, lack of public code is an availability limitation, not proof that the original result is irreproducible. Conversely, public code is not proof that the paper's numerical claims regenerate.

### 7.11 Failure regimes as research objects

The contradiction analysis suggests that many important VR research questions concern boundaries rather than average effects. Examples include the geometry at which an RDW controller changes rank, the latency or bandwidth at which distributed rendering becomes unacceptable, the exposure regime at which cybersickness offsets task benefit, the fidelity at which avatar realism ceases to improve experience, or the user characteristics under which an interaction technique becomes inaccessible.

A failure regime is therefore defined here as a region of the input, environment, population, or resource space in which a method ceases to satisfy its intended performance, safety, usability, fidelity, or reproducibility obligations. This definition turns limitations into testable objects. Instead of asking only whether method A outperforms method B on average, a stronger experiment asks where their ordering changes and whether that boundary generalizes.

### 7.12 Evidence-backed gap progression

The C0-C5 ladder is used to prevent speculative gaps from becoming manuscript claims. A C0 observation is only a suspected absence. C1 requires explicit support in the literature; C2 requires independent corroboration; C3 requires a testable formulation with identifiable comparators and metrics; C4 requires a benchmark-ready gap after prior-art checking; and C5 requires an executed method and evaluation.

The current RDW candidate is deliberately held below C4 completion because adaptive selection and predictive control already have prior art. Likewise, under-saturated review lanes such as networking/streaming, spatial audio, and reproducibility should not generate strong prevalence or absence claims until their evidence base is closed.

### 7.13 Synthesis

The current contradiction map supports three broad conclusions. First, many apparent contradictions in VR are produced by incompatible tasks, constructs, populations, interventions, or metrics rather than by direct replication failure. Second, reproducibility is multidimensional: availability, executability, regeneration, semantic fidelity, and independent reproduction are distinct states. Third, genuine regime effects can be scientifically valuable because they reveal where universal rankings fail.

These conclusions motivate the review's final synthesis strategy. Evidence should be compared only after semantic compatibility is established; negative and failed outcomes should remain visible; reproducibility claims should identify the level actually demonstrated; and open problems should be formulated as testable regime, mechanism, or evidence obligations rather than as unsupported statements that no prior work exists.

This Section 7 remains extensible. The eight audited contradiction families are sufficient to establish the framework and the controlled RDW regime example, but the final count and distribution of contradiction and reproducibility patterns will be frozen only after N14 expands across the closed systematic corpus.
