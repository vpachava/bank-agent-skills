---
name: platform-selection
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when evaluating cloud/provider/runtime platform options for a new banking banking initiative — produces a platform-selection decision (weighted score & risk-profile)."
required-inputs:
  - Banking initiative scope, complexity & NFRs
  - Relevant BIAN domain capabilities
  - Data-residency & UAE-regulatory constraints
  - Regulatory-exposure class (payment/KYC/core vs periphery)
  - Existing platform standards
expected-deliverables:
  - Platform-selection decision document
  - Capability alignment & weighting table
  - Banking-specific risk assessment
---

# /platform-selection

## When to apply
Use during the greenfield initiative-scoping phase to rigorously evaluate potential platforms (e.g., Azure vs AWS vs OCI/Private, PaaS vs K8s-native, microservices vs monolith-modernisation) against pre-agreed banking criteria. Moves the platform choice from "an architect's preference" to a documented, scored, and regulatory-defensible decision.

## Inputs
- **Initiative scope & NFRs** — criticality, concurrency, latency, availability, data-residency, security-sensitivity.
- **BIAN domain capabilities** — needed service domains BIAN-grounded (cross-link to BIAN mapping).
- **Compliance & residency** — CBUAE residency (in-country primary + separate-location backup requirement), free-zone SCC/BCR posture.
- **Regulatory-exposure class** — mapped to risk-appetite for platform novelty.

## Process
1. **Define the assessment criteria.** Select and weight criteria:
   - Compliance & Residency (mandatory gate).
   - Architectural fit (BIAN domain capability footprint).
   - Resilience (availability, DR, CBUAE regulatory expectation).
   - Operational cost & complexity (multi-cloud tax, platform-team maturity).
   - Security posture (Identity fabric, secrets, data-protection).
   - Ecosystem support (Oracle-core integration, vendor-support/Ecosystem).
2. **Assign candidate platforms.** e.g., Azure (`uaenorth`/`uaecentral`) vs AWS (`me-central-1`) vs hybrid/OCI.
3. **Score against weighted criteria.** Use a 1-5 scale per criterion×weight.
4. **Conduct a banking-specific risk assessment.**
   - Residency-fail risk per region-capacity.
   - Cross-zone transfer friction (per PDPL/DIFC/ADGM).
   - Oracle-core integration-tax per platform.
   - Skill-availability gap (e.g. AWS vs Azure teams).
5. **Issue recommendation & trade-off rationale.** Document why the selected platform is the best risk-adjusted fit, and explicitly state what the runner-up does *better*.

## Banking pitfalls
- **Unweighted "gut-feel" selection** — selecting based on vendor relationship or "what the team knows" without weighting compliance/resiliency.
- **Ignoring the in-country residency gate** — scoring a region-platform that can't meet CBUAE payment-data-residency rules (e.g. non-UAE region).
- **Ignoring the integration-tax** — cost of integration with on-prem Oracle core or OCI-hosted Exadata Cloud at Customer is usually the dominant cost driver.
- **Multi-cloud tax invisibility** — failing to account for the cost of maintaining multi-cloud security tooling, connectivity, and IAM sprawl.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of platform-selection meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the platform-selection process.**

## Outputs
- **Platform-selection decision document** — the verdict, criteria, and weighted decision-matrix.
- **Weighting & capability table** — formal scoring output.
- **Banking-specific risk assessment** — dedicated risk section on regulatory/operational/residency exposure.

## Related skills
- [reference-architecture](../reference-architecture/SKILL.md) — where the selected platform is anchored.
- [compliance](../../security/compliance/SKILL.md) — residency and transfer basis constraints.
- [modernization-roadmap](../../modernization/modernization-roadmap/SKILL.md) — sequencing dependencies on the platform.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

