---
id: "10"
slug: migration-skills
title: "Build the migration/ skills (6)"
map: wayfinder/map.md
label: wayfinder:task
type: task
status: open
blocked_by: ["01","04","05"]
blocks: []
---

## Question

Build the `migration/` category — **6 invoke-and-act skills**, each `migration/<name>/SKILL.md` on the locked archetype (ticket 01):

1. **cloud-migration** — plan a cloud migration (6Rs, landing-zone-aware) for a banking workload; produce a cloud-migration plan.
2. **database-migration** — plan a DB migration (schema, data, cutover, sync) including core-banking data constraints; produce the DB-migration plan.
3. **application-migration** — plan application migration (rehost/refactor/replatform) with integration seams (research 05); produce the app-migration plan.
4. **migration-wave-planning** — sequence workloads into migration waves by dependency/risk; produce a wave plan.
5. **rollback-plan** — author a rollback plan (triggers, steps, data-consistency) for a migration/rollout; produce the rollback plan.
6. **cutover-plan** — author a cutover plan (pre-checks, runbook, freeze, go/no-go, hypercare) for a banking release; produce the cutover plan.

Each skill: frontmatter + per-skill metadata; embedded banking checklists (zero-downtime, reconciliation, regulatory freeze, dual-run); Banking pitfalls (silent data drift, partial cutover, orphaned integrations); Outputs (named); Related skills cross-linked — `../modernization/modernization-roadmap`, `../devops/release-readiness`, `../governance/production-readiness`. Ground cloud landing zones (research 04) and integration seams (research 05) where they earn it.

Output = 6 skill files in `skills/migration/`. Resolution comment names files, close, Decisions-so-far pointer.

## Resolution
