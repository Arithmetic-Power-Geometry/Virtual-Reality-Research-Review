import math
from waypoint_paths import *
from geometry2d import rectangle_segments
from vispoly_sim import State
from arc_reset_execute import execute_arc_reset

def test_waypoints_reproducible_and_bounded():
    a=generate_relative_waypoints(121,20); b=generate_relative_waypoints(121,20)
    assert a==b
    assert all(2<=d<=6 and -math.pi<=t<=math.pi for d,t in a)

def test_published_timing_step_sizes():
    w,t=timed_motion(1.0,math.pi/2)
    assert len(w)==20 and all(abs(x-0.05)<1e-12 for x in w)
    assert len(t)==20 and all(abs(x-math.radians(4.5))<1e-12 for x in t)

def test_arc_reset_changes_physical_not_virtual_heading():
    p=rectangle_segments(4,4); v=rectangle_segments(10,10)
    s=State(3.4,2,0,5,5,0,0)
    n,target=execute_arc_reset(s,p,v)
    assert n.resets==1
    assert n.vh==s.vh
    assert n.ph==target
