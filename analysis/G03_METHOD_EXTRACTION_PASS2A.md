# G03 Method Extraction — Pass 2A

## Purpose
Convert the published-controller registry into implementation-level evidence. No code is labeled as a literature reproduction until every implementation-critical field is resolved.

## Visibility-Polygon controller
The open author manuscript provides the clearest implementation entry point currently verified.

At every frame the controller computes physical and virtual visibility polygons, partitions visible free space into slices, identifies the active virtual slice, selects the most similar physical slice, and derives redirection gains to steer toward the matched physical region.

### Implementation-ready
- frame-level control decomposition
- visibility-polygon representation
- polygon slicing concept
- physical/virtual slice-matching architecture

### Still unresolved
- exact active-slice boundary/tie behavior
- complete slice-similarity rule
- rotation, translation and curvature gain equations/thresholds
- reset trigger and reset policy
- all experimental constants

Vis.-Poly therefore remains **partial extraction**, not reproduced.

## ARC
ARC's objective is verified: align obstacle proximity in physical and virtual environments. Complexity Ratio and both simulation and headset evaluation are also verified. Exact alignment equations, gain mapping and constants still require extraction.

## Optimized Alignment/APF and APF-S2T
The 2023 and 2024 methods remain direct recent comparators. Their abstracts establish the controller concepts and comparison neighborhood but are insufficient for implementation.

## Reproduction gate
A controller receives a reproduced-from-literature status only after primary full text, equations/pseudocode, constants, gain limits, reset logic, environment/path generation, and all reconstruction deviations are documented.

## Decision
Do not code Vis.-Poly yet. Resolve its remaining gain/reset details first rather than create an approximation that could be mistaken for the published controller.

## Reproducibility lead
A public repository named pasumi cites ARC and Visibility-Polygon and provides a CMake-based experiment setup. It is recorded only as an unaudited third-party lead. Its license, provenance and implementation correspondence must be checked before reuse.
