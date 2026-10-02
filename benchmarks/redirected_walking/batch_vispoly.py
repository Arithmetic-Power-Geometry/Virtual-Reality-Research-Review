"""Seeded multi-path Vis.-Poly experiment harness.

Produces machine-readable regression artifacts. Results are reproduction
candidates until externally checked against the primary paper.
"""
from __future__ import annotations
import csv, hashlib, json, math, os
from geometry2d import rectangle_segments
from vispoly_sim import State, needs_reset, step_walk
from arc_reset_execute import execute_arc_reset
from waypoint_paths import generate_relative_waypoints, timed_motion

def obstacle_scene():
    # 10x10 boundary plus two interior walls; deterministic polygonal segment scene.
    return rectangle_segments(10,10)+[((4,1),(4,6)),((6,4),(6,9))]

def virtual_scene():
    return rectangle_segments(14,14)

def run_path(seed:int,waypoints:int=8,max_resets:int=100):
    p=obstacle_scene(); v=virtual_scene()
    s=State(2,2,0,7,7,0,0)
    distance=0.0; steps=0
    for d,turn in generate_relative_waypoints(seed,waypoints):
        walks,turns=timed_motion(d,turn)
        # virtual turn: endpoint update; physical rotation uses current controller rotation gain
        for tv in turns:
            try:
                _,gr,_,_=__import__("vispoly_sim").controller_gains(s,p,v,1 if tv>=0 else -1)
            except ValueError:
                gr=1.0
            s.ph += tv*gr; s.vh += tv; steps+=1
        for dv in walks:
            if needs_reset(s,p):
                if s.resets>=max_resets: return {"seed":seed,"resets":s.resets,"distance_m":distance,"steps":steps,"status":"reset_cap"}
                s,_=execute_arc_reset(s,p,v)
            try:
                s,_=step_walk(s,dv,p,v)
            except ValueError:
                return {"seed":seed,"resets":s.resets,"distance_m":distance,"steps":steps,"status":"geometry_failure"}
            distance+=dv; steps+=1
    return {"seed":seed,"resets":s.resets,"distance_m":distance,"steps":steps,"status":"complete"}

def run_batch(seeds=range(121,131),waypoints:int=8):
    return [run_path(s,waypoints) for s in seeds]

def write_artifacts(outdir:str):
    os.makedirs(outdir,exist_ok=True)
    rows=run_batch()
    csvp=os.path.join(outdir,"vispoly_batch.csv")
    with open(csvp,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["seed","resets","distance_m","steps","status"]); w.writeheader(); w.writerows(rows)
    complete=[r for r in rows if r["status"]=="complete"]
    summary={"runs":len(rows),"complete":len(complete),"total_resets":sum(r["resets"] for r in complete),"total_distance_m":sum(r["distance_m"] for r in complete)}
    summary["resets_per_100m"]=100*summary["total_resets"]/summary["total_distance_m"] if summary["total_distance_m"] else None
    jp=os.path.join(outdir,"vispoly_batch_summary.json")
    with open(jp,"w") as f: json.dump(summary,f,indent=2,sort_keys=True)
    hashes={}
    for p in (csvp,jp):
        hashes[os.path.basename(p)]=hashlib.sha256(open(p,"rb").read()).hexdigest()
    with open(os.path.join(outdir,"SHA256SUMS.json"),"w") as f: json.dump(hashes,f,indent=2,sort_keys=True)
    return rows,summary

if __name__=="__main__":
    _,s=write_artifacts("artifacts/rdw_batch")
    print(json.dumps(s,sort_keys=True))
