# Paper Assets

This directory is the manuscript-facing artifact layer for the Virtual Reality Research Review project. It does not contain manually invented paper results. Every scientific table, figure, algorithm description, and result placed here must trace to machine-readable evidence or tested code elsewhere in the repository.

## Structure
- `tables/` — manuscript-ready tables generated from frozen evidence/results.
- `figures/` — manuscript-ready figures plus their source data.
- `algorithms/` — paper-facing pseudocode/specifications linked to tested implementations.
- `results/` — frozen result CSV/JSON outputs used in manuscript claims.
- `statistics/` — statistical outputs, uncertainty, effect sizes, tests.
- `provenance/` — workflow IDs, commit SHAs, artifact hashes and reviewer decisions.
- `manifests/` — machine-readable mapping from paper asset to source evidence.

## Admission rule
An asset enters this directory only after the IEEE/TVCG adversarial reviewer gate permits its use. Smoke-test or engineering outputs must be clearly labeled and cannot silently become paper performance evidence.

## Reproduction rule
For every final paper figure/table, retain the source data and the script or deterministic procedure that generated it. TVCG reproducibility guidance motivates this organization.
