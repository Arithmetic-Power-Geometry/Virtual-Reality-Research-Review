"""Deterministic collision-free virtual path admission for the R1 benchmark.

This is a declared benchmark protocol, NOT a claim about the exact unpublished
path-validity procedure used by Williams et al. (2021). Candidate motion follows
the Azmandian Exploration-small distributions already registered in this repo:
distance U(2,6) m and relative turn U(-pi,pi), with RDWT WALK-THEN-TURN semantics.

A candidate straight walk is admitted only when the complete segment remains at
least margin_m from every virtual obstacle/boundary segment. Invalid candidates
are deterministically resampled from the same seeded RNG. The rejection count is
reported as benchmark provenance.
"""
from __future__ import annotations
import math, random
from geometry2d import point_segment_distance

def _orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def _on(a,b,p,eps=1e-9):
    return min(a[0],b[0])-eps<=p[0]<=max(a[0],b[0])+eps and min(a[1],b[1])-eps<=p[1]<=max(a[1],b[1])+eps and abs(_orient(a,b,p))<=eps

def segments_intersect(s1,s2,eps=1e-9):
    a,b=s1; c,d=s2
    o1,o2,o3,o4=_orient(a,b,c),_orient(a,b,d),_orient(c,d,a),_orient(c,d,b)
    if ((o1>eps and o2<-eps) or (o1<-eps and o2>eps)) and ((o3>eps and o4<-eps) or (o3<-eps and o4>eps)): return True
    return _on(a,b,c,eps) or _on(a,b,d,eps) or _on(c,d,a,eps) or _on(c,d,b,eps)

def segment_segment_distance(s1,s2):
    if segments_intersect(s1,s2): return 0.0
    a,b=s1; c,d=s2
    return min(point_segment_distance(a,s2)[0],point_segment_distance(b,s2)[0],
               point_segment_distance(c,s1)[0],point_segment_distance(d,s1)[0])

def segment_is_valid(a,b,segments,margin_m=0.5):
    walk=(a,b)
    return all(segment_segment_distance(walk,s)>=margin_m-1e-9 for s in segments)

def _candidate_path(rng,count,start,heading):
    pos=start; h=heading; out=[]
    for _ in range(count):
        d=rng.uniform(2.0,6.0); turn=rng.uniform(-math.pi,math.pi)
        nxt=(pos[0]+d*math.cos(h),pos[1]+d*math.sin(h))
        out.append({"distance_m":d,"turn_rad":turn,"start":pos,"end":nxt,"heading_before":h})
        pos=nxt; h+=turn
    return out

def generate_admitted_path(seed,count,segments,start=(7.0,7.0),heading=0.0,
                           margin_m=0.5,max_path_attempts=100000):
    """Reject complete candidate paths until every walk segment is valid.

    Whole-path rejection preserves WALK-THEN-TURN semantics: no turn is changed
    in response to a boundary during an admitted trajectory.
    """
    rng=random.Random(seed)
    for attempt in range(max_path_attempts):
        path=_candidate_path(rng,count,start,heading)
        if all(segment_is_valid(x["start"],x["end"],segments,margin_m) for x in path):
            for x in path: x["path_attempt"]=attempt
            return path,{"seed":seed,"segments":count,"rejected_paths":attempt,
                         "margin_m":margin_m,"semantics":"walk_then_turn",
                         "tier":"R1-BENCHMARK-not-R2-or-R3"}
    raise RuntimeError(f"unable to admit complete path after {max_path_attempts} attempts")
