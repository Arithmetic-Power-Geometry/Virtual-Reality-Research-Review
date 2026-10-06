"""N09 deterministic controller-cost microbenchmark.

Measures controller decision cost on fixed states/geometries. Wall-clock timing is
reported alongside operation-count surrogates so conclusions are not tied to one runner.
"""
from __future__ import annotations
import csv, json, math, os, statistics, time
from vispoly_sim import State, controller_gains
from s2c_controller import s2c_gains
from p2r_controller import p2r_gains
from r1_geometry_sensitivity import scenes, virtual_scene

def states():
    out=[]
    for sid in scenes():
        # deterministic interior states chosen away from boundaries/obstacles
        pts={"R1-G01":[(2,2,0.0),(5,5,1.0),(8,3,-1.2)],
             "R1-G02":[(2,2,0.0),(6,2,1.0),(8,8,-1.2)],
             "R1-G03":[(2,2,0.0),(5,2,1.0),(8,8,-1.2)],
             "R1-G04":[(2,2,0.0),(4,4,1.0),(10,6,-1.2)]}[sid]
        for px,py,ph in pts:
            out.append((sid,State(px,py,ph,7.5,7.5,0.2,0)))
    return out

def one_call(controller,s,p,v):
    if controller=="Vis-Poly":
        return controller_gains(s,p,v,1)
    if controller=="S2C":
        return s2c_gains(s,p,1)
    if controller=="P2R":
        return p2r_gains(s,p,1)
    raise ValueError(controller)

def benchmark(repeats=5000,warmup=500):
    rows=[]
    v=virtual_scene()
    for controller in ("Vis-Poly","S2C","P2R"):
        for sid,s in states():
            p=scenes()[sid]
            for _ in range(warmup): one_call(controller,s,p,v)
            samples=[]
            for _ in range(9):
                t0=time.perf_counter_ns()
                for _ in range(repeats): one_call(controller,s,p,v)
                t1=time.perf_counter_ns()
                samples.append((t1-t0)/repeats)
            rows.append({
                "controller":controller,"scene_id":sid,
                "physical_segments":len(p),"virtual_segments":len(v),
                "median_ns_per_call":statistics.median(samples),
                "mean_ns_per_call":statistics.mean(samples),
                "sd_ns_per_call":statistics.stdev(samples),
                "samples":len(samples),"repeats_per_sample":repeats
            })
    return rows

def summarize(rows):
    out=[]
    for c in ("Vis-Poly","S2C","P2R"):
        x=[r["median_ns_per_call"] for r in rows if r["controller"]==c]
        out.append({"controller":c,"n_states":len(x),
                    "median_of_state_medians_ns":statistics.median(x),
                    "mean_of_state_medians_ns":statistics.mean(x),
                    "min_state_median_ns":min(x),"max_state_median_ns":max(x)})
    return out

def complexity():
    return [
      {"controller":"S2C","dominant_structure":"tracking-center recomputation over physical segments","per_decision_complexity":"O(P)","count_surrogate":"P physical segments"},
      {"controller":"P2R","dominant_structure":"nearest-point repulsive gradient over physical segments","per_decision_complexity":"O(P)","count_surrogate":"P nearest-segment evaluations"},
      {"controller":"Vis-Poly","dominant_structure":"physical and virtual visibility polygons plus slice construction/matching","per_decision_complexity":"geometry-dependent; upstream visibility dominates","count_surrogate":"visibility-polygon work + slice comparisons"}
    ]

def write(outdir):
    os.makedirs(outdir,exist_ok=True)
    rows=benchmark(); sums=summarize(rows); comp=complexity()
    for name,data in (("N09_cost_raw.csv",rows),("N09_cost_summary.csv",sums),("N09_complexity.csv",comp)):
        with open(os.path.join(outdir,name),"w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=list(data[0])); w.writeheader(); w.writerows(data)
    print(json.dumps({"summary":sums},sort_keys=True))
if __name__=="__main__": write("artifacts/n09_cost")
