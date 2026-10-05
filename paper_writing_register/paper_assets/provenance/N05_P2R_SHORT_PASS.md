# N05 P2R Short Gate — PASS

Workflow: 37325636693
Head SHA: a220ef3c949ec1e57d29f639567181f1a594188b
Artifact ID: 11352710378
Artifact digest: sha256:d4a4f6a34741088b342d85eb6bc302670dd61631987fd5b01b1a62972bd08fad

Design: 10 seeds x 4 geometries = 40 P2R runs under the common R1 path/reset/safety benchmark.
Result: 40/40 complete.

Diagnostic mean resets/100m:
G01 8.3474
G02 13.9852
G03 24.2788
G04 19.3866

Claim boundary: implementation/short-gate evidence only. These values are not admitted as manuscript performance claims. Full 100-seed x 350m gate is required.

Comparability boundary: published P2R steering policy with analytic gradient of its stated repulsive potential, but common ARC reset and R1 navigation paths. Not a numerical reproduction of Thomas & Suma Rosenberg 2019.
