---
name: architecture-review
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when a banking design needs review against standards & lenses — produces an architecture review report (BIAN/TOGAF fit, NFRs, integration/security, risks) with findings, severity, and owners."
required-inputs:
  - The design artifact to review (HLD, LLD, or design doc)
  - Bank architecture standards & guardrails
  - Reference architecture where one exists (/reference-architecture)
  - Regulatory constraints (UAE/CBUAE) and NFRs
expected-deliverables:
  - Architecture review report (lenses applied, findings by severity)
  - Per-finding owner & remediation path (to ADR / redesign / accept)
  - Verdict: approved / approved-with-conditions / rework
---

# /architecture-review

## When to apply
Use before a design reaches the build or board — to check fit against standards, the reference architecture, NFRs, and the security/integration/residency obligations. Lighter/fast for an HLD, deeper for an LLD. Pairs with `/design-review` (component-focused) and feeds `/architecture-board` (the gate).

## Process
1. **Scope Classification**: Define whether this is a go/no-go or a shaping review.
2. **Lens Application**: Run the stack (BIAN fit, TOGAF coherence, NFR commitment, integration, security residency, resilience).
3. **Finding Attribution**: Score severity (Critical/Major/Minor) and assign remediation paths.
4. **Verdict Generation**: Issue final status (Approved / Conditional / Rework) with formal gating.

## Outputs
- **Architecture review report** — findings per lens, severity, and owner.
- **Verdict & Conditions** — documented gate decision.
- **Remediation Register** — cross-linked to RAID/ADR logs.

## Inputs
- **The design artifact** — HLD, LLD, or full design doc.
- **Bank architecture standards & guardrails** — reference architectures, mandated patterns, the guardrails (residency, security, tooling).
- **Reference architecture** where one exists — the design is reviewed against it for fit.
- **Regulatory constraints** — UAE/CBUAE, residency, KYC/AML, free-zone cross-border.
- **NFRs** — to verify the design commits them.

## Process
1. **State the review's scope & verdict criterion up front.** Is this a go/no-go for build, or a shaping review of a draft? Different bars; name it so findings land at the right severity.

2. **Apply the lens stack, one at a time:**
   - **Capability fit (BIAN)** — does the design's capability vocabulary align with the bank's BIAN map; selective-decomposition fit, not full-322 compliance; gaps surfaced.
   - **Method coherence (TOGAF)** — does the design follow the phase flow; are inputs/assumptions traceable to the requirements baseline.
   - **NFR commitment** — does the design actually commit the NFRs (RTO/RPO, residency, perf, audit), not just cite them.
   - **Integration** — does it honor the seams (API-gateway, ACL, strangler-fig, idempotency, reconciliation).
   - **Security & residency** — does it apply zero-trust, mark the residency perimeter, honor the cross-zone SCC/BCR obligation.
   - **External Exfiltration Boundary** — does the design explicitly map and classify all external data interactions (PII, Financial, Internal) and location boundaries (Onshore, DIFC, Offshore)? Any unclassified external interaction is a critical finding.
   - **Resilience** — HA/DR pairing & failover runbook committed.
   - **Reuse vs. replace** — does it honor reuse-over-rewrite against the legacy core.

3. **Score findings by severity — Critical / Major / Minor.** Critical blocks build (regulatory breach, missing NFR commitments, integration seam broken). Major requires remediation before approval. Minor are improvement notes. Avoid severity inflation — reserve Critical for actual-blocking.

4. **Assign each finding a remediation path.** ADR, redesign, redesign-with-condition, or explicit-accept with rationale. Findings without a path don't get closed.

5. **Produce the verdict.** Approved / approved-with-conditions / rework. Conditions must be concrete and tracked (link to ADRs / follow-ups).

6. **Flag what the design *doesn't* yet cover.** Unaddressed risk areas (the open questions, the not-yet-modeled exception paths) are findings of omission, not silence.

## Bulletproofing against Rationalization
- **Severity inflation** — everything "Critical" desensitizes the board and dilutes the genuinely-blocking findings; reserve Critical.
- **BIAN-compliance scored vs. fit-gap** — docking a design for not covering all 322 service domains when the bank runs selective decomposition; score selective-decomposition fit.
- **Residency not a lens** — reviewing a UAE-bank design without the onshore/DIFC/ADGM perimeter as an explicit lens misses the cross-border violation; make it a lens.
- **Integration seam review skipped** — "and the legacy core is integrated" treated as a checkbox rather than reviewed for ACL/strangler-fig/idempotency; findings get weak.
- **Findings without owners/paths** — "improve the observability story" with no owner and no ADR is a finding nobody closes; require a path.
- **Reuse posture not examined** — tacit accepting a big-bang-replace assumption in a design for a bank with a legacy core is a missed Critical; the reuse-vs-replace verdict is a lens.
- **Review as gatekeeping, not shaping** — a review that only says "approve/reject" without shaping the remedy is less useful; a good review names the path to approve.

## Bulletproofing against Rationalization
To prevent Architecture reviews from becoming ceremonial overviews, you MUST:

1. **Mandatory Independence:** Reviewers CANNOT be the primary architects of the solution under review.
2. **Mandatory Friction Requirement:** If a review yields zero structural feedback, risks, or optimizations, the review itself must be flagged as critically superficial.
3. **Mandatory Legacy Defense Check:** You MUST explicitly validate that the new solution does not introduce destabilizing synchronous load onto Legacy Core systems.
4. **Finality of Decision:** Finding escalations MUST be actively documented in the project RAID log, and progression to implementation MUST be formally gated on them.

**Violating these rules invalidates the Architecture Review.**

## Outputs
- **Architecture review report** — lenses applied, findings by severity with owners & remediation paths, unaddressed-risk notes.
- **Verdict** — approved / approved-with-conditions / rework, with conditions tracked.
- **Remediation register** — feeds the ADR / redesign work, and the RAID log.

## Related skills
- [design-review](../../governance/design-review/SKILL.md) — the component-depth companion; this is the architecture-altitude review.
- [architecture-board](../../governance/architecture-board/SKILL.md) — the gate that consumes this review's verdict.
- [reference-architecture](../../greenfield/reference-architecture/SKILL.md) — the standard this reviews against.
- [nfr-checklist](../nfr-checklist/SKILL.md) — supplies the NFR commitments to verify.
- [hld-generator](../hld-generator/SKILL.md) / [lld-generator](../lld-generator/SKILL.md) — the artifacts reviewed.
- [architecture-decision-records](../architecture-decision-records/SKILL.md) — where findings' remediations get recorded.
- [business-capability-map](../../discovery/business-capability-map/SKILL.md) — the BIAN map this reviews against.

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
