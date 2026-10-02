import math
from geometry2d import *

def test_ray_hits_rectangle_wall():
    h=nearest_hit((2,2),0.0,rectangle_segments(4,4))
    assert h is not None
    assert abs(h[0]-4)<1e-8 and abs(h[1]-2)<1e-8 and abs(h[2]-2)<1e-8

def test_visibility_rectangle_area():
    poly=visibility_polygon((2,2),rectangle_segments(4,4))
    assert len(poly)>=4
    assert abs(polygon_area(poly)-16)<1e-4

def test_internal_wall_occludes():
    segs=rectangle_segments(4,4)+[((2.5,1.0),(2.5,3.0))]
    h=nearest_hit((1,2),0.0,segs)
    assert h is not None
    assert abs(h[0]-2.5)<1e-8
    poly=visibility_polygon((1,2),segs)
    assert 0 < polygon_area(poly) < 16

def test_visibility_is_deterministic():
    segs=rectangle_segments(6,4)+[((3,1),(3,3))]
    assert visibility_polygon((1,2),segs)==visibility_polygon((1,2),segs)
