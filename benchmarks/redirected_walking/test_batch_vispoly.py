import tempfile
from batch_vispoly import *

def test_batch_deterministic():
    assert run_batch(range(121,124),2)==run_batch(range(121,124),2)

def test_run_schema_and_finite_counts():
    r=run_path(121,2)
    assert set(r)=={"seed","resets","distance_m","steps","status"}
    assert r["resets"]>=0 and r["distance_m"]>=0 and r["steps"]>=0

def test_artifact_writer():
    with tempfile.TemporaryDirectory() as d:
        rows,s=write_artifacts(d)
        assert len(rows)==10 and s["runs"]==10
        import os
        assert os.path.exists(d+"/vispoly_batch.csv")
        assert os.path.exists(d+"/vispoly_batch_summary.json")
        assert os.path.exists(d+"/SHA256SUMS.json")
