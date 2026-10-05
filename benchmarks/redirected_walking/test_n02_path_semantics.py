from waypoint_paths import generate_relative_waypoints
import math

def test_path_seed_is_deterministic():
    assert generate_relative_waypoints(121,8)==generate_relative_waypoints(121,8)

def test_exploration_small_sampling_bounds():
    for d,a in generate_relative_waypoints(121,100):
        assert 2.0 <= d <= 6.0
        assert -math.pi <= a <= math.pi

def test_first_sample_represents_walk_then_subsequent_turn():
    # Semantic regression: a (distance, angle) pair means walk the sampled
    # distance along current forward, then rotate for the NEXT segment.
    d,a=generate_relative_waypoints(121,1)[0]
    x,y,h=0.0,0.0,0.0
    x += d*math.cos(h); y += d*math.sin(h)
    h += a
    assert abs(x-d)<1e-12 and abs(y)<1e-12 and abs(h-a)<1e-12
