# Virtual Reality Research Review

A systematic and reproducible research program for analysing virtual reality (VR) methods, algorithms, evaluation practices, benchmarks, contradictions, reproducibility, and open research problems.

## Research sequence

This repository follows an evidence-first workflow:

1. Define the review protocol and research questions.
2. Mine historical and current VR literature.
3. Extract claims, methods, algorithms, hardware, datasets, populations, metrics, and limitations.
4. Audit methodological quality and reproducibility.
5. Build cross-study comparison matrices.
6. Detect contradictions, missing comparisons, condition gaps, replication gaps, and algorithmic gaps.
7. Select only defensible, testable gaps.
8. Reproduce or implement comparable baseline algorithms where feasible.
9. Design a novel algorithm only when the evidence establishes a genuine missing mechanism.
10. Run controlled benchmarks and statistical analyses.
11. Generate figures, tables, algorithm listings, timelines, and machine-readable artifacts through reproducible workflows.
12. Freeze results and only then prepare the research paper.

## Scope

The review covers core VR research themes including:

- displays, rendering, foveation, and visual quality
- tracking, sensing, eye tracking, and body tracking
- interaction, input, gesture, gaze, and hand interfaces
- locomotion, navigation, redirected walking, and telepresence
- haptics, audio, and multisensory interaction
- presence, embodiment, agency, cognition, and perception
- cybersickness, comfort, ergonomics, and human factors
- avatars, virtual humans, embodied agents, and AI-driven VR
- social and collaborative VR
- accessibility and inclusive VR
- privacy, security, safety, and ethics
- networking, streaming, edge/cloud support, and distributed VR
- software architectures, authoring systems, research toolkits, and reproducibility
- healthcare, education, training, industry, digital twins, and other application domains

## Evidence model

The unit of analysis is not only the paper. The project records:

- study
- research claim
- task and environment
- method or algorithm
- comparator or baseline
- hardware and software stack
- participant/sample characteristics
- dataset
- evaluation metric or questionnaire
- statistical analysis
- effect/result
- code/data/artifact availability
- replication status
- limitations
- contradiction links
- gap classification

No gap is treated as established merely because a paper lists it as future work.

## Gap classes

A candidate gap must be supported by evidence and is classified as one or more of:

- evidence gap
- comparison gap
- condition/generalisation gap
- contradiction gap
- replication gap
- measurement gap
- dataset gap
- reproducibility gap
- population/accessibility gap
- algorithmic or missing-mechanism gap

## Review-to-experiment gate

Algorithm comparison begins only after the literature map identifies methods that can be compared under sufficiently compatible tasks, inputs, outputs, datasets, hardware assumptions, and metrics.

A proposed algorithm is introduced only if:
1. the closest prior methods are identified;
2. the missing capability is explicit and testable;
3. suitable baselines exist;
4. evaluation metrics are pre-specified;
5. the experiment can generate reproducible artifacts.

## Repository outputs

Planned reproducible outputs include structured evidence tables, search records, screening decisions, taxonomies, timelines, comparison matrices, contradiction maps, gap maps, benchmark results, statistical summaries, figures, tables, and algorithm listings.

The repository is research infrastructure. The eventual paper will report verified results produced from the completed workflow; manuscript drafting is intentionally deferred until evidence extraction, comparisons, tests, and artifacts are complete.
