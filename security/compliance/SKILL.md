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


### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Compliance review for a new digital-only credit card issuance service.
- **Architecture Lens Check:** Verification of `AECB` data-sharing regulatory compliance and `CBUAE` Consumer Protection requirements.
- **Sample Outcome:** "Compliance Control Map: Verified AECB consent management workflows; AML monitoring enabled for initial credit card limit adjustment."
- **Common Pitfall:** Assuming `AECB` reporting is automatically handled by the core bank system without ensuring the new digital service correctly feeds the reporting pipeline.

#### (2) Customer Profile Management Example
**Scenario:** Compliance check for a cross-border customer dashboard.
- **Architecture Lens Check:** Review against `PDPL` (Personal Data Protection Law) data-residency requirements specifically ensuring non-UAE PII is isolated according to established residency rules.
- **Sample Outcome:** "Verification: Implemented data access controls to strictly isolate residency-restricted data sets as per CBUAE and PDPL directives."
- **Common Pitfall:** Failing to verify that customer data accessed outside of the UAE via the mobile dashboard is compliant with valid data transfer mechanisms (BCR/SCCs).

#### (3) Lending/Loans Onboarding Example
**Scenario:** Compliance review for a Sharia-compliant loan origination process.
- **Architecture Lens Check:** Compliance validation for `Sharia-Compliant Loan Structuring` and `AML` screening protocols.
- **Sample Outcome:** "Governance: Validated product structure against Internal Sharia Governance Board standards and confirmed automated AML screening integration."
- **Common Pitfall:** Ignoring the regulatory requirement to validate the *Sharia* appropriateness of the loan product structure, focusing solely on technical KYC compliance.