"""ARC reset execution wrapper.

Direction selection follows the verified ARC reset selector. The virtual view is
held at its pre-reset heading after completion; the physical user is reoriented
to the selected safe direction. This endpoint invariant is sufficient for
trajectory continuation. Intermediate visual rotation is not used as evidence.
"""
from __future__ import annotations
import math
from arc_reset import select_arc_reset_direction
from vispoly_sim import State, clearance

def nearest_obstacle_normal(state:State,segments):
    # Clean-room numerical estimate: choose the sampled ray with minimum clearance
    samples=360
    vals=[]
    for i in range(samples):
        th=2*math.pi*i/samples
        vals.append((clearance((state.px,state.py),th,segments),th))
    _,toward=min(vals)
    return (-math.cos(toward),-math.sin(toward))

def execute_arc_reset(state:State,physical_segments,virtual_segments,samples:int=20):
    normal=nearest_obstacle_normal(state,physical_segments)
    vf=clearance((state.vx,state.vy),state.vh,virtual_segments)
    def pc(theta): return clearance((state.px,state.py),theta,physical_segments)
    target=select_arc_reset_direction(pc,vf,normal,samples=samples)
    return State(state.px,state.py,target,state.vx,state.vy,state.vh,state.resets+1),target
