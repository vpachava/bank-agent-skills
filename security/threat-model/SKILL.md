---
name: threat-model
owner: Security Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when designing or reviewing a banking component's security posture — produces a threat model (STRIDE/PASTA, trust boundaries, data-flow) with findings, severities, and mitigation owners."
required-inputs:
  - Component scope & data-flow sketch
  - Trust boundaries (internal / partner / public / CBUAE-regulated zone)
  - NFRs relevant to security (availability, integrity, PII)
  - Existing controls inventory
expected-deliverables:
  - Threat model document (per in-scope component)
  - Findings register with STRIDE category & severity
  - Mitigation owners & residual-risk notes
---

# /threat-model

## When to apply
Use whenever a banking component is being designed or materially changed, or when an existing component enters a security review. Especially load-bearing for anything crossing a trust boundary (customer-facing, partner/fintech, core-banking) or handling PII/biometrics/payment data. Closes a gap the lighter `/owasp-review` doesn't — this is the *structural* threat surface, not the vuln checklist.

## Inputs
- **Component scope & data-flow sketch** — the in-scope system boundary and what's explicitly out of scope; where data enters, moves, and persists; mark PII / payment / biometric flows.
- **Trust boundaries** — internal / partner-fintech / public / the CBUAE-regulated data zone; and across onshore ↔ DIFC ↔ ADGM where the bank straddles free zones.
- **Security-relevant NFRs** — availability (RTO/RPO targets), integrity (audit/provenance), confidentiality (PII, residency).
- **Existing controls inventory** — what's already in place so you don't re-mitigate.

## Process
1. **Scope & draw the data-flow.** Bound the component; mark data stores, flows, and external actors. Call out PII/payment/biometric flows explicitly.
   > Per OWASP, the attacker's first lever is the boundary data crosses — get the boundaries right before enumerating threats.

2. **Draw trust boundaries.** Internal / partner / public / the CBUAE-regulated data zone. Every boundary crossing is a threat surface. Where the bank straddles onshore + a free zone (DIFC/ADGM), the cross-zone transfer is itself a boundary worth drawing — it carries the SCC/BCR transfer obligation, not just a data path.

3. **Enumerate threats — STRIDE across each boundary & flow.**
   - **Spoofing** — who can impersonate an actor on this flow? (esp. fintech/partner identity, UAE Pass assertions, provider-SDK identities)
   - **Tampering** — can data in flight or at rest be modified? (payment amounts, KYC verdicts, provenance ledger)
   - **Repudiation** — can an action be denied? (audit trails, dual-sign-off ceremonies)
   - **Information disclosure** — PII/biometric/payment leakage; cross-border/residency exposure
   - **Denial of service** — availability attack on a regulated path
   - **Elevation of privilege** — can a role step up? (the silent privilege-creep failure mode)

4. **(Where useful) layer PASTA** for risk-anchored decomposition — but STRIDE is the default; don't inflate.

5. **Severity & owner each finding.** Likelihood × impact against the bank's risk appetite; assign a mitigation owner; note residual risk after controls.

6. **Capture mitigations & residual risk.** Map each finding to a control (existing or new), owner, and a residual-risk statement for the risk register.
   > NIST CSF lens: each finding lands in Identify / Protect / Detect / Respond / Recover — useful for the compliance mapping, but STRIDE drives the enumeration.
   > UAE cyber-resilience specifically: treat **DESC / the NESA→Cybersecurity Council posture / standalone CBUAE cyber-resilience rule text as MEDIUM-verify** against a current CBUAE publication before freezing a checklist (research 02's agency-site failures). The structural threat model responds to the PDPL/CBUAE-residency facts (HIGH-confidence); the DESC/CBUAE-standalone specifics should be re-pinned during build.

7. **Model the provider-SDK trust boundary explicitly.** UAE Pass / EFR / UAEKYC SDKs are trust boundaries *inside* your scope, not external-safe — they handle biometrics, identity assertions, and IDV capture that downstream regulated decisions depend on.

## Banking pitfalls
- **Silent privilege creep across clouds** — IAM drifts as AWS/Azure accounts proliferate; least-privilege rots fast. Review IAM at every threat-model refresh, not just at design.
- **Key custody split across providers** — secrets divided across clouds become unauditable; prefer a single custody plane + per-cloud delegation.
- **Provider-plugin trust** — third-party IDV/KYC SDKs (UAE Pass / EFR / UAEKYC) are trust boundaries *inside* your scope, not external-safe; model the SDK→your-app boundary explicitly.
- **Audit/provenance as an afterthought** — field-level provenance (who/what produced a value) must be a threat you model, not a logging detail.
- **Residency leakage via logs/traces** — observability pipelines can exfiltrate PII across regions faster than the data store; model the telemetry path as a flow.
- **Cross-zone transfer unmodelled** — onshore ↔ DIFC/ADGM data movement treated as an ordinary flow rather than a compliance-bearing boundary with the SCC/BCR obligation.
- **Regenerated, not living** — a threat model written at design and never refreshed is worse than none; tie refresh to the change-advisory path.
- **UAE cyber-rule text shipped as fact** — DESC / NESA-transition / CBUAE-standalone specifics are MEDIUM-synthesized (research 02); verify before freezing into a checklist, cite the regulatory facts you can pin.

## Bulletproofing against Rationalization
To prevent threat models from becoming compliance theater, you MUST:

1. **Mandatory Boundary Identification:** The model MUST explicitly name the trust boundaries crossed by the data flow.
2. **Mandatory STRIDE Application:** You MUST apply all categories (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) against every element.
3. **Mandatory Mitigation Tracing:** Every identified high/critical threat MUST link to an architectural mitigation or a signed risk acceptance.

**Violating these rules invalidates the Threat Model.**

## Outputs
- **Threat model document** — per in-scope component: scope, data-flow, trust boundaries, threat-by-threat findings.
- **Findings register** — STRIDE category, severity, owner, mitigation, residual risk (feeds `/risk-register`).
- **Mitigation owners & residual-risk notes** — handoff to the risk/governance track.

## Related skills
- [owasp-review](../owasp-review/SKILL.md) — the vuln-list review that pairs with this structural model.
- [zero-trust](../zero-trust/SKILL.md) — posture design this model informs.
- [iam-review](../iam-review/SKILL.md) — the privilege-creep pitfall, operationalized.
- [security-architecture-review](../security-architecture-review/SKILL.md) — the broader review this feeds.
- [compliance](../compliance/SKILL.md) — the UAE/CBUAE obligations that bound this model.
- [risk-register](../../documentation/risk-register/SKILL.md) — where findings & residual risk land.
- [landing-zone-review](../../cloud/landing-zone-review/SKILL.md) — where the residency/cross-zone boundary physically lives.
