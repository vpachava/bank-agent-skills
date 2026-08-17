---
name: security-nfr-baseline-check
description: Use as the mandatory first step before any architecture or design assessment to verify essential security and regulatory NFRs.
togaf-phases: [Phase D]
togaf-artifacts: [Security Baseline]
bian-service-domains: [Security.Auth]
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

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management


