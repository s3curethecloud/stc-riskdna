🏗️ SecureTheCloud RiskDNA — Architecture

## 1. Purpose & Design Intent

**RiskDNA** is a Human-to-Cloud Risk Engine designed to quantify how identity behavior and privilege usage translate into real cloud attack surface.

The architecture is intentionally:
- **Deterministic** (no opaque ML in v1)
- **Explainable** (every score is traceable)
- **Privacy-aware** (HR-safe by design)
- **Composable** (identity, privilege, cloud impact separated)

This mirrors how modern security platforms are designed internally at large enterprises.

## 2. High-Level Architecture Overview
```
┌────────────────────┐
│ Identity Telemetry │
│ (IAM / Auth Logs) │
└─────────┬──────────┘
│
┌─────────▼──────────┐
│ Identity Risk │
│ Normalization │
└─────────┬──────────┘
│
┌─────────▼──────────┐
│ Privilege Analysis │
│ (Roles, Policies) │
└─────────┬──────────┘
│
┌─────────▼──────────┐
│ Cloud Exposure │
│ (CSPM Findings) │
└─────────┬──────────┘
│
┌─────────▼──────────┐
│ RiskDNA Engine │
│ (Weighted Scoring) │
└─────────┬──────────┘
│
┌─────────▼──────────┐
│ API Layer │
│ (FastAPI) │
└─────────┬──────────┘
│
┌─────────▼──────────┐
│ Executive / HR UI │
│ (Shield-style) │
└────────────────────┘
```
---

## 3. Component Breakdown

### 3.1 Data Sources (Telemetry Layer)
Inputs are read-only by design. RiskDNA does **not** modify identity or cloud resources.

```
| Source Type | Examples | Purpose |
|-------------|----------|---------|
| **Identity** | IAM events, auth logs | Human behavior analysis |
| **Privilege** | Role usage, policy breadth | Blast radius estimation |
| **Cloud** | CSPM findings, misconfigs | Impact correlation |
```
---
*All telemetry is anonymizable and replaceable with real integrations later.*

### 3.2 Normalization Layer
**Location:** `app/utils/normalizer.py`

**Responsibilities:**
- Convert heterogeneous telemetry into a common signal model
- Enforce bounded values (0–100)
- Strip PII before scoring

**This ensures:**
- HR-safe outputs
- Predictable scoring
- Clean separation from data collection

### 3.3 RiskDNA Engine (Core Logic)
**Location:** `app/engine/`

**Modules:**
- `identity_risk.py`
- `privilege_risk.py`
- `cloud_impact.py`
- `scoring.py`

The engine uses weighted deterministic scoring:
Final Risk Score =
(Identity Behavior × 45%)

(Privilege Exposure × 35%)

(Cloud Impact × 20%)

text

This weighting reflects real-world breach patterns:
1. **Identities** fail first
2. **Privileges** amplify damage
3. **Cloud misconfigurations** define blast radius

### 3.4 API Layer
**Location:** `app/api/`

The API layer exposes:
- Per-user risk scores
- Department-level aggregates
- Executive summaries

**Key design choice:** The API **never** exposes raw identity telemetry — only risk interpretations.

**This is critical for:**
- HR adoption
- Privacy compliance
- Executive trust

### 3.5 UI Layer (Shield-Grade)
**Location:** `ui/dashboard/`

The UI is designed for:
- **Executives** (risk posture)
- **HR leaders** (behavioral trends)
- **Security leadership** (risk drivers)

**Key UI principles:**
- No alert fatigue
- No raw logs
- Actionable narratives

## 4. Data Flow (End-to-End)
```
[ IAM / Auth Logs ]
│
▼
[ Normalized Signals ]
│
▼
[ Identity Risk Score ]
│
├──► [ Privilege Risk Score ]
│
├──► [ Cloud Impact Score ]
│
▼
[ RiskDNA Aggregator ]
│
▼
[ Risk Level Classification ]
│
▼
[ API Response / Dashboard ]
```
---

**Each step is:**
- Auditable
- Testable
- Replaceable

## 5. Trust Boundaries & Security Model

### 5.1 Trust Boundaries
```
```
| Boundary | Protection |
|----------|------------|
| Telemetry Ingest | Read-only, least privilege |
| Risk Engine | No external calls |
| API Layer | Auth-ready, RBAC-capable |
| UI | No direct telemetry access |
```
---
### 5.2 Security Posture (by design)
- No standing credentials required
- No mutation of cloud or IAM state
- No PII required for scoring
- Supports Zero Trust identity models

This makes RiskDNA **safe to demo, safe to deploy, and safe to scale**.

## 6. Scalability & Future Extensions

RiskDNA is intentionally built to evolve into:
- Just-In-Time access enforcement
- Automated remediation workflows
- AI-assisted risk explanation
- Multi-cloud federation (AWS / Azure / GCP)

*Without changing the core scoring engine.*

## 7. Why This Architecture Matters

This architecture demonstrates:
- **Systems thinking** (not tool usage)
- **Identity-first** security design
- **Executive-grade** risk communication
- **HR + CSO** alignment

It reflects how modern security platforms are **actually built**, not how labs are taught.

## 8. Summary

**RiskDNA is not a dashboard.**  
It is a **risk translation engine** that converts human behavior into cloud-relevant security outcomes.
