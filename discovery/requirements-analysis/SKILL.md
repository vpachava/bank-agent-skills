---
name: requirements-analysis
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when starting a banking initiative and the requirements are still loose — produces a requirements baseline (functional + non-functional) with sources, priorities, and the regulatory constraints that bind them."
required-inputs:
  - Initiative goal or problem statement
  - List of stakeholders & decision rights
  - Known regulatory / compliance constraints (UAE/CBUAE)
  - Existing systems in scope (legacy core, channels, partners)
expected-deliverables:
  - Requirements baseline document
  - Functional requirements with source attribution
  - NFR framing (delegates detail to /nfr-checklist)
  - Open-questions / assumptions register
---

# /requirements-analysis

## When to apply
Use at the start of a banking initiative before any design — when the ask is still loose ("modernize onboarding", "launch a new loan product", "go cloud"), and you need a disciplined requirements baseline. Especially load-bearing when regulatory constraints (CBUAE data-residency, consumer protection, AML/KYC) will shape the requirements *before* design rather than after. Pairs with `/stakeholder-workshop` (to elicit) and feeds `/gap-analysis`.

> This is **Discovery** in TOGAF's ADM (Phase A/B) — the capability & requirements framing that precedes target architecture. BIAN gives the *capability vocabulary*; requirements-analysis gives the *ask*.

## Inputs
- **Initiative goal / problem statement** — the one- or two-line business outcome, in the sponsor's words.
- **Stakeholders & decision rights** — who decides vs. who is consulted; include Risk, Compliance, Security, Ops (a banking initiative without these voices produces unbuildable requirements).
- **Regulatory / compliance constraints** — known CBUAE/UAE bounds *up front* (data-residency, KYC depth, AML, consumer protection) so requirements don't get designed past them.
- **Existing systems in scope** — legacy core, channels (mobile/web/branch), 3rd-party integrations; discovery is over what exists, not greenfield.

## Process
1. **Restate the goal and its success measure, in the sponsor's language.** If you can't state a success measure, that's an open question, not a requirement.
   > Often the real requirement is hidden in the *constraint*. "Launch faster" usually means "the BPM/issuance path is the bottleneck" — name the constraint, don't just echo the goal.

2. **Elicit functional requirements by stakeholder lens.** Walk each stakeholder's journey; capture what each *needs to do*. Group by banking capability area (BIAN service-domain names where they fit), but keep the language operative ("open a retail account in <X min") not encyclopedic.
   > **TOGAF for the method, BIAN for the content** — use BIAN capability vocabulary to structure the elicitation, not to force every requirement into a service-domain box. Banks run **selective** BIAN decomposition; don't over-normalize.

3. **Capture non-functional requirements at framing depth.** Performance, availability (RTO/RPO), security, compliance, resiliency — enough to bound the solution space. Don't enumerate NFRs to completion here; that's `/nfr-checklist`'s job. Goal: does this initiative have a resilience target? a residency constraint? an audit posture?

4. **Pin the regulatory constraints as first-class requirements, not footnotes.** CBUAE sectoral data-residency (SVF & Retail-Payment regs), PDPL cross-border rules, KYC/AML depth, and — for any bank with free-zone activity — the **onshore↔DIFC↔ADGM SCC/BCR obligation** on inter-zone data flows. Requirements that ignore these get re-designed later, expensively.

5. **Attribute every requirement to a source.** Who said it, what evidence. Unattributed requirements are assumptions in disguise and rot quietly. Mark business-rule requirements sourced to a policy/reg as such — they're change-controlled differently than engineering preferences.

6. **Prioritize.** MoSCoW (Must/Should/Could/Won't) or similar; bank initiatives almost always find that "compliance gates" are Musts and "nice-to-haves" vaporize when the regulatory perimeter bites.

7. **Surface the open questions and assumptions.** A good requirements baseline is *honest about what it doesn't yet know*. These feed `/gap-analysis` and the RAID log.

## Bulletproofing against Rationalization
To prevent solution-masked requirements and omitted constraints, you MUST:

1. **Hard Regulatory Precedence:** CBUAE data residency, KYC limits, and PDPL requirements MUST be isolated and documented as absolute Architectural Constraints BEFORE user operational requirements are gathered.
2. **Prohibition of Solutioning in Requirements:** "We need Kafka" is an architectural decision, not a requirement. You MUST strip technical solutions out of business capability requests.
3. **Mandatory Gatekeeper Inclusion:** Elicitation sessions and requirement sign-offs MUST document review from Risk, Compliance, and InfoSec. A requirement list signed only by Product is incomplete.
4. **Mandatory Sourcing Tracking:** Every single Non-Functional and Functional requirement MUST have a cited, trace-able owner/source (person or regulating body).

**Violating these rules invalidates the Requirements Baseline.**

## Banking pitfalls
- **Requirements stated as the solution** — "we need a Kafka cluster" is not a requirement; "we need near-real-time payment status with no loss" is. Strip the solution out of the ask before it locks the design.
- **Regulatory constraints discovered late** — KYC depth, data-residency, AML screening trigger requirements that reshape the whole journey if met early and explode the design if met late. Pull them front.
- **Stakeholder list missing Risk/Compliance/Ops** — IT-only requirements discovery in a bank produces unbuildable requirements; the regulatory & ops voices gate the build.
- **Treating the legacy core as a black box** — discovery that doesn't enumerate the core-banking touchpoints (and the seams) lands a requirements baseline that the modernization plan can't honor.
- **No success measure** — an initiative without a measurable outcome becomes unkillable; either it's "done" on vibes or it runs forever. Pin one.
- **Free-zone blindness** — for banks with DIFC/ADGM activity, omitting the SCC/BCR obligation on inter-zone flows produces requirements that silently violate transfer rules; surface it as a constraint on day one.

## Outputs
- **Requirements baseline document** — initiative goal + success measure, functional requirements (capability-grouped, source-attributed, prioritized), NFR framing, regulatory constraints as first-class, open questions & assumptions.
- **Functional requirements register** — each with source, owner, priority, linked regulatory constraint where applicable.
- **NFR framing** — headline NFRs; full enumeration deferred to `/nfr-checklist`.
- **Open-questions / assumptions register** — feeds `/gap-analysis` and the project's RAID log.

## Related skills
- [stakeholder-workshop](../stakeholder-workshop/SKILL.md) — the elicitation engine that gathers these requirements.
- [business-capability-map](../business-capability-map/SKILL.md) — the BIAN-aligned capability view that structures the functional requirements.
- [gap-analysis](../gap-analysis/SKILL.md) — consumes the requirements baseline against current-state capabilities.
- [nfr-checklist](../../architecture/nfr-checklist/SKILL.md) — takes the NFR framing to completion.
- [raid-log](../../documentation/raid-log/SKILL.md) — where the open questions & assumptions live as the initiative runs.

### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Gathering requirements for a retail bank's new "Instant Credit Card" product.
- **Sample Input (Requirement):** `Instant Approval` and `Virtual Card Issuance`.
- **UAE Context (Regulatory Constraint):** Must comply with `CBUAE` regulations on `Maximum Debt Burden Ratio (DBR)` and `AECB` credit score minimums *in the requirement framing* as hard "Must" criteria.
- **Sample Output (Requirements Baseline):** 
  - Req #1 [Credit Check]: Must verify AECB score >650 before instant virtual card issuance.
  - Req #2 [Compliance]: Must collect electronic signature in compliance with `Federal Decree Law No 46 of 2021` on Electronic Transactions.
- **Common Pitfall:** Listing "Instant Issuance" as a functional requirement while treating `AECB` check as a "future" or "post-issuance" task.

#### (2) Customer Profile Management Example
**Scenario:** Requirements gathering for a "Global Customer Dashboard" allowing customers to manage their profile.
- **Sample Input:** User needs to update `personal data` and `contact info`.
- **UAE Context:** Must adhere to `PDPL` (Data Residency) and `CBUAE` guidelines on `KYC` updates requiring in-person or high-assurance video verification for residency changes.
- **Common Pitfall:** Omitting the regulatory requirement for high-assurance KYC verification for profile data changes, leading to a system design that is too permissive (security and compliance failure).

#### (3) Lending/Loans Onboarding Example
**Scenario:** Requirements for a Sharia-compliant "Auto Finance" loan origination project.
- **Sample Input:** `Loan structure`, `Repayment terms`, `Amortization`.
- **UAE Context:** Product description, `Sharia Board Approval`, and `Takaful Insurance` inclusion are non-negotiable functional requirements.
- **Common Pitfall:** Defining loan requirements as a standard Interest-based product. Missing the mandatory `Sharia Governance` and `Takaful` components makes the product impossible to certify compliant.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

