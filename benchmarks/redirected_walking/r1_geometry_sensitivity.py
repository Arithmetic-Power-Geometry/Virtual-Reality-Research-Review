"""Paired R1 geometry-sensitivity experiment for the Vis.-Poly reproduction candidate."""
from __future__ import annotations
import csv, hashlib, json, math, os, statistics
from geometry2d import rectangle_segments
from vispoly_sim import State, needs_reset, step_walk
from arc_reset_execute import execute_arc_reset
from waypoint_paths import generate_relative_waypoints, timed_motion

def scenes():
    return {
      "R1-G01": rectangle_segments(10,10),
      "R1-G02": rectangle_segments(10,10)+[((4,1),(4,6))],
      "R1-G03": rectangle_segments(10,10)+[((4,1),(4,6)),((6,4),(6,9))],
      "R1-G04": rectangle_segments(12,8)+[((6,2),(6,6))],
    }

def virtual_scene(): return rectangle_segments(14,14)

def start_for(scene_id):
    return (2,2,0) if scene_id!="R1-G04" else (2,4,0)

def run(seed,scene_id,waypoints=8,max_resets=100):
    p=scenes()[scene_id]; v=virtual_scene(); x,y,h=start_for(scene_id)
    s=State(x,y,h,7,7,0,0); distance=0.; steps=0
    for d,turn in generate_relative_waypoints(seed,waypoints):
        walks,turns=timed_motion(d,turn)
        for tv in turns:
            try: _,gr,_,_=__import__("vispoly_sim").controller_gains(s,p,v,1 if tv>=0 else -1)
            except ValueError: gr=1.
            s.ph+=tv*gr; s.vh+=tv; steps+=1
        for dv in walks:
            if needs_reset(s,p):
                if s.resets>=max_resets: return row(seed,scene_id,s,distance,steps,"reset_cap")
                s,_=execute_arc_reset(s,p,v)
            try: s,_=step_walk(s,dv,p,v)
            except ValueError: return row(seed,scene_id,s,distance,steps,"geometry_failure")
            distance+=dv; steps+=1
    return row(seed,scene_id,s,distance,steps,"complete")

def row(seed,scene_id,s,distance,steps,status):
    return {"seed":seed,"scene_id":scene_id,"resets":s.resets,"distance_m":distance,"steps":steps,"status":status,
            "resets_per_100m":(100*s.resets/distance if distance else None)}

def experiment(seeds=range(121,131),waypoints=8):
    return [run(seed,sid,waypoints) for seed in seeds for sid in scenes()]

def summarize(rows):
    out=[]
    for sid in scenes():
        x=[r for r in rows if r["scene_id"]==sid and r["status"]=="complete"]
        rates=[r["resets_per_100m"] for r in x]
        out.append({"scene_id":sid,"n":len(x),"mean_resets_per_100m":statistics.mean(rates) if rates else None,
                    "sd_resets_per_100m":statistics.stdev(rates) if len(rates)>1 else 0.0,
                    "total_distance_m":sum(r["distance_m"] for r in x)})
    return out

def write(outdir):
    os.makedirs(outdir,exist_ok=True); rows=experiment(); sums=summarize(rows)
    files=[]
    for name,data,fields in [
      ("r1_geometry_runs.csv",rows,["seed","scene_id","resets","distance_m","steps","status","resets_per_100m"]),
      ("r1_geometry_summary.csv",sums,["scene_id","n","mean_resets_per_100m","sd_resets_per_100m","total_distance_m"])]:
        p=os.path.join(outdir,name); files.append(p)
        with open(p,"w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(data)
    manifest={"seeds":[121,122,123,124,125,126,127,128,129,130],"waypoints_per_seed":8,
              "paired_design":True,"scenes":list(scenes()),"interpretation":"R1 protocol-compatible geometry sensitivity; not direct published numerical replication"}
    mp=os.path.join(outdir,"r1_manifest.json"); files.append(mp)
    with open(mp,"w") as f: json.dump(manifest,f,indent=2,sort_keys=True)
    hashes={os.path.basename(p):hashlib.sha256(open(p,"rb").read()).hexdigest() for p in files}
    hp=os.path.join(outdir,"SHA256SUMS.json")
    with open(hp,"w") as f: json.dump(hashes,f,indent=2,sort_keys=True)
    return rows,sums

if __name__=="__main__":
    _,s=write("artifacts/r1_geometry_sensitivity")
    print(json.dumps(s,sort_keys=True))
