# N09 Computational-Cost Gate — PASS

Workflow: 37329936208
Head SHA: ac486b0d2828baf3717c2f66485242403a52209e
Artifact ID: 11353444096
Artifact digest: sha256:3d6961e280c0e6549175dbb542e9f5562d6bdf3d3d199c21d73f1458327fb7de

Method:
- actual controller decision functions benchmarked on 12 deterministic state/geometry combinations;
- full pytest suite executed before timing;
- 500 warm-up calls;
- 9 timing samples per state;
- 5000 calls per timing sample;
- Python perf_counter_ns;
- wall-clock results are reported with structural complexity so the paper does not treat one GitHub runner as universal hardware performance.

Measured median of per-state medians:
- Vis.-Poly: 251.448 microseconds/decision
- S2C: 2.022 microseconds/decision
- P2R: 3.938 microseconds/decision

Relative descriptive cost on this runner:
- Vis.-Poly / S2C ≈ 124.4x
- Vis.-Poly / P2R ≈ 63.9x
- P2R / S2C ≈ 1.95x

Complexity interpretation:
- S2C: O(P) in the current implementation because tracking center is recomputed from P physical segments each decision; this could be O(1) if the center were cached for static geometry.
- P2R: O(P), accumulating nearest-point repulsive contributions across P physical segments.
- Vis.-Poly: dominated by physical and virtual visibility-polygon construction plus slice construction/matching; the exact asymptotic cost depends on the visibility-polygon implementation and polygon complexity.

Claim boundary:
This is a controller-decision microbenchmark, not end-to-end VR frame time. It excludes rendering, path planning, reset execution, I/O and HMD/network latency. Use it to discuss relative algorithmic controller overhead under a common software/hardware environment, not device-independent real-time guarantees.
