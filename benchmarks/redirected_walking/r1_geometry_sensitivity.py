"""Paired R1 geometry-sensitivity experiment for the Vis.-Poly reproduction candidate."""
from __future__ import annotations
import csv, hashlib, json, math, os, statistics
from geometry2d import rectangle_segments, nearest_segment_clearance
from vispoly_sim import State, needs_reset, step_walk
from arc_reset_execute import execute_arc_reset
from waypoint_paths import generate_relative_waypoints, timed_motion
from rdw_motion import turning_step

def scenes():
    return {
      "R1-G01": rectangle_segments(10,10),
      "R1-G02": rectangle_segments(10,10)+[((4,1),(4,6))],
      "R1-G03": rectangle_segments(10,10)+[((4,1),(4,6)),((6,4),(6,9))],
      "R1-G04": rectangle_segments(12,8)+[((6,2),(6,6))],
    }

def virtual_scene(): return rectangle_segments(14,14)

def start_for(scene_id):
    # Same valid physical start across all substitute geometries preserves pairing.
    return (2,2,0)

def run(seed,scene_id,waypoints=8,max_resets=100,diagnostics=None):
    p=scenes()[scene_id]; v=virtual_scene(); x,y,h=start_for(scene_id)
    s=State(x,y,h,7,7,0,0); distance=0.; steps=0; reset_armed=True
    for waypoint_index,(d,turn) in enumerate(generate_relative_waypoints(seed,waypoints)):
        walks,turns=timed_motion(d,turn)
        # Azmandian/RDWT path semantics: WALK THEN TURN. The sampled rotation
        # changes the forward direction for the following segment.
        for dv in walks:
            in_trigger=needs_reset(s,p)
            if reset_armed and in_trigger:
                if s.resets>=max_resets: return row(seed,scene_id,s,distance,steps,"reset_cap")
                s,_=execute_arc_reset(s,p,v)
                reset_armed=False
            elif not in_trigger:
                reset_armed=True
            try:
                s,_=step_walk(s,dv,p,v)
            except ValueError as e:
                return failure_row(seed,scene_id,s,distance,steps,"geometry_failure",waypoint_index,"walk",str(e),p,v,diagnostics)
            distance+=dv; steps+=1
        for tv in turns:
            try:
                _,gr,_,_=__import__("vispoly_sim").controller_gains(s,p,v,1 if tv>=0 else -1)
            except ValueError as e:
                return failure_row(seed,scene_id,s,distance,steps,"controller_failure",waypoint_index,"turn",str(e),p,v,diagnostics)
            s.ph=turning_step(s.ph,tv,gr); s.vh+=tv; steps+=1
    return row(seed,scene_id,s,distance,steps,"complete")


def failure_row(seed,scene_id,s,distance,steps,status,waypoint_index,phase,reason,p,v,diagnostics):
    pd,_,_=nearest_segment_clearance((s.px,s.py),p)
    vd,_,_=nearest_segment_clearance((s.vx,s.vy),v)
    detail={"seed":seed,"scene_id":scene_id,"status":status,"waypoint_index":waypoint_index,
            "phase":phase,"reason":reason,"steps":steps,"distance_m":distance,"resets":s.resets,
            "px":s.px,"py":s.py,"ph":s.ph,"vx":s.vx,"vy":s.vy,"vh":s.vh,
            "physical_clearance_m":pd,"virtual_clearance_m":vd}
    if diagnostics is not None: diagnostics.append(detail)
    return row(seed,scene_id,s,distance,steps,status)

def row(seed,scene_id,s,distance,steps,status):
    return {"seed":seed,"scene_id":scene_id,"resets":s.resets,"distance_m":distance,"steps":steps,"status":status,
            "resets_per_100m":(100*s.resets/distance if distance else None)}

def experiment(seeds=range(121,131),waypoints=8,diagnostics=None):
    return [run(seed,sid,waypoints,diagnostics=diagnostics) for seed in seeds for sid in scenes()]

def summarize(rows):
    out=[]
    for sid in scenes():
        allx=[r for r in rows if r["scene_id"]==sid]
        complete=[r for r in allx if r["status"]=="complete"]
        rates=[r["resets_per_100m"] for r in complete]
        status_counts={s:sum(r["status"]==s for r in allx) for s in sorted({r["status"] for r in allx})}
        out.append({"scene_id":sid,"n_total":len(allx),"n_complete":len(complete),
                    "completion_rate":len(complete)/len(allx) if allx else 0.0,
                    "mean_resets_per_100m_complete":statistics.mean(rates) if rates else None,
                    "sd_resets_per_100m_complete":statistics.stdev(rates) if len(rates)>1 else 0.0,
                    "total_distance_m_all":sum(r["distance_m"] for r in allx),
                    "status_counts":json.dumps(status_counts,sort_keys=True)})
    return out

def write(outdir):
    os.makedirs(outdir,exist_ok=True); diagnostics=[]; rows=experiment(diagnostics=diagnostics); sums=summarize(rows)
    files=[]
    for name,data,fields in [
      ("r1_geometry_runs.csv",rows,["seed","scene_id","resets","distance_m","steps","status","resets_per_100m"]),
      ("r1_geometry_summary.csv",sums,["scene_id","n_total","n_complete","completion_rate","mean_resets_per_100m_complete","sd_resets_per_100m_complete","total_distance_m_all","status_counts"])]:
        p=os.path.join(outdir,name); files.append(p)
        with open(p,"w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(data)
    dp=os.path.join(outdir,"r1_failures.json"); files.append(dp)
    with open(dp,"w") as f: json.dump(diagnostics,f,indent=2,sort_keys=True)
    manifest={"seeds":[121,122,123,124,125,126,127,128,129,130],"waypoints_per_seed":8,
              "paired_design":True,"scenes":list(scenes()),"common_physical_start":[2,2,0],"interpretation":"R1 protocol-compatible short geometry sensitivity; not published-scale and not direct numerical replication"}
    mp=os.path.join(outdir,"r1_manifest.json"); files.append(mp)
    with open(mp,"w") as f: json.dump(manifest,f,indent=2,sort_keys=True)
    hashes={os.path.basename(p):hashlib.sha256(open(p,"rb").read()).hexdigest() for p in files}
    hp=os.path.join(outdir,"SHA256SUMS.json")
    with open(hp,"w") as f: json.dump(hashes,f,indent=2,sort_keys=True)
    return rows,sums

if __name__=="__main__":
    _,s=write("artifacts/r1_geometry_sensitivity")
    print(json.dumps(s,sort_keys=True))
