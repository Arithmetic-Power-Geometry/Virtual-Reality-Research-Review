# Algorithm A01 — R1 Navigation-Aware Paired Benchmark Path

**Status:** validated benchmark algorithm; not a published-controller reproduction.

**Input:** virtual boundary/obstacle segments V; seed s; target path length L; clearance c; grid spacing h.

1. Construct candidate navigation nodes on an h-spaced grid inset by clearance c.
2. Remove nodes that violate the declared virtual-space clearance.
3. Connect neighboring nodes only when the entire connecting segment is collision-free.
4. Initialize the route at the valid node nearest the declared common virtual start.
5. Seed the deterministic random generator with s.
6. Randomly permute candidate target nodes and select a reachable target with shortest-path length >= 2 m.
7. Append the deterministic shortest path to the route.
8. Repeat Steps 6-7 until cumulative virtual length >= L.
9. For each consecutive route edge, rotate the virtual heading to the edge bearing, then walk the edge.
10. Reuse the identical virtual route for every physical-geometry condition associated with seed s.
11. Record seed, target/actual length, clearance, spacing, node count, path-family label, and output hashes.

**Invariants:** deterministic by seed; collision-free virtual segments; paired reuse across physical scenes; no silent clipping; explicit distinction from R2/R3 reproduction.
