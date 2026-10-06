# Stage 5 Citation Coverage Audit

## Current bibliography state
- master_references.bib: 174 entries
- citation-use ledger rows: 131
- two ledger aliases do not match the current BibTeX keys: Liu2024RDWSurvey and Williams2021VisPoly
- 45 current BibTeX keys are not represented by exact key in the existing citation-use ledger
- after accounting for the two aliases, 43 additional bibliography entries still need explicit prose placement in the final LaTeX manuscript

The user's earlier target of 212 references is not supported by the frozen verified bibliography. Stage 5 does not invent 38 references to reach an arbitrary count. The submission package must use the **174 currently verified BibTeX entries**, and references retained in the final bibliography must be cited in substantive prose rather than parked uncited in the reference list.

## Alias repairs for typesetting
- Liu2024RDWSurvey -> use the verified current key corresponding to the RDW survey in master_references.bib during LaTeX citation normalization.
- Williams2021VisPoly -> Williams2021VisibilityPolygons.

## Unplaced exact BibTeX keys and prose clusters

### RDW foundations, thresholds, steering, taxonomies
Razzaque2001RedirectedWalking; Steinicke2010DetectionThresholds; Peck2010ImprovedRedirection; Grechkin2016Thresholds; Thomas2019P2R; Bachmann2019APF; Strauss2020RL; Williams2021VisibilityPolygons; Azmandian2022Adaptive; Hirt2024PredictiveMultiuser; Fan2023RDWReview; Chen2024APFS2T; Wang2026DGMRDW; Nilsson2018FifteenYears; Hodgson2013FourApproaches; Steinicke2008Sensitivity; Bolling2019ShrinkingCircles; Liu2024SpatialConstraints; MayorMarquez2025MTRW; Azmandian2015PhysicalSpace; Azmandian2016RDWToolkit.

Placement: Introduction/Related Work/RDW method lineage. These sources should support historical development, perceptual thresholds, constrained-space dependence, APF/P2R, visibility polygons, RL/adaptive/predictive/multi-user methods, and review taxonomy. They must not be used to imply present-paper controller novelty.

### Measurement, presence, cybersickness, healthcare
Bareisyte2024Questionnaires; Caserman2021Cybersickness; OjedaDeOcampo2026Presence; Erbas2024HealthcarePresence.

Placement: presence/embodiment, cybersickness, evaluation, and healthcare synthesis. Erbas2024HealthcarePresence remains one of the two reports not retrieved; it must not be used for full-text-dependent claims beyond verified bibliographic/abstract-level context.

### Prediction, resets, multi-user, alternative RDW mechanisms
Thomas2022IKPaths; Zank2016EyeTracking; Azmandian2017TwoUser; Zhang2023OutOfPlaceReset; Gandrud2016Destination; Bremer2021FuturePosition; Stein2022EyeLSTM; You2022StrafingGain; Suma2012Taxonomy; Suma2012ImpossibleSpaces; Suma2011ChangeBlindness; Vasylevska2013FlexibleSpaces; Azmandian2014Enhanced; Peck2011RFED; Sun2018Saccadic; Thomas2020ReactiveAlignment; Langbehn2018Bending.

Placement: RDW Related Work. Use these sources to show the breadth of prediction, reset, redirection, layout, change-blindness, multi-user, and perceptual manipulation approaches. Zank2016EyeTracking is not full-text retrieved and must be bounded accordingly.

### Adjacent interaction/perception evidence
Bruder2015Cognitive; Rietzler2017Breaking; Sheng2024HandGestures.

Placement: interaction/perceptual manipulation synthesis; do not force them into the RDW performance comparison.

## Stage-6 citation rule
The LaTeX build must run a machine check:
1. extract all BibTeX keys;
2. extract all citation keys from the TeX source;
3. fail if a bibliography entry intended for the final paper is uncited;
4. fail if a citation key is absent from the BibTeX file;
5. report duplicate/alias keys;
6. retain citations in semantically relevant prose, not citation-dump paragraphs.

Status: CITATION COVERAGE AUDITED; FINAL 174-KEY PROSE PLACEMENT RESERVED FOR LATEX INTEGRATION.
