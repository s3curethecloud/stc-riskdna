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
