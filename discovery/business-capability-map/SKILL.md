---
name: business-capability-map
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when you need to map a retail bank's business capabilities — produces a BIAN-aligned capability map (Business Area → Domain → Service Domain) with a heat-map of maturity, duplication, and investment focus."
required-inputs:
  - Bank's business domains / org structure (current)
  - Known systems supporting each area (legacy core, channels, partners)
  - Initiative scope (which capabilities matter to this effort)
  - Any existing capability map (to extend, not rebuild)
expected-deliverables:
  - Capability map (BIAN Business Area → Domain → Service Domain)
  - Heat-map (maturity / duplication / investment / strategic focus per capability)
  - Notes on selective-adoption depth (where the bank actually decomposes v. leaves coarse)
---

# /business-capability-map

## When to apply
Use when you need a shared, structured picture of *what the bank does* — to anchor a reference architecture, drive a gap analysis, scope an initiative, or rationalize applications. Especially load-bearing for greenfield/new-platform efforts and for modernization that needs to know what it's modernizing. Feeds `/gap-analysis`, `/reference-architecture`, and `/solution-options`.

> BIAN = the capability *content*; TOGAF = the *method* of capability-based planning. This skill produces the BIAN-aligned **content**.

## Inputs
- **Bank's business domains / org structure** — current divisions, product lines, channels; the as-is before any BIAN overlay.
- **Systems supporting each area** — legacy core, channels (mobile/web/branch/contact-center, partner/fintech) and major 3rd-party integrations; capabilities are realized by systems.
- **Initiative scope** — which capabilities this effort cares about (full-bank map is rare; pick the relevant axis).
- **Existing capability map** — if the bank has one, extend it; don't rebuild from scratch and fracture the vocabulary.

## Process
1. **Pick the decomposition depth up front, honestly.** Full BIAN is ~322 service domains; banks run **selective** (BIAN's own Coreless Banking piloted just three areas). Decide whether this map goes Business Area → Domain, or Area → Domain → Service Domain. Default to Area → Domain → Service Domain for the *in-scope* capabilities and Area → Domain for the rest.
   > Over-decomposing to all 322 service domains produces an unreadable map nobody maintains. **Pragmatism rule:** depth follows investment focus.

2. **Map business domains to BIAN Business Areas.** Use BIAN Service Landscape v14.0 as the vocabulary (it added an Insurance area and reorganized Payments). Don't invent service-domain IDs; cite BIAN for each node.

3. **Decompose in-scope Areas → Domains → Service Domains.** Each Service Domain owns one business object and exposes Service Operations + (where surfaced) ~250 BIAN Semantic APIs. Stop at the depth the initiative earns.

4. **Map systems to capabilities (realization view).** A capability without the system that realizes it is abstract; mark which legacy core modules, channels, and partner systems deliver each Service Domain. This is the seam that reveals duplication and gaps.

5. **Build the heat-map.** One bubble per capability across axes: **maturity** (green/amber/red), **duplication** (how many systems realize it), **strategic/investment focus** (is this where the money goes), **regulatory exposure** (KYC/AML/residency-bearing). The heat-map is what makes the map *actionable*, not just a poster.

6. **Capture selective-adoption notes per area.** Where the bank decomposes only Area→Domain (not Service Domain), note it — so downstream skills don't assume Service-Domain granularity exists everywhere.
   > BIAN v14.0 pruned Service Operations; if you decompose to the operation level, flag that operations were re-organized in v14.0 and verify taxonomy against current Portal before freezing.

7. **Tie back to initiative scope & success.** Re-scope the map to the initiative; a full-bank map divorced from a decision is reference material, not a discovery artifact.

## Bulletproofing against Rationalization
To prevent abstract map-generation and detached capability siloing without measurable context, you MUST:

1. **Mandatory System Realization Mapping:** A BIAN Service Domain plotted WITHOUT naming the legacy core module, SaaS, or microservice that currently realizes it is an invalid mapping. You must trace to execution.
2. **Mandatory Disavowal of Theoretical Maturity:** The heat-map MUST score maturity based on operational reality, not theoretical platform potential. If the feature exists but operations cannot use it, maturity is Amber/Red.
3. **Mandatory Depth Limitations:** Explicitly justify any mapping traversing beneath Area->Domain; mapping abstract capabilities below Domain without a targeted modernization or investment initiative is forbidden overhead.
4. **Duplication Penalty Mandate:** Where multiple systems map to a singular Service Domain, it MUST trigger a duplication alert in the heatmap.

**Violating these rules invalidates the Business Capability Map.**

## Banking pitfalls
- **Aspirational BIAN compliance** — mapping all 322 service domains because the framework exists, when the bank only realistically decomposes a subset. Score fit-gap, not "BIAN compliance."
- **Rebuilding an existing map** — if the bank has a capability map, extend; a parallel map fractures vocabulary and confuses the architecture board.
- **Capability maps without realization** — capabilities floating free of the systems that deliver them are unfalsifiable; insist on the system-to-capability tie.
- **Ignoring selective decomposition** — treating every area as if it has Service-Domain detail when half the bank only goes Area→Domain, then planning against a granularity that doesn't exist.
- **Heat-map as decoration** — a maturity heat-map that doesn't drive a decision (rationalize, invest, modernize) is a poster; design the heat-map *for* the decision you'll make from it.
- **Post-prune operation confusion** — v14.0 reorganized Service Operations; skills citing operation-level granularity against pre-v14.0 materials cite a stale taxonomy.

## Outputs
- **Capability map** — BIAN Area → Domain → Service Domain for in-scope capabilities; Area → Domain elsewhere; with the depth decision recorded.
- **Heat-map** — maturity / duplication / strategic-investment / regulatory-exposure per capability.
- **Realization notes** — which systems deliver each in-scope Service Domain (feeds app rationalization & gap-analysis).
- **Selective-adoption notes** — where the bank decomposes only Area→Domain, flagged for downstream skills.

## Related skills
- [gap-analysis](../gap-analysis/SKILL.md) — current-state map vs. target state, to find the gaps.
- [reference-architecture](../../greenfield/reference-architecture/SKILL.md) — the BIAN-grounded architecture the map enables.
- [requirements-analysis](../requirements-analysis/SKILL.md) — the ask the map is scoped to serve.
- [architecture-review](../../architecture/architecture-review/SKILL.md) — the BIAN-lens review that uses this map.
- [legacy-assessment](../../modernization/legacy-assessment/SKILL.md) — the realization view feeding legacy-health assessment.

### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Mapping the capability "Credit Card Origination" for a retail bank launching a new digital-only card.
- **Sample Input (Capability):** `Retail Banking` -> `Payments` -> `Credit Card Origination`
- **Sample Input (Realization):** Realized by `Legacy-Core` and `Digital-Origination-Microsvc`.
- **UAE Context:** Must include CBUAE-mandated `AECB` credit check capability *prior* to final approval.
- **Sample Output (Heatmap Entry):** `[Credit Card Origination]: Maturity=Amber, Duplication=High, Regulatory-Exposure=High`
- **Common Pitfall:** Mapping "Credit Card Origination" but forgetting the integration with `AECB` reporting, leading to a gap in the business capability map that will cause a regulatory block in production.

#### (2) Customer Profile Management Example
**Scenario:** Rationalizing customer data across branch, mobile, and web channels.
- **Sample Input:** `Retail Banking` -> `Customer Domain` -> `Customer Profile Management`
- **UAE Context:** Must comply with `PDPL` (Personal Data Protection Law) standards regarding data residency in UAE.
- **Common Pitfall:** Mapping "Customer Profile" as a single domain when, in practice, the bank maintains "KYC Profile" and "Marketing Profile" separately. Failing to decompose these leads to PIPL/PDPL compliance issues.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Mapping a new Sharia-compliant personal loan product.
- **Sample Input:** `Retail Banking` -> `Lending` -> `Sharia-Compliant Loan Origination`
- **UAE Context:** Requires integration with a `Sharia Governance Board` service domain for product certification.
- **Common Pitfall:** Treating Sharia-compliant lending as a generic loan process. It differs significantly in the `Amortization Schedule` and `Interest-Equivalent Calculation` capabilities.
