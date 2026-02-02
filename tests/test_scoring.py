from app.engine.scoring import (
    calculate_human_risk_score,
    classify_risk,
)


def test_risk_classification():
    assert classify_risk(10) == "LOW"
    assert classify_risk(45) == "MODERATE"
    assert classify_risk(70) == "HIGH"
    assert classify_risk(90) == "CRITICAL"


def test_final_risk_score_aggregation():
    identity_score = 80
    privilege_score = 70
    cloud_score = 60

    result = calculate_human_risk_score(
        identity_behavior_score=identity_score,
        privilege_risk_score=privilege_score,
        cloud_impact_score=cloud_score,
    )

    assert "risk_score" in result
    assert "risk_level" in result

    assert result["risk_level"] in ["HIGH", "CRITICAL"]
