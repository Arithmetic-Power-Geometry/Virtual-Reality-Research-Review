# Stage 3 Computational-Cost and Execution Provenance

## Frozen benchmark provenance
The authoritative N09 cost benchmark records:
- GitHub Actions workflow: 37329936208
- Head SHA: ac486b0d2828baf3717c2f66485242403a52209e
- Artifact ID: 11353444096
- Artifact digest: sha256:3d6961e280c0e6549175dbb542e9f5562d6bdf3d3d199c21d73f1458327fb7de

## Timing protocol
- actual controller decision functions;
- 12 deterministic state/geometry combinations;
- full pytest suite before timing;
- 500 warm-up calls;
- 9 timing samples per state;
- 5000 calls per timing sample;
- Python perf_counter_ns.

Median of per-state medians:
- Vis-Poly: 251.448 microseconds/decision.
- S2C: 2.022 microseconds/decision.
- P2R: 3.938 microseconds/decision.

Descriptive ratios on that runner:
- Vis-Poly/S2C approximately 124.4x.
- Vis-Poly/P2R approximately 63.9x.
- P2R/S2C approximately 1.95x.

## Structural complexity
- S2C: O(P) in the current implementation because the tracking center is recomputed from P physical segments; static geometry could cache the center and reduce that component to O(1).
- P2R: O(P) nearest-segment/repulsive-gradient accumulation.
- Vis-Poly: geometry-dependent, dominated by physical/virtual visibility-polygon construction plus slice construction/matching.

## Claim boundary
These are controller-decision microbenchmarks under one common CI software/hardware environment. They exclude rendering, path planning, reset execution, I/O, HMD latency, network latency, and user response. They are therefore evidence about **relative controller computation in this implementation**, not a device-independent real-time guarantee.

## Hardware limitation
The preserved N09 manuscript-facing provenance identifies the GitHub Actions workflow and immutable artifact but does not preserve a sufficiently detailed CPU-model/OS runner specification for hardware-normalized timing claims. Stage 3 does not invent it. The timing result is reported as runner-specific.
