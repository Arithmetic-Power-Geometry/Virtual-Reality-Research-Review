"""N03 paired analysis for a reviewer-approved N02-FULL artifact.
Standard-library only; deterministic bootstrap for paired scene differences.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,math,os,random,statistics
from itertools import combinations

def load_runs(path):
 with open(path,newline="") as fh:return list(csv.DictReader(fh))

def validate(rows):
 if not rows: raise ValueError("empty input")
 scenes=sorted({r["scene_id"] for r in rows}); seeds=sorted({int(r["seed"]) for r in rows})
 if any(r["status"]!="complete" for r in rows): raise ValueError("N03 requires complete N02-FULL runs")
 if len(rows)!=len(scenes)*len(seeds): raise ValueError("unbalanced seed x scene matrix")
 seen={(int(r["seed"]),r["scene_id"]) for r in rows}
 if len(seen)!=len(rows): raise ValueError("duplicate seed-scene row")
 for s in seeds:
  if {g for ss,g in seen if ss==s}!=set(scenes): raise ValueError("unpaired seed")
 return seeds,scenes

def quantile(xs,p):
 ys=sorted(xs); pos=(len(ys)-1)*p; lo=math.floor(pos); hi=math.ceil(pos)
 return ys[lo] if lo==hi else ys[lo]*(hi-pos)+ys[hi]*(pos-lo)

def bootstrap_ci(diffs,n=10000,seed=2601):
 rng=random.Random(seed); m=len(diffs); vals=[]
 for _ in range(n): vals.append(statistics.mean(diffs[rng.randrange(m)] for __ in range(m)))
 return quantile(vals,.025),quantile(vals,.975)

def analyze(rows):
 seeds,scenes=validate(rows); by={(int(r["seed"]),r["scene_id"]):float(r["resets_per_100m"]) for r in rows}; out=[]
 for a,b in combinations(scenes,2):
  d=[by[s,b]-by[s,a] for s in seeds]; lo,hi=bootstrap_ci(d)
  out.append({"scene_a":a,"scene_b":b,"n_pairs":len(d),"mean_difference_b_minus_a":statistics.mean(d),
   "median_difference_b_minus_a":statistics.median(d),"sd_difference":statistics.stdev(d) if len(d)>1 else 0.0,
   "bootstrap95_low":lo,"bootstrap95_high":hi,"positive_pairs":sum(x>0 for x in d),
   "negative_pairs":sum(x<0 for x in d),"ties":sum(x==0 for x in d)})
 return out

def write(infile,outdir):
 rows=load_runs(infile); out=analyze(rows);os.makedirs(outdir,exist_ok=True)
 p=os.path.join(outdir,"paired_scene_differences.csv")
 with open(p,"w",newline="") as fh:w=csv.DictWriter(fh,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
 m={"input_sha256":hashlib.sha256(open(infile,"rb").read()).hexdigest(),"bootstrap_replicates":10000,
 "bootstrap_seed":2601,"effect":"paired difference in resets_per_100m (scene_b - scene_a)",
 "claim_boundary":"descriptive/uncertainty analysis of R1 benchmark; no controller superiority claim"}
 with open(os.path.join(outdir,"analysis_manifest.json"),"w") as fh:json.dump(m,fh,indent=2,sort_keys=True)
 return out

if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("runs_csv");ap.add_argument("--outdir",default="artifacts/n03")
 a=ap.parse_args();print(json.dumps(write(a.runs_csv,a.outdir),sort_keys=True))
