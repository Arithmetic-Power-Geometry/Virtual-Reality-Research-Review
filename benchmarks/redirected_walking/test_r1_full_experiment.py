import json
from r1_full_experiment import write
def test_full_driver_preflight(tmp_path):
 rows,sums=write(str(tmp_path),range(901,903),20.0)
 assert len(rows)==8 and len(sums)==4
 assert all(r["status"]=="complete" for r in rows)
 assert (tmp_path/"runs.csv").exists()
 assert (tmp_path/"summary.csv").exists()
 assert (tmp_path/"manifest.json").exists()
 assert (tmp_path/"SHA256SUMS.json").exists()
 m=json.loads((tmp_path/"manifest.json").read_text())
 assert m["paired_design"] is True and m["common_virtual_path_per_seed"] is True
