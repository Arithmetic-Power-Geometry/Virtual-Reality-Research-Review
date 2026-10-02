"""End-to-end Vis.-Poly reproduction candidate.

Connects repository geometry, Vis.-Poly primitives, motion semantics and ARC
reset trigger. Intended for deterministic regression before literature-scale
experiments; not yet a performance reproduction.
"""
from __future__ import annotations
import math
from dataclasses import dataclass
from geometry2d import visibility_polygon, nearest_hit, Segment
from vispoly_controller import build_slices, active_slice, most_similar_slice, gain_selection
from rdw_motion import walking_step
from arc_reset import reset_triggered

@dataclass
class State:
    px: float; py: float; ph: float
    vx: float; vy: float; vh: float
    resets: int=0

def clearance(origin,heading,segments):
    h=nearest_hit(origin,heading,segments)
    return float("inf") if h is None else h[2]

def controller_gains(state:State,physical_segments:list[Segment],virtual_segments:list[Segment],turn_direction:int=1):
    pp=visibility_polygon((state.px,state.py),physical_segments)
    vp=visibility_polygon((state.vx,state.vy),virtual_segments)
    ps=build_slices((state.px,state.py),pp)
    vs=build_slices((state.vx,state.vy),vp)
    av=active_slice(vs,state.vh)
    target=most_similar_slice(av,ps,state.ph)
    return gain_selection(av,target,state.ph,turn_direction)

def step_walk(state:State,virtual_distance:float,physical_segments:list[Segment],virtual_segments:list[Segment]):
    gt,gr,radius,sgn=controller_gains(state,physical_segments,virtual_segments)
    nx,ny,nh=walking_step(state.px,state.py,state.ph,virtual_distance,gt,radius,sgn)
    nvx=state.vx+virtual_distance*math.cos(state.vh)
    nvy=state.vy+virtual_distance*math.sin(state.vh)
    return State(nx,ny,nh,nvx,nvy,state.vh,state.resets),{"gt":gt,"gr":gr,"radius":radius,"curvature_sign":sgn}

def needs_reset(state:State,physical_segments:list[Segment],trigger_m:float=0.7):
    return reset_triggered(clearance((state.px,state.py),state.ph,physical_segments),trigger_m)

def replay(state:State,distances:list[float],physical_segments:list[Segment],virtual_segments:list[Segment]):
    rows=[]
    for i,d in enumerate(distances):
        if needs_reset(state,physical_segments):
            state.resets+=1
            rows.append({"step":i,"event":"reset_required","px":state.px,"py":state.py})
            break
        state,g=step_walk(state,d,physical_segments,virtual_segments)
        rows.append({"step":i,"event":"walk","px":state.px,"py":state.py,**g})
    return state,rows
