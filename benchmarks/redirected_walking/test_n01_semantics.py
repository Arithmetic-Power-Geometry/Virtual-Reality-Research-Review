import math
from geometry2d import point_segment_distance, nearest_segment_clearance
from vispoly_sim import State, needs_reset
from arc_reset_execute import nearest_obstacle_normal

def test_point_segment_distance_interior_and_endpoint():
    d,q=point_segment_distance((2,1),((0,0),(4,0)))
    assert abs(d-1)<1e-12 and q==(2.0,0.0)
    d,q=point_segment_distance((5,0),((0,0),(4,0)))
    assert abs(d-1)<1e-12 and q==(4.0,0.0)

def test_reset_is_nearest_obstacle_not_heading_ray():
    seg=[((0,0),(10,0))]
    # User is 0.69 m above wall but faces parallel to it.
    s=State(5,0.69,0,5,5,0)
    assert needs_reset(s,seg)
    s2=State(5,0.71,0,5,5,0)
    assert not needs_reset(s2,seg)

def test_exact_away_normal_from_nearest_face():
    seg=[((0,0),(10,0))]
    s=State(5,0.5,0,5,5,0)
    nx,ny=nearest_obstacle_normal(s,seg)
    assert abs(nx)<1e-12 and abs(ny-1)<1e-12
