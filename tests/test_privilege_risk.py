from app.engine.scoring import calculate_privilege_risk


def test_no_privilege_risk():
    signals = {
        "admin_role_usage_minutes": 10,
        "wildcard_policies": False,
        "standing_privileges": False,
    }

    score = calculate_privilege_risk(signals)
    assert score == 0


def test_full_privilege_risk():
    signals = {
        "admin_role_usage_minutes": 240,
        "wildcard_policies": True,
        "standing_privileges": True,
    }

    score = calculate_privilege_risk(signals)
    assert score == 100
