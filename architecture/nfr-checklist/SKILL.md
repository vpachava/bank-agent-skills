---
name: nfr-checklist
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when a banking design needs its non-functional requirements enumerated and committed — produces an NFR baseline (perf, scale, availability, security, compliance, residency) with measurable targets and a trace-to-design map."
required-inputs:
  - Requirements baseline (/requirements-analysis) — NFR framing
  - Regulatory constraints (UAE/CBUAE, residency)
  - Service-level expectations & user volumes
  - The current-state performance/availability posture (if known)
expected-deliverables:
  - NFR baseline document, one row per NFR with target, measure, source, owner
  - Residency & compliance NFRs as first-class (not footnotes)
  - NFR-to-design trace map (which design decision satisfies each NFR)
---

# /nfr-checklist

## When to apply
Use to take the *headline NFRs* from `/requirements-analysis` to *completion* — enumerate every non-functional requirement, pin a measurable target, and map each to the design decision that satisfies it. Feeds `/hld-generator` and `/lld-generator` and is verified by `/architecture-review` and gated by `/production-readiness`.

> NFRs in a bank are not "ilities"; for a regulated platform they are residency, audit, breach-clock, and reconciliation — first-class design drivers, not quality attributes bolted on at the end.

## Inputs
- **Requirements baseline** — the NFR *framing* from `/requirements-analysis` (headline targets).
- **Regulatory constraints** — UAE/CBUAE residency, breach clocks (72-hour), retention (~5 years), KYC depth, AML cadence, free-zone cross-border SCC.
- **Service-level expectations & volumes** — user counts, transaction rates, peak (e.g., salary-day, payment cut-off).
- **Current-state posture** — existing perf/availability baselines to improve on (or not regress).

## Process
1. **Enumerate NFRs by category, each as a row with target + measure.** Categories: Performance (latency, throughput), Scalability (peak, growth), Availability (RTO, RPO, SLO), Resilience/DR, Security, Compliance/Residency, Auditability, Operability/Maintainability, Cost/Run, Usability (where material).

2. **Pin measurable targets — no "high" / "robust".** Latency: p95 < X ms for Y operation. Availability: 99.9% with RTO 30min / RPO 5min. Residency: payment data in-country, breach reported ≤72h. An NFR without a number is an aspiration.

3. **Promote residency & compliance NFRs to first-class rows.** Not footnotes. Each UAE/CBUAE obligation is an NFR with a target and a trace; e.g., "PII never leaves onshore without SCC", "AML screening ≤24h cadence", "breach notification ≤72h".

4. **Attribute source & owner per NFR.** Which stakeholder or reg source set it; who owns honoring it ("Risk owns the AML cadence NFR"). Unowned NFRs drift.

5. **Distinguish must vs. should.** A regulated NFR (residency, audit, breach-clock) is a Must; a performance polish is a Should. MoSCoW the NFRs so the build knows what's gating.

6. **Map NFRs to design decisions — the trace.** Each Must NFR must trace to a design choice (a retry policy, a residency choice, a cache tier, a screening cadence). Untraced NFRs are aspirational — flag them.

7. **Surface the NFR *tensions* as decisions.** Availability-vs-cost, latency-vs-consistency, residency-vs-latency (in-country may cost latency). These tensions are ADRs (`/architecture-decision-records`), not silent trade-offs.

8. **Re-validate against current-state posture** — does the target regress anywhere vs. today (e.g., a modernization that worsens latency)? Flag regressions explicitly; the board will ask.

## Bulletproofing against Rationalization
- **Aspirational NFRs** — "highly available", "secure", "performant" with no number; unmeasurable NFRs are unverifiable and unenforceable. Pin a number.
- **Residency as a footnote** — UAE/CBUAE residency treated as an aside rather than a Must NFR with a target and trace; this is how a build ships a cross-border violation. First-class row.
- **No NFR-to-design trace** — the NFR baseline that doesn't map to a design decision is a wish-list; production-readiness will fail the build for "NFRs not met" precisely because the design never honored them.
- **NFR tensions undeclared** — availability-vs-cost, latency-vs-consistency silently resolved in one head; these are exactly the trade-offs that should be ADRs. Surface them.
- **Regulatory NFRs marked "Should"** — residency, breach-clock, AML cadence are Must; mis-MoSCoW-ing them relaxes a regulatory obligation.
- **No owner per NFR** — NFRs owned by "the team" aren't owned; assign to the function (Risk/Security/Ops) that owns honoring it.
- **Reg blindness in volumes** — salary-day / payment-cut-off peaks ignored in scalability targets — bank NFRs without peak context miss the actual load.

## Bulletproofing against Rationalization
To prevent vague Non-Functional Requirements that engineers cannot test against, you MUST:

1. **Mandatory Quantifiable Metrics:** NFRs like "System must be fast and reliable" are explicitly rejected. NFRs MUST define absolute quantifiable metrics (e.g., "99.99% Uptime", "RTO < 4 hours", "< 200ms API response p95").
2. **Mandatory Testability Clauses:** Every defined NFR MUST be accompanied by an explicit definition of HOW it will be tested/measured in CI/CD or Load profiles.
3. **Regulatory Supremacy:** Data Residency, Audit logging, and Security Baseline NFRs CANNOT be "deferred to phase 2."
4. **Mandatory Cost Baseline:** Scale and Performance NFRs MUST document the underlying estimated cost envelope.

**Violating these rules invalidates the NFR Checklist.**

## Outputs
- **NFR baseline** — one row per NFR: category, target (measured), source, owner, Must/Should, trace-to-design.
- **Residency & compliance NFRs** — first-class, with the cross-zone SCC obligation if free-zone is in scope.
- **NFR-to-design trace map** — and the untraced (aspirational) NFRs flagged.
- **NFR-tension ADRs** — the trade-offs escalated to `/architecture-decision-records`.

## Related skills
- [requirements-analysis](../../discovery/requirements-analysis/SKILL.md) — supplies the headline NFR framing this enumerates.
- [hld-generator](../hld-generator/SKILL.md) — commits the headline NFRs into the HLD.
- [lld-generator](../lld-generator/SKILL.md) — traces each NFR to a design decision.
- [architecture-decision-records](../architecture-decision-records/SKILL.md) — for the NFR-tension trade-offs.
- [architecture-review](../architecture-review/SKILL.md) — verifies the design commits the NFRs.
- [production-readiness](../../governance/production-readiness/SKILL.md) — the gate that the NFRs satisfy.
- [dr-review](../../governance/dr-review/SKILL.md) — owns the availability/DR NFRs.
- [sre-review](../../devops/sre-review/SKILL.md) — owns the SLO/error-budget family of NFRs.

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

