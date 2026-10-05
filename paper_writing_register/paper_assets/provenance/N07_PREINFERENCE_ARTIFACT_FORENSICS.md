# N07 Pre-Inference Artifact Forensics — CORRECTION REQUIRED

Before any paired inference, the original GitHub Actions artifacts and job logs for N02, N04 and N05 were re-downloaded and audited.

## Authoritative workflow outputs

### N02 Vis.-Poly
Workflow: 37268780131
Artifact: 11328322863
Artifact digest: sha256:2d7a1a14f49de7a8f9a6f2d8f04f20810d3bfc2fe5777195c5542f5b3024516e
Job log reports 400 runs, 384 complete.

Per scene:
- G01: 92/100 complete; mean resets/100m among completes 13.5809562558
- G02: 99/100; 17.9396526205
- G03: 94/100; 24.0224235529
- G04: 99/100; 20.5771167076

### N04 S2C
Workflow: 37323011397
Artifact: 11351206228
Previously frozen N04 completion counts remain consistent with the recovered raw artifact:
- total 378/400 complete.

### N05 P2R
Workflow: 37325937407
Artifact: 11352157903
Artifact digest: sha256:d4cc7175e573d4d4d588bfa6a37cdf98232b80a906b384132955db7c018e615e
Job log reports 400 runs, 381 complete.

Per scene:
- G01: 100/100; mean 12.1674852521
- G02: 100/100; 18.1135928128
- G03: 81/100; 24.6256135551
- G04: 100/100; 20.7961089188

## Correction
Earlier manuscript-facing N02 and N05 summaries claimed 400/400 completion and different reset means. Those summaries are inconsistent with the immutable GitHub Actions job logs and downloadable artifacts referenced by the same workflow/artifact IDs.

Therefore:
- original workflow artifacts and job logs are authoritative;
- prior N02 and N05 manuscript summaries/provenance are superseded;
- N03-N06 manuscript assets derived from the incorrect summaries must be regenerated before inference;
- no N07 statistical claim may use the superseded summaries.

This correction is retained as part of the reproducibility record rather than silently replacing history.
