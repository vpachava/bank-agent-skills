---
id: "09"
slug: modernization-skills
title: "Build the modernization/ skills (5)"
map: wayfinder/map.md
label: wayfinder:task
type: task
status: closed
assignee: architect
blocked_by: ["01"]
blocks: []
---

## Question

Build the `modernization/` category — **5 invoke-and-act skills**, each `modernization/<name>/SKILL.md` on the locked archetype (ticket 01):

1. **legacy-assessment** — assess a legacy system (health, coupling, risk, modernization potential); produce a legacy-assessment report.
2. **impact-analysis** — analyze blast-radius/impact of a change across a bank's interdependent estate; produce an impact-analysis report.
3. **technical-debt** — inventory & classify technical debt (interest, principal, risk); produce a tech-debt register + prioritization.
4. **refactoring-plan** — produce a refactoring plan (strangler-fig / seams / incremental) with safe steps; produce the plan.
5. **modernization-roadmap** — sequence modernization over waves (strangler-fig, wedge-first, reuse-over-rewrite); produce the roadmap.

Each skill: frontmatter + per-skill metadata; embedded banking checklists (legacy core + interdependencies, regulatory freeze windows, zero-downtime pressure); Banking pitfalls; Outputs (named); Related skills cross-linked — esp. `../migration/cutover-plan`, `../migration/rollback-plan`, `../discovery/gap-analysis`, `../architecture/architecture-decision-records`. The CC onboarding effort's strangler-fig/wedge-first migration notes are reusable worked context for `modernization-roadmap`.

Output = 5 skill files in `skills/modernization/`. Resolution comment names files, close, Decisions-so-far pointer.

## Resolution

**Resolved 2026-08-09. 5 skills built in `skills/modernization/<name>/SKILL.md` (~65–71 lines):**
- `legacy-assessment` — multi-axis health + **coupling map** (the real feasibility brake) + regulatory-exposure axis; verdict **Reuse/Wrap/Replace/Retire** with rationale.
- `impact-analysis` — direct + **ripple (two-hops-min)** + **async/event ripple** (the silent-break); regulatory-pathseverity-amplified; compensating per Major.
- `technical-debt` — debt by **interest × principal × separate-risk** (interest-prevails, low-interest on untouched code is benign); pay-now/service-alongside/accept; skills-debt captured ("only one person knows X").
- `refactoring-plan` — **strangler-fig wedge-first** house posture; step one is often *making a seam*; every step still-runs+rollback; freeze windows honored; **per-slice retirement dates** set.
- `modernization-roadmap` — waves by dependency/value not proximity; wedge-first per wave; six-Rs incl. **Retain-as-legitimate**; **cross-wave invariants** (deterministic regulated paths, residency, audit continuity); governance gates per wave.

**On the archetype:** all 5 follow the locked template — structured-list frontmatter, trigger-first body, inline `>` grounding, banking pitfalls, folder-relative related-skills. `description` strings use the "Use when… — produces…" house style.

**Notes:**
- The CC onboarding effort's **strangler-fig / wedge-first** migration notes were consciously reused as worked context for `refactoring-plan` and `modernization-roadmap` (per the map's Notes pointer to CC as reusable worked examples — content only, not conflating the two efforts).
- **Grounding:** integration research (05) — outbox/idempotent-consumer patterns cited in `refactoring-plan` (async-seam handling); UAE-compliance (02) — residency & cross-zone obligations surfaced in roadmap cross-wave invariants.
- **No research-specific caveats** for this category (it didn't depend on 04 cloud-WAF).
- Minor prose fixes applied during close (a garbled line in `modernization-roadmap`; a stray non-ASCII glyph in `architecture/deployment-diagrams` from an earlier batch — both corrected).
