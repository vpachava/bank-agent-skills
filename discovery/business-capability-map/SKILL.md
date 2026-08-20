---
name: business-capability-map
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when you need to map a retail bank's business capabilities â€” produces a BIAN-aligned capability map (Business Area â†’ Domain â†’ Service Domain) with a heat-map of maturity, duplication, and investment focus."
required-inputs:
  - Bank's business domains / org structure (current)
  - Known systems supporting each area (legacy core, channels, partners)
  - Initiative scope (which capabilities matter to this effort)
  - Any existing capability map (to extend, not rebuild)
expected-deliverables:
  - Capability map (BIAN Business Area â†’ Domain â†’ Service Domain)
  - Heat-map (maturity / duplication / investment / strategic focus per capability)
  - Notes on selective-adoption depth (where the bank actually decomposes v. leaves coarse)
togaf-phases: [Phase A]
togaf-artifacts: [Architecture Vision]
bian-service-domains: [Customer Account.Origination]
---

# /business-capability-map

## When to apply
Use when you need a shared, structured picture of *what the bank does* â€” to anchor a reference architecture, drive a gap analysis, scope an initiative, or rationalize applications. Especially load-bearing for greenfield/new-platform efforts and for modernization that needs to know what it's modernizing. Feeds `/gap-analysis`, `/reference-architecture`, and `/solution-options`.

> BIAN = the capability *content*; TOGAF = the *method* of capability-based planning. This skill produces the BIAN-aligned **content**.

## Inputs
- **Bank's business domains / org structure** â€” current divisions, product lines, channels; the as-is before any BIAN overlay.
- **Systems supporting each area** â€” legacy core, channels (mobile/web/branch/contact-center, partner/fintech) and major 3rd-party integrations; capabilities are realized by systems.
- **Initiative scope** â€” which capabilities this effort cares about (full-bank map is rare; pick the relevant axis).
- **Existing capability map** â€” if the bank has one, extend it; don't rebuild from scratch and fracture the vocabulary.

## Process
1. **Pick the decomposition depth up front, honestly.** Full BIAN is ~322 service domains; banks run **selective** (BIAN's own Coreless Banking piloted just three areas). Decide whether this map goes Business Area â†’ Domain, or Area â†’ Domain â†’ Service Domain. Default to Area â†’ Domain â†’ Service Domain for the *in-scope* capabilities and Area â†’ Domain for the rest.
   > Over-decomposing to all 322 service domains produces an unreadable map nobody maintains. **Pragmatism rule:** depth follows investment focus.

2. **Map business domains to BIAN Business Areas.** Use BIAN Service Landscape v14.0 as the vocabulary (it added an Insurance area and reorganized Payments). Don't invent service-domain IDs; cite BIAN for each node.

3. **Decompose in-scope Areas â†’ Domains â†’ Service Domains.** Each Service Domain owns one business object and exposes Service Operations + (where surfaced) ~250 BIAN Semantic APIs. Stop at the depth the initiative earns.

4. **Map systems to capabilities (realization view).** A capability without the system that realizes it is abstract; mark which legacy core modules, channels, and partner systems deliver each Service Domain. This is the seam that reveals duplication and gaps.

5. **Build the heat-map.** One bubble per capability across axes: **maturity** (green/amber/red), **duplication** (how many systems realize it), **strategic/investment focus** (is this where the money goes), **regulatory exposure** (KYC/AML/residency-bearing). The heat-map is what makes the map *actionable*, not just a poster.

6. **Capture selective-adoption notes per area.** Where the bank decomposes only Areaâ†’Domain (not Service Domain), note it â€” so downstream skills don't assume Service-Domain granularity exists everywhere.
   > BIAN v14.0 pruned Service Operations; if you decompose to the operation level, flag that operations were re-organized in v14.0 and verify taxonomy against current Portal before freezing.

7. **Tie back to initiative scope & success.** Re-scope the map to the initiative; a full-bank map divorced from a decision is reference material, not a discovery artifact.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Banking pitfalls
- **Aspirational BIAN compliance** â€” mapping all 322 service domains because the framework exists, when the bank only realistically decomposes a subset. Score fit-gap, not "BIAN compliance."
- **Rebuilding an existing map** â€” if the bank has a capability map, extend; a parallel map fractures vocabulary and confuses the architecture board.
- **Capability maps without realization** â€” capabilities floating free of the systems that deliver them are unfalsifiable; insist on the system-to-capability tie.
- **Ignoring selective decomposition** â€” treating every area as if it has Service-Domain detail when half the bank only goes Areaâ†’Domain, then planning against a granularity that doesn't exist.
- **Heat-map as decoration** â€” a maturity heat-map that doesn't drive a decision (rationalize, invest, modernize) is a poster; design the heat-map *for* the decision you'll make from it.
- **Post-prune operation confusion** â€” v14.0 reorganized Service Operations; skills citing operation-level granularity against pre-v14.0 materials cite a stale taxonomy.

## Outputs
- **Capability map** â€” BIAN Area â†’ Domain â†’ Service Domain for in-scope capabilities; Area â†’ Domain elsewhere; with the depth decision recorded.
- **Heat-map** â€” maturity / duplication / strategic-investment / regulatory-exposure per capability.
- **Realization notes** â€” which systems deliver each in-scope Service Domain (feeds app rationalization & gap-analysis).
- **Selective-adoption notes** â€” where the bank decomposes only Areaâ†’Domain, flagged for downstream skills.

## Related skills
- [gap-analysis](../gap-analysis/SKILL.md) â€” current-state map vs. target state, to find the gaps.
- [reference-architecture](../../greenfield/reference-architecture/SKILL.md) â€” the BIAN-grounded architecture the map enables.
- [requirements-analysis](../requirements-analysis/SKILL.md) â€” the ask the map is scoped to serve.
- [architecture-review](../../architecture/architecture-review/SKILL.md) â€” the BIAN-lens review that uses this map.
- [legacy-assessment](../../modernization/legacy-assessment/SKILL.md) â€” the realization view feeding legacy-health assessment.

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

## Regulatory References
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Anti-patterns
- **Conflating technical components or systems with business capabilities**
  - **Consequence:** Inability to align IT investments with business outcomes, leading to system redundancy.
  - **Correct Approach:** Define capabilities as "what" the business does (e.g., Deposit Taking) rather than "how" it does it.
- **Developing the capability map inside a silo without business stake validation**
  - **Consequence:** Low adoption rate of the map, and inaccurate representing of real processes.
  - **Correct Approach:** Design the map in collaborative workshops with business unit leaders and analysts.
- **Failing to link capability definitions with regulatory controls**
  - **Consequence:** System gaps that violate compliance rules.
  - **Correct Approach:** Map regulatory requirements (CBUAE, PDPL, PCI-DSS) directly to affected capabilities in the taxonomy.
