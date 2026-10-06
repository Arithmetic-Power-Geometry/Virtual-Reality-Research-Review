"""N02-FULL: long paired R1 geometry-sensitivity experiment."""
from __future__ import annotations
import argparse,csv,hashlib,json,os,statistics,time
from r1_geometry_sensitivity import experiment,scenes

def ci95(xs):
 if len(xs)<2:return None
 return 1.96*statistics.stdev(xs)/(len(xs)**0.5)

def summarize(rows):
 out=[]
 for sid in scenes():
  allx=[r for r in rows if r["scene_id"]==sid]; ok=[r for r in allx if r["status"]=="complete"]
  rates=[r["resets_per_100m"] for r in ok]
  out.append({"scene_id":sid,"n_total":len(allx),"n_complete":len(ok),
   "completion_rate":len(ok)/len(allx),"mean_resets_per_100m":statistics.mean(rates) if rates else None,
   "sd_resets_per_100m":statistics.stdev(rates) if len(rates)>1 else 0.0,
   "ci95_halfwidth":ci95(rates),"median_resets_per_100m":statistics.median(rates) if rates else None,
   "min_resets_per_100m":min(rates) if rates else None,"max_resets_per_100m":max(rates) if rates else None,
   "total_distance_m":sum(r["distance_m"] for r in allx),
   "status_counts":json.dumps({z:sum(r["status"]==z for r in allx) for z in sorted({r["status"] for r in allx})},sort_keys=True)})
 return out

def write(outdir,seeds,target_m):
 os.makedirs(outdir,exist_ok=True);diag=[];t0=time.time();rows=experiment(seeds=seeds,target_m=target_m,diagnostics=diag);elapsed=time.time()-t0
 sums=summarize(rows); specs=[("runs.csv",rows,list(rows[0])),("summary.csv",sums,list(sums[0]))]; files=[]
 for name,data,fields in specs:
  p=os.path.join(outdir,name);files.append(p)
  with open(p,"w",newline="") as fh:w=csv.DictWriter(fh,fieldnames=fields);w.writeheader();w.writerows(data)
 for name,obj in [("failures.json",diag),("manifest.json",{"seeds":list(seeds),"seed_count":len(seeds),"scene_count":len(scenes()),
  "target_virtual_distance_m":target_m,"expected_runs":len(seeds)*len(scenes()),"paired_design":True,
  "path_family":"navigation-aware-clearance-grid","common_virtual_path_per_seed":True,
  "common_physical_start":[2,2,0],"elapsed_seconds":elapsed,
  "claim_boundary":"R1 declared benchmark; not R2/R3 direct reproduction"})]:
  p=os.path.join(outdir,name);files.append(p)
  with open(p,"w") as fh:json.dump(obj,fh,indent=2,sort_keys=True)
 hashes={os.path.basename(p):hashlib.sha256(open(p,"rb").read()).hexdigest() for p in files}
 with open(os.path.join(outdir,"SHA256SUMS.json"),"w") as fh:json.dump(hashes,fh,indent=2,sort_keys=True)
 return rows,sums

if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("--seed-start",type=int,default=1001);ap.add_argument("--seed-count",type=int,default=100)
 ap.add_argument("--target-m",type=float,default=350.0);ap.add_argument("--outdir",default="artifacts/r1_full")
 a=ap.parse_args(); rows,sums=write(a.outdir,range(a.seed_start,a.seed_start+a.seed_count),a.target_m)
 print(json.dumps({"runs":len(rows),"complete":sum(r["status"]=="complete" for r in rows),"summary":sums},sort_keys=True))
