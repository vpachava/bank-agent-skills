---
name: security-nfr-baseline-check
description: Use as the mandatory first step before any architecture or design assessment to verify essential security and regulatory NFRs.
---

# /security-nfr-baseline-check

## Overview
A mandatory checklist-based verification to be performed before any design assessment begins, ensuring essential non-functional requirements (NFRs) are defined, acknowledged, and feasible within the proposed architecture.

## When to apply
Mandatory, first-step gate before any design assessment (discovery, greenfield, modernization).

## Checklist
- [ ] **Data Residency:** Confirmed mapping of all PII/regulated data to required geographic/zone residency (CBUAE/PDPL/AECB compliant).
- [ ] **Encryption Strategy:** Confirmed at-rest and in-transit encryption standards compliant with bank policy.
- [ ] **Availability NFRs:** RTO/RPO objectives defined and baseline feasibly met by deployment topology.
- [ ] **PII/Regulated Data Identification:** All PII/regulated data paths tagged with classification level.
- [ ] **AuthN/AuthZ Baseline:** Initial alignment on identity provider fabric (e.g., UAE Pass, IAM) and zero-trust boundary strategy.

## Process
1. **Verification:** Review the raw requirement against the checklist.
2. **Identification:** Flag any missing, ambiguous, or violated NFRs as immediate blockers.
3. **Escalation:** If a blocker is identified, escalate to Architecture Board immediately; proceed only when resolved.
4. **Documentation:** Produce a `NFR-Baseline-Verdict.md` artifact.

## Outputs
- **NFR Baseline Verdict (artifact)**
- **Blocker Registry** (if any)
