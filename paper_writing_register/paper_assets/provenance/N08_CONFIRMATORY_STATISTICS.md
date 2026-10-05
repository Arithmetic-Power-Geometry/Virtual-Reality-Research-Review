# N08 Confirmatory Statistics — Corrected Raw-Artifact Analysis

Inputs: original N02/N04/N05 raw workflow runs, joined by exact seed and scene after N07 artifact forensics.

Analyses:
- paired Wilcoxon signed-rank sensitivity analysis for reset burden among complete pairs;
- Benjamini-Hochberg FDR and Holm family-wise corrections across the 12 planned controller-by-geometry contrasts;
- exact paired completion-discordance tests (binomial form of McNemar test);
- Friedman omnibus comparison among triple-complete runs within each geometry.

Key confirmatory pattern:
- G01: strong reset-burden differences among all three controllers; Vis.-Poly also has significantly worse completion than S2C and P2R.
- G02: Vis.-Poly vs P2R is not distinguishable on reset burden; S2C differs from both under multiplicity correction.
- G03: geometry is the difficult regime. Vis.-Poly vs S2C remains significant after Holm; Vis.-Poly vs P2R is weaker (BH significant, Holm not); S2C vs P2R is not significant. Vis.-Poly has significantly better completion than P2R in the exact paired completion test.
- G04: S2C vs P2R remains significant after Holm; Vis.-Poly comparisons are weaker/non-significant under Holm.
- Friedman omnibus tests detect controller differences in every geometry, though G03 is only marginally below 0.05.

Scientific conclusion boundary:
The evidence does not support a universal controller ranking. Controller performance and robustness depend on geometry, with the hardest G03 condition changing both completion ordering and reset-burden contrasts. This supports a controller-by-geometry regime hypothesis, but does not by itself establish a new adaptive algorithm.

All p-values are secondary to effect sizes and completion outcomes. No failed run is assigned an artificial reset value.
