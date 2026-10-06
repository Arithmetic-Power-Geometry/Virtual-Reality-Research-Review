# Virtual Reality Research: A Systematic Review of Methods, Algorithms, Evaluation, and Open Research Problems

> Draft 01 — Sections 1–3 only. Final corpus counts, PRISMA values, contribution bullets, and novelty claims are intentionally unfrozen.

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

Searches cover scholarly indexes and publisher libraries appropriate to VR, including IEEE Xplore, the ACM Digital Library, Scopus and/or Web of Science where accessible, ScienceDirect, SpringerLink, PubMed for health-related evidence, and backward/forward citation chasing. Search strings are versioned and are intended to retain database, query, execution date, result count, export identity, deduplication outcome, and inclusion stage.

Bibliographic records are verified before manuscript use. DOI, title, year, venue, and author metadata are checked against authoritative publisher or bibliographic records, and each retained reference is assigned a manuscript evidence role. The master bibliography, verification ledger, citation-use ledger, screening tables, analysis outputs, and provenance notes are maintained as machine-readable repository artifacts. The working bibliography is still expanding toward evidence saturation; therefore, counts in this draft are deliberately not presented as final PRISMA values.

### 2.3 Screening and study-family resolution

Screening proceeds through deduplication, title/abstract screening, full-text eligibility assessment, study-family classification, domain classification, and evidence extraction. Full-text exclusion reasons are recorded. Related publications are grouped into study families to avoid treating reviews, follow-up analyses, toolkits, and closely related reports as independent empirical replications when they are not.

Evidence is classified into foundational/theoretical studies, algorithms and systems, empirical human-subject studies, datasets and benchmarks, measurement/instrument studies, reproducibility/toolkit/software studies, systematic or scoping reviews and meta-analyses, and application-domain studies. Secondary reviews provide landscape structure and snowballing support; primary studies remain the principal basis for claims about algorithmic or intervention performance.

### 2.4 Evidence extraction

For eligible primary studies, extraction records bibliographic identity, VR modality, research problem, task and environment, algorithm or intervention, comparator, hardware, software or engine, sensing and input modalities, datasets, participant population and sample size, exposure duration, dependent variables, objective metrics, subjective instruments, statistical procedures, effect estimates where available, limitations, code/data/material availability, replication information, funding or conflicts when relevant, contradiction links, and candidate gaps.

Quality is represented dimensionally rather than collapsed into a single opaque score. Audited dimensions include research-question clarity, comparator adequacy, protocol clarity, sample justification, participant relevance, metric validity, statistical adequacy, uncertainty reporting, hardware/software specification, parameter disclosure, code and data availability, study-material availability, deterministic execution information, and independent replication.

### 2.5 Citation chasing and corpus freeze

Backward and forward citation chasing is performed from high-value family hubs and from records that expose unresolved comparisons or methodological gaps. Citation-chased records are tracked separately from the formal source-query stream so that the final flow can distinguish how each record entered the corpus. The corpus will be frozen only after formal source execution, deduplication, all canonical full-text decisions, study-family resolution, and citation-chasing closure. Final PRISMA counts and final included-study totals are therefore intentionally withheld from this draft.

### 2.6 Reproducibility assessment

Reproducibility is evaluated independently of whether a reported result is positive, negative, or null. The audit records code, data, configuration, environment, study-material, seed, statistical-procedure, and execution information when applicable. Code unavailability is not labeled reproduction failure. A reproduction failure requires an attempted reproduction or sufficiently specific evidence that the reported experiment cannot be reconstructed.

For computational artifacts generated in this project, derived results are frozen in machine-readable form with workflow and provenance records. Tables and statistics are generated from these frozen outputs rather than manually retyped. This policy is particularly important for the RDW case study, where a pre-inference forensic audit identified and corrected earlier summary inconsistencies before confirmatory analysis.

## 3. Evidence and Comparability Framework

### 3.1 Semantic comparability

Numerical comparison is admitted only when studies are sufficiently compatible along six dimensions: **Problem**, **Input**, **Output**, **Dataset/Environment**, **Constraints**, and **Metric**. Compatibility does not require identical implementations, but the compared systems must answer materially comparable questions under assumptions that do not invalidate the interpretation of their numerical difference.

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