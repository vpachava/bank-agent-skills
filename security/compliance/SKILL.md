---
name: compliance
owner: Architectural Governance
version: 0.1.1
last-reviewed: 2026-08-16
description: Use when verifying an architecture against local rules, ensuring PCI-DSS, CBUAE, NESA, or GDPR regulations are strictly enforced.
---

# /compliance

## Focus Areas
- Automated AML surveillance.
- Automated regulatory report generation (RegTech).

## Automated Regulatory Reporting (RegTech) Integration Patterns
To ensure scalable and accurate regulatory reporting, all automated compliance solutions MUST include:
1. **Data Lineage:** Provenance tracing from raw transaction data to regulatory report output (traceability).
2. **Schema Standardization:** Adherence to regulatory reporting data standards (e.g., XBRL for CBUAE, ISO 20022 messages).
3. **Automated Submission:** API-based integration with regulator portals where applicable.
4. **Immutable Audit Trail:** All generated reports and their source data snapshots MUST be archived in an immutable data store.

## When to apply
Use when verifying an architecture against local rules, ensuring PCI-DSS, CBUAE, NESA, or GDPR regulations are strictly enforced.

## Process
1. **Constraint Mapping**: Identify applicable regulatory/security controls for the scope.
2. **Automated Verification**: Implement hooks for AML and regulatory reporting, following the RegTech integration patterns.
3. **Audit Artifact Generation**: Ensure immutable evidence trail for regulators.

## Outputs
- **Compliance Control Map** (requirement mapping).
- **Automated Verification Hooks** (AML/Report generation configs).
- **Compliance Audit Artifacts**.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of compliance meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the compliance process.**
