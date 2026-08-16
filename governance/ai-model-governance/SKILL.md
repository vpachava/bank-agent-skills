---
name: ai-model-governance
description: Use when designing or deploying AI models that require tracking for drift, bias, and regulatory compliance.
---

# /ai-model-governance

## Overview
Provides a framework for governing AI/ML models in a banking context, focusing on operational performance (drift), fairness (bias), and adherence to regional regulatory standards (CBUAE/PDPL/AECB).

## When to Use
- Designing new AI models for credit decisioning, fraud detection, or customer insights.
- Transitioning models from PoC to production.
- Regular review of production AI models.

## Core Process
1. **Model Inventory:** Register all AI models with metadata (version, purpose, data sensitivity).
2. **Bias Assessment:** Define and track fairness metrics appropriate for the banking domain.
3. **Drift Monitoring:** Establish baselines and set alerting thresholds for performance decay/data drift.
4. **Explainability Audit:** Ensure model decisions are explainable according to regulatory requirements (e.g., adverse action notices).
5. **Regulatory Mapping:** Document compliance with regional standards (PDPL for PII, CBUAE for credit models).

## Mandatory Compliance Block
Any ADR referencing a model governed by this skill MUST include: 
- **Model Bias Risk:** [None/Low/Med/High]
- **Regulatory Jurisdiction:** [CBUAE/PDPL/Other]
- **Drift Mitigation Strategy:** [e.g., Retraining frequency, Monitoring tool]

## Related Skills
- [threat-model](../../security/threat-model/SKILL.md) (for adversarial AI threats)
- [data-governance](../../governance/data-governance/SKILL.md) (for model input/output data)
