"""Short paired R1 geometry-sensitivity gate using declared navigation-aware paths."""
from __future__ import annotations
import csv,hashlib,json,math,os,statistics
from geometry2d import rectangle_segments,nearest_segment_clearance
from vispoly_sim import State,needs_reset,step_walk,controller_gains,swept_segment_safe
from arc_reset_execute import execute_arc_reset
from waypoint_paths import timed_motion
from rdw_motion import turning_step
from r1_navigation_paths import generate_navigation_path

def scenes():
 return {"R1-G01":rectangle_segments(10,10),
 "R1-G02":rectangle_segments(10,10)+[((4,1),(4,6))],
 "R1-G03":rectangle_segments(10,10)+[((4,1),(4,6)),((6,4),(6,9))],
 "R1-G04":rectangle_segments(12,8)+[((6,2),(6,6))]}
def virtual_scene(): return rectangle_segments(14,14)
def start_for(_): return (2,2,0)

def row(seed,sid,s,distance,steps,status):
 return {"seed":seed,"scene_id":sid,"resets":s.resets,"distance_m":distance,"steps":steps,"status":status,
 "resets_per_100m":100*s.resets/distance if distance else None}
def failure(seed,sid,s,distance,steps,status,idx,phase,reason,p,v,diag):
 pd,_,_=nearest_segment_clearance((s.px,s.py),p); vd,_,_=nearest_segment_clearance((s.vx,s.vy),v)
 d={"seed":seed,"scene_id":sid,"status":status,"route_segment":idx,"phase":phase,"reason":reason,
 "steps":steps,"distance_m":distance,"resets":s.resets,"px":s.px,"py":s.py,"ph":s.ph,
 "vx":s.vx,"vy":s.vy,"vh":s.vh,"physical_clearance_m":pd,"virtual_clearance_m":vd}
 if diag is not None: diag.append(d)
 return row(seed,sid,s,distance,steps,status)

def run(seed,sid,target_m=35.0,max_resets=100,diagnostics=None):
 p=scenes()[sid]; v=virtual_scene(); x,y,h=start_for(sid); s=State(x,y,h,7.5,7.5,0,0)
 route,_=generate_navigation_path(seed,v,target_m=target_m,start=(7.5,7.5))
 distance=0.; steps=0; reset_armed=True; vh=0.
 for idx in range(len(route)-1):
  a,b=route[idx],route[idx+1]; d=math.dist(a,b); desired=math.atan2(b[1]-a[1],b[0]-a[0])
  turn=((desired-vh+math.pi)%(2*math.pi))-math.pi
  walks,turns=timed_motion(d,turn)
  for dv in walks:
   trig=needs_reset(s,p)
   if reset_armed and trig:
    if s.resets>=max_resets:return row(seed,sid,s,distance,steps,"reset_cap")
    s,_=execute_arc_reset(s,p,v); reset_armed=False
   elif not trig: reset_armed=True
   try:
    candidate,_=step_walk(s,dv,p,v)
    if not swept_segment_safe((s.px,s.py),(candidate.px,candidate.py),p,0.2):
     if s.resets>=max_resets:return row(seed,sid,s,distance,steps,"reset_cap")
     s,_=execute_arc_reset(s,p,v); reset_armed=False
     candidate,_=step_walk(s,dv,p,v)
     if not swept_segment_safe((s.px,s.py),(candidate.px,candidate.py),p,0.2):
      return failure(seed,sid,s,distance,steps,"geometry_failure",idx,"swept_walk","unsafe after reset",p,v,diagnostics)
    s=candidate
   except ValueError as e:return failure(seed,sid,s,distance,steps,"geometry_failure",idx,"walk",str(e),p,v,diagnostics)
   distance+=dv;steps+=1
  for tv in turns:
   try:_,gr,_,_=controller_gains(s,p,v,1 if tv>=0 else -1)
   except ValueError as e:return failure(seed,sid,s,distance,steps,"controller_failure",idx,"turn",str(e),p,v,diagnostics)
   s.ph=turning_step(s.ph,tv,gr);s.vh+=tv;steps+=1
  vh=desired
 return row(seed,sid,s,distance,steps,"complete")

def experiment(seeds=range(121,131),target_m=35.,diagnostics=None):
 return [run(seed,sid,target_m,diagnostics=diagnostics) for seed in seeds for sid in scenes()]
def summarize(rows):
 out=[]
 for sid in scenes():
  allx=[r for r in rows if r["scene_id"]==sid]; ok=[r for r in allx if r["status"]=="complete"]
  rates=[r["resets_per_100m"] for r in ok]; counts={z:sum(r["status"]==z for r in allx) for z in sorted({r["status"] for r in allx})}
  out.append({"scene_id":sid,"n_total":len(allx),"n_complete":len(ok),"completion_rate":len(ok)/len(allx),
  "mean_resets_per_100m_complete":statistics.mean(rates) if rates else None,
  "sd_resets_per_100m_complete":statistics.stdev(rates) if len(rates)>1 else 0.,
  "total_distance_m_all":sum(r["distance_m"] for r in allx),"status_counts":json.dumps(counts,sort_keys=True)})
 return out
def write(outdir):
 os.makedirs(outdir,exist_ok=True);diag=[];rows=experiment(diagnostics=diag);sums=summarize(rows);files=[]
 specs=[("r1_geometry_runs.csv",rows,list(rows[0])),
 ("r1_geometry_summary.csv",sums,list(sums[0]))]
 for name,data,fields in specs:
  p=os.path.join(outdir,name);files.append(p)
  with open(p,"w",newline="") as fh:w=csv.DictWriter(fh,fieldnames=fields);w.writeheader();w.writerows(data)
 dp=os.path.join(outdir,"r1_failures.json");files.append(dp)
 with open(dp,"w") as fh:json.dump(diag,fh,indent=2,sort_keys=True)
 manifest={"seeds":list(range(121,131)),"path_family":"navigation-aware-clearance-grid","target_virtual_distance_m":35.,
 "paired_design":True,"scenes":list(scenes()),"common_physical_start":[2,2,0],
 "interpretation":"R1 navigation-aware short geometry sensitivity benchmark; not R2/R3 reproduction and not published-scale"}
 mp=os.path.join(outdir,"r1_manifest.json");files.append(mp)
 with open(mp,"w") as fh:json.dump(manifest,fh,indent=2,sort_keys=True)
 hashes={os.path.basename(p):hashlib.sha256(open(p,"rb").read()).hexdigest() for p in files}
 with open(os.path.join(outdir,"SHA256SUMS.json"),"w") as fh:json.dump(hashes,fh,indent=2,sort_keys=True)
 return rows,sums
if __name__=="__main__":print(json.dumps(write("artifacts/r1_geometry_sensitivity")[1],sort_keys=True))
