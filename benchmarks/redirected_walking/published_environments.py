"""Exact static environment layouts published in the Vis.-Poly supplement.

Coordinates are transcribed from Williams, Bera & Manocha (TVCG 2021)
supplementary material. Experiment 3 reuses Experiment 1 physical and
Experiment 2 virtual environments.
"""
from __future__ import annotations
from geometry2d import Segment

def polygon_segments(vertices):
    return [(vertices[i],vertices[(i+1)%len(vertices)]) for i in range(len(vertices))]

E1P=[
 [(-6,-6),(6,-6),(6,6),(-6,6)],
 [(-4,-4),(-1,-4),(-1,-1),(-4,-1)],
 [(1,-4),(4,-4),(4,-1),(1,-1)],
 [(1,1),(4,1),(4,4),(1,4)],
 [(-4,1),(-1,1),(-1,4),(-4,4)],
]
E1V=[
 [(-11,-6),(6,-6),(6,6),(-11,6)],
 [(-4,-4),(-1,-4),(-1,-1),(-4,-1)],
 [(1,-4),(4,-4),(4,-1),(1,-1)],
 [(1,1),(4,1),(4,4),(1,4)],
 [(-4,1),(-1,1),(-1,4),(-4,4)],
 [(-9,1),(-6,1),(-6,4),(-9,4)],
 [(-9,-4),(-6,-4),(-6,-1),(-9,-1)],
]
E2P=[
 [(-5,-5),(5,-5),(5,5),(-5,5)],
 [(-4.5,-4.5),(-2.5,-4.5),(-2.5,-2.5),(-4.5,-2.5)],
 [(-2,-1),(2,-1),(2,1),(-2,1)],
 [(-2,4),(2,4),(2,5),(-2,5)],
]
E2V=[
 [(10,-10),(10,10),(-10,10),(-10,-10)],
 [(-4.5,-4.5),(-2.5,-4.5),(-3.5,-2.5)],
 [(0,2),(2,1),(1,-2),(-1,-2),(-2,1)],
 [(-2,4),(2,4),(2,5),(-2,5)],
 [(-8.5,8.5),(-8.5,2.5),(-6.5,2.5),(-7,7),(-2.5,6.5),(-2.5,8.5)],
 [(-8,-1),(-8,-2),(-7,-2),(-7,-1)],
 [(-7,-3),(-7,-4),(-6,-4),(-6,-3)],
 [(-9,-5),(-9,-7),(-8,-7),(-8,-5)],
 [(-6,-9),(-3,-7),(-3,-6),(-7,-8)],
 [(3,-4),(3,-8),(7,-8),(7,-4)],
 [(5,9),(4,8),(8,4),(8,8)],
]

def environment(experiment:int,space:str)->list[Segment]:
    if experiment==1: polys=E1P if space=="physical" else E1V
    elif experiment==2: polys=E2P if space=="physical" else E2V
    elif experiment==3: polys=E1P if space=="physical" else E2V
    else: raise ValueError("static published layouts implemented for experiments 1-3")
    return [s for poly in polys for s in polygon_segments(poly)]
