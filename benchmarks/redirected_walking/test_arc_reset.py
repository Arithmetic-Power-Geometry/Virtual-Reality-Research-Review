import math
from arc_reset import select_arc_reset_direction, reset_triggered

def test_trigger():
    assert reset_triggered(0.7)
    assert not reset_triggered(0.700001)

def test_prefers_clearance_match_with_constraints():
    target=3.0
    def clearance(theta):
        return 3.0 if abs(theta) < 1e-12 else 5.0
    th=select_arc_reset_direction(clearance,target,(1.0,0.0),samples=20)
    assert abs(th) < 1e-12

def test_fallback_when_no_candidate_has_enough_clearance():
    def clearance(theta):
        return 1.9 if abs(theta) < 1e-12 else 1.0
    th=select_arc_reset_direction(clearance,3.0,(1.0,0.0),samples=20)
    assert abs(th) < 1e-12

def test_samples_twenty_directions():
    seen=[]
    def clearance(theta):
        seen.append(theta); return 10.0
    select_arc_reset_direction(clearance,1.0,(1.0,0.0),samples=20)
    assert 0 < len(seen) <= 20
