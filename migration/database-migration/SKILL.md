---
name: database-migration
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when planning a banking database migration (schema, data, cutover, sync) â€” produces a DB-migration plan including core-banking data constraints."
required-inputs:
  - Source & target database schema/tech stack
  - Data privacy & residency sensitivity (PII/Payment-data)
  - Latency/throughput NFRs
  - Maintenance window/Uptime constraints
expected-deliverables:
  - Database migration strategy document
  - Data-synchronization runbook (dual-write/CDC)
  - Cutover validation plan
togaf-phases: [Phase F]
togaf-artifacts: [Migration Plan]
bian-service-domains: [Integration.Migration]
---

# /database-migration

## When to apply
Use for migrating banking data, especially core-banking or payment data. Focuses on minimizing downtime, ensuring data integrity, and respecting strict residency requirements for sensitive banking information.

## Inputs
- **Schema & Tech** â€” Source database (e.g., Oracle RAC) to target (e.g., Azure SQL, OCI Exadata).
- **Sensitive Data Profile** â€” Maps PII, PCI, and payment data for residency enforcement (PDPL).
- **Migration constraints** â€” Required downtime window, max latency, replication bandwidth.

## Process
1. **Define Data Migration Pattern.** Select from:
   - *Offline (Bulk Copy):* High downtime, simple, low risk for small static datasets.
   - *Online (CDC/Double-Write):* Near-zero downtime, high complexity, requires robust integration seams ([integration-seams](../../modernization/research/integration-seams.md)).
2. **Residency Verification.** Validate target data-storage location strictly satisfies CBUAE/PDPL residency rules for the data class in-flight ("in-country").
3. **Draft Sync/Verification strategy.** How is data validated during the migration (e.g., checksums, row-count reconciliation, dual-read compare)?
4. **Plan Cutover.** Design the final sync-and-switch: freeze source, final sync, point app to target, verify, release source-freeze (or retire source).
5. **Author DB-migration runbook.** Detailed steps, triggers, rollback procedure ([rollback-plan](../rollback-plan/SKILL.md)).

## Banking pitfalls
- **Silent data drift** â€” Replication issues or CDC-lag introduce inconsistencies between source/target without triggering failure-alerts.
- **Orphaned integrations** â€” Migrating the DB *before* updating all integrations (e.g., downstream reporting systems) breaks existing banking services.
- **Ignoring "reconciliation debt"** â€” Failing to automate the final data-validity check between source/target before cutover, necessitating manual, high-risk, time-consuming investigation.
- **Insecure migration-transit** â€” Moving sensitive payment data over networks (even cloud-internal) that lack sufficiently rigorous encryption/TLS/MTLS compliance for banking workloads.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of database-migration meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the database-migration process.**

## Outputs
- **Database migration strategy** â€” The authoritative migration approach document.
- **Data-synchronization runbook** â€” Detailed steps for dual-write or CDC-based sync.
- **Cutover validation plan** â€” Checklists to ensure data integrity pre/post-cutover.

## Related skills
- [integration-seams](../../modernization/research/integration-seams.md)
- [rollback-plan](../rollback-plan/SKILL.md)
- [production-readiness](../../governance/production-readiness/SKILL.md)

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


