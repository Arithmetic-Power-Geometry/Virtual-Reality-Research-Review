import tempfile
from r1_geometry_sensitivity import *

def test_paired_design_shape():
    rows=experiment(range(121,124),2)
    assert len(rows)==12
    for seed in range(121,124):
        assert {r["scene_id"] for r in rows if r["seed"]==seed}==set(scenes())

def test_deterministic():
    assert experiment(range(121,123),2)==experiment(range(121,123),2)

def test_summary_has_all_scenes():
    s=summarize(experiment(range(121,124),2))
    assert {x["scene_id"] for x in s}==set(scenes())

def test_artifacts():
    with tempfile.TemporaryDirectory() as d:
        write(d)
        import os
        for n in ("r1_geometry_runs.csv","r1_geometry_summary.csv","r1_manifest.json","SHA256SUMS.json"):
            assert os.path.exists(os.path.join(d,n))
