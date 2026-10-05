# N03 Analysis Readiness Gate

Status: IMPLEMENTATION VALIDATED; SCIENTIFIC EXECUTION BLOCKED UNTIL N02-FULL PASSES.

The paired analysis implementation is intentionally separate from the running N02-FULL workflow. It:
- requires every input run to be complete;
- requires a balanced seed x scene matrix with unique pairs;
- computes all six pairwise scene contrasts for resets per 100 m;
- reports mean and median paired differences, SD, direction counts, and a deterministic 10,000-replicate bootstrap 95% interval;
- records the SHA-256 hash of the admitted N02 input;
- does not make controller-superiority or direct-replication claims.

CI validation:
- workflow run 37268111093
- conclusion: success

Scientific execution remains blocked until the N02-FULL artifact is complete, hash-checked, failure-audited, and reviewer-approved.
