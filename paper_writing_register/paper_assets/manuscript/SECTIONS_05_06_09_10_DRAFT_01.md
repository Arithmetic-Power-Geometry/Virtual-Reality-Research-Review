# Virtual Reality Research: A Systematic Review of Methods, Algorithms, Evaluation, and Open Research Problems

> Draft 02 — Sections 5, 6, 9, and 10. Uses corrected N07-N09 artifacts only. Earlier pre-forensic N02/N05 summaries and the stale N06 admission counts are superseded.

## 5. Redirected-Walking Case-Study Methods

### 5.1 Purpose and benchmark design

The redirected-walking (RDW) case study was designed as a controlled demonstration of context-sensitive algorithm comparison rather than as a claim of universal controller superiority. Three executable controllers—Visibility-Polygon redirection (Vis.-Poly), Steer-to-Center (S2C), and Potential-to-Redirect (P2R)—were evaluated under the same benchmark runner, path-generation process, safety checks, reset policy, geometry set, and seed schedule. Four physical-environment geometries (R1-G01 to R1-G04) were used, with 100 paired seeds per geometry and a target virtual travel distance of approximately 350 m per run, yielding 1,200 planned controller-condition cells.

The authoritative completion totals after the pre-inference raw-artifact audit are 384/400 for Vis.-Poly, 378/400 for S2C, and 381/400 for P2R. These values supersede earlier manuscript-facing summaries that had incorrectly reported complete execution for Vis.-Poly and P2R. The correction was made before inferential analysis by re-downloading the immutable GitHub Actions artifacts and job logs and was retained in the provenance record rather than silently overwritten.

### 5.2 Controller set and implementation boundaries

Vis.-Poly uses physical and virtual visibility polygons together with slice construction and matching to select redirection behavior. S2C recomputes a steering direction toward the tracking-space center from the current physical geometry. P2R uses repulsive artificial-potential contributions from nearby physical boundaries to derive a steering direction. All three implementations are clean-room executable comparators under the common R1 benchmark.

A fourth contemporary method, APF-S2T, was reviewed as a literature comparator but was not numerically admitted because the recoverable primary-method description did not fully determine the discretization choices required for a faithful implementation. The case study therefore treats APF-S2T as prior methodological context, not as an executable benchmark row. This distinction avoids presenting an implementation guess as a replication.

### 5.3 Common reset and failure handling

The controller comparison uses a common reset policy so that differences in steering behavior are not confounded by different reset mechanisms. Completion and reset burden are treated as separate outcomes. Failed or incomplete runs are retained as outcomes and are never assigned synthetic reset scores. Reset-burden comparisons are consequently conditional on both members of a controller pair completing the same seed in the same geometry.

This failure-aware design is important because a controller can exhibit low reset burden on its successful runs while failing more often in a difficult geometry. Collapsing these outcomes into a single imputed score would obscure the robustness-performance trade-off.

### 5.4 Paired statistical analysis

Within each geometry, controller pairs were joined by exact seed. For reset burden, the primary effect was the paired difference in resets per 100 m among complete pairs. Deterministic percentile bootstrap confidence intervals used 10,000 resamples with seed 2601. Sign counts were retained to show how often each controller had lower burden.

Confirmatory analysis used paired Wilcoxon signed-rank tests for reset burden, Benjamini-Hochberg false-discovery-rate and Holm family-wise multiplicity corrections across the 12 planned controller-by-geometry contrasts, exact paired completion-discordance tests, and geometry-wise Friedman omnibus tests among triple-complete seeds. P-values were interpreted alongside effect magnitudes and completion outcomes rather than as standalone evidence.

### 5.5 Computational-cost benchmark

Controller decision cost was measured separately from task performance. The actual controller decision functions were benchmarked on 12 deterministic state/geometry combinations. The full test suite was executed before timing; each state used 500 warm-up calls, nine timing samples, and 5,000 calls per timing sample with `perf_counter_ns`.

These timings measure controller-decision overhead only. They exclude rendering, path planning, reset execution, file I/O, HMD latency, and network latency. Structural complexity is therefore reported with the measured wall-clock results, and the timing values are interpreted only as relative costs under the common runner.

## 6. RDW Results

### 6.1 Completion behavior

Completion varied by both controller and geometry. Across the four geometries, Vis.-Poly completed 384/400 runs, S2C 378/400, and P2R 381/400. The difficult R1-G03 geometry produced the clearest robustness separation: Vis.-Poly completed 94/100 runs, S2C 86/100, and P2R 81/100. In contrast, G01 produced 92/100 completion for Vis.-Poly and 100/100 for both S2C and P2R; G02 produced 99/100, 97/100, and 100/100, respectively; and G04 produced 99/100, 95/100, and 100/100.

Paired completion tests show that the same controller is not uniformly most robust. In G01, Vis.-Poly had significantly worse completion than both S2C and P2R (exact paired p=0.007812 for each comparison). In G03, Vis.-Poly had significantly better completion than P2R (p=0.010622), whereas its completion difference from S2C was not significant at conventional levels (p=0.115318). Other pairwise completion differences were not statistically compelling after exact paired testing.

### 6.2 Reset burden among completed pairs

Reset burden also changed with geometry. In G01, S2C had the lowest complete-pair burden, followed by P2R and then Vis.-Poly. The mean paired Vis.-Poly minus S2C difference was 2.643 resets/100 m (95% bootstrap CI 2.258 to 3.025), and Vis.-Poly minus P2R was 1.395 (1.033 to 1.760). S2C minus P2R was -1.272 (-1.532 to -1.021), confirming the same ordering.

G02 showed a different pattern. S2C was lower than both comparators: Vis.-Poly minus S2C was 0.680 (0.334 to 1.011), while S2C minus P2R was -0.834 (-1.230 to -0.434). Vis.-Poly and P2R were not distinguishable on complete-pair burden, with a mean difference of -0.180 and a confidence interval spanning zero (-0.575 to 0.204).

G03 reversed the G01 ordering. Vis.-Poly had lower reset burden than both S2C and P2R on complete pairs: Vis.-Poly minus S2C was -1.004 (-1.588 to -0.417), and Vis.-Poly minus P2R was -0.742 (-1.345 to -0.136). S2C and P2R were not distinguishable, with a mean difference of 0.162 (-0.452 to 0.788). Thus the geometry that most reduced completion also changed the burden ranking.

In G04, S2C again had the lowest reset burden. S2C minus P2R was -0.726 (-1.134 to -0.324), while Vis.-Poly minus S2C was 0.572 (0.190 to 0.963). Vis.-Poly and P2R were again not clearly separated, with a mean difference of -0.210 (-0.591 to 0.168).

### 6.3 Confirmatory inference

The multiplicity-adjusted Wilcoxon analysis supports the descriptive regime pattern. All three G01 pairwise burden differences remained significant after Holm correction. In G02, S2C differed from both Vis.-Poly and P2R after Holm correction, whereas Vis.-Poly versus P2R did not. In G03, Vis.-Poly versus S2C remained significant after Holm correction (Holm-adjusted p=0.00945); Vis.-Poly versus P2R was significant under Benjamini-Hochberg control but not Holm family-wise correction (BH p=0.02772; Holm p=0.09795); and S2C versus P2R was not significant. In G04, S2C versus P2R remained significant after Holm correction, while the two Vis.-Poly contrasts did not.

Friedman omnibus tests among triple-complete seeds detected controller differences in every geometry: G01 χ²=100.78, p=1.31×10^-22; G02 χ²=14.68, p=0.000648; G03 χ²=6.06, p=0.0483; and G04 χ²=9.53, p=0.00852. G03 was therefore the weakest omnibus separation but still crossed the nominal 0.05 threshold.

Taken together, the completion and reset analyses do not support a universal controller ranking. Geometry changes both the performance ordering and the robustness profile. The strongest controlled evidence is therefore a controller-by-geometry regime effect, not a claim that one controller is globally best.

### 6.4 Computational cost

The common-runner microbenchmark showed substantial differences in controller-decision overhead. The median of the 12 per-state medians was 251.448 microseconds for Vis.-Poly, 2.022 microseconds for S2C, and 3.938 microseconds for P2R. On this runner, Vis.-Poly was approximately 124.4× slower than S2C and 63.9× slower than P2R, while P2R was approximately 1.95× slower than S2C.

The structural analysis explains the broad direction of this difference. S2C is O(P) in the current implementation because the tracking center is recomputed from P physical segments at each decision, although this could become O(1) for static geometry if cached. P2R is O(P) because repulsive contributions are accumulated across physical segments. Vis.-Poly is dominated by physical and virtual visibility-polygon construction plus slice construction and matching, so its exact asymptotic cost depends on polygon complexity and the visibility implementation.

These measurements are not end-to-end frame times and do not establish device-independent real-time guarantees. They show that the controller choice can introduce a nontrivial computational-overhead dimension that should be considered together with completion and reset burden.

## 9. Threats to Validity

The review and case study have several distinct validity boundaries. First, the systematic-review corpus is not yet frozen. The current verified bibliography and staged full-text decisions are sufficient for drafting stable methodological sections, but final PRISMA counts, final included-study totals, and prevalence claims must wait for completion of all canonical full-text decisions, formal-source execution, study-family resolution, and citation-chasing closure.

Second, broad VR evidence is heterogeneous. Hardware, tracking volume, interaction method, task, virtual environment, population, exposure duration, questionnaires, objective measures, and statistical procedures vary across studies. The comparability framework reduces the risk of invalid numerical synthesis, but it cannot eliminate publication bias or missing methodological detail in the primary literature.

Third, study-family dependence can inflate apparent evidence volume when reviews, toolkits, follow-up analyses, and empirical studies stem from closely related projects. Family resolution is therefore part of the corpus freeze, but residual dependence may remain when publications do not clearly disclose lineage.

Fourth, the RDW benchmark is simulation-based and uses four selected physical geometries under a common runner. The observed controller-by-geometry interaction is internally interpretable because seeds, paths, reset policy, and evaluation rules are paired, but it does not imply the same ordering for all room layouts, path distributions, walking behavior, HMDs, or live-user conditions. Simulator-to-user transfer remains an external-validity question even where prior work supports simulation as a useful evaluation tool.

Fifth, controller fidelity is asymmetric. Vis.-Poly, S2C, and P2R are executable under the common benchmark, whereas APF-S2T was withheld from numerical comparison because the exact discretization needed for a faithful reconstruction was unresolved. This conservative admission rule reduces implementation-speculation risk but narrows the executable comparator set.

Sixth, wall-clock microbenchmarks depend on software and hardware. The N09 timings quantify relative decision overhead under one common runner and are accompanied by structural-complexity analysis; they should not be interpreted as universal latency values.

Finally, the pre-inference artifact audit revealed that earlier manuscript-facing N02 and N05 summaries disagreed with the immutable workflow artifacts. The analysis was corrected before confirmatory inference and the discrepancy was preserved in provenance. This episode strengthens the case for raw-artifact checking, but it also demonstrates that reproducibility pipelines require continuous internal consistency audits rather than assuming that a generated summary is automatically authoritative.

## 10. Reproducibility and Data/Code Availability

The project repository is organized so that manuscript claims can be traced to machine-readable evidence, analysis outputs, and provenance records. The review pipeline retains the master bibliography, citation-use ledger, screening and full-text tables, study-family mappings, citation-chasing register, workstream coverage audits, contradiction/comparability maps, and dated pipeline snapshots.

The RDW case study retains executable controller code, benchmark logic, algorithm specifications, workflow provenance, raw-artifact audit records, corrected descriptive tables, paired-effect files, completion-discordance files, confirmatory statistical outputs, and computational-cost results. The principal N07 paired bootstrap used 10,000 deterministic resamples with seed 2601, while controller timing used deterministic state/geometry combinations and a fixed measurement protocol.

For the three controller families, the authoritative post-forensic completion data are derived from original GitHub Actions artifacts and job logs rather than from superseded manuscript summaries. The correction record identifies the relevant workflow and artifact identifiers and preserves the historical inconsistency. This provenance rule is deliberate: a reproducibility record should show how a correction was obtained, not merely replace the earlier result.

Machine-readable tables and figure-source files are kept separate from prose so that manuscript values can be regenerated rather than manually re-entered. Likewise, failed RDW runs remain explicit outcomes, and no synthetic reset value is inserted to force complete numerical matrices.

Open code and stored artifacts improve executability, but they are not treated as proof of independent reproducibility. Independent reproduction would require a separate execution or validation under sufficiently documented conditions. The repository therefore distinguishes code availability, protocol completeness, deterministic regeneration, and independent reproduction as separate evidence states.

At the current manuscript stage, Sections 1–3 and 5–6 and 9–10 are draftable from frozen evidence. Final Abstract, final contribution claims, Discussion headline, Conclusion, final PRISMA flow, and any C4/C5 novelty claim remain gated by corpus closure and the N10 novelty decision.
