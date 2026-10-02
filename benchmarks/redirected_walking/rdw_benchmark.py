"""Deterministic redirected-walking benchmark scaffold.

The initial controllers are transparent engineering baselines. They are not
presented as reproductions of named literature algorithms.
"""
from __future__ import annotations
import argparse, csv, json, math, random
from pathlib import Path

def wrap(a):
    return (a + math.pi) % (2 * math.pi) - math.pi

def trajectory(cfg, seed):
    rng = random.Random(seed)
    dt = cfg["dt_seconds"]
    n = int(cfg["trajectory"]["duration_seconds"] / dt)
    interval = max(1, int(cfg["trajectory"]["turn_interval_seconds"] / dt))
    heading = 0.0
    turns = [math.radians(x) for x in cfg["trajectory"]["turn_degrees"]]
    out = []
    for i in range(n):
        if i and i % interval == 0:
            heading = wrap(heading + rng.choice(turns))
        out.append((cfg["default_speed_mps"], heading))
    return out

def center_heading(x, y, w, h):
    return math.atan2(h/2-y, w/2-x)

def clearance(x, y, w, h):
    return min(x, y, w-x, h-y)

def steering(controller, x, y, physical_heading, w, h, margin, dt):
    if controller == "none":
        return 0.0
    target = center_heading(x, y, w, h)
    err = wrap(target - physical_heading)
    c = clearance(x, y, w, h)
    if controller == "center":
        gain = 0.18
    elif controller == "boundary":
        gain = 0.10 if c > 2*margin else 0.45
    else:
        raise ValueError(controller)
    max_rate = math.radians(30)
    return max(-max_rate*dt, min(max_rate*dt, gain*err*dt))

def run(cfg, space, controller, seed):
    dt = cfg["dt_seconds"]; w=space["width_m"]; h=space["length_m"]
    x=w/2; y=h/2; ph=0.0
    resets=viol=0; min_c=float("inf"); pd=vd=0.0; rotations=[]
    for speed, vh in trajectory(cfg, seed):
        delta = steering(controller,x,y,ph,w,h,cfg["boundary_margin_m"],dt)
        ph = wrap(ph + wrap(vh-ph)*0.08 + delta)
        step=speed*dt
        nx=x+step*math.cos(ph); ny=y+step*math.sin(ph)
        vd += step; pd += step; rotations.append(abs(delta))
        if not (0 <= nx <= w and 0 <= ny <= h):
            viol += 1; resets += 1
            x=w/2; y=h/2
            ph=wrap(ph+math.pi)
        else:
            x,y=nx,ny
        min_c=min(min_c,clearance(x,y,w,h))
    return {
      "space":space["id"],"controller":controller,"seed":seed,
      "resets":resets,"boundary_violations":viol,
      "min_clearance_m":round(min_c,6),
      "physical_distance_m":round(pd,6),"virtual_distance_m":round(vd,6),
      "mean_abs_injected_rotation_deg":round(math.degrees(sum(rotations)/len(rotations)),6),
      "max_abs_injected_rotation_deg":round(math.degrees(max(rotations)),6)
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--config",default="config.json")
    ap.add_argument("--output",default="results.csv")
    ap.add_argument("--seeds",default="121,122,123,124,125")
    a=ap.parse_args()
    cfg=json.loads(Path(a.config).read_text())
    seeds=[int(x) for x in a.seeds.split(",")]
    rows=[run(cfg,s,c,z) for s in cfg["spaces"] for c in cfg["controllers"] for z in seeds]
    with open(a.output,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f"wrote {len(rows)} runs to {a.output}")
if __name__=="__main__":
    main()
