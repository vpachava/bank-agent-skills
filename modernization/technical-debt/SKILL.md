---
name: technical-debt
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when the bank's accumulated shortcuts & aging systems need surfacing — produces a technical-debt register (debt items with type, interest, principal, risk) and a prioritization that funds the right paydown."
required-inputs:
  - Estate inventory & legacy assessments
  - Incident history & defect/MTTR data
  - Architecture review & audit findings
  - Roadmap pressure & change-cost drivers
expected-deliverables:
  - Technical-debt register (item, type, interest, principal, risk, owner)
  - Debt-prioritization (pay now vs. service vs. accept)
  - Funding tie — which roadmap items absorb which debt paydown
---

# /technical-debt

## When to apply
Use to make the hidden cost-of-doing-business visible — the shortcuts, aging systems, missing tests, accumulated workarounds. Feeds the roadmap (debt paydown as scoped phases) and the risk register (accepted debt as risks). Lives throughout an initiative, not just at the start.

## Inputs
- **Estate inventory & legacy assessments** — `/legacy-assessment` verdicts surface the biggest debt items up front.
- **Incident history & defect/MTTR data** — interest signals: where does change take longest, where do defects cluster.
- **Architecture review & audit findings** — `/architecture-review` findings are debt surfacing in disguise.
- **Roadmap pressure & change-cost** — upcoming features that will be expensive *because* of debt.

## Process
1. **Inventory debt items by type.** Code debt (duplication, coupling, dead code), design debt (architecture violations, missing seams), test debt (no coverage on critical paths), doc debt (the spec nobody wrote), dependency debt (end-of-life runtimes/libs), infrastructure debt (no DR, no observability on a critical path), skills debt (only one person knows it).

2. **Quantify the *interest* — the recurring cost of not paying.** Each debt item carries an interest: extra hours per change, incident cost, lost feature velocity, the audit finding reappearing quarterly. Interest is what makes debt worth servicing — a 0-interest item can often stay.
   > Interest is the more useful number than principal. The debt you *never* touch because nobody touches that code has low realized interest even if its principal is large; the debt on a hot integration you change weekly bleeds.

3. **Estimate the *principal* — the one-time cost of paying it down.** The refactor, the test harness, the runtime upgrade. Where principal dwarfs realistic interest, leave it.

4. **Capture risk — not just cost.** A debt item may carry regulatory/security/resilience risk disproportionate to its interest (a no-DR critical path has low "interest" until the outage); rate the risk separately and let it upgrade priority.

5. **Prioritize — pay now / service alongside features / accept.** Pay now: high interest + low principal + feature-critical. Service alongside: bundle paydown into a roadmap item that touches that code. Accept: low interest and you'll continue to live with it; record as risk.

6. **Tie paydown to the roadmap.** Most debt paydown ships *with* feature work that touches the area — pure-debt phases are a hard sell in a bank; sequence the paydown into the roadmap, not as a standalone "trust us" phase.

7. **Assign owners & make it living.** A register with no owner per item and no review cadence rots; review each quarter with the engineering leads (the `/sre-review` reads this).

## Banking pitfalls
- **Treating all debt as bad** — 0-interest debt on a system nobody touches is benign; flagging it "pay down" wastes effort that should go to the interest-bleeding items; rate interest not just existence.
- **No interest number, only principal** — "this is a big refactor" without the recurring cost is unrankable; quantify what it bleeds.
- **Risk underweighted** — low "interest" (rarely touched) hiding high *risk* (no DR on a critical path that hasn't broken *yet*); risk should upgrade priority independent of interest.
- **Pure-debt phases as standalone asks** — "let's spend Q3 paying down tech debt" gets de-prioritized by business; bundle paydown into feature work that touches the code.
- **Register with no owner/cadence** — a debt list nobody reviews is theatre; pair each item with an owner and a quarterly review.
- **Audit/regulatory findings not folded in** — `/architecture-review` and audit findings are debt items + risk; failing to capture them means they recur and aren't tracked as the debt they are.
- **Skills debt missed** — "only one person knows system X" is the most dangerous and least-catalogued debt in a bank; capture it.

## Bulletproofing against Rationalization
To prevent tech debt tracking from becoming a graveyard of ignored tickets, you MUST:

1. **Mandatory Cost-of-Delay Quantification:** Every tech debt item MUST include a quantitative business impact (e.g., "$5K/month in infra cost", "3 days delay per release").
2. **Mandatory Burn-Down Allocation:** Tech debt registers without a committed sprint-capacity allocation (e.g., 20%) are rejected.
3. **Risk Association:** High-severity tech debt MUST be linked to the principal project Risk Register.

**Violating these rules invalidates the Technical Debt tracking.**

## Outputs
- **Technical-debt register** — item, type, interest, principal, risk, owner, recommended action.
- **Debt-prioritization** — pay now / service-alongside / accept (with rationale).
- **Funding tie** — which roadmap items absorb which paydown.

## Related skills
- [legacy-assessment](../legacy-assessment/SKILL.md) — surfaces the biggest debt items.
- [refactoring-plan](../refactoring-plan/SKILL.md) — the paydown plan for code-design debt.
- [modernization-roadmap](../modernization-roadmap/SKILL.md) — phases paydown alongside features.
- [architecture-review](../../architecture/architecture-review/SKILL.md) — findings that become debt items.
- [risk-register](../../documentation/risk-register/SKILL.md) — accepted debt lands as risks.
- [sre-review](../../devops/sre-review/SKILL.md) — reads the register for resilience/observability debt.
- [raid-log](../../documentation/raid-log/SKILL.md) — debt items live here as the register's companion.

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

