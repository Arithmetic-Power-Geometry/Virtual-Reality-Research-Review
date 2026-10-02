from geometry2d import rectangle_segments
from vispoly_sim import *

def test_centered_replay_is_deterministic():
    p=rectangle_segments(10,10); v=rectangle_segments(10,10)
    s=State(5,5,0,5,5,0)
    a,ra=replay(s,[0.05]*10,p,v)
    s=State(5,5,0,5,5,0)
    b,rb=replay(s,[0.05]*10,p,v)
    assert a==b and ra==rb

def test_centered_symmetric_scene_uses_valid_gains():
    p=rectangle_segments(10,10); v=rectangle_segments(10,10)
    s=State(5,5,0,5,5,0)
    _,rows=replay(s,[0.05]*5,p,v)
    walks=[r for r in rows if r["event"]=="walk"]
    assert walks
    assert all(0.86 <= r["gt"] <= 1.26 for r in walks)
    assert all(r["gr"] in (0.67,1.24) for r in walks)
    assert all(r["radius"]==7.5 for r in walks)

def test_reset_required_near_forward_wall():
    p=rectangle_segments(4,4); v=rectangle_segments(10,10)
    s=State(3.4,2,0,5,5,0)
    end,rows=replay(s,[0.05],p,v)
    assert end.resets==1
    assert rows[0]["event"]=="reset_required"

def test_no_reset_from_center():
    p=rectangle_segments(4,4)
    s=State(2,2,0,5,5,0)
    assert not needs_reset(s,p)
