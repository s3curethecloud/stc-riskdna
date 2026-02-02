"""
RiskDNA Scoring Engine

This module calculates a Human-to-Cloud Risk Score by correlating:
- Identity behavior
- Privilege usage
- Cloud exposure impact

Scores are deterministic and explainable by design.
"""

from typing import Dict


# -----------------------------
# Weights (v1 – locked)
# -----------------------------

WEIGHTS = {
    "identity_behavior": 0.45,
    "privilege_risk": 0.35,
    "cloud_impact": 0.20,
}

RISK_LEVELS = {
    "LOW": (0, 29),
    "MODERATE": (30, 59),
    "HIGH": (60, 79),
    "CRITICAL": (80, 100),
}


# -----------------------------
# Core Scoring Functions
# -----------------------------

def calculate_identity_behavior_risk(signals: Dict) -> int:
    """
    Identity behavior risk (0–100)
    Signals expected:
      - mfa_failures
      - login_anomaly
      - dormant_privileged_account
    """

    score = 0

    if signals.get("mfa_failures", 0) >= 5:
        score += 30

    if signals.get("login_anomaly", False):
        score += 25

    if signals.get("dormant_privileged_account", False):
        score += 25

    excessive_auth = signals.get("excessive_auth_attempts", False)
    if excessive_auth:
        score += 20

    return min(score, 100)


def calculate_privilege_risk(signals: Dict) -> int:
    """
    Privilege exposure risk (0–100)
    Signals expected:
      - admin_role_usage_minutes
      - wildcard_policies
      - standing_privileges
    """

    score = 0

    if signals.get("admin_role_usage_minutes", 0) > 120:
        score += 40

    if signals.get("wildcard_policies", False):
        score += 35

    if signals.get("standing_privileges", False):
        score += 25

    return min(score, 100)


def calculate_cloud_impact_risk(signals: Dict) -> int:
    """
    Cloud blast-radius impact (0–100)
    Signals expected:
      - public_resource
      - encryption_disabled
      - network_exposed
    """

    score = 0

    if signals.get("public_resource", False):
        score += 40

    if signals.get("encryption_disabled", False):
        score += 30

    if signals.get("network_exposed", False):
        score += 30

    return min(score, 100)


# -----------------------------
# Aggregation Logic
# -----------------------------

def calculate_human_risk_score(
    identity_behavior_score: int,
    privilege_risk_score: int,
    cloud_impact_score: int,
) -> Dict:
    """
    Final RiskDNA score aggregation
    Returns score + human-readable risk level
    """

    final_score = (
        identity_behavior_score * WEIGHTS["identity_behavior"]
        + privilege_risk_score * WEIGHTS["privilege_risk"]
        + cloud_impact_score * WEIGHTS["cloud_impact"]
    )

    final_score = round(final_score)

    return {
        "risk_score": final_score,
        "risk_level": classify_risk(final_score),
    }


def classify_risk(score: int) -> str:
    """
    Converts numeric score into executive-friendly category
    """

    for level, (low, high) in RISK_LEVELS.items():
        if low <= score <= high:
            return level

    return "UNKNOWN"
