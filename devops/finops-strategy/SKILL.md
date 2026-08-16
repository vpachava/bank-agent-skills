---
name: finops-strategy
owner: DevOps
version: 0.1.0
last-reviewed: 2026-08-16
description: Use for cloud cost optimization, specifically for high-frequency financial workloads in banking environments.
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
