# Target Architecture: CLI Automation Platform

## 1. High-Level Architecture (C4 Context/Container)

The CLI platform integrates distributed cross-cloud (AWS/Azure) and on-premises (core bank) components.

- **On-Premises (Onshore):** Fiserv/Fiserv-Adapter, Operational Data Store (ODS), Enterprise Data Warehouse (DWH), Enterprise MQ (Fiserv response).
- **Azure:** UiPath RPA (Orchestration & Rules), RPA Database.
- **AWS:** Digital Engagement API, Amazon MQ, Event Hub (Notification Broker), Notification Center, Middleware, PostgreSQL (Application Store).

A formal C4 container diagram is needed to visualize:
[User] -> [Mobile App] -> [Digital Engagement API] -> [Amazon MQ] -> [UiPath RPA] -> [Credit Engine/AECB/DMS] ...

## 2. Key Architectural Decisions (ADRs)
- **ADR-0001: Orchestration Strategy (Hybrid):** RPA manages Phase 1 orchestration/rules, API-first interfaces allow eventual migration to Credit Engine.

## 3. Data Ownership & Flow
- **System of Record:** Fiserv (Card Limit/Status).
- **Orchestration Staging:** RPA Database (used for processing state, not long-term persistence).
- **Application Engagement:** PostgreSQL (Offer/Consent/Status).

## 4. Key Security & Compliance Posture
- **Regulatory:** UAE/CBUAE compliance for AECB report usage (30-day freshness rule).
- **Integration:** Azure AD for RPA service-to-service auth.
- **Data Protection:** Card hash used as business identifier; PII minimization in messages/URL deep links.

## 5. Non-Functional Targets (Headline)
- **Availability:** 99.95% (Customer journey endpoints).
- **Capacity:** ~3,000 offers/week.

## 6. Open Questions
- AECB integration pattern confirmation (Real-time vs Batch retrieval).
- Fiserv API capability confirmation for async limit updates via MQ.
