"""N05 short paired P2R gate under the common R1 benchmark.

Only steering policy changes. Paths, ARC reset, timing, safety invariant,
starts and physical geometries are inherited from the validated benchmark.
"""
from __future__ import annotations
import math
import r1_geometry_sensitivity as base
from vispoly_sim import State,needs_reset,swept_segment_safe
from arc_reset_execute import execute_arc_reset
from waypoint_paths import timed_motion
from rdw_motion import turning_step,walking_step
from p2r_controller import p2r_gains

def p2r_step_walk(s,dv,p):
 gt,gr,radius,sgn=p2r_gains(s,p)
 nx,ny,nh=walking_step(s.px,s.py,s.ph,dv,gt,radius,sgn)
 nvx=s.vx+dv*math.cos(s.vh);nvy=s.vy+dv*math.sin(s.vh)
 return State(nx,ny,nh,nvx,nvy,s.vh,s.resets)

def run_p2r(seed,sid,target_m=35.,max_resets=100):
 p=base.scenes()[sid];v=base.virtual_scene();x,y,h=base.start_for(sid)
 s=State(x,y,h,7.5,7.5,0,0)
 route,_=base.generate_navigation_path(seed,v,target_m=target_m,start=(7.5,7.5))
 distance=0.;steps=0;reset_armed=True;vh=0.
 for idx in range(len(route)-1):
  a,b=route[idx],route[idx+1];d=math.dist(a,b);desired=math.atan2(b[1]-a[1],b[0]-a[0])
  turn=((desired-vh+math.pi)%(2*math.pi))-math.pi
  walks,turns=timed_motion(d,turn)
  for tv in turns:
   _,gr,_,_=p2r_gains(s,p,1 if tv>=0 else -1)
   s.ph=turning_step(s.ph,tv,gr);s.vh+=tv;steps+=1
  vh=desired
  for dv in walks:
   trig=needs_reset(s,p)
   if reset_armed and trig:
    if s.resets>=max_resets:return base.row(seed,sid,s,distance,steps,"reset_cap")
    s,_=execute_arc_reset(s,p,v);reset_armed=False
   elif not trig:reset_armed=True
   try:candidate=p2r_step_walk(s,dv,p)
   except ValueError:return base.row(seed,sid,s,distance,steps,"controller_failure")
   if not swept_segment_safe((s.px,s.py),(candidate.px,candidate.py),p,0.2):
    if s.resets>=max_resets:return base.row(seed,sid,s,distance,steps,"reset_cap")
    s,_=execute_arc_reset(s,p,v);reset_armed=False
    try:candidate=p2r_step_walk(s,dv,p)
    except ValueError:return base.row(seed,sid,s,distance,steps,"controller_failure")
    if not swept_segment_safe((s.px,s.py),(candidate.px,candidate.py),p,0.2):
     return base.row(seed,sid,s,distance,steps,"geometry_failure")
   s=candidate;distance+=dv;steps+=1
 return base.row(seed,sid,s,distance,steps,"complete")

def experiment(seeds=range(121,131),target_m=35.):
 rows=[]
 for seed in seeds:
  for sid in base.scenes():
   r=run_p2r(seed,sid,target_m);r["controller"]="P2R";rows.append(r)
 return rows
