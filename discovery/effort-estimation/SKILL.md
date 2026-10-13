---
name: effort-estimation
owner: Delivery Management & Architecture Governance
version: 1.0.0
description: "Enterprise effort and sizing estimation skill for Product Owners, Scrum Masters, AI PMs, and Heads of IT. Maps architectural deliverables to sizing archetypes, t-shirt sizes, story points, and sprint roadmaps with FinOps and regulatory overhead adjustments."
required-inputs:
  - Architecture deliverables (HLD/LLD, C4 Model, API inventory, or Capability Gap Matrix)
  - Target jurisdiction & regulatory requirements (e.g., CBUAE, SAMA, DORA, PCI-DSS)
  - Team composition / delivery velocity assumption
expected-deliverables:
  - Effort Breakdown Structure (EBS) by architectural layer
  - Story point / sprint roadmap estimation
  - Regulatory & compliance tax multiplier calculation
  - FinOps infrastructure run-cost estimate
---

# /discovery/effort-estimation

## When to Apply
Use when a **Product Owner (PO)**, **AI Product Manager (AI PM)**, **Scrum Master (SM)**, **Head of IT**, or **Enterprise Architect** requires an objective, repeatable estimate for a banking initiative before budget sign-off or sprint planning.

## 1. Enterprise Banking Sizing Archetypes

| Archetype | Description | Base Sizing | Regulatory/Security Tax | Typical Duration |
| :--- | :--- | :--- | :--- | :--- |
| **Micro-Integration** | Single REST/Kafka route, 1-2 system endpoints | 13 - 21 pts (S) | +15% (Data validation, audit logging) | 1 - 2 Sprints |
| **New Core Service** | New domain microservice, PostgreSQL, Event Hub | 34 - 55 pts (M) | +25% (Idempotency, PCI/PII tokenization, HSM) | 3 - 5 Sprints |
| **Dual-Orchestration / Complex STP** | BPM + RPA hybrid workflow with human exceptions | 89 - 144 pts (L) | +40% (Maker-checker, CBUAE/SAMA dual reporting) | 6 - 8 Sprints |
| **AI-Native Transformation** | Local SLM/RAG integration, mobile UX, guardrails | 89 - 144 pts (L) | +35% (EU AI Act / SAMA AI ethical bias validation) | 6 - 9 Sprints |
| **Core Modernization / Greenfield Bank** | Full multi-tier banking platform replacement | 233+ pts (XL) | +50% (DORA DR testing, Basel III/IV sign-off) | 12+ Sprints |

## 2. Regulatory & Compliance Tax Multiplier
Every banking estimate applies the following multiplicative overhead factors to pure engineering effort:
* **PCI-DSS 4.0 / PII Encryption:** $\times 1.15$
* **Idempotent Core Financial Ledger Interaction:** $\times 1.20$
* **Jurisdiction Audit Trail (CBUAE / SAMA / DORA):** $\times 1.15$
* **Security & Penetration Testing Remediation Buffer:** $\times 1.10$

$$\text{Total Estimated Effort} = \text{Base Engineering Hours} \times \prod (\text{Regulatory Taxes})$$

## 3. Output Template
1. **Executive Sizing Summary:** T-shirt size, estimated sprints, team shape (FTEs).
2. **Layered Breakdown:** Mobile / BFF / Microservices / Core Adapters / Data Lakehouse.
3. **Delivery Risks & Governance Checkpoints:** Architecture Review Board (ARB), Evidence-Gate, Penetration Testing.
