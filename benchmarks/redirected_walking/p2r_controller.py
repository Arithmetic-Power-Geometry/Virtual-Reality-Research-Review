"""Clean-room P2R steering primitives from Thomas & Suma Rosenberg (IEEE VR 2019).

For the published repulsive potential U=sum(1/d_i), this implementation uses
the analytic negative gradient rather than an unstated finite-difference step.
This avoids inventing a hidden epsilon while preserving the stated potential.
"""
from __future__ import annotations
import math
from vispoly_controller import wrap

GT_MIN=0.86
GT_NEUTRAL=1.0
GR_MIN=0.67
GR_MAX=1.24
CURVATURE_RADIUS_M=7.5

def nearest_point_segment(p,a,b):
 px,py=p; ax,ay=a; bx,by=b
 dx,dy=bx-ax,by-ay
 q=dx*dx+dy*dy
 if q<=1e-18:return a
 t=max(0.0,min(1.0,((px-ax)*dx+(py-ay)*dy)/q))
 return ax+t*dx,ay+t*dy

def repulsive_negative_gradient(px,py,segments):
 """Negative gradient of sum_i 1/d_i to nearest point on each segment."""
 gx=gy=0.0
 for a,b in segments:
  qx,qy=nearest_point_segment((px,py),a,b)
  vx,vy=px-qx,py-qy
  d=math.hypot(vx,vy)
  if d<=1e-12: raise ValueError("P2R undefined on obstacle/boundary")
  # U=1/d; -grad(U) points away from the obstacle with magnitude 1/d^2.
  gx += vx/(d**3); gy += vy/(d**3)
 if math.hypot(gx,gy)<=1e-15: return None
 return gx,gy

def p2r_gains(state,segments,turn_direction=1):
 g=repulsive_negative_gradient(state.px,state.py,segments)
 if g is None:return GT_NEUTRAL,1.0,CURVATURE_RADIUS_M,0
 target=math.atan2(g[1],g[0]);err=wrap(target-state.ph)
 fx,fy=math.cos(state.ph),math.sin(state.ph)
 gt=GT_MIN if g[0]*fx+g[1]*fy<0 else GT_NEUTRAL
 sign=0 if abs(err)<1e-12 else (1 if err>0 else -1)
 toward=turn_direction*err>0
 gr=GR_MAX if toward else GR_MIN
 return gt,gr,CURVATURE_RADIUS_M,sign
