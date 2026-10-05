# N02 Corrected Navigation Execution Short Gate — PASS

Workflow: 37268573221
Head SHA: 7f0203a5b4dec540d3d088165efda59dd94f579d
Artifact ID: 11327651104
Artifact digest: sha256:ea259f3dcf70530060a9d300a6d37cb3c533ae20127c5cc0aed0823a3845675d

## Precondition
Exact navigation-route tracking regressions passed for 35 m seeds and representative 350 m seeds. The corrected executor turns to each geometric route edge before walking it.

## Result
40/40 short runs completed; failures.json is empty.

| Scene | Complete | Mean resets/100 m | SD |
|---|---:|---:|---:|
| R1-G01 | 10/10 | 16.35059 | 6.07230 |
| R1-G02 | 10/10 | 19.48407 | 6.70495 |
| R1-G03 | 10/10 | 25.16753 | 4.46405 |
| R1-G04 | 10/10 | 21.94758 | 2.48108 |

## Artifact hashes
- runs: 579349dbb048982d2ac9408a7e1dcbc0d6dab90fc48bb327fa5388191583215c
- summary: bc0e8eeebcd304827402e884b8cf4b57920727fdf48ada211f151e73bc12d391
- failures: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- manifest: 4febe6317a6899e1786e5acf89dd88eb27828ef33cf4254b2d4a6fff122bb56e

Reviewer decision: PASS short gate. Numerical values remain diagnostic until corrected N02-FULL passes.
