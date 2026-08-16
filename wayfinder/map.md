---
id: map
title: "UAE Retail-Bank Solution-Architect Skills Library"
label: wayfinder:map
status: open
---

## Destination

A working library of **64 invoke-and-act Claude Code skills + a root README** written into this `skills/` repo, covering the full solution-architecture lifecycle for a **large retail bank in the UAE** — from discovery through operational readiness. Each skill is a triggered process (its own slash command) that produces a concrete deliverable, with banking/UAE-specific checklists and pitfalls embedded as the steps and industry-framework grounding (BIAN, TOGAF, C4, AWS Well-Architected, Azure CAF, OWASP, NIST, SRE, ITIL 4) inline and actionable. The library is practical for immediate project work, not just a reference catalogue. The map is done when all 64 skills + the README exist, are consistent with the locked archetype, and their grounding research is folded in.

> **Execution is carried into the map** (a `## Notes` override): category-batched **task** tickets write the actual `SKILL.md` files. Research tickets (AFK) settle the banking/UAE-specific content first; each category ships once its grounding decisions are firm. This overrides wayfinder's default "plan, don't do."

## Notes

**Standing decisions that shape every ticket (locked in the charting grilling — do not re-litigate):**

1. **Destination** — build the 64 skills + README *into this repo*, not a spec for them. Execution carried into the map; tickets write files.
2. **Skill type — invoke-and-act hybrid.** Each skill is triggerable (e.g. `/threat-model`) and runs a process producing a deliverable (the threat model, the ADR, the risk register). Checklists & pitfalls are the *steps*, not a reference appendix; framework grounding is inline and actionable.
3. **Shared section template (canonized by ticket 01 — the archetype):** frontmatter (name, description, + metadata: owner, version, last-reviewed, required-inputs, expected-deliverables) · Purpose & when-to-apply · Inputs/process as embedded checklists · Banking-specific pitfalls · Outputs · Related skills (cross-linked via folder-relative paths). **Depth — flex to fit:** target ~200–400 lines, heavier where the domain earns it (cloud/security), lighter for discovery/workshop skills; heavy reference material lives in a per-skill `references/` folder where the skill earns it.
4. **Naming — short, unprefixed.** Each `name` is its own slash command; the **category folder** groups the catalogue, not the name. Folders (11): `discovery/`, `architecture/`, `greenfield/`, `modernization/`, `migration/`, `integration/`, `security/`, `cloud/`, `devops/`, `documentation/`, `governance/`. (The summary said "12 categories"; the skill table lists 11 — the table is authoritative; all 64 fit the 11 folders.)
5. **Scope — MVP first.** Destination = 64 skills + root README + per-skill metadata frontmatter. **Phase 2** (parked in *Not yet specified*, graduates once skills exist and their shape is visible): bank-specific templates, worked examples, Mermaid/draw.io diagram templates, maturity ratings (foundational/intermediate/advanced), and the BIAN/TOGAF/Well-Architected/NIST/OWASP/SRE/ITIL framework index.
6. **Build batching — category-batched.** ~11 build tickets (one per category, building that category's skills in a session on the locked archetype), each preceded by a grounding `research` ticket where the category needs external UAE/banking facts.

**Skill counts per category (the catalogue to build):**

- `discovery/` — requirements-analysis, stakeholder-workshop, business-capability-map, gap-analysis, solution-options (5)
- `architecture/` — hld-generator, lld-generator, c4-model, sequence-diagrams, deployment-diagrams, architecture-review, architecture-decision-records, nfr-checklist (8)
- `greenfield/` — platform-selection, technology-evaluation, poc-planning, roadmap, reference-architecture (5)
- `modernization/` — legacy-assessment, impact-analysis, technical-debt, refactoring-plan, modernization-roadmap (5)
- `migration/` — cloud-migration, database-migration, application-migration, migration-wave-planning, rollback-plan, cutover-plan (6)
- `integration/` — api-design, event-driven, messaging, data-sync, etl, integration-patterns (6)
- `security/` — threat-model, owasp-review, zero-trust, iam-review, compliance, security-architecture-review (6)
- `cloud/` — aws-review, azure-review, gcp-review, kubernetes, terraform, landing-zone-review (6)
- `devops/` — cicd-review, release-readiness, observability, sre-review, performance-review (5)
- `documentation/` — executive-summary, proposal, raid-log, risk-register, project-charter, design-document (6) - **COMPLETE**
- `governance/` — architecture-board, solution-review, design-review, production-readiness, dr-review, operational-readiness (6) - **COMPLETE**

**Context available in the repo (worked examples & fog-source):** the parent `C:\code\ai\BrainStorming\CC\` holds a separate, closed AI-native-onboarding wayfinder effort (`map.md`, 15 tickets, `design-document.md`, `diagrams.md`, `research/`) plus onboarding decks. It is a *different project* — mine its **content as ready worked examples** for relevant skills (sequence-diagrams, deployment-diagrams, api-design, etc.) and its **tracker format**, but do not conflate the two efforts.

**Skills every session should consult:** `/grilling` + `/domain-modeling` for the archetype grilling ticket (01); `/research` for research tickets (02–05); the locked archetype from ticket 01 before writing any skill; `/prototype` only if a ticket shifts to "how should it look/behave".

**Tracker:** local-markdown (no issue tracker / no git here). Map: `wayfinder/map.md`. Tickets: `wayfinder/tickets/NN-slug.md`. Blocking via `blocked_by` / `blocks` in frontmatter (no native dependency relationship). The **frontier** = open tickets whose `blocked_by` list is entirely closed. **Research** tickets (02–05) are AFK and fire in parallel during charting (already dispatched).

**Effort start: 2026-08-06** *(date carried to 2026-08-07 mid-charter)*.

## Decisions so far

- [Pin the SKILL.md section template & metadata frontmatter (the archetype)](tickets/01-skill-archetype.md) — Archetype pinned at `wayfinder/skill-archetype.md`.
- [Banking integration standards & event patterns](tickets/05-banking-integration-patterns.md)
- [BIAN service-domain & capability landscape for retail banking](tickets/03-bian-capability-landscape.md)
- [UAE/CBUAE regulatory, compliance & data-residency posture](tickets/02-uae-compliance-posture.md)
- [Build the discovery/ skills (5)](tickets/06-discovery-skills.md) — **Built.**
- [Build the architecture/ skills (8)](tickets/07-architecture-skills.md) — **Built.**
- [Build the modernization/ skills (5)](tickets/09-modernization-skills.md) — **Built.**
- [Build the integration/ skills (6)](tickets/11-integration-skills.md) — **Built.**
- [Build the security/ skills (6)](tickets/12-security-skills.md) — **Built.**
- [Cloud Well-Architected & Landing-Zone Posture (Research)](tickets/04-cloud-well-architected-banking.md) — **Done.**
- [Build the documentation/ skills (6)](tickets/documentation-skills.md) — **Built.**
- [Build the governance/ skills (6)](tickets/governance-skills.md) — **Built.**

## Not yet specified

<!-- Phase 2 — parked until the 64 skills exist and their shape is visible; each graduates into ticket(s) -->
- **Bank-specific templates**
- **Worked examples**
- **Mermaid & draw.io diagram templates**
- **Maturity / complexity rating** per skill
- **Framework index**

## Out of scope

- **Skills beyond the 64 in the catalogue**
- **Implementation / consulting engagements**
- **A bank-specific live environment**
- **Tooling/scripts beyond SKILL.md + references/**
- **Categories beyond the 11 folders**
