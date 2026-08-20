---
name: modernization-roadmap
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when modernization across the bank needs sequencing across waves â€” produces a modernization roadmap (phases/waves, dependencies, value-per-wave) that honors reuse-over-rewrite and the bank's release calendar."
required-inputs:
  - Legacy assessments & refactoring plans for the candidates
  - The target architecture / capability target
  - Impact analyses & dependency graph across candidates
  - Resource & capability constraints (teams, skills)
expected-deliverables:
  - Modernization roadmap (phase/wave structure, scope per wave)
  - Dependency & value-per-wave view
  - Risk & freeze-window posture per wave
togaf-phases: [Phase F]
togaf-artifacts: [Migration Plan]
bian-service-domains: [Integration.Migration]
---

# /modernization-roadmap

## When to apply
Use to sequence multiple modernization initiatives across the bank into phases/waves â€” not micro-managing each, but ordering them by dependency, value, and risk per the release calendar. Feeds the exec summary, the risk register, and the governance gates. Distinct from `/greenfield/roadmap` (a single greenfield initiative) â€” this is the bank-wide modernization arc.

## Inputs
- **Legacy assessments & refactoring plans** â€” per candidate system, the verdict and the plan.
- **Target architecture / capability target** â€” what "modernized" looks like (from `/reference-architecture` or `/hld-generator`).
- **Impact analyses & dependency graph** â€” which candidates depend on which; what must modernize first to unblock others.
- **Resource & capability constraints** â€” teams, skills, the things only one person knows (skills debt).

## Process
1. **Group candidates into waves by dependency & value, not by proximity.** A wave is a coherent set of modernization that can ship together and that delivers visible value. Don't wave-group by "all the batch systems" if the actual dependency/value structure cuts across that line.

2. **Order by dependency â€” respect what must coalesce first.** Identify the foundational modernizations (a data-platform seam, an identity gateway, an event backbone) whose completion unblocks downstream waves; sequence them first even if individually less flashy. Reverse-ordering starves the value-earning waves.

3. **Apply wedge-first per wave.** Each wave leads with a thin high-value slice that proves the pattern end-to-end before the wave's broader effort commits; the wedge de-risks the wave the same way a refactoring step de-risks a cut.

4. **Six-Rs the candidates honestly.** Rehost, Replatform, Refactor, Repurchase, Retain, Retire per the cloud-migration discipline â€” but applied to modernization. "Retain" is a legitimate roadmap entry (an asset consciously left), not a failure to modernize.

5. **Weight value and risk per wave.** Each wave's value stated (customer/business outcome, capability unlock), and its risk stated (regulatory exposure, migration risk, the dual-run cost). The roadmap is a *sequence*, not a list â€” show how each wave unlocks or raises the stakes for the next.

6. **Honor the release calendar & freeze windows.** Waves scheduled around regulatory freezes, statement-run periods, peak periods; the preparatory work in a freeze, the irreversible cuts outside it. A roadmap that ignores the bank's calendar is fiction.

7. **Surface the cross-wave invariants.** The things that must remain true across every wave â€” zero Replace rows in the core (reuse-over-rewrite invariant, or its documented exception), regulated paths stay deterministic, data residency honored, audit continuity. The invariants are what lets the bank operate through the roadmap.

8. **Tie waves to the governance gates.** Each wave enters and exits with its gates â€” design review, architecture review, production-readiness â€” so the roadmap is bounded by oversight, not just by time.

## Banking pitfalls
- **Waves as proximity buckets** â€” grouping by "systems that touch each other geographically" or by org rather than by dependency/value structure; the roadmap then front-loads easy things and starves load-bearing modernization.
- **Reverse-ordered dependencies** â€” modernizing dependents before the foundation they depend on is ready (e.g., microservices split before the event backbone exists); the downstream wave drifts.
- **No wedge-first** â€” each wave launching full-bore instead of with a thin proving slice; a wave-level failure then has no circuit-breaker.
- **Big-bang replace assumed** â€” a roadmap that quietly depends on a freeze-and-rewrite of the core rather than reuse-over-rewrite strangler-fig; reuse is the bank's default and replace must be a documented exception with rationale.
- **Freeze windows ignored** â€” waves scheduled over regulatory freezes / statement runs / peaks; the bank's calendar binds the roadmap.
- **"Retain" treated as a modernization failure** â€” pressing a consciously-retained asset into a future wave inflates scope; retain-with-rationale is a legitimate roadmap entry.
- **Cross-wave invariants unstated** â€” without the invariants (deterministic regulated paths, residency, audit continuity), the roadmap allows the bank to drift into a state mid-arc that a single wave's success hides.
- **Roadmap without governance gates** â€” waves bounded only by time, not by design/architecture/production-readiness reviews; a wave can't be declared done without the gates.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of modernization-roadmap meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the modernization-roadmap process.**

## Outputs
- **Modernization roadmap** â€” phase/wave structure, scope per wave, the wedge-first slice per wave, six-R verdict per candidate.
- **Dependency & value-per-wave view** â€” what each wave unlocks and the visible value it delivers.
- **Risk & freeze-window posture** â€” per wave.
- **Cross-wave invariants** â€” stated, so the bank operates through the arc.

## Related skills
- [legacy-assessment](../legacy-assessment/SKILL.md) â€” the verdicts feeding the candidates.
- [refactoring-plan](../refactoring-plan/SKILL.md) â€” the per-candidate plan the waves phase.
- [impact-analysis](../impact-analysis/SKILL.md) â€” dependency & ordering inputs.
- [technical-debt](../technical-debt/SKILL.md) â€” the debt register paydown sequenced in.
- [reference-architecture](../../greenfield/reference-architecture/SKILL.md) â€” the target the roadmap moves toward.
- [architecture-review](../../architecture/architecture-review/SKILL.md) â€” the gate each wave passes.
- [production-readiness](../../governance/production-readiness/SKILL.md) â€” the gate each wave exits through.
- [cloud-migration](../../migration/cloud-migration/SKILL.md) â€” the cloud-ward waves' detail.
- [risk-register](../../documentation/risk-register/SKILL.md) â€” risks surfaced across the arc.

### Banking Context & Examples

#### (1) Core Banking Modernization Roadmap Example
**Scenario:** Multi-year modernization of `Core-Banking-System`.
- **Architecture Lens Check:** Verification of `Data-Residency` and `Audit` continuity across phased waves.
- **Sample Outcome:** "Wave 1: Migrate read-only AECB reporting data to cloud-sink. Wave 2: Strangler-fig account balance queries behind Facade, preserving legacy ledger. Wave 3: Migrate transaction-engine, ensuring Sharia-Governance certification end-to-end."
- **Common Pitfall:** Sequencing waves by "team-capacity" instead of by "regulatory-foundation"; attempting the transaction engine (Wave 3) before establishing the AECB/residency anchor (Wave 1) results in un-compliant production paths.

#### (2) Digital Banking Expansion Roadmap Example
**Scenario:** Roadmap for expanding digital services into a new foreign branch.
- **Architecture Lens Check:** Cross-referencing `PDPL` residency constraints per jurisdiction in phased delivery.
- **Sample Outcome:** "Roadmap Phase A: Onboard UAE-resident customers on onshore-cloud. Phase B: Onboard foreign-branch customers on local-sovereign-cloud, segregating data-flows to maintain residency-compliance."
- **Common Pitfall:** Assuming a single unified cloud-roadmap works for all market expansions; failure to map `PDPL` residency constraints onto the roadmap waves leads to unlawful cross-border data transfers until caught.

#### (3) Sharia Product Modernization Example
**Scenario:** Modernizing the ledger systems for Sharia-compliant product offerings.
- **Architecture Lens Check:** Ensuring roadmap phases for legacy decommissioning do *not* disrupt the `Sharia-Compliant` audit-trail requirements.
- **Sample Outcome:** "Roadmap Wave-X: Migration of Sharia ledger to target-architecture, following formal `Sharia-Governance-Board` sign-off and ledger-parallel-run."
- **Common Pitfall:** Inadvertently introducing a temporary "interest-based ledger" path during a modernization wave; this would disqualify the bank from Sharia-certification compliance for all affected accounts, a permanent regulatory error.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Anti-patterns
- **Planning monolithic, multi-year rewrites without intermediate valuable deliverables**
  - **Consequence:** Stakeholders cancel funding in Year 2 because no tangible business improvements have reached customers.
  - **Correct Approach:** Structure the roadmap around iterative, incremental releases (Strangler Fig pattern) that deliver slice-by-slice value.
- **Failing to budget for the "dual-run" cost phase during transition**
  - **Consequence:** Budgets are destroyed when the organization realizes it must pay for both the old mainframe and the new cloud footprint simultaneously.
  - **Correct Approach:** Explicitly forecast overlapping infrastructure, licensing, and operational support costs in the roadmap financial model.
- **Attempting to modernize technology stacks while keeping old siloed organizational structures**
  - **Consequence:** The new cloud-native microservices function like a distributed monolith due to Conway's Law organizational constraints.
  - **Correct Approach:** Build organizational change management (shifting to DevOps or product-aligned squads) directly into the roadmap timeline.
