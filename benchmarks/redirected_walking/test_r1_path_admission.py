import math
from geometry2d import rectangle_segments
from r1_path_admission import *

V=rectangle_segments(14,14)

def test_deterministic_admission():
    a,ma=generate_admitted_path(121,12,V)
    b,mb=generate_admitted_path(121,12,V)
    assert a==b and ma==mb

def test_all_admitted_segments_are_collision_free_with_margin():
    path,_=generate_admitted_path(122,40,V,margin_m=0.5)
    assert all(segment_is_valid(x["start"],x["end"],V,0.5) for x in path)

def test_sampling_bounds_and_walk_then_turn_chain():
    path,_=generate_admitted_path(123,30,V)
    for i,x in enumerate(path):
        assert 2<=x["distance_m"]<=6
        assert -math.pi<=x["turn_rad"]<=math.pi
        if i:
            assert path[i-1]["end"]==x["start"]
            assert abs(x["heading_before"]-(path[i-1]["heading_before"]+path[i-1]["turn_rad"]))<1e-12

def test_rejection_is_reported_not_hidden():
    _,m=generate_admitted_path(121,100,V)
    assert m["rejected_candidates"]>=0
    assert m["tier"]=="R1-BENCHMARK-not-R2-or-R3"

def test_internal_obstacle_is_respected():
    segs=V+[((8,2),(8,12))]
    path,_=generate_admitted_path(124,50,segs,start=(4,7),margin_m=0.5)
    assert all(segment_is_valid(x["start"],x["end"],segs,0.5) for x in path)
