from app.engine.scoring import calculate_identity_behavior_risk


def test_low_identity_risk():
    signals = {
        "mfa_failures": 0,
        "login_anomaly": False,
        "dormant_privileged_account": False,
        "excessive_auth_attempts": False,
    }

    score = calculate_identity_behavior_risk(signals)
    assert score == 0


def test_high_identity_risk():
    signals = {
        "mfa_failures": 6,
        "login_anomaly": True,
        "dormant_privileged_account": True,
        "excessive_auth_attempts": True,
    }

    score = calculate_identity_behavior_risk(signals)
    assert score == 100
