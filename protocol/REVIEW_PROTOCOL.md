# Review Protocol

## Objective

To produce a systematic, reproducible, comparative synthesis of virtual reality research that establishes what has been studied, how it has been evaluated, which findings agree or conflict, how reproducible the evidence is, and which unresolved problems are genuinely testable.

## Review design

The project combines systematic-review reporting, scoping where breadth is required, quantitative descriptive synthesis, structured evidence mapping, contradiction analysis, reproducibility auditing, and benchmark-oriented gap validation.

## Core research questions

**RQ1 — Evolution.** How has VR research evolved across technologies, methods, research problems, application domains, and evaluation practices?

**RQ2 — Methods and algorithms.** Which major method and algorithm families are used for rendering, tracking, interaction, locomotion, sensing, prediction, adaptation, networking, security, accessibility, and related VR problems?

**RQ3 — Evaluation.** Which objective and subjective metrics, questionnaires, datasets, tasks, hardware platforms, and experimental protocols are used, and where are they incompatible or weakly validated?

**RQ4 — Comparative evidence.** Which methods have been directly compared under equivalent conditions, and which important pairwise or multi-method comparisons are missing?

**RQ5 — Robustness and generalisation.** How stable are findings across hardware, environments, exposure duration, populations, tasks, and application domains?

**RQ6 — Contradictions.** Where do studies report conflicting findings, and which methodological or contextual variables plausibly explain the disagreement?

**RQ7 — Reproducibility.** To what extent are code, data, configurations, environments, study materials, seeds, statistical procedures, and artifacts available and sufficient for replication?

**RQ8 — Open problems.** Which gaps remain after separating unsupported future-work statements from evidence-backed, testable research deficiencies?

**RQ9 — Benchmarkability.** Which gaps can be converted into reproducible computational or experimental benchmarks using public data, simulators, open-source implementations, or controlled synthetic data?

**RQ10 — Algorithmic opportunity.** Does any validated gap represent a missing computational mechanism for which a novel algorithm can be proposed and compared fairly with the closest baselines?

## Study families

Evidence is grouped into:
- foundational/theoretical work
- algorithms and systems
- empirical human-subject studies
- datasets and benchmarks
- measurement/instrument studies
- reproducibility/toolkit/software studies
- systematic/scoping reviews and meta-analyses
- application-domain studies

Secondary reviews are used for landscape and snowballing, but primary studies remain the principal source for claims about method performance.

## Search strategy

Searches should cover major scholarly indexes and publisher libraries appropriate to VR, including IEEE Xplore, ACM Digital Library, Scopus and/or Web of Science where accessible, ScienceDirect, SpringerLink, PubMed for health-related subdomains, and backward/forward snowballing.

Search strings are versioned. Each search records database, query, execution date, result count, export identifier, deduplication outcome, and inclusion stage.

## Screening

Screening proceeds through:
1. deduplication;
2. title/abstract screening;
3. full-text eligibility;
4. study-family classification;
5. domain classification;
6. evidence extraction.

Exclusion reasons are recorded at full-text stage.

## Extraction schema

Each eligible primary study should capture, when applicable:
- bibliographic identity
- year and venue
- VR definition/modality
- research problem
- task/environment
- algorithm/method
- comparator
- hardware
- software/engine
- sensing/input modalities
- dataset
- population and sample size
- exposure duration
- dependent variables
- objective metrics
- subjective instruments
- statistical tests
- effect estimates where available
- reported limitations
- code/data/material availability
- replication/reproduction information
- funding/conflicts where relevant
- candidate contradiction links
- candidate gaps

## Quality and reproducibility audit

Quality is recorded as dimensions rather than collapsed prematurely into one opaque score. Dimensions include:
- research-question clarity
- comparator adequacy
- protocol clarity
- sample justification
- participant diversity/relevance
- metric validity
- statistical adequacy
- effect-size/uncertainty reporting
- hardware/software specification
- parameter/configuration disclosure
- code availability
- data availability
- study-material availability
- deterministic/reproducible execution information
- independent replication

## Gap validation

A gap is retained only when its supporting evidence can be traced to included studies. Candidate gaps are tested against:
- existence of prior solutions
- existence of direct comparisons
- evidence quality
- contradictory findings
- scope limitations
- replication status
- public benchmark availability
- feasibility of independent testing

## Algorithm comparison gate

Algorithms are compared only when semantic compatibility is established: comparable problem definition, input/output assumptions, task, dataset or environment, metrics, and constraints. Incompatible algorithms are described taxonomically but not placed in a misleading numerical ranking.

## Novel algorithm gate

A novel algorithm is considered only after the review demonstrates a specific missing mechanism or unresolved trade-off. The algorithm must have:
- explicit problem formulation
- closest baselines
- ablation design
- robustness checks
- computational-cost analysis
- reproducible implementation
- pre-specified primary metrics
- statistical or uncertainty analysis where appropriate

## Artifact policy

All derived results should be regenerable from scripts/workflows. Figures and tables should be generated from frozen machine-readable outputs rather than manually transcribed values.

## Paper-writing gate

The paper is drafted after:
- screening is frozen;
- extraction validation is complete;
- principal gaps are verified;
- benchmark selection is frozen;
- all planned tests finish;
- all figures/tables are regenerated successfully;
- claims are reconciled against artifacts.
