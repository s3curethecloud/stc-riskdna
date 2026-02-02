from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict

from app.engine.scoring import (
    calculate_identity_behavior_risk,
    calculate_privilege_risk,
    calculate_cloud_impact_risk,
    calculate_human_risk_score,
)

router = APIRouter()


# -----------------------------
# Request / Response Models
# -----------------------------

class RiskSignals(BaseModel):
    identity_behavior: Dict
    privilege: Dict
    cloud_impact: Dict


class RiskScoreResponse(BaseModel):
    risk_score: int
    risk_level: str


# -----------------------------
# API Endpoint
# -----------------------------

@router.post("/score", response_model=RiskScoreResponse)
def calculate_risk_score(payload: RiskSignals):
    """
    Calculate Human-to-Cloud Risk Score (RiskDNA)
    """

    identity_score = calculate_identity_behavior_risk(
        payload.identity_behavior
    )

    privilege_score = calculate_privilege_risk(
        payload.privilege
    )

    cloud_score = calculate_cloud_impact_risk(
        payload.cloud_impact
    )

    result = calculate_human_risk_score(
        identity_behavior_score=identity_score,
        privilege_risk_score=privilege_score,
        cloud_impact_score=cloud_score,
    )

    return result
