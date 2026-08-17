---
name: ai-governance
owner: Security & Architecture
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when evaluating an architecture implementing LLMs or predictive models to enforce CBUAE boundary constraints, prompt security, and fallback rules."
required-inputs:
  - Architecture diagram detailing the AI interaction boundaries
  - Data privacy mapping for PII and financial datasets
  - LLM invocation paths (internal vs external cloud)
expected-deliverables:
  - LLM Data Residency sign-off
  - Semantic Guardrail configuration
  - Deterministic Fallback mechanism approval
---

﻿---
name: ai-model-governance
description: Framework for monitoring AI model performance, drift, and regulatory compliance.
metadata:
  type: reference
---

# /ai-model-governance

## Objective
Ensure AI-based credit/decisioning models adhere to regulatory standards and maintain operational integrity.

## Key Components
- **Model Inventory:** Catalog of all active models, versions, and training data provenance.
- **Drift Monitoring:** Automated alerts for performance degradation (e.g., population stability index checks).
- **Compliance Guardrails:** Automated bias assessments and audit-trail generation for explainability (e.g., SHAP/LIME integration).

## When to apply
Use when evaluating an architecture implementing LLMs or predictive models to enforce CBUAE boundary constraints, prompt security, and fallback rules.

## Process
1. **Perimeter Assessment**: Boundary check (PII/Financial data isolation).
2. **Hardening**: Apply semantic/prompt injection guardrails.
3. **Traceability**: Audit log setup for AI decisions.
4. **Resilience**: Validate deterministic fallback mechanism.

## Outputs
- **AI Boundary Sign-off** (residency/isolation).
- **Guardrail Configuration** (injection/bias mitigation).
- **Audit-Trail Specs** (for regulated output).
- **Deterministic Fallback Approval**.

## Why:
AI models in banking require proactive governance to satisfy CBUAE and other regulatory requirements regarding fairness, transparency, and accountability.
## Bulletproofing against Rationalization
To prevent compliance breaches and unchecked data exfiltration via LLMs, you MUST:

1. **Mandatory PII/Financial Data Boundary:** The governance gate MUST explicitly verify that no production PII, PCI, or strategic financial data enters an untrusted or non-residency-compliant external LLM API boundary.
2. **Mandatory Prompt Injection Hardening:** Consumer-facing LLM deployments MUST explicitly document and test semantic guardrails, rate limiters, and prompt injection defensive blocks.
3. **Mandatory Audit Logging for Regulated Output:** If AI generates content impacting a customer's financial posture or access, the prompt AND the generated output MUST be immutably retained in standard audit logs.
4. **Mandatory Deterministic Fallback:** Any probabilistic AI process in a critical path MUST possess a deterministic, rule-based fallback mechanism for handling LLM latency or hallucination failures.

**Violating these rules invalidates the AI Governance gate.**


### Banking Context & Examples

#### (1) Retail Banking Scenario
**Scenario:** Applying this skill in a retail bank core-modernization effort.
- **Architecture Lens Check:** Verification of compliance with CBUAE data-residency rules (e.g. [[compliance]]).
- **Sample Outcome:** "Design: Automated workflow integration; [[observability]] logs scrubbed of PII."
- **Common Pitfall:** Ignoring the Sharia-governance impact on the product-schema.

#### (2) Corporate Banking Scenario
**Scenario:** Using this skill for a corporate digital-onboarding integration.
- **Architecture Lens Check:** Alignment with AECB credit-reporting integration for legal-entity applicants.
- **Sample Outcome:** "Design: Integration-seam validated for high-assurance KYC; [[api-design]] handles large payload-signatures."
- **Common Pitfall:** Bypassing the mandatory legal-entity KYC check due to tight project timelines.

#### (3) Islamic Banking Scenario
**Scenario:** Utilizing this skill for Sharia-compliant loan product rollouts.
- **Architecture Lens Check:** Sharia-Board approval workflow documented within the [[architecture-decision-records]].
- **Sample Outcome:** "Design: Profit-distribution calculation encapsulated; [[api-design]] schema includes mandatory Sharia-compliance flag."
- **Common Pitfall:** Applying standard interest-based loan models to Islamic products, violating compliance.
