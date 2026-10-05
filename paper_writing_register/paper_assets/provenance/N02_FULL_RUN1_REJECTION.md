# N02-FULL Run 1 — REJECTED after artifact audit

Workflow run: 37267086735
Head SHA: d58fc61b66459d164ecca94710cc2c3e4f9f3f92
Artifact ID: 11327048243
Artifact digest: sha256:205faac21de569e125c6e00fe1425f3f7df36196e55787ac00f0e9c79364ab1c
Elapsed: 889.1193 s
Expected runs: 400

## Integrity
Artifact SHA-256 values were independently recomputed and matched the manifest:
- runs.csv f13cfd122cdd58ae71c91ae1c6a6e52193e08cfafeddf9a478b46d1d8867480a
- summary.csv ac1953179e7f9ad9a836c5c07b69155563a1746fe3064579cb19ded20280d449
- failures.json cef8e777a468cd71ebf797a0bb99c22d4dd3eb13b16ee200214f50a3b3eb4ddd
- manifest.json 4cb570d3fabc9fd6e9e62e5138e1f1dafe0ae61ede6fc4fa3df0b224a7c98e24

## Reviewer decision
**REJECT for scientific promotion.** CI success is not scientific validity.

Completion was only 66%-77%. Failure diagnostics showed virtual positions reaching or exceeding the 14x14 VE boundary despite the generated navigation route itself being clearance-safe.

## Root cause
The navigation-aware route executor inherited the earlier random-path WALK-THEN-TURN convention. A route defined by consecutive geometric nodes requires TURN-TO-SEGMENT-BEARING THEN WALK. Walking before the bearing change causes virtual-state drift away from the validated route. Long trajectories exposed this defect.

## Treatment
The run is retained as rejected diagnostic evidence. Its numerical performance values must not appear as scientific results. Correct only route execution, add exact route-tracking tests, repeat the 40-case short gate, and rerun N02-FULL only after reviewer PASS.
