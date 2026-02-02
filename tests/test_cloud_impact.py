from app.engine.scoring import calculate_cloud_impact_risk


def test_low_cloud_impact():
    signals = {
        "public_resource": False,
        "encryption_disabled": False,
        "network_exposed": False,
    }

    score = calculate_cloud_impact_risk(signals)
    assert score == 0


def test_high_cloud_impact():
    signals = {
        "public_resource": True,
        "encryption_disabled": True,
        "network_exposed": True,
    }

    score = calculate_cloud_impact_risk(signals)
    assert score == 100
