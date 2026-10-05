from geometry2d import rectangle_segments
from vispoly_sim import swept_segment_safe

def test_swept_guard_rejects_boundary_crossing():
 p=rectangle_segments(10,10)
 assert not swept_segment_safe((1,1),(-0.1,1),p,0.2)

def test_swept_guard_accepts_clear_interior_step():
 p=rectangle_segments(10,10)
 assert swept_segment_safe((2,2),(2.1,2),p,0.2)

def test_swept_guard_respects_body_clearance():
 p=rectangle_segments(10,10)
 assert not swept_segment_safe((0.1,2),(0.15,2),p,0.2)
