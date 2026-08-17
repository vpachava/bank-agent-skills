---
name: database-design
description: Use when designing database schemas and infrastructure, including vector database integration for AI-native workloads.
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---

# /database-design

## Overview
Standards for relational and non-relational database design, with specific focus on high-performance, resilient, and AI-native vector requirements.

## When to Use
- Designing schemas for core banking domains.
- Integrating vector databases for AI-native workloads.
- Infrastructure choices (RDBMS vs NoSQL vs Vector).

## Core Principles
1. **Schema Integrity:** Normalization vs De-normalization balance based on read/write patterns.
2. **Resilience & Availability:** Replication, sharding, and backup/recovery strategies.
3. **AI-Native Integration (Vector):** Design patterns for vector embedding persistence and retrieval.
4. **Data Sovereignty:** Alignment with regional data residency requirements.

## Vector Database Integration Patterns
1. **Embedding Storage:** Structured storage for high-dimensional vector embeddings with associated metadata.
2. **Retrieval Strategy:** Hybrid search enablement (vector similarity + metadata filtering).
3. **Synchronization:** Ensuring embedding updates maintain consistency with source transaction data.

## Mandatory Compliance Block
Any ADR referencing a database design MUST include: 
- **Data Classification:** [Public/Internal/Restricted/Confidential]
- **Residency Requirement:** [Onshore/Cloud-Regional/None]
- **Performance Expectation:** [IOPS/Latency/Throughput]

## Related Skills
- [data-governance](../../governance/data-governance/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)

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


