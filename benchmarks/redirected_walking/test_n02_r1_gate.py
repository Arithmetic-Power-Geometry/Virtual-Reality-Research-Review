from r1_geometry_sensitivity import run,experiment,summarize
from rdw_motion import turning_step

def test_r1_rotation_uses_virtual_over_physical_gain():
    assert abs(turning_step(0.0,1.0,0.5)-2.0)<1e-12
    assert abs(turning_step(0.0,1.0,2.0)-0.5)<1e-12

def test_r1_paired_design_shape_and_common_seed_scene_grid():
    rows=experiment(seeds=range(121,124),waypoints=2)
    assert len(rows)==12
    assert {(r["seed"],r["scene_id"]) for r in rows}=={(s,g) for s in range(121,124) for g in ("R1-G01","R1-G02","R1-G03","R1-G04")}

def test_summary_never_hides_noncomplete_runs():
    rows=[
      {"scene_id":"R1-G01","status":"complete","resets_per_100m":1.0,"distance_m":100},
      {"scene_id":"R1-G01","status":"reset_cap","resets_per_100m":10.0,"distance_m":50},
    ]
    # Add one complete row for each other scene so summarize can process all registered scenes.
    for g in ("R1-G02","R1-G03","R1-G04"):
        rows.append({"scene_id":g,"status":"complete","resets_per_100m":2.0,"distance_m":100})
    s={x["scene_id"]:x for x in summarize(rows)}
    assert s["R1-G01"]["n_total"]==2
    assert s["R1-G01"]["n_complete"]==1
    assert s["R1-G01"]["completion_rate"]==0.5
    assert '"reset_cap": 1' in s["R1-G01"]["status_counts"]
