"""Minimal deterministic 2-D geometry for RDW benchmark scenes.

Clean-room implementation. Visibility is computed by casting rays immediately
before/at/after each segment endpoint. This is intentionally simple and
auditable; it is not copied from a third-party visibility library.
"""
from __future__ import annotations
import math

EPS=1e-9
Point=tuple[float,float]
Segment=tuple[Point,Point]

def cross(a:Point,b:Point)->float:
    return a[0]*b[1]-a[1]*b[0]

def sub(a:Point,b:Point)->Point:
    return a[0]-b[0],a[1]-b[1]

def ray_segment_intersection(origin:Point,theta:float,seg:Segment):
    d=(math.cos(theta),math.sin(theta)); a,b=seg; e=sub(b,a)
    den=cross(d,e)
    if abs(den)<EPS: return None
    ao=sub(a,origin)
    t=cross(ao,e)/den
    u=cross(ao,d)/den
    if t < -EPS or u < -EPS or u > 1+EPS: return None
    return origin[0]+max(0.0,t)*d[0],origin[1]+max(0.0,t)*d[1],max(0.0,t)

def nearest_hit(origin:Point,theta:float,segments:list[Segment]):
    hits=[h for s in segments if (h:=ray_segment_intersection(origin,theta,s)) is not None]
    return min(hits,key=lambda x:x[2]) if hits else None

def visibility_polygon(origin:Point,segments:list[Segment],angle_eps:float=1e-7):
    angles=[]
    for a,b in segments:
        for p in (a,b):
            base=math.atan2(p[1]-origin[1],p[0]-origin[0])
            angles.extend((base-angle_eps,base,base+angle_eps))
    pts=[]
    for ang in sorted(angles):
        h=nearest_hit(origin,ang,segments)
        if h is not None:
            p=(h[0],h[1])
            if not pts or math.hypot(p[0]-pts[-1][0],p[1]-pts[-1][1])>1e-7:
                pts.append(p)
    if len(pts)>1 and math.hypot(pts[0][0]-pts[-1][0],pts[0][1]-pts[-1][1])<=1e-7:
        pts.pop()
    return pts

def polygon_area(poly:list[Point])->float:
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly))))/2 if len(poly)>=3 else 0.0

def rectangle_segments(width:float,height:float)->list[Segment]:
    p=[(0.,0.),(width,0.),(width,height),(0.,height)]
    return [(p[i],p[(i+1)%4]) for i in range(4)]
