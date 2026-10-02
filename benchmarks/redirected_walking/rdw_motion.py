"""RDW motion/gain primitives for the literature-compatible benchmark.

Conventions are explicit and unit-tested. Translation gain is defined as
physical displacement / virtual displacement. Rotation gain is physical
rotation / virtual rotation. Curvature radius controls additional physical
heading change while walking.
"""
from __future__ import annotations
import math

def physical_translation(virtual_distance: float, translation_gain: float) -> float:
    if translation_gain <= 0:
        raise ValueError("translation_gain must be positive")
    return virtual_distance * translation_gain

def physical_rotation(virtual_rotation: float, rotation_gain: float) -> float:
    if rotation_gain <= 0:
        raise ValueError("rotation_gain must be positive")
    return virtual_rotation * rotation_gain

def curvature_heading_delta(physical_distance: float, radius_m: float, sign: int) -> float:
    if sign == 0:
        return 0.0
    if radius_m <= 0:
        raise ValueError("radius_m must be positive")
    return (1 if sign > 0 else -1) * physical_distance / radius_m

def walking_step(
    x: float, y: float, heading: float,
    virtual_distance: float, translation_gain: float,
    curvature_radius_m: float, curvature_sign: int,
):
    d=physical_translation(virtual_distance,translation_gain)
    dh=curvature_heading_delta(d,curvature_radius_m,curvature_sign)
    mid=heading+dh/2
    return x+d*math.cos(mid), y+d*math.sin(mid), heading+dh

def turning_step(physical_heading: float, virtual_turn: float, rotation_gain: float) -> float:
    return physical_heading + physical_rotation(virtual_turn,rotation_gain)
