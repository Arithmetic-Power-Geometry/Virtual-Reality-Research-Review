# N05 Comparator Admission Gate — Pass 1

Purpose: admit only published controllers whose benchmark-critical rules can be implemented clean-room without silently inventing missing method details.

## Decision

### P2R / General Reactive APF (Thomas & Suma Rosenberg, 2019)
**Status: SELECTED FOR NEXT EXTRACTION.**
Primary conference record and paper metadata verify a reactive artificial-potential-function controller designed for complex/irregular physical spaces and comparison against Steer-to-Center. It belongs to the same reactive stratum as the current R1 benchmark and is therefore the strongest next candidate. Exact potential-function equations, obstacle representation, force aggregation, gain mapping, reset rule, and numerical parameters must be frozen before implementation.

### APF-RDW (Bachmann et al., 2019)
**Status: HOLD AS LINEAGE / POSSIBLE LATER COMPARATOR.**
The paper introduces APF redirection/resetting with multi-user support. Its multi-user scope is broader than the current single-user benchmark. Do not implement until single-user equations and reset semantics are extracted and compatibility with the common reset design is resolved.

### FORCE (Zmuda et al., 2013)
**Status: DO NOT MIX INTO REACTIVE N05 SET YET.**
FORCE uses a map of the tracking space plus multistep probabilistic prediction in a known virtual environment and search-based optimization. It is scientifically relevant but belongs to a predictive/search stratum. It should be evaluated separately unless the benchmark supplies the path-prediction inputs required by the published method.

### RL-Steering (2020)
**Status: HOLD — learned stratum.**
Faithful reproduction requires state/action/reward/training-environment extraction and training protocol. Do not approximate with an unverified policy.

### ARC controller (2021)
**Status: HOLD FOR CONTROLLER EXTRACTION.**
ARC reset semantics are already used and audited, but the controller itself requires a separate exact extraction before being admitted as a steering comparator.

### Alignment-Optimized (2023) and APF-S2T (2024)
**Status: HIGH-PRIORITY AFTER P2R.**
Recent comparison-rich controllers, but exact objective/target sampling/gain rules remain incomplete in the current extraction ledger.

## N05 rule
No comparator enters N06 merely because its name and high-level mechanism are known. Admission requires: primary-source equation/rule extraction; parameter freeze; semantic unit tests; common benchmark compatibility statement; short paired gate; adversarial reviewer PASS.

Next action: complete P2R equation/parameter extraction from the primary paper before writing code.
