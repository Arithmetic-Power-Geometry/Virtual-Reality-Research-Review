import math
from geometry2d import rectangle_segments
from vispoly_sim import State
from s2c_controller import tracking_center,target_heading,s2c_gains

def test_center_from_boundary_geometry():
 assert tracking_center(rectangle_segments(10,10))==(5.0,5.0)
 assert tracking_center(rectangle_segments(12,8))==(6.0,4.0)

def test_target_points_to_center():
 p=rectangle_segments(10,10)
 assert abs(target_heading(2,5,p)-0.0)<1e-12
 assert abs(target_heading(5,2,p)-math.pi/2)<1e-12

def test_curvature_steers_toward_center():
 p=rectangle_segments(10,10)
 s=State(2,5,math.pi/2,7.5,7.5,0,0)
 gt,gr,r,sign=s2c_gains(s,p,1)
 assert gt==1.0 and r==7.5 and sign==-1
 assert gr in (0.67,1.24)

def test_center_has_no_curvature_bias():
 p=rectangle_segments(10,10)
 s=State(5,5,0,7.5,7.5,0,0)
 assert s2c_gains(s,p)==(1.0,1.0,7.5,0)
