from n05_p2r_short import experiment

def test_p2r_short_pairing_and_completion_small():
    rows=experiment(seeds=range(121,123),target_m=10)
    assert len(rows)==8
    assert all(r['controller']=='P2R' for r in rows)
    assert {r['scene_id'] for r in rows}=={'R1-G01','R1-G02','R1-G03','R1-G04'}
    assert all(r['status']=='complete' for r in rows)
