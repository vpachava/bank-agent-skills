---
name: gap-analysis
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when comparing the bank's current capabilities or systems against a target — produces a gap register (missing / under-invested / duplicated capabilities) with severity and initiative linkage."
required-inputs:
  - Current-state capability map or inventory (/business-capability-map)
  - Target state (or target capabilities / requirements)
  - Initiative scope & priorities
  - Realization view (systems → capabilities)
expected-deliverables:
  - Gap register (capability, gap type, severity, rationale, linked initiative)
  - Duplication & rationalization calls (where multiple systems realize one capability)
  - Priority view (which gaps the initiative will close)
---

# /gap-analysis

## When to apply
Use after you have both a current-state capability map *and* a target (target capabilities, a requirements baseline, or a target architecture) — gap-analysis is the comparison that produces the register of what's missing, under-invested, or over-duplicated. Pairs with `/business-capability-map` (the input) and feeds `/solution-options` and the roadmap.

> Run **TOGAF's method** (gap-identification in Phase B/C) over a **BIAN** capability map. The map is the content; gap-analysis is the method that turns it into decisions.

## Inputs
- **Current-state capability map / inventory** — typically the output of `/business-capability-map` (BIAN Area→Domain→Service Domain where decomposed), plus the realization view (systems → capabilities).
- **Target state** — target capabilities, requirements baseline, or target architecture. Without a target, "gap" has no meaning.
- **Initiative scope & priorities** — which gaps this effort will address vs. which are noted and left.
- **Realization view** — which systems deliver each capability (so duplication is detectable).

## Process
1. **Fix both endpoints first.** Current capability map on one side, target on the other. If the target isn't defined, that's a prerequisite (run `/business-capability-map` for current and define the target), not a gap-analysis input.

2. **Align the two on the same vocabulary.** Both current and target must use the same BIAN capability decomposition (or the same coarse level where decomposition is selective). A gap on a capability that exists at Area-level in current but Service-Domain-level in target is a measurement artifact, not a real gap.

3. **Identify gaps three ways — missing, under-invested, and duplicated.** Missing = target has a capability the current lacks. Under-invested = current has it but maturity falls short of target (use the heat-map). Duplicated = multiple systems realize the same capability when the target expects one. Duplicated is the one most teams miss and it's the most expensive gap there is.
   > BIAN v14.0 has ~322 service domains; **banks run selective**. Judge a gap against selective depth, not against the full catalogue — don't manufacture gaps by comparing to a Utopian full-BIAN baseline.

4. **Score severity by consequence, not size.** A small gap under a regulated path (KYC depth, AML screening, payment resilience) is severity-Critical; a large gap on a back-office nicety is severity-Low. Score against risk appetite and regulatory exposure.

5. **Link each gap to the realization view.** A gap isn't abstract — it's a capability the current systems don't deliver, or deliver X times. Naming the systems makes the gap actionable (close via build, buy, modernize, or rationalize).

6. **Tie gaps to initiatives & decisions.** Each high-severity gap should resolve into an initiative (build / modernize / rationalize / retire) or a deliberate "accept" with rationale. Gaps with no owning initiative become the roadmap's hidden scope.

7. **Flag gaps that are actually decisions not yet made.** Some "gaps" are unresolved target-state decisions wearing a gap's clothing; surface them as decisions (`/solution-options`) rather than letting them masquerade as capability holes.

## Bulletproofing against Rationalization
To prevent cosmetic gap classification and effort-bias planning, you MUST:

1. **Mandatory Consequence Scoring:** Severity MUST be derived exclusively from Regulatory Exposure, Strategic Critical-Path adherence, and Risk. If you score severity based on how "big" the effort is to fix, the analysis is rejected.
2. **Duplication Cost Mandate:** System duplication across capabilities MUST be classed as an explicit gap. "Working in two places" is a gap of efficiency.
3. **Mandatory Remediation Linkage:** Every High and Critical severity gap MUST explicitly identify its linked remediation initiative or explicit formal "Accepted" risk state. Gaps cannot be left open without a recorded owner.
4. **Mandatory Endpoint Anchorage:** You CANNOT record a gap without citing both the current-state baseline and target-state requirement. Subjective observations are not Gaps.

**Violating these rules invalidates the Gap Analysis.**

## Banking pitfalls
- **A capability inventory mislabelled a gap analysis.** Listing capabilities without target-state comparison produces a catalogue, not gaps. Both endpoints must exist.
- **Manufactured gaps vs. selective BIAN depth** — comparing against full 322-domain BIAN produces a forest of "gaps" the bank will never, and needn't, close; measure against selective depth.
- **Duplication treated as a lesser gap** — duplication is usually the most expensive gap (redundant licenses, duplicated teams of owners, divergent data) and the easiest to miss; call it out explicitly with the system-to-capability tie.
- **Severity scored by size** — a big cosmetic gap scored Critical starves the real Critical (a small regulated-path gap). Score by consequence.
- **Gaps with no owning initiative** — a register of gaps that nobody will close is theatre; each high-severity gap needs an owning decision or an explicit "accept" rationale.
- **Ignoring the legacy-core gap** — and the modernization cost it implies; surface the legacy core's gaps with the `/legacy-assessment` stub attached, because closing them is a multi-wave effort, not a sprint.

## Outputs
- **Gap register** — per capability: gap type (missing/under-invested/duplicated), severity, rationale, linked systems, linked decision/initiative or explicit "accept."
- **Duplication / rationalization calls** — which duplicate realizations to retire, retain, or consolidate.
- **Priority view** — which gaps the in-scope initiative will close; the rest noted for the roadmap.

## Related skills
- [business-capability-map](../business-capability-map/SKILL.md) — supplies the current-state map this analyses.
- [solution-options](../solution-options/SKILL.md) — resolves gaps that need a buy/build/modernize decision.
- [requirements-analysis](../requirements-analysis/SKILL.md) — the target requirements side of the comparison.
- [roadmap](../../greenfield/roadmap/SKILL.md) — turns the priority view into a phased plan.
- [legacy-assessment](../../modernization/legacy-assessment/SKILL.md) — for gaps on legacy-core capabilities.
