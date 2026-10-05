import tempfile
from n04_s2c_full import write
def test_n04_full_driver_small_gate():
 with tempfile.TemporaryDirectory() as d:
  rows,sums,failures=write(d,seed_start=901,seed_count=2,target_m=20)
  assert len(rows)==8 and len(sums)==4 and failures==[]
  assert all(r["status"]=="complete" and r["controller"]=="S2C" for r in rows)
  assert all(s["n_total"]==2 and s["n_complete"]==2 for s in sums)
