---
name: finops-strategy
owner: DevOps
version: 0.1.0
last-reviewed: 2026-08-16
description: Use for cloud cost optimization, specifically for high-frequency financial workloads in banking environments.
togaf-phases: [Phase G]
togaf-artifacts: [Compliance Checklist]
bian-service-domains: [Security.Auth]
---

# /finops-strategy

## Overview
A framework for managing cloud expenditure, balancing performance, resilience, and cost, with a focus on bank-grade high-frequency workloads.

## When to Use
- Designing cloud architectures for cost-efficiency.
- Ongoing monitoring and optimization of cloud spend.
- Setting up automated alert and remediation workflows for cost anomalies.

## Core Principles
1. **Visibility:** Granular tagging and cost allocation by business capability.
2. **Optimization:** Right-sizing, reserved instances/savings plans, and spot instance usage for non-critical workloads.
3. **Accountability:** Business unit-level accountability for cloud spend.
4. **Resilience Awareness:** Cost optimization must not degrade RTO/RPO objectives.

## Banking High-Frequency Workload Patterns
1. **Tiered Storage:** Moving non-critical hot data to cold storage tiers automated based on access patterns.
2. **Burst Load Management:** Utilizing serverless and horizontal auto-scaling to avoid over-provisioning for peak traffic.
3. **Automated Cleanup:** Ephemeral environment management and automated deletion of unused resources.

## Mandatory Compliance Block
Any FinOps ADR MUST include:
- **Cost Impact:** Projected monthly saving/spend for the workload.
- **Resource Lifecycle:** Automated resource deletion policies (TTL) or retention policies.
- **Compliance Alignment:** Confirmation that cost-saving measures do not violate data sovereignty or performance NFRs.

## Related Skills
- [observability](../observability/SKILL.md)
- [cicd-review](../cicd-review/SKILL.md)

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


