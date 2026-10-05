from r1_geometry_sensitivity import experiment
def test_common_navigation_path_gate_shape():
 rows=experiment(seeds=range(121,124),target_m=10)
 assert len(rows)==12
 assert {(r["seed"],r["scene_id"]) for r in rows}=={(s,g) for s in range(121,124) for g in ("R1-G01","R1-G02","R1-G03","R1-G04")}
def test_short_navigation_gate_has_no_reset_cap():
 rows=experiment(seeds=range(121,124),target_m=10)
 assert all(r["status"]!="reset_cap" for r in rows)
