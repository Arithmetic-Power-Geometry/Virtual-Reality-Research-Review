from r1_geometry_sensitivity import run

def test_reset_encounter_is_not_counted_every_frame():
    # Regression guard: short deterministic paths must not explode to the reset cap
    # merely because the user remains inside the trigger band for several frames.
    for seed in range(121,131):
        for scene in ("R1-G01","R1-G02","R1-G03","R1-G04"):
            r=run(seed,scene,waypoints=2,max_resets=100)
            assert r["status"]!="reset_cap"
