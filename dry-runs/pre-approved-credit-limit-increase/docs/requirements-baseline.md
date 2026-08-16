---
name: requirements-analysis
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-15
description: Requirements baseline for CLI Automation Platform (UAE)
inputs:
  goal: Automate Credit Limit Increase (CLI) for 3000 pre-approved thick-file customers/week.
  stakeholders:
    - Business (Sponsor)
    - Risk (Credit Rules)
    - Compliance/Legal (UAE Regs)
    - Security
    - IT Ops
  regulatory:
    - CBUAE Sectoral data-residency
    - AECB 30-day report reuse policy
    - Consumer Protection
    - AML/KYC
  systems:
    - Fiserv (On-prem/Core)
    - ODS/DWH (On-prem)
    - Enterprise MQ (On-prem)
    - UiPath RPA (Azure)
    - Middleware (AWS)
    - Digital Engagement (AWS, PostgreSQL)
    - Event Hub (AWS)
    - Notification Center (AWS)
expected-deliverables:
  - Requirements baseline (Goal, Funtional, NFRs)
  - Functional requirements register
  - Open questions/Assumptions
---

# /requirements-analysis: CLI Automation Platform

## 1. Initiative Goal & Success Measures

**Goal:** Automate pre-approved Credit Limit Increase (CLI) offers for 3000 selected "thick-file" customers per week, integrating cross-cloud (AWS/Azure) and on-premises (Fiserv/DWH) systems.

**Success Measures:**
*   **Throughput:** Process 3,000 offers per week.
*   **Latency:** Immediate visibility of updated limit upon successful processing.
*   **Resiliency:** 99.95% availability for critical customer-facing components.
*   **Reconciliation:** Zero-drift between RPA database, Fiserv, and Digital Engagement systems.
*   **Regulatory:** Full auditability for credit decisions and consent (30-day AECB reuse policy compliant).

## 2. Functional Requirements (BIAN Structured)

| Capability (BIAN) | Functional Requirement | Priority | Source |
| :--- | :--- | :--- | :--- |
| **Credit Risk Management** | Automate pre-approved CLI eligibility for thick-file population. | Must | Risk |
| **Retail Payments** | Execute card-limit update in Fiserv (async/reconciled). | Must | Core |
| **Customer Identity** | Securely obtain and audit customer consent for CLI. | Must | Compliance |
| **Communication** | Multi-channel notification (Push/SMS/Email) with secure deep-link. | Must | Ops/UX |
| **Credit Risk Management** | Evaluate bureau-based eligibility using fresh/30-day AECB report. | Must | Reg/Risk |

## 3. Non-Functional Requirement Framing

*   **Availability:** 99.95% (Customer journey endpoints & integration interfaces).
*   **Security:** Multi-cloud (AWS/Azure/On-prem) cross-zone data transfer security (TLS, mTLS), Azure AD for API Auth.
*   **Idempotency:** Strict enforcement across all orchestration stages (RPA, MQ, Middleware, Fiserv).
*   **Observability:** Distributed tracing using correlation IDs to trace record-level events across zones without leaking PII.

## 4. Regulatory Constraints (UAE Bound)

*   **AECB:** Credit decisioning must respect the 30-day AECB integration policy.
*   **Residency:** Cross-cloud data transfer must comply with CBUAE data-residency/sovereignty requirements.
*   **Consent:** Explicit, auditable consent for CLI application; "pre-approved" status does not bypass mandatory credit policy checks.
*   **Cooling-off:** 30-day mandate after success or failure before next offer.

## 5. Open Questions & Assumptions

### Assumptions
*   *Assumption:* The bank's existing credit-rules implementation in UiPath RPA allows for the migration to a target-state Credit Engine after Phase 1.
*   *Assumption:* Fiserv API supports asynchronous limit-update processing via MQ.

### Open Questions
*   *Question:* What is the exact regulatory stance on "pre-approved" vs "full underwriting" for this journey regarding KYC/AML refreshes?
*   *Question:* Are the existing credit rules in UiPath RPA already compliant with the target Credit Engine decision-logic model (for future alignment)?
