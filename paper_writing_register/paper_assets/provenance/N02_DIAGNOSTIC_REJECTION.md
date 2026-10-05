# N02 diagnostic run — REJECTED for scientific use

Workflow run 37264252135 (head 35df29beaf441469f54f36c6efaef3e149c18cda) completed successfully and generated the first corrected-reset R1 sensitivity output. The adversarial reviewer rejected the numerical output for paper use.

## Reject reasons
1. Three short runs reached the 100-reset cap, signalling pathological behavior requiring semantic investigation.
2. Canonical RDW gain definitions are virtual/physical. The repository motion layer still applied translation and rotation gains as physical/virtual.
3. The run uses only 10 seeds and 8 waypoints and is explicitly not the published-scale 100-path, approximately 350 m protocol.
4. Summary statistics excluded reset-cap runs and therefore cannot be used as unbiased performance estimates.

## Use
Retained only as a provenance/debugging artifact demonstrating why the reviewer gate stopped progression. No manuscript performance claim may cite these numbers.
