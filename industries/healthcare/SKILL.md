---
name: healthcare-architecture
owner: Healthcare Solution Architecture
version: 0.1.0
description: "Use when designing HIPAA/HITECH compliant healthcare solution architectures, PHI data pipelines, and FHIR API integrations."
expected-deliverables:
  - HIPAA Compliance Matrix & BAA Audit Plan
  - HL7 FHIR Interoperability Architecture Spec
togaf-phases: [Phase C, Phase D]
---

# /industries/healthcare

## Overview
Provides architectural guardrails for regulated healthcare platforms handling Protected Health Information (PHI). Enforces HIPAA Security/Privacy Rules, HITECH Act, and HL7 FHIR API standards.

## Process
1. **PHI Boundary Definition:** Isolate electronic PHI (ePHI) in dedicated encrypted data vaults.
2. **BAA & Vendor Audit:** Ensure all cloud services (AWS/Azure/GCP) carry signed Business Associate Agreements (BAA).
3. **FHIR Interoperability:** Model clinical data exchanges using standardized HL7 FHIR v4 REST resources.
4. **Audit Trail Logging:** Enforce immutable, non-repudiable audit trails for every ePHI access event.
