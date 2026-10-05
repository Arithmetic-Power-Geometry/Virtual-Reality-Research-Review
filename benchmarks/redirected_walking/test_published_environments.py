from published_environments import environment,E1P,E1V,E2P,E2V

def test_published_environment_segment_counts():
    assert len(environment(1,"physical"))==20
    assert len(environment(1,"virtual"))==28
    assert len(environment(2,"physical"))==16
    assert len(environment(2,"virtual"))==46

def test_experiment3_reuses_published_pair_components():
    assert environment(3,"physical")==environment(1,"physical")
    assert environment(3,"virtual")==environment(2,"virtual")

def test_published_boundary_extents():
    e1p=E1P[0]; e1v=E1V[0]; e2p=E2P[0]; e2v=E2V[0]
    assert (max(x for x,y in e1p)-min(x for x,y in e1p),max(y for x,y in e1p)-min(y for x,y in e1p))==(12,12)
    assert (max(x for x,y in e1v)-min(x for x,y in e1v),max(y for x,y in e1v)-min(y for x,y in e1v))==(17,12)
    assert (max(x for x,y in e2p)-min(x for x,y in e2p),max(y for x,y in e2p)-min(y for x,y in e2p))==(10,10)
    assert (max(x for x,y in e2v)-min(x for x,y in e2v),max(y for x,y in e2v)-min(y for x,y in e2v))==(20,20)
