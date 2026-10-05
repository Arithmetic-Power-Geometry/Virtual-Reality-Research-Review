import math
from geometry2d import rectangle_segments
from r1_navigation_paths import generate_navigation_path
from waypoint_paths import timed_motion

def replay_virtual_route(route):
 x,y=route[0]; h=0.0
 for i in range(len(route)-1):
  a,b=route[i],route[i+1]
  desired=math.atan2(b[1]-a[1],b[0]-a[0])
  turn=((desired-h+math.pi)%(2*math.pi))-math.pi
  walks,turns=timed_motion(math.dist(a,b),turn)
  for tv in turns: h+=tv
  for dv in walks:
   x+=dv*math.cos(h); y+=dv*math.sin(h)
  assert math.dist((x,y),b)<1e-8
  h=desired
 return x,y,h

def test_navigation_executor_tracks_every_route_node_35m():
 v=rectangle_segments(14,14)
 for seed in range(121,131):
  route,_=generate_navigation_path(seed,v,target_m=35,start=(7.5,7.5))
  x,y,_=replay_virtual_route(route)
  assert math.dist((x,y),route[-1])<1e-8

def test_navigation_executor_tracks_every_route_node_350m():
 v=rectangle_segments(14,14)
 for seed in (1001,1025,1050,1075,1100):
  route,_=generate_navigation_path(seed,v,target_m=350,start=(7.5,7.5))
  x,y,_=replay_virtual_route(route)
  assert math.dist((x,y),route[-1])<1e-8
