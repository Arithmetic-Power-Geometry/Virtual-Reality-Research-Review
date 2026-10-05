# N07 Corrected Paired Controller Analysis

Source: original GitHub Actions raw run artifacts for N02 (Vis.-Poly), N04 (S2C), and N05 (P2R), after the pre-inference forensic correction.

Method:
- join by exact seed within each geometry;
- reset-burden comparisons use only pairs where both controllers completed;
- effect = controller A minus controller B in resets/100m;
- deterministic bootstrap: 10,000 resamples, seed 2601, percentile 95% CI;
- sign counts retained;
- completion discordance reported separately; failed runs are never assigned synthetic reset scores.

Main descriptive findings:
- G01: S2C < P2R < Vis.-Poly on complete-pair reset burden.
- G02: S2C lower than P2R; Vis.-Poly vs P2R interval includes zero.
- G03: Vis.-Poly lower than both S2C and P2R on complete-pair reset burden; S2C vs P2R interval includes zero.
- G04: S2C lower than Vis.-Poly and P2R; Vis.-Poly vs P2R interval includes zero.
- Completion ranking itself changes with geometry, especially G03.

Interpretation boundary:
These are paired effect estimates, not the final confirmatory inference. N08 performs multiplicity correction, nonparametric sensitivity tests, paired completion tests, and formal controller-by-geometry interaction analysis.
