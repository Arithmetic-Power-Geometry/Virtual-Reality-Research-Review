# G02 Technical Landscape — Pass 1

This document records the first technical mining pass. It is deliberately conservative: a source can establish a method family or methodological problem without establishing a novel gap.

## 1. Cybersickness

### Established landscape
Recent reviews continue to treat cybersickness as a central barrier to VR use and distinguish measurement, prediction, and mitigation. Measurement commonly combines subjective questionnaires with physiological, behavioral, or system signals, but protocols and labels vary across studies.

### Comparison problem
Prediction studies may use different sickness instruments, sampling windows, participant populations, content, headsets, and sensor sets. Reported classifier/regressor performance is therefore not automatically cross-study comparable.

### G02 action
Build a predictor matrix with:
- sickness target/instrument;
- prediction horizon;
- content/task;
- headset;
- signals available at inference;
- participant-independent vs participant-dependent split;
- within-dataset vs cross-dataset/device validation;
- calibration;
- uncertainty;
- code/data.

### Candidate benchmark
Cross-dataset or leave-device/content-out evaluation is potentially stronger than reproducing within-dataset accuracy. Remains C1 until datasets and closest methods are verified.

## 2. Redirected walking and locomotion

### Established landscape
Redirected walking research includes steering/redirection gains, reset strategies, path planning, user-aware methods, multi-user redirection, and increasingly optimization/learning-based controllers. Results depend strongly on physical-space geometry, virtual paths, user model, collision/reset definition, and perceptual constraints.

### Comparison problem
A lower reset count under one room/path distribution does not establish general superiority.

### G02 action
Extract:
- physical-space shape/size;
- virtual-path generator;
- number of users;
- redirection gains/constraints;
- reset rule;
- collision handling;
- prediction model;
- resets;
- redirected distance;
- path deviation;
- collisions;
- clearance/safety;
- computational cost.

### Candidate benchmark
A common scenario suite with fixed seeds and multiple room/path distributions appears technically feasible. This is currently one of the strongest candidates for a repository benchmark, but remains C1 pending closest-work and simulator audit.

## 3. Foveated rendering

### Established landscape
Foveated rendering exploits visual acuity falloff and increasingly combines eye tracking, gaze prediction, variable-rate rendering or neural/perceptual rendering.

### Comparison problem
Image-quality gains and speedups depend on GPU, display resolution, eye-tracker latency/accuracy, scene complexity, eccentricity model, and quality metric. Hardware-specific speedup should not be pooled as if platform-independent.

### G02 action
Separate:
- fixed vs gaze-contingent foveation;
- raster vs neural methods;
- gaze prediction component;
- quality metric;
- perceptual/user-study outcome;
- frame time/FPS;
- eye-tracking latency;
- end-to-end latency;
- GPU/platform.

### Candidate benchmark
Open scene + gaze-trace replay could support perceptual/quality comparison, but implementation portability must first be verified.

## 4. Tracking and pose

Tracking is not one benchmark family. Eye gaze, hands, full body, controllers, and inside-out device pose use different inputs and outputs. G02 will partition them before extracting algorithms. Any field-wide accuracy ranking would be invalid.

## 5. Motion prediction and latency compensation

Prediction methods should be grouped by prediction horizon, signal history, motion type, target (head/gaze/controller/body), and deployment purpose. A horizon sweep on shared traces is a plausible computational benchmark if public traces and reproducible baselines are available.

## 6. Streaming, viewport prediction, and edge VR

### Established landscape
Immersive streaming research couples viewport prediction, tiled/quality-adaptive delivery, bandwidth allocation, latency, QoE, and sometimes edge computation.

### Comparison problem
Methods differ in FoV representation, video format, network traces, prediction horizon, bitrate ladder, codec, QoE objective, and latency assumptions.

### Candidate benchmark
Trace-driven replay is promising because it can compare predictors and allocation policies without requiring identical physical HMDs. G02 must first identify reusable public viewport/network traces and standard QoE formulations.

## 7. Security and privacy

The existing VR security/privacy survey provides a strong taxonomy, but attacks, defenses, and authentication cannot be ranked together. G02 will separate:
- identity/authentication;
- motion/gaze/voice inference attacks;
- de-anonymization;
- spoofing/manipulation;
- privacy-preserving learning/processing;
- system/network attacks.

Benchmarking requires a fixed threat model and ethical/public data.

## 8. Adaptive AI-VR

AI-driven VR is rapidly expanding, but "AI in VR" is too broad for algorithm comparison. A technically useful formulation must identify:
state -> observation -> policy/controller -> adaptation action -> objective -> constraint.

Potential objectives include sickness, task performance, presence, rendering quality, latency, accessibility, or multi-objective combinations. No novel controller is justified yet.

## Current benchmark priority

**Priority A — Redirected walking:** high simulation feasibility; requires simulator/closest-benchmark audit.

**Priority B — Cybersickness prediction:** high scientific importance; requires harmonized labels and public cross-domain data.

**Priority C — Streaming/viewport prediction:** high computational reproducibility potential; requires open trace audit.

**Priority D — Motion prediction:** potentially clean shared-trace benchmark; requires sufficient VR-specific closest work.

**Priority E — Foveated rendering:** important but hardware/rendering-stack dependence increases reproduction cost.

Tracking, security/privacy, adaptive AI-VR, and accessibility remain active but require narrower problem formulations before numerical comparison.

## Decision
No algorithm is proposed in Pass 1. The next gate is G02-Pass-2: primary-study and benchmark mining for Priorities A–C, followed by a reproducibility/availability audit.
