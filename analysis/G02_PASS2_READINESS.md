# G02 Pass 2 — Benchmark Readiness Decision

## Decision rule
This pass ranks **readiness for reproducible benchmarking**, not scientific importance and not algorithm quality.

## Priority A — Redirected walking

### Why it currently leads
Redirected walking has a relatively explicit control problem: keep a user within a bounded physical tracked space while allowing traversal of a larger virtual environment. Many methods can be evaluated through simulation before human validation. Common outcomes include resets, collisions, clearance, distance/path efficiency, and redirection behavior.

### What is still missing
- exact primary-controller list;
- open/reimplementable simulator selection;
- common room geometries and path generators;
- fixed gain/threshold assumptions;
- multi-user vs single-user separation;
- reproducible seeds;
- computational-cost reporting.

### Status
**C2 approaching C3**, not C4. The problem is corroborated and testable, but benchmark assets and baseline implementations are not yet frozen.

## Priority B — Cybersickness prediction

### Strength
High scientific relevance and a natural supervised prediction formulation.

### Blocking issue
Studies may predict different targets derived from SSQ/VRSQ/FMS or other instruments, use different temporal windows and signals, and evaluate participant-dependent versus participant-independent splits. High reported accuracy under incompatible protocols cannot be treated as a fair leaderboard.

### Status
**C1/C2 methodological opportunity.** Do not benchmark until at least one sufficiently large public dataset and compatible baselines are verified.

## Priority C — Streaming / viewport prediction

### Strength
Trace-driven replay can potentially remove HMD hardware from part of the benchmark and permits deterministic network conditions.

### Blocking issue
Viewport representations, prediction horizons, codecs/tiling, bitrate ladders, network traces and QoE functions differ substantially. Viewport prediction and end-to-end streaming optimization must be benchmarked as separate layers before combining them.

### Status
**C1/C2.** Promising but requires dataset/trace and exact baseline audit.

## Go/no-go

**GO to G03 for redirected walking benchmark construction.**
This is not approval to claim a new algorithm. G03 must first establish an executable baseline benchmark.

**CONTINUE MINING cybersickness and streaming in parallel.**
They remain valuable review strata and may later yield stronger secondary benchmarks.

## G03 requirements

1. Resolve canonical redirected-walking controller families to exact primary papers.
2. Identify open-source simulator(s) or implement a neutral simulator from published equations.
3. Freeze physical-space scenarios.
4. Freeze virtual-path distributions.
5. Freeze redirection constraints and reset definitions.
6. Implement/reproduce baseline controllers.
7. Add deterministic seeds and unit tests.
8. Produce baseline-only artifacts.
9. Analyze failure cases.
10. Only then formulate a missing mechanism and test whether a new controller is warranted.

## Anti-overclaim rule
If baseline reproduction shows that an apparent gap is already addressed, the candidate novel algorithm is abandoned and the evidence map is updated accordingly.
