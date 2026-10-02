"""Clean-room implementation of the ARC reset-direction selection rule.

Implements only the reset-direction decision described in Williams et al.
(IEEE TVCG 2021). Geometry/raycasting is supplied by the benchmark caller.
No third-party source code is copied.
"""
from __future__ import annotations
import math
from typing import Callable, Iterable

TAU = 2.0 * math.pi

def unit(theta: float) -> tuple[float, float]:
    return math.cos(theta), math.sin(theta)

def dot(a: tuple[float,float], b: tuple[float,float]) -> float:
    return a[0]*b[0] + a[1]*b[1]

def angular_distance(a: float,b: float) -> float:
    return abs((a-b+math.pi) % TAU - math.pi)

def select_arc_reset_direction(
    physical_clearance: Callable[[float], float],
    virtual_forward_clearance: float,
    obstacle_normal: tuple[float,float],
    samples: int = 20,
    phase: float = 0.0,
) -> float:
    if samples <= 0:
        raise ValueError("samples must be positive")
    candidates=[]
    for i in range(samples):
        theta=(phase + TAU*i/samples) % TAU
        if dot(unit(theta), obstacle_normal) > 0.0:
            d=float(physical_clearance(theta))
            candidates.append((theta,d))
    if not candidates:
        raise ValueError("no sampled direction faces away from obstacle")
    feasible=[x for x in candidates if x[1] >= virtual_forward_clearance]
    pool=feasible if feasible else candidates
    theta,_=min(pool,key=lambda x:(abs(x[1]-virtual_forward_clearance),x[0]))
    return theta

def reset_triggered(distance_to_obstacle: float, trigger_m: float = 0.7) -> bool:
    return distance_to_obstacle <= trigger_m
