# N01 Semantic Audit — Frozen CI Provenance

- Stage: N01 Pre-R1 semantic correctness audit
- Adversarial reviewer decision after correction: **PASS for R1 sensitivity; R2 remains conditional on static path-model reconstruction**
- Final workflow run: 37263870923
- Head SHA: 2ed091d5c781a006585da91b19091a2964ef5e4a
- Conclusion: success
- Test result: 46 passed
- Corrected scientific issues:
  1. reset detection uses nearest physical-obstacle clearance rather than heading-ray clearance;
  2. reset threshold reflects 0.5 m user radius plus 0.2 m obstacle clearance;
  3. ARC obstacle normal uses exact nearest-segment face geometry rather than 360-ray approximation;
  4. exact published static Vis.-Poly environment coordinates are registered and implemented.
- Remaining reproduction boundary: exact static path instances/seeds are not published; cited Azmandian et al. path/motion model must be reconstructed for R2 condition-faithful reproduction.
- Claim permission: R1 protocol-compatible sensitivity experiments may proceed if labeled as such. No R3 numerical-replication claim is permitted.
