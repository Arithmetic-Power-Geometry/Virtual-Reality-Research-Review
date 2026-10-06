# Stage 2 Operational Coding Manual

## Purpose
This manual converts the manuscript's comparability, evidence-state, reproducibility, workstream, and contradiction concepts into explicit coding rules. It does not claim psychometric validation. It defines a reproducible protocol that can be independently applied and tested.

## 1. Evidence descriptor
Each study/claim is represented as

E = (P, I, O, D, C, M, V)

where:
- **P — Problem/population:** scientific question and, for human studies, target population.
- **I — Intervention/input:** algorithm, interface, treatment, stimulus, sensing/input configuration, or manipulated factor.
- **O — Outcome:** construct or endpoint being interpreted.
- **D — Data/environment:** dataset, physical/virtual geometry, task environment, scenario, or experimental material.
- **C — Constraints:** hardware limits, gain limits, exposure constraints, safety rules, eligibility restrictions, or other boundary conditions.
- **M — Metric/measurement:** operational measure, instrument, scale, estimator, aggregation rule, or statistical endpoint.
- **V — Validation design:** simulation, offline benchmark, controlled lab experiment, field study, clinical/educational trial, review/meta-analysis, independent reproduction, or other validation level.

The previous six-dimension prose is superseded: validation design V is explicitly separate from metric M.

## 2. Dimension-level compatibility
For each dimension k in {P,I,O,D,C,M,V}, code:

gamma_k(a,b) in {1, 0, U}

- **1 COMPATIBLE:** differences do not invalidate the intended comparison.
- **0 INCOMPATIBLE:** a difference changes the estimand/construct/regime enough that a direct numerical comparison would be misleading.
- **U UNCERTAIN:** reporting is insufficient, ambiguous, or only indirectly comparable.

Coders must record a short evidence note for every 0 or U.

### P
1 when the scientific question and relevant population are materially aligned.
0 when population/problem changes the target inference.
U when population/problem is underspecified.

### I
1 when interventions/algorithms/interfaces instantiate the same comparison class or are legitimate alternatives for the stated question.
0 when nominally similar labels conceal different intervention content or objectives.
U when implementation detail is insufficient.

### O
1 when the same construct/end point is targeted.
0 when different constructs are being treated as the same outcome.
U when construct mapping is unclear.

### D
1 when data/task/environment differences are controlled, matched, or known not to change the intended estimand.
0 when environment/task/dataset defines a materially different regime.
U when environment detail is insufficient.

### C
1 when relevant constraints are matched or analytically accommodated.
0 when constraints change feasibility or interpretation.
U when constraints are missing.

### M
1 when metrics/instruments are identical or a justified transformation/equivalence exists.
0 when measures are non-equivalent for the claimed comparison.
U when scoring/aggregation is incompletely reported.

### V
1 when validation designs support the same level of inference.
0 when one design cannot support the inference being compared (e.g., simulation performance versus clinical effectiveness).
U when validation level is unclear.

## 3. Pair-level Gamma
Gamma(a,b) is not a distance score.

- **Gamma = 1 (DIRECTLY_COMPARABLE)** only if all seven gamma_k = 1.
- **Gamma = 0 (NOT_DIRECTLY_COMPARABLE)** if any gamma_k = 0.
- **Gamma = U (COMPARABILITY_UNCERTAIN)** if no gamma_k = 0 and at least one gamma_k = U.

A sensitivity field may record whether a conclusion changes if U is provisionally treated as compatible; the primary classification remains U.

## 4. Contradiction classification
A pair/family may be classified:
- **GENUINE_REGIME_EFFECT:** Gamma=1 and outcomes/rankings differ across an explicitly varied moderator/regime under a common benchmark/design.
- **COMPARABILITY_LIMITED:** Gamma=0; apparent conflict is not a direct replication failure.
- **UNRESOLVED:** Gamma=U or evidence is insufficient.
- **CONSISTENT:** Gamma=1 and results are directionally compatible for the stated estimand.

No contradiction prevalence is inferred beyond the audited family set unless all eligible records are systematically coded for that purpose.

## 5. C0-C5 evidence ladder
The levels are ordinal evidence-obligation states, not an interval scale.

- **C0 MENTIONED:** a gap/opportunity is asserted without traceable supporting evidence.
- **C1 CANDIDATE:** at least one traceable source or observed artifact motivates the gap.
- **C2 CORROBORATED:** at least two independent evidence sources/families support the same unresolved issue, with contrary evidence recorded.
- **C3 TESTABLE:** C2 plus an operational hypothesis, variables/outcomes, comparator, and falsification criterion.
- **C4 BENCHMARK_READY:** C3 plus executable/obtainable data or environment, baseline(s), metric(s), protocol, and reproducibility specification sufficient for a fair test.
- **C5 EVALUATED:** C4 plus completed analysis whose artifacts and uncertainty are recorded.

Monotonicity rule: promotion requires all obligations of lower levels. A claim cannot skip C3 to reach C4.

Independence rule for C2: two papers from the same study family do not automatically count as two independent corroborations.

## 6. Reproducibility state/failure coding
Availability and failure are separated.

Evidence states:
R0 SPECIFIED? protocol/parameters sufficiently specified.
R1 ARTIFACT_AVAILABLE? required code/data/materials available.
R2 EXECUTABLE? supplied artifact executes in documented environment.
R3 REGENERATES? reported computational result/table/figure can be regenerated.
R4 SEMANTIC_MATCH? regenerated output measures the same construct/estimand claimed.
R5 INDEPENDENT_RESULT? an independent implementation/study reproduces the substantive result within a stated tolerance or compatible inference.

Failure labels are assigned only after the relevant obligation is attempted/testable:
- specification failure;
- artifact failure;
- execution failure;
- regeneration failure;
- semantic failure;
- independent-result failure.

"Not available" is not automatically "failed".

## 7. Workstream coding
A01-A21 are overlapping analytical tags, not mutually exclusive bins. Each assignment requires one sentence identifying the report's direct contribution. A paper may receive multiple tags. Workstream counts therefore must not be summed as unique-study totals.

## 8. Study-family rule
Use the Stage-1 family rules: primary experiments may remain separate while belonging to a common lineage; reviews do not count as independent replications of the primary studies they synthesize; software/toolkit evidence supports reproducibility/infrastructure rather than effect size.

## 9. Independent-coding protocol
For validation, two coders must independently code a predeclared sample before adjudication. Required outputs:
- raw coder-A and coder-B values;
- percent agreement by field;
- Cohen's kappa for nominal binary/three-state fields where estimable;
- weighted kappa for ordinal C0-C5 where appropriate;
- disagreement ledger;
- adjudicated values stored separately.

Until a real second coder completes this protocol, agreement is **NOT_MEASURED** and no kappa value may be reported.

## 10. Stage-2 validity boundary
This stage validates the operational definition of the framework and audits existing classifications for traceability. It does not fabricate independent-rater evidence. Empirical inter-rater validation remains an external human-coding requirement unless a genuine second-coder file is supplied.
