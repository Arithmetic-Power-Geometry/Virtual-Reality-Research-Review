import math
from vispoly_sim import State
from p2r_controller import nearest_point_segment,repulsive_negative_gradient,p2r_gains

def test_nearest_point_segment():
 assert nearest_point_segment((2,3),(0,0),(4,0))==(2.0,0.0)

def test_single_wall_gradient_points_away():
 gx,gy=repulsive_negative_gradient(2,2,[((0,0),(4,0))])
 assert abs(gx)<1e-12 and gy>0

def test_symmetric_walls_cancel():
 assert repulsive_negative_gradient(5,5,[((0,0),(0,10)),((10,0),(10,10)),((0,0),(10,0)),((0,10),(10,10))]) is None

def test_walking_against_gradient_uses_min_translation():
 seg=[((0,0),(0,10))]
 s=State(2,5,math.pi,7.5,7.5,0,0)
 gt,gr,r,sign=p2r_gains(s,seg,1)
 assert gt==0.86 and r==7.5
 assert gr in (0.67,1.24) and sign!=0

def test_turn_toward_gradient_uses_max_rotation():
 seg=[((0,0),(0,10))]
 s=State(2,5,math.pi/2,7.5,7.5,0,0)
 # gradient points +x; clockwise turn is negative and reduces error
 assert p2r_gains(s,seg,-1)[1]==1.24
 assert p2r_gains(s,seg,1)[1]==0.67
