# Virtual Reality Research: A Systematic Review of Methods, Algorithms, Evaluation, and Open Research Problems

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

## 1. Introduction

Virtual reality (VR) research is often described through its component technologies—displays, rendering, tracking, interaction, locomotion, haptics, audio, avatars, networking, and intelligent agents—or through application domains such as health, education, training, and industry. This decomposition is useful for engineering, but it can obscure a central methodological problem: a VR result is produced by a coupled technical and human experimental system. Hardware, software, sensing, control algorithms, virtual environments, participant populations, exposure duration, tasks, outcome measures, and statistical procedures can all alter the observed result. Consequently, two studies that appear to evaluate the same broad idea may not support a valid numerical comparison, while apparently conflicting findings may instead reflect different experimental regimes.

The literature also spans markedly different forms of evidence. Algorithm papers may emphasize objective performance under simulated or controlled environments; human-subject studies may prioritize presence, embodiment, workload, usability, or cybersickness; application studies may measure learning, clinical, behavioral, or industrial outcomes; and toolkit or reproducibility papers may focus on whether an experiment can be implemented, shared, and repeated. Reviews across several VR subdomains already report heterogeneous protocols, instruments, interventions, and evaluation practices. These differences make a simple catalogue of methods insufficient for establishing which conclusions generalize, which comparisons are fair, and which research gaps are genuinely unresolved.

This review therefore treats comparability and reproducibility as first-class properties of the evidence. Its organizing question is not merely which methods exist, but under what problem definitions, inputs, outputs, environments, constraints, metrics, and validation conditions their results can be compared. We distinguish a genuine contradiction—different outcomes for sufficiently comparable questions—from incompatibility caused by different populations, hardware, tasks, interventions, measurement instruments, or validation levels. We likewise distinguish unavailable code from demonstrated reproduction failure. These distinctions are necessary to avoid converting heterogeneous evidence into unsupported universal rankings or research-gap claims.

The review covers 21 coordinated workstreams spanning foundations; displays and rendering; tracking and sensing; interaction; locomotion and redirected walking; haptics; spatial audio and multisensory systems; presence and embodiment; cybersickness; avatars and virtual humans; AI and embodied agents; social and multiuser VR; networking and streaming; security and authentication; accessibility; evaluation and statistics; software, toolkits, and reproducibility; healthcare; education and training; industrial applications; and cross-cutting contradiction, comparison, and reproducibility auditing. Secondary reviews are used to map landscapes and support citation chasing, whereas claims about method performance are anchored preferentially in primary studies.

A controlled redirected-walking (RDW) case study complements the broad evidence synthesis. RDW is a useful methodological test because controller performance depends on physical geometry, virtual motion, gain limits, reset behavior, and evaluation protocol. Rather than assuming that a controller ranking obtained in one condition is globally valid, the case study evaluates multiple executable controllers with paired seeds across common benchmark geometries, separates completion from reset burden, and retains failures rather than replacing them with synthetic scores. The resulting analysis demonstrates why context-aware comparison matters: controller ordering changes across geometries, and the difficult geometry changes both completion behavior and reset-burden contrasts. This observation is treated as evidence for a controller-by-geometry regime hypothesis, not as automatic proof of a novel adaptive controller.

The intended contribution is consequently methodological as well as substantive. The review links literature mining to explicit evidence obligations, semantic comparability, reproducibility auditing, contradiction analysis, and benchmark-oriented gap validation. Candidate gaps advance through a staged evidence ladder from mention to corroboration, testability, benchmark readiness, and experimental evaluation. A novel algorithm is considered only if the evidence establishes a missing mechanism or unresolved trade-off with compatible baselines and a reproducible evaluation protocol. This structure is designed to prevent two common errors in broad reviews: treating absence from a limited search as novelty, and treating incomparable numerical results as a ranking.

## 2. Review Methodology

### 2.1 Review design and research questions

The study combines systematic-review reporting with scoping synthesis where breadth is necessary, structured evidence mapping, reproducibility auditing, contradiction analysis, and benchmark-oriented gap validation. Ten research questions organize the analysis: evolution of VR research; major method and algorithm families; evaluation practices; direct comparative evidence; robustness and generalization; contradictory findings; reproducibility; evidence-backed open problems; benchmarkability; and algorithmic opportunity.

The review is partitioned into 21 workstreams (A01–A21) to reduce the risk that a mature subfield, particularly locomotion, dominates the evidence base. Workstream assignment is not mutually exclusive. A study may contribute to several workstreams when, for example, an avatar study also evaluates embodiment, social interaction, or privacy. Cross-workstream evidence is retained rather than forced into a single taxonomy node.

### 2.2 Search, verification, and provenance

Evidence discovery drew on scholarly indexes and publisher libraries appropriate to VR, including IEEE Xplore, the ACM Digital Library, Scopus and/or Web of Science where accessible, ScienceDirect, SpringerLink, PubMed for health-related evidence, and backward/forward citation chasing. The registered review ledger preserves the verified evidence library and downstream screening and provenance decisions. Raw yield counts from every earliest exploratory database query were not preserved, and those historical identification counts are not reconstructed retrospectively.

Bibliographic records are verified before manuscript use. DOI, title, year, venue, and author metadata are checked against authoritative publisher or bibliographic records, and each retained reference is assigned a manuscript evidence role. The master bibliography, verification ledger, citation-use ledger, screening tables, analysis outputs, and provenance notes are maintained as machine-readable repository artifacts. The final registered evidence library contains 174 verified records. After one exact DOI duplicate, 173 canonical reports were sought; 171 were retrieved and assessed, yielding 165 direct eligible VR/XR reports and six supporting/context reports, while two reports were not retrieved.

### 2.3 Screening and study-family resolution

Screening proceeds through deduplication, title/abstract screening, full-text eligibility assessment, study-family classification, domain classification, and evidence extraction. Full-text exclusion reasons are recorded. Related publications are grouped into study families to avoid treating reviews, follow-up analyses, toolkits, and closely related reports as independent empirical replications when they are not.

Evidence is classified into foundational/theoretical studies, algorithms and systems, empirical human-subject studies, datasets and benchmarks, measurement/instrument studies, reproducibility/toolkit/software studies, systematic or scoping reviews and meta-analyses, and application-domain studies. Secondary reviews provide landscape structure and snowballing support; primary studies remain the principal basis for claims about algorithmic or intervention performance.

### 2.4 Evidence extraction

For eligible primary studies, extraction records bibliographic identity, VR modality, research problem, task and environment, algorithm or intervention, comparator, hardware, software or engine, sensing and input modalities, datasets, participant population and sample size, exposure duration, dependent variables, objective metrics, subjective instruments, statistical procedures, effect estimates where available, limitations, code/data/material availability, replication information, funding or conflicts when relevant, contradiction links, and candidate gaps.

Quality is represented dimensionally rather than collapsed into a single opaque score. Audited dimensions include research-question clarity, comparator adequacy, protocol clarity, sample justification, participant relevance, metric validity, statistical adequacy, uncertainty reporting, hardware/software specification, parameter disclosure, code and data availability, study-material availability, deterministic execution information, and independent replication.

### 2.5 Citation chasing and corpus freeze

Backward and forward citation chasing is performed from high-value family hubs and from records that expose unresolved comparisons or methodological gaps. Citation-chased records are tracked separately from the formal source-query stream so that the final flow can distinguish how each record entered the corpus. The registered evidence-library corpus was frozen after deduplication, canonical full-text decisions, study-family resolution, and citation-chasing closure. The final flow contains 174 verified records, one duplicate, 173 canonical reports, 171 assessed reports, 165 direct eligible reports, six supporting/context reports, and two reports not retrieved. Raw per-database yields from the earliest exploratory discovery stage were not preserved and are not reconstructed retrospectively.

### 2.6 Reproducibility assessment

Reproducibility is evaluated independently of whether a reported result is positive, negative, or null. The audit records code, data, configuration, environment, study-material, seed, statistical-procedure, and execution information when applicable. Code unavailability is not labeled reproduction failure. A reproduction failure requires an attempted reproduction or sufficiently specific evidence that the reported experiment cannot be reconstructed.

For computational artifacts generated in this project, derived results are frozen in machine-readable form with workflow and provenance records. Tables and statistics are generated from these frozen outputs rather than manually retyped. This policy is particularly important for the RDW case study, where a pre-inference forensic audit identified and corrected earlier summary inconsistencies before confirmatory analysis.

## 3. Evidence and Comparability Framework

### 3.1 Semantic comparability

Numerical comparison is admitted only when studies are sufficiently compatible along seven dimensions, represented as E=(P,I,O,D,C,M,V): **Problem/population**, **Intervention/input**, **Outcome**, **Data/environment**, **Constraints**, **Metric/measurement**, and **Validation design**. Each dimension is coded compatible (1), incompatible (0), or uncertain (U). Pair-level Gamma is 1 only when all seven dimensions are compatible, 0 when any dimension is incompatible, and U when no dimension is incompatible but at least one remains uncertain. Compatibility does not require identical implementations, but the compared systems must answer materially comparable questions under assumptions that preserve the intended comparison.

When compatibility is insufficient, methods remain in the taxonomy and qualitative synthesis but are not placed in a common numerical ranking. This rule is especially important across VR studies because differences in hardware, tracking volume, field of view, interaction technique, virtual scene, exposure duration, population, locomotion constraints, questionnaires, and application content can alter outcomes independently of the method nominally being compared.

### 3.2 Contradiction versus incompatibility

A contradiction is recorded only when studies address sufficiently comparable constructs or problems. Otherwise, differences are first treated as candidate moderators. For example, evidence concerning avatar customization, animation fidelity, human likeness, and identity expression should not be reduced to a single axis of “avatar realism.” Likewise, objective physiological markers of embodiment and subjective embodiment questionnaires measure related but non-interchangeable constructs.

The same principle applies to application evidence. A positive learning or health outcome under one VR intervention does not establish a generic media effect when instructional content, exposure, comparator equivalence, participant population, or outcome measures differ. Apparent disagreement is therefore decomposed into genuine result tension, methodological incompatibility, or a plausible regime/moderator effect.

### 3.3 Gap-evidence ladder

Candidate research gaps progress through six evidence states. **C0 (Mentioned)** denotes future work stated by one or more sources. **C1 (Candidate)** indicates an apparent unresolved issue in verified secondary evidence. **C2 (Corroborated)** requires multiple independent sources and/or an updated primary-study search. **C3 (Testable)** requires an explicit problem formulation, observable outcome, and feasible comparison. **C4 (Benchmark-ready)** additionally requires compatible baselines, data or environment, metrics, and evaluation protocol. **C5 (Experimentally evaluated)** requires reproducible results that directly address the gap.

Only C2 or stronger gaps enter the principal research-gap synthesis. Only C4 gaps can motivate a new benchmark or algorithm. Novelty is never inferred from keyword absence; exact terminology, synonyms, historical terminology, closest algorithm families, backward and forward citations, and current literature must be checked first.

### 3.4 Negative evidence and failure regimes

Null and negative findings are retained. In computational comparisons, failed runs are not assigned artificial performance values merely to preserve a ranking. Completion or failure is analyzed separately from conditional performance among completed runs. This distinction prevents a method with selective failures from appearing artificially strong or weak because its unsuccessful runs were numerically imputed.

The RDW case study illustrates the distinction. Complete-pair reset burden favors different controllers in different geometries, while completion ordering also changes in the difficult geometry. Because the controllers are evaluated with common geometries and paired seeds, this pattern is interpretable as a controlled regime effect rather than a cross-study incompatibility. It supports the hypothesis that geometry modifies controller performance and robustness, but does not by itself establish that a new adaptive controller is novel or superior.

### 3.5 From evidence synthesis to algorithmic opportunity

The final algorithmic-opportunity decision is downstream of the review, not an assumption built into it. A proposed mechanism must survive comparison with the closest adaptive, predictive, learned, geometry-aware, and switching approaches; have an explicit problem formulation; identify compatible baselines; specify primary metrics; include ablation and robustness checks; quantify computational cost; and provide a reproducible implementation. If those obligations cannot be met, the review retains the empirical separation or gap result without forcing an algorithmic contribution.

This separation between evidence synthesis and algorithm invention is central to the study design. It permits a publishable outcome even when the strongest conclusion is that performance is conditional, existing evidence is incomparable, or a purported gap has already been partially addressed.

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

The cross-domain synthesis is interpreted as a structured evidence map rather than a prevalence analysis. The registered evidence library is frozen at 174 verified records, 173 canonical reports, 171 retrieved and assessed reports, 165 direct eligible reports, six supporting/context reports, and two reports not retrieved. Workstream overlap and the deliberately selected contradiction families prevent simple frequency counts from being interpreted as population prevalence.

## 5. Redirected-Walking Case-Study Methods

### 5.1 Purpose and benchmark design

The redirected-walking (RDW) case study was designed as a controlled demonstration of context-sensitive algorithm comparison rather than as a claim of universal controller superiority. Three executable controllers—Visibility-Polygon redirection (Vis.-Poly), Steer-to-Center (S2C), and Potential-to-Redirect (P2R)—were evaluated under the same benchmark runner, path-generation process, safety checks, reset policy, geometry set, and seed schedule. Four physical-environment geometries (R1-G01 to R1-G04) were used, with 100 paired seeds per geometry and a target virtual travel distance of approximately 350 m per run, yielding 1,200 planned controller-condition cells.

The authoritative completion totals after the pre-inference raw-artifact audit are 384/400 for Vis.-Poly, 378/400 for S2C, and 381/400 for P2R. These values supersede earlier manuscript-facing summaries that had incorrectly reported complete execution for Vis.-Poly and P2R. The correction was made before inferential analysis by re-downloading the immutable GitHub Actions artifacts and job logs and was retained in the provenance record rather than silently overwritten.

### 5.2 Controller set and implementation boundaries

Vis.-Poly uses physical and virtual visibility polygons together with slice construction and matching to select redirection behavior. S2C recomputes a steering direction toward the tracking-space center from the current physical geometry. P2R uses repulsive artificial-potential contributions from nearby physical boundaries to derive a steering direction. All three implementations are clean-room executable comparators under the common R1 benchmark.

A fourth contemporary method, APF-S2T, was reviewed as a literature comparator but was not numerically admitted because the recoverable primary-method description did not fully determine the discretization choices required for a faithful implementation. The case study therefore treats APF-S2T as prior methodological context, not as an executable benchmark row. This distinction avoids presenting an implementation guess as a replication.

### 5.3 Common reset and failure handling

The controller comparison uses a common reset policy so that differences in steering behavior are not confounded by different reset mechanisms. Completion and reset burden are treated as separate outcomes. Failed or incomplete runs are retained as outcomes and are never assigned synthetic reset scores. Reset-burden comparisons are consequently conditional on both members of a controller pair completing the same seed in the same geometry.

This failure-aware design is important because a controller can exhibit low reset burden on its successful runs while failing more often in a difficult geometry. Collapsing these outcomes into a single imputed score would obscure the robustness-performance trade-off.

### 5.4 Paired statistical analysis

Within each geometry, controller pairs were joined by exact seed. For reset burden, the primary effect was the paired difference in resets per 100 m among complete pairs. Deterministic percentile bootstrap confidence intervals used 10,000 resamples with seed 2601. Sign counts were retained to show how often each controller had lower burden.

Confirmatory analysis used paired Wilcoxon signed-rank tests for reset burden, Benjamini-Hochberg false-discovery-rate and Holm family-wise multiplicity corrections across the 12 planned controller-by-geometry contrasts, exact paired completion-discordance tests, and geometry-wise Friedman omnibus tests among triple-complete seeds. P-values were interpreted alongside effect magnitudes and completion outcomes rather than as standalone evidence.

### 5.5 Computational-cost benchmark

Controller decision cost was measured separately from task performance. The actual controller decision functions were benchmarked on 12 deterministic state/geometry combinations. The full test suite was executed before timing; each state used 500 warm-up calls, nine timing samples, and 5,000 calls per timing sample with `perf_counter_ns`.

These timings measure controller-decision overhead only. They exclude rendering, path planning, reset execution, file I/O, HMD latency, and network latency. Structural complexity is therefore reported with the measured wall-clock results, and the timing values are interpreted only as relative costs under the common runner.

## 6. RDW Results

### 6.1 Completion behavior

Completion varied by both controller and geometry. Across the four geometries, Vis.-Poly completed 384/400 runs, S2C 378/400, and P2R 381/400. The difficult R1-G03 geometry produced the clearest robustness separation: Vis.-Poly completed 94/100 runs, S2C 86/100, and P2R 81/100. In contrast, G01 produced 92/100 completion for Vis.-Poly and 100/100 for both S2C and P2R; G02 produced 99/100, 97/100, and 100/100, respectively; and G04 produced 99/100, 95/100, and 100/100.

Paired completion tests show that the same controller is not uniformly most robust. In G01, Vis.-Poly had significantly worse completion than both S2C and P2R (exact paired p=0.007812 for each comparison). In G03, Vis.-Poly had significantly better completion than P2R (p=0.010622), whereas its completion difference from S2C was not significant at conventional levels (p=0.115318). Other pairwise completion differences were not statistically compelling after exact paired testing.

### 6.2 Reset burden among completed pairs

Reset burden also changed with geometry. In G01, S2C had the lowest complete-pair burden, followed by P2R and then Vis.-Poly. The mean paired Vis.-Poly minus S2C difference was 2.643 resets/100 m (95% bootstrap CI 2.258 to 3.025), and Vis.-Poly minus P2R was 1.395 (1.033 to 1.760). S2C minus P2R was -1.272 (-1.532 to -1.021), confirming the same ordering.

G02 showed a different pattern. S2C was lower than both comparators: Vis.-Poly minus S2C was 0.680 (0.334 to 1.011), while S2C minus P2R was -0.834 (-1.230 to -0.434). Vis.-Poly and P2R were not distinguishable on complete-pair burden, with a mean difference of -0.180 and a confidence interval spanning zero (-0.575 to 0.204).

G03 reversed the G01 ordering. Vis.-Poly had lower reset burden than both S2C and P2R on complete pairs: Vis.-Poly minus S2C was -1.004 (-1.588 to -0.417), and Vis.-Poly minus P2R was -0.742 (-1.345 to -0.136). S2C and P2R were not distinguishable, with a mean difference of 0.162 (-0.452 to 0.788). Thus the geometry that most reduced completion also changed the burden ranking.

In G04, S2C again had the lowest reset burden. S2C minus P2R was -0.726 (-1.134 to -0.324), while Vis.-Poly minus S2C was 0.572 (0.190 to 0.963). Vis.-Poly and P2R were again not clearly separated, with a mean difference of -0.210 (-0.591 to 0.168).

### 6.3 Confirmatory inference

The multiplicity-adjusted Wilcoxon analysis supports the descriptive regime pattern. All three G01 pairwise burden differences remained significant after Holm correction. In G02, S2C differed from both Vis.-Poly and P2R after Holm correction, whereas Vis.-Poly versus P2R did not. In G03, Vis.-Poly versus S2C remained significant after Holm correction (Holm-adjusted p=0.00945); Vis.-Poly versus P2R was significant under Benjamini-Hochberg control but not Holm family-wise correction (BH p=0.02772; Holm p=0.09795); and S2C versus P2R was not significant. In G04, S2C versus P2R remained significant after Holm correction, while the two Vis.-Poly contrasts did not.

Friedman omnibus tests among triple-complete seeds detected controller differences in every geometry: G01 χ²=100.78, p=1.31×10^-22; G02 χ²=14.68, p=0.000648; G03 χ²=6.06, p=0.0483; and G04 χ²=9.53, p=0.00852. G03 was therefore the weakest omnibus separation but still crossed the nominal 0.05 threshold.

Taken together, the completion and reset analyses do not support a universal controller ranking. Geometry changes both the performance ordering and the robustness profile. The strongest controlled evidence is therefore a controller-by-geometry regime effect, not a claim that one controller is globally best.

### 6.4 Computational cost

The common-runner microbenchmark showed substantial differences in controller-decision overhead. The median of the 12 per-state medians was 251.448 microseconds for Vis.-Poly, 2.022 microseconds for S2C, and 3.938 microseconds for P2R. On this runner, Vis.-Poly was approximately 124.4× slower than S2C and 63.9× slower than P2R, while P2R was approximately 1.95× slower than S2C.

The structural analysis explains the broad direction of this difference. S2C is O(P) in the current implementation because the tracking center is recomputed from P physical segments at each decision, although this could become O(1) for static geometry if cached. P2R is O(P) because repulsive contributions are accumulated across physical segments. Vis.-Poly is dominated by physical and virtual visibility-polygon construction plus slice construction and matching, so its exact asymptotic cost depends on polygon complexity and the visibility implementation.

These measurements are not end-to-end frame times and do not establish device-independent real-time guarantees. They show that the controller choice can introduce a nontrivial computational-overhead dimension that should be considered together with completion and reset burden.

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

The RDW novelty gate is closed for this paper: adaptive selection and predictive control already have prior art, so no new controller or selector is claimed. Cross-domain prevalence claims remain bounded by the frozen registered evidence library and by semantic comparability rather than inferred from raw citation counts.

### 7.13 Synthesis

The current contradiction map supports three broad conclusions. First, many apparent contradictions in VR are produced by incompatible tasks, constructs, populations, interventions, or metrics rather than by direct replication failure. Second, reproducibility is multidimensional: availability, executability, regeneration, semantic fidelity, and independent reproduction are distinct states. Third, genuine regime effects can be scientifically valuable because they reveal where universal rankings fail.

These conclusions motivate the review's final synthesis strategy. Evidence should be compared only after semantic compatibility is established; negative and failed outcomes should remain visible; reproducibility claims should identify the level actually demonstrated; and open problems should be formulated as testable regime, mechanism, or evidence obligations rather than as unsupported statements that no prior work exists.

The final N14 audit contains eight pre-specified contradiction families: seven are comparability-limited and one is a genuine controlled regime effect. These proportions characterize the audited families and are not presented as corpus-wide prevalence.

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

Finally, the RDW benchmark is simulation-based, uses four geometries, and evaluates three executable controllers under one common implementation environment. The observed regime effect is internally controlled but is not generalized to deployed VR systems. Live-user validation is outside the design of this paper, and broader-geometry generalization is not claimed.

## 9. Threats to Validity

The review and case study have several distinct validity boundaries. First, the frozen registered evidence-library flow is curated rather than reconstructible from raw per-database discovery exports. It contains 174 verified records, one exact duplicate, 173 canonical reports, 171 retrieved and assessed reports, 165 direct eligible reports, six supporting/context reports, and two reports not retrieved. Because raw per-database discovery yields from the earliest exploratory stage were not preserved, database-specific identification counts are not reconstructed retrospectively.

Second, broad VR evidence is heterogeneous. Hardware, tracking volume, interaction method, task, virtual environment, population, exposure duration, questionnaires, objective measures, and statistical procedures vary across studies. The comparability framework reduces the risk of invalid numerical synthesis, but it cannot eliminate publication bias or missing methodological detail in the primary literature.

Third, study-family dependence can inflate apparent evidence volume when reviews, toolkits, follow-up analyses, and empirical studies stem from closely related projects. Family resolution is therefore part of the corpus freeze, but residual dependence may remain when publications do not clearly disclose lineage.

Fourth, the RDW benchmark is simulation-based and uses four selected physical geometries under a common runner. The observed controller-by-geometry regime dependence is internally interpretable because seeds, paths, reset policy, and evaluation rules are paired, but it does not imply the same ordering for all room layouts, path distributions, walking behavior, HMDs, or live-user conditions. Simulator-to-user transfer is outside the evidential scope of this paper even where prior work supports simulation as a useful evaluation tool.

Fifth, controller fidelity is asymmetric. Vis.-Poly, S2C, and P2R are executable under the common benchmark, whereas APF-S2T was withheld from numerical comparison because the exact discretization needed for a faithful reconstruction was unresolved. This conservative admission rule reduces implementation-speculation risk but narrows the executable comparator set.

Sixth, wall-clock microbenchmarks depend on software and hardware. The N09 timings quantify relative decision overhead under one common runner and are accompanied by structural-complexity analysis; they should not be interpreted as universal latency values.

Finally, the pre-inference artifact audit revealed that earlier manuscript-facing N02 and N05 summaries disagreed with the immutable workflow artifacts. The analysis was corrected before confirmatory inference and the discrepancy was preserved in provenance. This episode strengthens the case for raw-artifact checking, but it also demonstrates that reproducibility pipelines require continuous internal consistency audits rather than assuming that a generated summary is automatically authoritative.

## 10. Reproducibility and Data/Code Availability

The project repository is organized so that manuscript claims can be traced to machine-readable evidence, analysis outputs, and provenance records. The review pipeline retains the master bibliography, citation-use ledger, screening and full-text tables, study-family mappings, citation-chasing register, workstream coverage audits, contradiction/comparability maps, and dated pipeline snapshots.

The RDW case study retains executable controller code, benchmark logic, algorithm specifications, workflow provenance, raw-artifact audit records, corrected descriptive tables, paired-effect files, completion-discordance files, confirmatory statistical outputs, and computational-cost results. The principal N07 paired bootstrap used 10,000 deterministic resamples with seed 2601, while controller timing used deterministic state/geometry combinations and a fixed measurement protocol.

For the three controller families, the authoritative post-forensic completion data are derived from original GitHub Actions artifacts and job logs rather than from superseded manuscript summaries. The correction record identifies the relevant workflow and artifact identifiers and preserves the historical inconsistency. This provenance rule is deliberate: a reproducibility record should show how a correction was obtained, not merely replace the earlier result.

Machine-readable tables and figure-source files are kept separate from prose so that manuscript values can be regenerated rather than manually re-entered. Likewise, failed RDW runs remain explicit outcomes, and no synthetic reset value is inserted to force complete numerical matrices.

Open code and stored artifacts improve executability, but they are not treated as proof of independent reproducibility. Independent reproduction would require a separate execution or validation under sufficiently documented conditions. The repository therefore distinguishes code availability, protocol completeness, deterministic regeneration, and independent reproduction as separate evidence states.

All manuscript sections, the numerical Abstract, final contribution statements, evidence-library flow, N14 synthesis, reference freeze, and N10 novelty boundary are now frozen. The paper makes no C4/C5 algorithmic novelty claim.

## 11. Conclusion

VR evidence is most informative when the conditions under which a result holds are treated as part of the result itself. Across the reviewed domains, many apparent contradictions arise because studies use different tasks, constructs, populations, interventions, hardware, metrics, or validation levels. The eight-family contradiction audit demonstrates this directly: seven families were comparability-limited, while the controlled RDW family exposed a genuine regime effect.

The redirected-walking benchmark reinforces the same conclusion experimentally. Visibility-Polygon, S2C, and P2R controllers showed different completion, reset-burden, and computational-cost profiles, and their ordering changed with geometry. No controller was universally best. The paper therefore rejects a new-controller novelty claim and instead contributes a failure-aware, provenance-backed way to reason about conditional performance.

The broader methodological implication is that VR reviews should move beyond inventories of techniques toward explicit evidence obligations. Comparability should precede ranking; failure should remain distinct from conditional performance; reproducibility should identify the level actually demonstrated; and research gaps should progress from observation to corroboration, testability, benchmark readiness, and experimental evaluation. Under this view, the most useful open problems are not unsupported absences in the literature but reproducible boundaries where existing methods change behavior, fail, or cease to generalize.

## Final Corpus Statement

The frozen registered evidence-library flow contains 174 verified records, one exact duplicate, 173 canonical reports, 171 retrieved and assessed reports, 165 direct eligible VR/XR reports, six supporting/context reports, and two reports not retrieved. No canonical record remains unassessed. Raw per-database discovery yields from the earliest exploratory stage were not preserved and are not reconstructed retrospectively.
