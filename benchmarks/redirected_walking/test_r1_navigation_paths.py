from geometry2d import rectangle_segments
from r1_navigation_paths import *

V=rectangle_segments(14,14)
OBS=V+[((8,2),(8,12))]

def test_navigation_path_is_deterministic():
    a,ma=generate_navigation_path(121,V,target_m=35)
    b,mb=generate_navigation_path(121,V,target_m=35)
    assert a==b and ma==mb

def test_navigation_path_reaches_target_and_is_safe():
    p,m=generate_navigation_path(122,V,target_m=35)
    assert route_length(p)>=35
    assert route_segments_valid(p,V,0.5)
    assert m["actual_m"]==route_length(p)

def test_navigation_path_avoids_internal_obstacle():
    p,m=generate_navigation_path(123,OBS,target_m=35,start=(4.5,7.5))
    assert route_segments_valid(p,OBS,0.5)
    assert m["actual_m"]>=35

def test_seed_changes_route_but_not_protocol():
    a,ma=generate_navigation_path(121,V,target_m=35)
    b,mb=generate_navigation_path(122,V,target_m=35)
    assert a!=b
    assert ma["margin_m"]==mb["margin_m"]==0.5
    assert ma["spacing_m"]==mb["spacing_m"]==1.0

def test_published_scale_target_supported():
    p,m=generate_navigation_path(130,V,target_m=350)
    assert m["actual_m"]>=350
    assert route_segments_valid(p,V,0.5)
