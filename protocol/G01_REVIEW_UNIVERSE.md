# G01 — Review Universe and Seed-Mining Protocol

## Purpose
G01 establishes the controlled literature universe before domain workstreams begin independent extraction. It prevents topic drift, duplicated searching, selective gap discovery, and comparisons between semantically incompatible studies.

## Temporal coverage
Foundational VR literature is eligible without a lower year bound when it establishes a concept, method, measurement instrument, algorithm family, or experimental paradigm. Systematic contemporary coverage extends through the final search date. Search dates are recorded so the corpus can be updated reproducibly.

## Evidence strata
1. Foundational/concept-defining works.
2. Field-level scientometric and broad reviews.
3. Technical systematic/scoping reviews.
4. Human-factor and measurement reviews.
5. Application-domain systematic reviews/meta-analyses.
6. Primary algorithm/system papers.
7. Primary controlled user studies.
8. Dataset, benchmark, toolkit, and reproducibility papers.

Reviews are discovery and synthesis sources; performance claims are traced back to primary studies whenever possible.

## Search families
S01 Foundations: "virtual reality" AND (history OR taxonomy OR immersion OR presence)
S02 Rendering/display: "virtual reality" AND (rendering OR foveated OR display OR visual quality)
S03 Tracking/sensing: "virtual reality" AND (tracking OR eye tracking OR body tracking OR sensing)
S04 Interaction: "virtual reality" AND (interaction OR hand OR gesture OR gaze OR input)
S05 Locomotion: "virtual reality" AND (locomotion OR navigation OR redirected walking OR teleportation)
S06 Haptics/audio: "virtual reality" AND (haptic OR tactile OR spatial audio OR multisensory)
S07 Human factors: "virtual reality" AND (presence OR embodiment OR agency OR cybersickness OR simulator sickness)
S08 Avatars/agents: "virtual reality" AND (avatar OR virtual human OR embodied agent OR intelligent agent)
S09 Social/collaborative: "virtual reality" AND (social OR collaborative OR multi-user)
S10 Infrastructure: "virtual reality" AND (network OR streaming OR edge OR cloud OR latency)
S11 Security/privacy: "virtual reality" AND (security OR privacy OR authentication OR attack)
S12 Accessibility: "virtual reality" AND (accessibility OR disability OR inclusive)
S13 Evaluation: "virtual reality" AND (evaluation OR questionnaire OR metric OR benchmark OR measurement)
S14 Reproducibility: "virtual reality" AND (reproducibility OR replication OR toolkit OR open source OR dataset)
S15 AI: "virtual reality" AND ("artificial intelligence" OR "machine learning" OR LLM OR adaptive)
S16 Healthcare: "virtual reality" AND (healthcare OR clinical OR rehabilitation OR therapy)
S17 Education/training: "virtual reality" AND (education OR learning OR training OR simulation)
S18 Industry/digital twin: "virtual reality" AND (industry OR engineering OR "digital twin" OR design)

Each family is executed with review terms for secondary-study discovery and without them for primary-study discovery.

## Source hierarchy
Core scholarly sources include IEEE Xplore, ACM Digital Library, Scopus and/or Web of Science when accessible, ScienceDirect, SpringerLink, and PubMed for health-related evidence. Backward and forward citation chasing is used after seed reviews are verified.

## Inclusion criteria
Include a work when it contributes directly to immersive VR theory, technology, algorithms, evaluation, empirical evidence, datasets/benchmarks, research infrastructure, or a clearly defined VR application problem. Mixed XR studies are retained only when VR evidence is separable.

## Exclusion criteria
Exclude works where VR is incidental; AR/MR-only evidence without separable VR results; editorials without substantive evidence; marketing/product material; non-scholarly summaries used as evidence; duplicate reports of the same experiment unless they add distinct results; and papers for which the relevant claim cannot be verified sufficiently for the intended synthesis.

## Seed-review role
A seed review is not treated as proof that a gap still exists. It is used to:
- recover terminology and prior taxonomies;
- identify primary-study clusters;
- identify established measures and algorithm families;
- discover reported contradictions and limitations;
- locate newer forward citations;
- define what the present review must not duplicate.

## Comparison-validity audit
For every direct comparison, record:
- equivalence of task/problem;
- equivalence of input information;
- equivalence of output objective;
- dataset/environment equivalence;
- hardware/software equivalence;
- training/tuning budget equivalence where applicable;
- content/instruction equivalence for human studies;
- exposure/time equivalence;
- metric equivalence;
- statistical uncertainty/effect-size reporting;
- known confounds.

A published comparison is not automatically a valid benchmark.

## Stop conditions
G01 is complete only when:
1. every A01–A20 workstream has at least one verified seed source or an explicit documented absence;
2. search vocabulary is stable enough for reproducible execution;
3. closest broad and technical reviews are mapped;
4. extraction fields cover the variables needed by those reviews and our additional cross-domain questions;
5. no candidate novelty claim is based solely on absence from a single database or review.
