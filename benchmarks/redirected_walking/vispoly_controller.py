"""Clean-room Vis.-Poly controller primitives from Williams, Bera & Manocha (2021).

This module implements independently testable slice/matching/gain primitives.
It does not yet claim an end-to-end reproduction of the published simulator.
"""
from __future__ import annotations
import math
from dataclasses import dataclass

Point=tuple[float,float]
TAU=2*math.pi

@dataclass(frozen=True)
class Slice:
    a: Point
    b: Point
    area: float
    bisector: float
    average_length: float

def wrap(a:float)->float:
    return (a+math.pi)%TAU-math.pi

def dist(a:Point,b:Point)->float:
    return math.hypot(a[0]-b[0],a[1]-b[1])

def triangle_area(o:Point,a:Point,b:Point)->float:
    return abs((a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0]))/2

def _angle(o:Point,p:Point)->float:
    return math.atan2(p[1]-o[1],p[0]-o[0])

def _mean_angle(a:float,b:float)->float:
    return a+wrap(b-a)/2

def build_slices(origin:Point,polygon:list[Point])->list[Slice]:
    if len(polygon)<3: return []
    out=[]
    for i,a in enumerate(polygon):
        b=polygon[(i+1)%len(polygon)]
        ar=triangle_area(origin,a,b)
        if ar<=1e-12: continue
        aa,ab=_angle(origin,a),_angle(origin,b)
        out.append(Slice(a,b,ar,wrap(_mean_angle(aa,ab)),(dist(origin,a)+dist(origin,b))/2))
    return out

def active_slice(slices:list[Slice],heading:float)->Slice:
    if not slices: raise ValueError("no slices")
    return min(slices,key=lambda s:abs(wrap(s.bisector-heading)))

def eligible_physical_slices(slices:list[Slice],physical_heading:float)->list[Slice]:
    return [s for s in slices if abs(wrap(s.bisector-physical_heading)) < math.pi/2]

def most_similar_slice(active_virtual:Slice,physical_slices:list[Slice],physical_heading:float)->Slice:
    eligible=eligible_physical_slices(physical_slices,physical_heading)
    if not eligible: raise ValueError("no eligible physical slice")
    return min(eligible,key=lambda s:(abs(s.area-active_virtual.area),abs(wrap(s.bisector-physical_heading))))

def gain_selection(active_virtual:Slice,target_physical:Slice,physical_heading:float,turn_direction:int):
    """Return translation gain, rotation gain, curvature radius, curvature sign.

    turn_direction: -1 or +1 indicates current physical turn direction.
    Rotation gain follows whether that turn moves toward the optimal direction.
    """
    gt=max(0.86,min(1.26,target_physical.average_length/active_virtual.average_length))
    err=wrap(target_physical.bisector-physical_heading)
    toward=(turn_direction*err)>0
    gr=1.24 if toward else 0.67
    curvature_sign=0 if abs(err)<1e-12 else (1 if err>0 else -1)
    return gt,gr,7.5,curvature_sign
