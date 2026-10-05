import math
import pytest
from rdw_motion import *

def test_translation_identity():
    assert physical_translation(2.0,1.0)==2.0

def test_translation_gain_virtual_over_physical():
    # g_T = T_virtual/T_physical, so 2 virtual m at g=1.25 requires 1.6 physical m.
    assert abs(physical_translation(2.0,1.25)-1.6)<1e-12

def test_rotation_identity():
    assert physical_rotation(math.pi/2,1.0)==math.pi/2

def test_rotation_gain_virtual_over_physical():
    # g_R = R_virtual/R_physical.
    assert abs(physical_rotation(1.0,0.5)-2.0)<1e-12
    assert abs(physical_rotation(1.0,2.0)-0.5)<1e-12

def test_curvature_arc_relation():
    assert abs(curvature_heading_delta(7.5,7.5,1)-1.0)<1e-12
    assert abs(curvature_heading_delta(7.5,7.5,-1)+1.0)<1e-12

def test_straight_step_without_curvature():
    x,y,h=walking_step(0,0,0,1,1,7.5,0)
    assert abs(x-1)<1e-12 and abs(y)<1e-12 and h==0

def test_invalid_gain_rejected():
    with pytest.raises(ValueError):
        physical_translation(1,0)
