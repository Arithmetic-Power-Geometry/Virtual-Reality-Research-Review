import math
from vispoly_controller import *

def square_slices():
    o=(0.0,0.0)
    p=[(1,1),(-1,1),(-1,-1),(1,-1)]
    return o,build_slices(o,p)

def test_build_four_square_slices():
    _,s=square_slices()
    assert len(s)==4
    assert all(abs(x.area-1.0)<1e-12 for x in s)

def test_active_slice_follows_heading():
    _,s=square_slices()
    a=active_slice(s,math.pi/2)
    assert abs(wrap(a.bisector-math.pi/2))<math.pi/4+1e-9

def test_eligibility_within_ninety_degrees():
    _,s=square_slices()
    e=eligible_physical_slices(s,0.0)
    assert e
    assert all(abs(wrap(x.bisector))<math.pi/2 for x in e)

def test_area_matching():
    v=Slice((0,0),(0,0),2.0,0.0,2.0)
    p=[Slice((0,0),(0,0),1.0,0.1,2.0),Slice((0,0),(0,0),2.1,0.2,2.0)]
    assert most_similar_slice(v,p,0.0).area==2.1

def test_translation_clamps():
    v=Slice((0,0),(0,0),1,0,1)
    lo=Slice((0,0),(0,0),1,0,0.1)
    hi=Slice((0,0),(0,0),1,0,10)
    assert gain_selection(v,lo,0,1)[0]==0.86
    assert gain_selection(v,hi,0,1)[0]==1.26

def test_rotation_toward_and_away():
    v=Slice((0,0),(0,0),1,0,1)
    p=Slice((0,0),(0,0),1,0.5,1)
    assert gain_selection(v,p,0,1)[1]==1.24
    assert gain_selection(v,p,0,-1)[1]==0.67

def test_curvature_sign_and_radius():
    v=Slice((0,0),(0,0),1,0,1)
    p=Slice((0,0),(0,0),1,-0.5,1)
    _,_,r,sgn=gain_selection(v,p,0,1)
    assert r==7.5 and sgn==-1
