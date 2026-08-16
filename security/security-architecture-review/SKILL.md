---
name: security-architecture-review
owner: Security Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when running an end-to-end security review across a banking solution — produces a security architecture review report synthesizing threat model, OWASP, zero-trust, IAM, and compliance findings with severity, owners, and gate verdicts."
required-inputs:
  - The solution architecture (HLD/LLD, data-flow, deployment view)
  - Outputs from component-level security skills (threat-model, owasp-review, zero-trust, iam-review, compliance)
  - NFRs relevant to security
  - Known risk-acceptance decisions
expected-deliverables:
  - Security architecture review report
  - Consolidated findings register (severity-ranked, deduplicated)
  - Gate verdict (pass / conditional-pass / fail) with conditions
  - Residual-risk register for accepted risks
---

# /security-architecture-review

## When to apply
Use as the **capstone security gate** — after the component-level security skills (`/threat-model`, `/owasp-review`, `/zero-trust`, `/iam-review`, `/compliance`) have run, this synthesizes their findings into an end-to-end review of the solution's security architecture. Gates production-readiness (feeds `/production-readiness`). Also use stand-alone when a lightweight but whole-solution security review is needed and the component skills haven't been run individually — in that case, this skill covers the key lenses itself, albeit at lower depth.

## Inputs
- **The solution architecture** — HLD/LLD, data-flow diagrams, deployment view; the thing being reviewed.
- **Component-level security outputs** — findings from `/threat-model`, `/owasp-review`, `/zero-trust`, `/iam-review`, `/compliance` where they've been run. If they haven't been run, this review covers their key lenses at summary depth and flags the gap.
- **Security-relevant NFRs** — availability (RTO/RPO), integrity (audit/provenance), confidentiality (PII, residency).
- **Known risk-acceptance decisions** — risks the business has already accepted; this review validates the acceptance is informed, not stale.

## Process

1. **Load the solution architecture and orient.** Understand the scope: what components, what boundaries, what data categories, what deployment topology. Mark the regulated paths (payment, KYC, PII, biometric) — these get the hardest scrutiny.

2. **Ingest component-level findings.** Pull in outputs from `/threat-model`, `/owasp-review`, `/zero-trust`, `/iam-review`, `/compliance`. Deduplicate findings that appear across multiple skills (a cross-zone transfer gap may surface in threat-model, compliance, and zero-trust). Consolidate into a single findings register.

3. **Review the solution-level attack surface.** The component skills review *their* surfaces; this step reviews what emerges *between* them:
   - **Cross-component trust** — do components trust each other appropriately? Is there implicit trust from deployment proximity?
   - **Data-flow integrity end-to-end** — does data maintain its integrity (provenance, non-repudiation) across the full journey, not just within each component?
   - **Blast-radius containment** — if one component is compromised, how far does the blast travel? Are micro-perimeters effective end-to-end?
   - **Observability coverage** — are there gaps in the security-telemetry surface? Unmonitored paths between components?

4. **Review the Regional Data Sovereignty and UAE-specific security posture end-to-end.**
   - **Data Sovereignty Compliance (CBUAE/PDPL/AECB)** — verify all data paths and storage locations confirm to regional residency requirements for financial and PII data; any cross-border data flow requires an explicit residency-waiver assessment.
   - **Cross-zone transfers** — verify the transfer-basis register covers every onshore↔DIFC↔ADGM flow; check that enforcement sits at the boundary, not after it.
   - **UAE identity fabric** — verify UAE Pass/EFR/UAEKYC assertions are validated per-use, never inherited as blanket trust; verify biometric data handling respects PDPL residency.
   - **CBUAE sectoral** — verify the 72-hour breach-notification path is exercised (not just documented); verify in-country residency for SVF/payment data.
   > Carry the MEDIUM-verify caveat: DESC / NESA→Cybersecurity Council / standalone CBUAE cyber-resilience specifics are MEDIUM-synthesized (research 02). Verify against current CBUAE publication before freezing into the review.

5. **Review secrets management and key custody.** Across the solution: where are secrets stored, rotated, accessed? Is key custody split across providers in a way that's unauditable? Prefer a single custody plane with per-cloud delegation.

6. **Review the security of the AI tier (where present).** The bank's AI-native surface is a first-class security surface:
   - Prompt-injection paths (from external input → agent tool-calls → regulated actions).
   - Excessive agency (agent decision-power vs. the deterministic regulated spine).
   - Model-gateway controls (rate-limiting, content-filtering, audit).
   - Training/fine-tuning data governance (if applicable).

7. **Score and rank findings.** Deduplicated findings, severity-ranked by consequence (not count). Critical = payment/PII/biometric/regulated-path compromise; High = lateral-movement or privilege-escalation; Medium = defense-in-depth gap; Low = hardening opportunity.

8. **Issue the gate verdict.**
   - **Pass** — no Critical or High findings; Medium/Low findings have owners and timelines.
   - **Conditional pass** — High findings exist but have mitigations committed with timelines; conditions listed explicitly.
   - **Fail** — Critical findings unmitigated, or High findings without committed remediation.
   The verdict feeds `/production-readiness` and `/architecture-board`.

9. **Build the residual-risk register.** For accepted risks: document what was accepted, by whom, when, under what conditions, and when it should be re-reviewed. Accepted risks without a review date are stale.

## Banking pitfalls
- **Component reviews done, solution review skipped** — the gaps *between* components (cross-component trust, end-to-end data integrity, blast-radius) only surface at the solution level; component reviews alone miss them.
- **"We ran OWASP" as the whole security review** — OWASP is the vuln checklist; the architecture review covers structural trust, posture, and the UAE-specific lens that OWASP doesn't touch.
- **Risk acceptance without expiry** — a risk accepted two years ago under different conditions, never re-reviewed; accepted risks need a review date.
- **AI tier excluded from the security review** — the AI-native surface (prompt-injection, excessive agency, model-gateway) is a first-class security surface; excluding it leaves the most novel attack surface unreviewed.
- **Cross-zone transfer register filed and forgotten** — the register is a living artifact; this review verifies it's current, not just that it exists.
- **Breach-notification path documented but never tested** — the 72-hour CBUAE/DIFC/ADGM path must be *exercised*, not just written down; verify it's been tested.
- **Secrets in environment variables across clouds** — secrets management reviewed per-cloud but not across the solution; a secret accessible in one cloud often has a copy path to another.
- **UAE cyber-rule text as fact** — DESC / NESA-transition / CBUAE-standalone specifics are MEDIUM-synthesized (research 02); flag in the review, don't ship as verified.
- **Gate verdict without conditions** — a "conditional pass" that doesn't list its conditions is a pass in disguise; conditions must be explicit, owned, and time-bound.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of security-architecture-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.
4. **Mandatory Data Classification:** Every external end-point identified in design artifacts MUST include explicit metadata classification (PII, Financial, Internal). Any unclassified integration fails the security gate.

**Violating these rules invalidates the security-architecture-review process.**

## Outputs
- **Security architecture review report** — end-to-end findings, UAE-specific posture, AI-tier review, secrets/key custody.
- **Consolidated findings register** — deduplicated, severity-ranked, with owners.
- **Gate verdict** — pass / conditional-pass / fail, with conditions listed.
- **Residual-risk register** — accepted risks with owner, date, review expiry.

## Related skills
- [threat-model](../threat-model/SKILL.md) — the structural review this synthesizes.
- [owasp-review](../owasp-review/SKILL.md) — the vuln-list review this synthesizes.
- [zero-trust](../zero-trust/SKILL.md) — the posture review this synthesizes.
- [iam-review](../iam-review/SKILL.md) — the identity/access review this synthesizes.
- [compliance](../compliance/SKILL.md) — the compliance assessment this synthesizes.
- [production-readiness](../../governance/production-readiness/SKILL.md) — the gate this verdict feeds.
- [architecture-board](../../governance/architecture-board/SKILL.md) — where the verdict is presented.
- [risk-register](../../documentation/risk-register/SKILL.md) — where residual risks land.
- [architecture-review](../../architecture/architecture-review/SKILL.md) — the broader architecture review; this is the security-specific complement.
