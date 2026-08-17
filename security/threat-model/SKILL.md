---
name: threat-model
owner: Security Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when designing or reviewing a banking component's security posture â€” produces a threat model (STRIDE/PASTA, trust boundaries, data-flow) with findings, severities, and mitigation owners."
required-inputs:
  - Component scope & data-flow sketch
  - Trust boundaries (internal / partner / public / CBUAE-regulated zone)
  - NFRs relevant to security (availability, integrity, PII)
  - Existing controls inventory
expected-deliverables:
  - Threat model document (per in-scope component)
  - Findings register with STRIDE category & severity
  - Mitigation owners & residual-risk notes
togaf-phases: [Phase D]
togaf-artifacts: [Security Baseline]
bian-service-domains: [Security.Auth]
---

# /threat-model

## When to apply
Use whenever a banking component is being designed or materially changed, or when an existing component enters a security review. Especially load-bearing for anything crossing a trust boundary (customer-facing, partner/fintech, core-banking) or handling PII/biometrics/payment data. Closes a gap the lighter `/owasp-review` doesn't â€” this is the *structural* threat surface, not the vuln checklist.

## Inputs
- **Component scope & data-flow sketch** â€” the in-scope system boundary and what's explicitly out of scope; where data enters, moves, and persists; mark PII / payment / biometric flows.
- **Trust boundaries** â€” internal / partner-fintech / public / the CBUAE-regulated data zone; and across onshore â†” DIFC â†” ADGM where the bank straddles free zones.
- **Security-relevant NFRs** â€” availability (RTO/RPO targets), integrity (audit/provenance), confidentiality (PII, residency).
- **Existing controls inventory** â€” what's already in place so you don't re-mitigate.

## Process
1. **Scope & draw the data-flow.** Bound the component; mark data stores, flows, and external actors. Call out PII/payment/biometric flows explicitly.
   > Per OWASP, the attacker's first lever is the boundary data crosses â€” get the boundaries right before enumerating threats.

2. **Draw trust boundaries.** Internal / partner / public / the CBUAE-regulated data zone. Every boundary crossing is a threat surface. Where the bank straddles onshore + a free zone (DIFC/ADGM), the cross-zone transfer is itself a boundary worth drawing â€” it carries the SCC/BCR transfer obligation, not just a data path.

3. **Enumerate threats â€” STRIDE across each boundary & flow.**
   - **Spoofing** â€” who can impersonate an actor on this flow? (esp. fintech/partner identity, UAE Pass assertions, provider-SDK identities)
   - **Tampering** â€” can data in flight or at rest be modified? (payment amounts, KYC verdicts, provenance ledger)
   - **Repudiation** â€” can an action be denied? (audit trails, dual-sign-off ceremonies)
   - **Information disclosure** â€” PII/biometric/payment leakage; cross-border/residency exposure
   - **Denial of service** â€” availability attack on a regulated path
   - **Elevation of privilege** â€” can a role step up? (the silent privilege-creep failure mode)

4. **(Where useful) layer PASTA** for risk-anchored decomposition â€” but STRIDE is the default; don't inflate.

5. **Severity & owner each finding.** Likelihood Ã— impact against the bank's risk appetite; assign a mitigation owner; note residual risk after controls.

6. **Capture mitigations & residual risk.** Map each finding to a control (existing or new), owner, and a residual-risk statement for the risk register.
   > NIST CSF lens: each finding lands in Identify / Protect / Detect / Respond / Recover â€” useful for the compliance mapping, but STRIDE drives the enumeration.
   > UAE cyber-resilience specifically: treat **DESC / the NESAâ†’Cybersecurity Council posture / standalone CBUAE cyber-resilience rule text as MEDIUM-verify** against a current CBUAE publication before freezing a checklist (research 02's agency-site failures). The structural threat model responds to the PDPL/CBUAE-residency facts (HIGH-confidence); the DESC/CBUAE-standalone specifics should be re-pinned during build.

7. **Model the provider-SDK trust boundary explicitly.** UAE Pass / EFR / UAEKYC SDKs are trust boundaries *inside* your scope, not external-safe â€” they handle biometrics, identity assertions, and IDV capture that downstream regulated decisions depend on.

## Banking pitfalls
- **Silent privilege creep across clouds** â€” IAM drifts as AWS/Azure accounts proliferate; least-privilege rots fast. Review IAM at every threat-model refresh, not just at design.
- **Key custody split across providers** â€” secrets divided across clouds become unauditable; prefer a single custody plane + per-cloud delegation.
- **Provider-plugin trust** â€” third-party IDV/KYC SDKs (UAE Pass / EFR / UAEKYC) are trust boundaries *inside* your scope, not external-safe; model the SDKâ†’your-app boundary explicitly.
- **Audit/provenance as an afterthought** â€” field-level provenance (who/what produced a value) must be a threat you model, not a logging detail.
- **Residency leakage via logs/traces** â€” observability pipelines can exfiltrate PII across regions faster than the data store; model the telemetry path as a flow.
- **Cross-zone transfer unmodelled** â€” onshore â†” DIFC/ADGM data movement treated as an ordinary flow rather than a compliance-bearing boundary with the SCC/BCR obligation.
- **Regenerated, not living** â€” a threat model written at design and never refreshed is worse than none; tie refresh to the change-advisory path.
- **UAE cyber-rule text shipped as fact** â€” DESC / NESA-transition / CBUAE-standalone specifics are MEDIUM-synthesized (research 02); verify before freezing into a checklist, cite the regulatory facts you can pin.

## Bulletproofing against Rationalization
To prevent threat models from becoming compliance theater, you MUST:

1. **Mandatory Boundary Identification:** The model MUST explicitly name the trust boundaries crossed by the data flow.
2. **Mandatory STRIDE Application:** You MUST apply all categories (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) against every element.
3. **Mandatory Mitigation Tracing:** Every identified high/critical threat MUST link to an architectural mitigation or a signed risk acceptance.

**Violating these rules invalidates the Threat Model.**

## Outputs
- **Threat model document** â€” per in-scope component: scope, data-flow, trust boundaries, threat-by-threat findings.
- **Findings register** â€” STRIDE category, severity, owner, mitigation, residual risk (feeds `/risk-register`).
- **Mitigation owners & residual-risk notes** â€” handoff to the risk/governance track.

## Related skills
- [owasp-review](../owasp-review/SKILL.md) â€” the vuln-list review that pairs with this structural model.
- [zero-trust](../zero-trust/SKILL.md) â€” posture design this model informs.
- [iam-review](../iam-review/SKILL.md) â€” the privilege-creep pitfall, operationalized.
- [security-architecture-review](../security-architecture-review/SKILL.md) â€” the broader review this feeds.
- [compliance](../compliance/SKILL.md) â€” the UAE/CBUAE obligations that bound this model.
- [risk-register](../../documentation/risk-register/SKILL.md) â€” where findings & residual risk land.
- [landing-zone-review](../../cloud/landing-zone-review/SKILL.md) â€” where the residency/cross-zone boundary physically lives.


### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Threat modeling a new digital credit-card issuance service.
- **Architecture Lens Check:** Model the trust boundary between the mobile banking app (Public/Partner) and the `Credit-Card-Origination` service (Regulated).
- **Sample Outcome:** "STRIDE Threat: [Tampering] - malicious actor could inject fake credit-limit request into the API gateway. Mitigation: Implement mTLS and per-request AECB score verification."
- **Common Pitfall:** Modeling the public-facing API endpoint as a secure boundary without accounting for the `UAE Pass` assertion being hijacked at the mobile-client-to-gateway layer.

#### (2) Customer Profile Management Example
**Scenario:** Threat modeling the profile management dashboard.
- **Architecture Lens Check:** Identify threats to PII as it traverses the trust boundary between onshore mobile and offshore data-analytics zones.
- **Sample Outcome:** "Information Disclosure Threat: [Data Residency] - PII leakage into non-resident logs during profile updates. Mitigation: PII masking pipeline enabled for telemetry across cross-zone boundaries."
- **Common Pitfall:** Treating data movement across free-zone boundaries (e.g., Onshore to DIFC) as simple intra-network flow, ignoring the mandatory SCC/BCR transfer audit requirements.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Threat modeling a Sharia-compliant loan origination process.
- **Architecture Lens Check:** Identify spoofing/tampering threats affecting the `Internal Sharia Governance Board` workflow sign-off, which relies on a deterministic internal ledger.
- **Sample Outcome:** "Spoofing Threat: [Repudiation] - Sharia Board signature spoofed via service-account compromise. Remediation: Implement dual-sign-off mandate using non-repudiable biometric signing from Sharia Board members."
- **Common Pitfall:** Assuming internal Service Account identities for Sharia Board sign-off are structurally secure, thereby failing to model the elevation of privilege risk when those accounts are compromised.
### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Conducting threat modeling exercises at the very end of the software development lifecycle**
  - **Consequence:** Discovered flaws (like a lack of encryption on a legacy link) require tearing down the codebase and delaying the launch by months.
  - **Correct Approach:** Model threats during the initial design phase before writing code, using frameworks like STRIDE or PASTA.
- **Modeling threats using generic components rather than accurate system boundaries and data flows**
  - **Consequence:** Missing critical spoofing or tampering threats because specific network hops and data payload trust boundaries were omitted.
  - **Correct Approach:** Build the threat model exclusively on top of a detailed L3 C4 Container diagram mapping precise data flow Trust Boundaries.
- **Detailing exhaustive lists of theoretical threats without realistic, actionable mitigation plans**
  - **Consequence:** The threat model becomes empty paperwork; developers ignore it and deploy the vulnerabilities anyway.
  - **Correct Approach:** Tie every identified threat to a specific, tracked engineering task (e.g., "Implement TLS 1.3 on API edge") in the backlog.
