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
from geometry2d import nearest_segment_clearance

def nearest_obstacle_normal(state:State,segments):
    """Exact nearest-face away vector from segment geometry.

    ARC requires the normal of the closest obstacle face that triggers reset.
    For our segment representation, the vector from the closest point on that
    face toward the user is the required away-facing normal. Endpoint ties are
    deterministic but remain a declared geometric convention.
    """
    _,_,q=nearest_segment_clearance((state.px,state.py),segments)
    if q is None: raise ValueError("no physical obstacle segments")
    dx=state.px-q[0]; dy=state.py-q[1]; n=math.hypot(dx,dy)
    if n<=1e-12: raise ValueError("user lies on obstacle segment; normal undefined")
    return dx/n,dy/n

def execute_arc_reset(state:State,physical_segments,virtual_segments,samples:int=20):
    normal=nearest_obstacle_normal(state,physical_segments)
    vf=clearance((state.vx,state.vy),state.vh,virtual_segments)
    def pc(theta): return clearance((state.px,state.py),theta,physical_segments)
    target=select_arc_reset_direction(pc,vf,normal,samples=samples)
    return State(state.px,state.py,target,state.vx,state.vy,state.vh,state.resets+1),target
