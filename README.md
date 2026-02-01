# SecureTheCloud – Human-to-Cloud Risk Engine

## Overview
The Human-to-Cloud Risk Engine quantifies organizational cyber risk by correlating
human identity behavior with cloud infrastructure exposure.

Unlike traditional security tools that focus only on infrastructure or alerts,
this platform measures how employee actions directly influence cloud attack surface.

## Why This Matters
Over 80% of cloud breaches involve compromised identities.
Security teams lack a way to quantify human-driven cloud risk in a way
that executives and HR leaders can understand.

This project closes that gap.

## Key Capabilities
- Identity behavior risk scoring
- Privilege exposure analysis
- Cloud misconfiguration impact correlation
- Executive and HR-friendly dashboards

## Architecture
- Python (FastAPI) risk engine
- Policy-as-Code (Terraform, Checkov)
- Simulated IAM & cloud telemetry (production-ready design)
- Secure-by-design landing zone

## Outcomes
- Quantified human attack surface
- Reduced identity-driven cloud risk
- Board-ready security posture reporting

## Skills Demonstrated
- Cloud Security Architecture
- Identity & Zero Trust Design
- Infrastructure as Code
- Policy as Code
- Risk Modeling & Executive Communication

```
stc-riskdna/
├── README.md                     # Executive + recruiter narrative
├── ARCHITECTURE.md               # System & data flow diagrams
├── ROADMAP.md                    # Phases (v1 → v3)
├── LICENSE
│
├── docs/
│   ├── executive-overview.md     # Board / HR explanation
│   ├── risk-model.md             # Scoring logic (authoritative)
│   ├── data-sources.md           # IAM, cloud, policy signals
│   └── screenshots/              # Dashboard visuals
│
├── app/
│   ├── main.py                   # FastAPI entry point
│   ├── api/
│   │   ├── health.py
│   │   ├── risk_scores.py        # Core API
│   │   └── departments.py
│   │
│   ├── engine/
│   │   ├── __init__.py
│   │   ├── scoring.py            # RiskDNA formula
│   │   ├── identity_risk.py
│   │   ├── privilege_risk.py
│   │   └── cloud_impact.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── department.py
│   │   └── risk.py
│   │
│   └── utils/
│       ├── normalizer.py
│       └── weights.py
│
├── data/
│   ├── mock/
│   │   ├── iam_events.json
│   │   ├── auth_logs.json
│   │   ├── cloud_findings.json
│   │   └── departments.json
│   │
│   └── samples/
│       └── anonymized-demo.json
│
├── infrastructure/
│   ├── terraform/
│   │   ├── landing-zone/
│   │   ├── iam/
│   │   └── logging/
│   │
│   ├── policy/
│   │   ├── checkov/
│   │   └── tfsec/
│   │
│   └── diagrams/
│       └── riskdna-architecture.drawio
│
├── ui/
│   ├── dashboard/
│   │   ├── index.html
│   │   ├── css/
│   │   └── js/
│   │
│   └── assets/
│
├── tests/
│   ├── test_scoring.py
│   └── test_engine.py
│
└── .github/
    ├── workflows/
    │   └── security-pipeline.yml
    └── ISSUE_TEMPLATE.md
```
