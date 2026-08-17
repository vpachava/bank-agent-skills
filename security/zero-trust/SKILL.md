---
name: zero-trust
owner: Security Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when designing the trust posture for a banking estate that no perimeter can hold â€” produces a zero-trust design (identity segmentation, mTLS, policy-as-code, micro-perimeters) with the UAE identity fabric and cross-zone posture addressed."
required-inputs:
  - The estate's identities & service inventory
  - Current network segmentation & the cloud landing zone
  - UAE identity fabric context (UAE Pass, EFR, UAEKYC) where relevant
  - Residency / cross-zone obligations (onshore â†” DIFC/ADGM)
expected-deliverables:
  - Zero-trust posture design (identity-, segmentation-, micro-perimeter-)
  - Policy-as-code locations & enforcement planes
  - Cross-zone & provider-SDK trust treatment
togaf-phases: [Phase D]
togaf-artifacts: [Security Baseline]
bian-service-domains: [Security.Auth]
---

# /zero-trust

## When to apply
Use to design the trust posture â€” when the bank's perimeter (legacy core + multi-cloud + partner/fintech + AI tiers) no longer has a defensible edge, and trust must be asserted per-request, per-identity, per-segment. Feeds `/security-architecture-review`, `/iam-review`, and `/landing-zone-review`.

> The bank has no perimeter. The legacy core, multiple clouds, partners, and AI tiers each have their own boundary â€” "inside the network" stopped being a useful security concept. NIST Zero-Trust Architecture (SP 800-207) frames the posture; this skill applies it.

## Inputs
- **Identities & service inventory** â€” workloads + humans + partner/fintech identities; the things that assert trust.
- **Current network segmentation & cloud landing zone** â€” the existing boundary structure to evolve, not tear down.
- **UAE identity fabric context** â€” UAE Pass (national ID/SSO), EFR / UAEKYC (IDV/KYC SDKs) where the surface involves identity verification.
- **Residency / cross-zone obligations** â€” onshore â†” DIFC/ADGM transfer obligation; PII/payment residency.

## Process

1. **Adopt the three tenets explicitly: never trust, always verify; assume breach; verify explicitly.** State them as design constraints for every component, not a slogan. Every request asserts identity, context, and policy â€” no implicit trust from network location.

2. **Anchor trust in identity, not network.** Authenticate every workload and human identity (SPIFFE/SPIRE or equivalent for workloads, OAuth2/FAPI2/mTLS for users/partners); service-to-service calls carry workload identity, not a trusted-network assumption. The bank's legacy core was built on implicit-network trust; zero-trust means the core's callers now assert identity too.

3. **Segment by micro-perimeters, not a flat internal.** Around each capability/service-domain, a policy-controlled boundary; lateral movement between segments requires re-assertion. The legacy core is its own segment, the AI tier is its own, partner/fintech its own; cross-segment is policy-mediated, not open.

4. **Enforce policy at the access plane, as code.** Policy-as-code at the micro-perimeter boundary (an API gateway, a service mesh sidecar, the cloud landing-zone guardrails); policy changes ship as code (not config-fiddling), audited, with a canary path. The DNSP is the decision point; enforcement sits at the perimeter.

5. **Treat the UAE identity fabric as identity, not a trust transfer.** UAE Pass is an identity *assertion* / SSO layer; EFR/UAEKYC own the authoritative IDV (face-match/liveness/capture). Zero-trust consumes their *assertions*, validates per-use, and never grants downstream rights solely on "UAE Pass logged them in."

6. **Govern the cross-zone transfer explicitly.** Where data crosses onshore â†” DIFC/ADGM, zero-trust enforces the SCC/BCR transfer basis *at the boundary*, logs the transfer with provenance, and treats the free zone as a separate trust domain. Don't fold a free-zone into "internal."

7. **Treat provider SDKs and partner integrations as untrusted by default.** Third-party IDV/KYC SDKs and fintech integrations are workloads that need identity, scopes, and an enforcement point at the SDKâ†’your-app seam.

8. **Make the policy enforcement observable.** Every policy decision is logged (decision + identity + action + context); the zero-trust posture's health is a telemetry surface, not a hope.

## Banking pitfalls
- **"Inside the network" inheritance** â€” granting trust because a call comes from "the corporate network" / "an internal subnet"; the whole point is to stop inheriting trust from network location.
- **Single perimeter, not micro-perimeters** â€” a flat internal where a partner compromise or a pod-hopped AI agent can reach the core; segment per capability with re-assertion across boundaries.
- **UAE Pass treated as trust transfer**
- the SSO logged you in, therefore everything is permitted; zero-trust consumes the *assertion* per-use, scopes-down, never inherits full rights.
- **Cross-zone folded into "internal"** â€” treating DIFC/ADGM as just another subnet; the transfer carries the SCC/BCR obligation and is a separate trust domain.
- **Policy in configs, not code** â€” policy changed by hand at a console, unaudited, with no canary; policy-as-code with audit + canary or it drifts.
- **Workload identity unauthenticated** â€” service-to-service assumed trusted on the network; SPIFFE/mTLS or equivalent so a pod-hopping attacker can't impersonate a service.
- **Enforcement point bypassable** â€” a "trusted" internal path that skips the policy decision point; enforcement must sit at every micro-perimeter, no bypass.
- **Desc/CBUAE cyber-rule text as fact** â€” verify the UAE-cyber-standards specifics before freezing into the policy-as-code (MEDIUM-verify per research 02).

## Bulletproofing against Rationalization
To prevent implicit trust from compromising the network, you MUST:

1. **Mandatory Network Segmentation:** The design MUST explicitly enforce micro-segmentation. "Internal network is trusted" assumptions are rejected.
2. **Mandatory Continuous Authentication:** Verification MUST occur at every transaction layer, not just the perimeter gateway.
3. **Device Health Verification:** The architecture MUST explicitly block access from unmanaged or unhealthy end-user devices.

**Violating these rules invalidates the Zero Trust architecture.**

## Outputs
- **Zero-trust posture design** â€” identity-anchored, micro-perimeter segmented, policy-as-code at the boundary.
- **Policy enforcement locations** â€” per micro-perimeter, the decision point and enforcement plane.
- **Cross-zone & provider-SDK treatment** â€” transfer-basis-logged + provider-SDK-as-untrusted-workload.
- **Observability posture** â€” policy decisions logged.

## Related skills
- [iam-review](../iam-review/SKILL.md) â€” the identity/scopes this leans on.
- [landing-zone-review](../../cloud/landing-zone-review/SKILL.md) â€” where the segmentation/policy physically lives.
- [security-architecture-review](../security-architecture-review/SKILL.md) â€” the review that gates this posture.
- [threat-model](../threat-model/SKILL.md) â€” the trust boundaries this operationalizes.
- [compliance](../compliance/SKILL.md) â€” the UAE/CBUAE rules the cross-zone posture honors.
- [api-design](../../integration/api-design/SKILL.md) â€” the authn/z contract surface.
- [kubernetes](../../cloud/kubernetes/SKILL.md) / [terraform](../../cloud/terraform/SKILL.md) â€” where workload identity + policy-as-code ship.


### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Zero-trust design for a digital credit card issuance platform.
- **Architecture Lens Check:** Implementation of mutual-TLS (mTLS) for all service-to-service communication between the `Origination-Service` and the `AECB-Interface`, explicitly rejecting identity inheritance from network segment.
- **Sample Outcome:** "Zero-Trust Design: Identity-anchored perimeter; each service-to-service call consumes per-transaction workload identity tokens."
- **Common Pitfall:** Relying on network-level IP allow-listing (e.g., firewall policy) instead of workload identity (SPIFFE) to authorize service-to-service calls.

#### (2) Customer Profile Management Example
**Scenario:** Trust posture for cross-zone (onshore â†” DIFC) profile dashboard updates.
- **Architecture Lens Check:** Enforcing separate identity per-zone with SCC-logged transfer basis for identity assertions moving across the `Onshore` and `DIFC` boundaries.
- **Sample Outcome:** "Policy-as-code: Enforcing strict per-zone identity validation for profile-update request from mobile dashboard."
- **Common Pitfall:** Treating the bank's entire environment (DIFC + Onshore) as a single flat internal network, enabling unauthorized cross-zone data movement without provenance logs.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Trust design for Sharia-compliant loan workflow and its `Internal Sharia Board` verification.
- **Architecture Lens Check:** Micro-segmentation around the `Loan Origination Service` ensuring the `Sharia-Governance-Engine` acts as a separate, policy-controlled trust domain.
- **Sample Outcome:** "Policy-as-code: Decision point at boundary gate ensuring all amendment requests carry valid crypto-signature from authorized Sharia Board members."
- **Common Pitfall:** Allowing the `Origination Service` to access or modify loan-structure business rules directly without traversing the required policy-gateway (Trust Anchor) check.
### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management


