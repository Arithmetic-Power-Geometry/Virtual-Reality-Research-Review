# Gap Evidence Rules

## Principle
Absence of evidence in one review is not evidence of a research gap. A gap claim requires a traceable search and evidence chain.

## Status levels
- C0 Mentioned: stated as future work by one or more papers.
- C1 Candidate: appears absent or unresolved in a verified secondary source.
- C2 Corroborated: supported by multiple independent sources and/or updated primary-study search.
- C3 Testable: has an explicit problem formulation, observable outcome, and feasible comparison.
- C4 Benchmark-ready: compatible baselines, data/environment, metrics, and evaluation protocol are available.
- C5 Experimentally evaluated: repository contains reproducible results addressing the gap.

Only C2+ gaps may appear in the principal research-gap synthesis. Only C4 gaps may motivate a new benchmark or algorithm.

## Contradiction rule
A contradiction is recorded only when studies address sufficiently comparable constructs/problems. Differences caused by population, hardware, exposure, task, measurement instrument, or intervention content are first treated as candidate moderators rather than contradictory truth claims.

## Novelty rule
Novelty is never inferred from keyword absence. Before describing a mechanism as missing, search:
1. exact problem terminology;
2. synonyms and historical terminology;
3. closest algorithm families;
4. backward references;
5. forward citations;
6. patents/technical reports when relevant to priority claims;
7. current papers through the final search date.

## Negative-result rule
Null and negative findings are retained. Evidence synthesis must not privilege positive performance improvements.

## Reproducibility rule
"Code unavailable" and "not reproducible" are distinct labels. Reproducibility failure requires an attempted reproduction or sufficiently specific evidence that the reported experiment cannot be reconstructed.
