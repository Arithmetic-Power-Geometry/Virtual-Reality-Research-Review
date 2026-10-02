import json
from pathlib import Path
from rdw_benchmark import trajectory, run

CFG=json.loads((Path(__file__).parent/"config.json").read_text())

def test_trajectory_deterministic():
    assert trajectory(CFG,121)==trajectory(CFG,121)

def test_trajectory_seed_changes():
    assert trajectory(CFG,121)!=trajectory(CFG,122)

def test_run_deterministic():
    s=CFG["spaces"][0]
    assert run(CFG,s,"none",121)==run(CFG,s,"none",121)

def test_all_baselines_return_metrics():
    s=CFG["spaces"][0]
    for c in CFG["controllers"]:
        r=run(CFG,s,c,121)
        assert r["resets"] >= 0
        assert r["physical_distance_m"] > 0
        assert r["virtual_distance_m"] > 0
