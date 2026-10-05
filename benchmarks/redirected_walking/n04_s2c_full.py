"""N04-FULL S2C-only paired experiment.

Runs the already validated S2C policy on the exact N02-FULL seed/scene/path
design. Vis.-Poly is not recomputed; comparison is against the frozen N02 data.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,os,statistics
from n04_s2c_short import run_s2c
from r1_geometry_sensitivity import scenes

def experiment(seed_start=1001,seed_count=100,target_m=350.):
 return [dict(run_s2c(seed,sid,target_m),controller="S2C")
         for seed in range(seed_start,seed_start+seed_count) for sid in scenes()]

def write(outdir,seed_start=1001,seed_count=100,target_m=350.):
 os.makedirs(outdir,exist_ok=True);rows=experiment(seed_start,seed_count,target_m)
 expected=seed_count*len(scenes())
 if len(rows)!=expected: raise RuntimeError(f"expected {expected} rows got {len(rows)}")
 failures=[r for r in rows if r["status"]!="complete"]
 sums=[]
 for sid in scenes():
  x=[r for r in rows if r["scene_id"]==sid];ok=[r for r in x if r["status"]=="complete"]
  rates=[r["resets_per_100m"] for r in ok]
  sums.append({"controller":"S2C","scene_id":sid,"n_total":len(x),"n_complete":len(ok),
   "completion_rate":len(ok)/len(x),"mean_resets_per_100m":statistics.mean(rates) if rates else None,
   "sd_resets_per_100m":statistics.stdev(rates) if len(rates)>1 else 0.,
   "median_resets_per_100m":statistics.median(rates) if rates else None,
   "total_distance_m":sum(r["distance_m"] for r in x)})
 for name,data in (("runs.csv",rows),("summary.csv",sums)):
  with open(os.path.join(outdir,name),"w",newline="") as f:
   w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
 with open(os.path.join(outdir,"failures.json"),"w") as f:json.dump(failures,f,indent=2,sort_keys=True)
 manifest={"controller":"S2C","seed_start":seed_start,"seed_count":seed_count,"scene_count":len(scenes()),
 "expected_runs":expected,"target_virtual_distance_m":target_m,"paired_against":"N02-FULL frozen Vis-Poly",
 "paired_design":True,"common_virtual_path_per_seed":True,
 "claim_boundary":"N04 comparator benchmark; no global controller-superiority claim"}
 with open(os.path.join(outdir,"manifest.json"),"w") as f:json.dump(manifest,f,indent=2,sort_keys=True)
 names=["runs.csv","summary.csv","failures.json","manifest.json"]
 hashes={n:hashlib.sha256(open(os.path.join(outdir,n),"rb").read()).hexdigest() for n in names}
 with open(os.path.join(outdir,"SHA256SUMS.json"),"w") as f:json.dump(hashes,f,indent=2,sort_keys=True)
 return rows,sums,failures

if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--seed-start",type=int,default=1001);p.add_argument("--seed-count",type=int,default=100)
 p.add_argument("--target-m",type=float,default=350.);p.add_argument("--outdir",default="artifacts/n04_s2c_full");a=p.parse_args()
 rows,sums,failures=write(a.outdir,a.seed_start,a.seed_count,a.target_m)
 print(json.dumps({"runs":len(rows),"failures":len(failures),"summary":sums},sort_keys=True))
