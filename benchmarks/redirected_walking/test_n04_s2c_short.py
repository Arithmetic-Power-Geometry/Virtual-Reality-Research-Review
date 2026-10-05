from n04_s2c_short import experiment
def test_n04_short_complete_and_paired():
 rows=experiment(seeds=range(121,123),target_m=10)
 assert len(rows)==16
 assert all(r["status"]=="complete" for r in rows)
 for seed in range(121,123):
  for sid in ("R1-G01","R1-G02","R1-G03","R1-G04"):
   x=[r for r in rows if r["seed"]==seed and r["scene_id"]==sid]
   assert {r["controller"] for r in x}=={"Vis-Poly","S2C"}
   assert abs(x[0]["distance_m"]-x[1]["distance_m"])<1e-9
