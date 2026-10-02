"""Seeded waypoint/path utilities for RDW reproduction experiments."""
from __future__ import annotations
import math, random

def generate_relative_waypoints(seed:int,count:int,min_distance:float=2.0,max_distance:float=6.0):
    rng=random.Random(seed)
    return [(rng.uniform(min_distance,max_distance),rng.uniform(-math.pi,math.pi)) for _ in range(count)]

def timed_motion(distance_m:float,turn_rad:float,dt:float=0.05,speed_mps:float=1.0,turn_speed_deg_s:float=90.0):
    if dt<=0 or speed_mps<=0 or turn_speed_deg_s<=0: raise ValueError("positive timing parameters required")
    walk_step=speed_mps*dt
    turn_step=math.radians(turn_speed_deg_s)*dt
    walks=[walk_step]*(int(distance_m//walk_step))
    rem=distance_m-sum(walks)
    if rem>1e-12: walks.append(rem)
    sign=1 if turn_rad>=0 else -1
    turns=[sign*turn_step]*(int(abs(turn_rad)//turn_step))
    remt=abs(turn_rad)-sum(abs(x) for x in turns)
    if remt>1e-12: turns.append(sign*remt)
    return walks,turns
