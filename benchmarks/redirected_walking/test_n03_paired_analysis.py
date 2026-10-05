import csv
import pytest
from n03_paired_analysis import analyze
def rows(status="complete"):
 out=[]
 for s in range(1,6):
  for g,off in [("G1",0),("G2",2),("G3",4),("G4",6)]:
   out.append({"seed":str(s),"scene_id":g,"status":status,"resets_per_100m":str(10+s+off)})
 return out
def test_paired_analysis_shape_and_direction():
 x=analyze(rows());assert len(x)==6
 q=[r for r in x if r["scene_a"]=="G1" and r["scene_b"]=="G4"][0]
 assert q["mean_difference_b_minus_a"]==6 and q["positive_pairs"]==5
def test_rejects_incomplete():
 r=rows();r[0]["status"]="reset_cap"
 with pytest.raises(ValueError):analyze(r)
def test_rejects_unbalanced():
 with pytest.raises(ValueError):analyze(rows()[:-1])
