"""Clean-room Steer-to-Center comparator for the R1 RDW benchmark.

Steering target: vector from the current physical position to the declared
tracking-space center. Gain thresholds and motion conventions are shared with
the benchmark's verified RDW primitives. This module intentionally implements
only the controller policy; reset/path/safety logic remains common.
"""
from __future__ import annotations
import math
from vispoly_controller import wrap

GT_NEUTRAL=1.0
GR_TOWARD=1.24
GR_AWAY=0.67
CURVATURE_RADIUS_M=7.5

def tracking_center(physical_segments):
    xs=[p[0] for seg in physical_segments for p in seg]
    ys=[p[1] for seg in physical_segments for p in seg]
    if not xs or not ys: raise ValueError("physical geometry is empty")
    return (min(xs)+max(xs))/2,(min(ys)+max(ys))/2

def target_heading(px,py,physical_segments):
    cx,cy=tracking_center(physical_segments)
    if math.hypot(cx-px,cy-py)<=1e-12: return None
    return math.atan2(cy-py,cx-px)

def s2c_gains(state,physical_segments,turn_direction=1):
    target=target_heading(state.px,state.py,physical_segments)
    if target is None:
        return GT_NEUTRAL,1.0,CURVATURE_RADIUS_M,0
    err=wrap(target-state.ph)
    toward=(turn_direction*err)>0
    gr=GR_TOWARD if toward else GR_AWAY
    sign=0 if abs(err)<1e-12 else (1 if err>0 else -1)
    return GT_NEUTRAL,gr,CURVATURE_RADIUS_M,sign
