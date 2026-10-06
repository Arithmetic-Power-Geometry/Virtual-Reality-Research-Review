# IEEE Final Submission Package — 6 October 2026

**Paper:** Virtual Reality Research: A Systematic Review of Methods, Algorithms, Evaluation, and Open Research Problems

This folder freezes the repository-side evidence/code bundle used by the final IEEE LaTeX package.

## Frozen paper state

- 174 verified bibliography records
- 173 canonical reports
- 171 reports retrieved and assessed
- 165 direct eligible VR/XR reports
- 6 supporting/context reports
- 2 reports not retrieved
- 0 unassessed canonical reports
- N10: no new RDW-controller novelty claim
- N13/N14/N15: closed
- N16: release freeze passed with the documented historical raw-database-yield limitation

## Quantitative policy

Only corrected N07--N09 artifacts are authoritative for the final RDW claims. Earlier pre-forensic N02/N05 summaries and the stale N05 three-controller figure source must not be used where they conflict with N07.

## References

The verified project master contains **174 references, not 212**. No references were invented to reach a numerical quota. The final IEEE manuscript cites 65 evidence-bearing sources in prose; the complete verified 174-entry master bibliography is included here as `master_references_174.bib`.

## Research chronology represented in the paper

concept and evidence architecture -> software implementation -> versioned workflow execution -> immutable-artifact audit -> statistical analysis -> manuscript interpretation.

The repository is the code/data/provenance record supporting the research, not a manuscript-generation mechanism.

The compiled submission ZIP and PDF are supplied with the final deliverable; this repository folder preserves the exact authoritative source evidence and benchmark implementation used by that package.


## Build

From this folder:

1. Run `python make_figures.py`.
2. Run `pdflatex -interaction=nonstopmode -halt-on-error main.tex`.
3. Run the same `pdflatex` command a second time to resolve cross-references.

Required LaTeX packages are standard IEEE/TeX Live packages: `IEEEtran`, `graphicx`, `booktabs`, `array`, `multirow`, `amsmath`, `amssymb`, `algorithm`, `algpseudocode`, `float`, `microtype`, `hyperref`, `xurl`, and `balance`.

## Final mechanical audit

The compiled submission package was checked for:
- 65/65 manuscript citation keys resolving;
- every declared table, figure, and algorithm cited in prose;
- 6 tables, 4 figures, and 1 algorithm using `[H]`;
- no undefined cross-references;
- no undefined citations;
- no overfull horizontal boxes;
- corrected N07--N09 values only in final RDW tables/figures.

The complete verified 174-entry bibliography remains available as `master_references_174.bib`; the manuscript itself cites the 65 references materially used by its prose.
