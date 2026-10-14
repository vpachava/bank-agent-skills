---
id: "14"
slug: devops-skills
title: "Build the devops/ skills (5)"
map: solution-arch-orchestrator/map.md
label: wayfinder:task
type: task
status: open
blocked_by: ["01"]
blocks: []
---

## Question

Build the `devops/` category — **5 invoke-and-act skills**, each `devops/<name>/SKILL.md` on the locked archetype (ticket 01):

1. **cicd-review** — review a CI/CD pipeline (build, test gates, promote, artifacts) for a banking team; produce the review report.
2. **release-readiness** — gate a release for go/no-go (change-advisory, test evidence, rollback); produce a release-readiness checklist/verdict.
3. **observability** — design/review observability (metrics, logs, traces, OTel) for a banking solution; produce the observability design/review.
4. **sre-review** — run an SRE review (SLOs/SLIs, error budgets, toil, incident mgmt per ITIL/SRE) for a banking service; produce the SRE review.
5. **performance-review** — design/run a performance review (load, capacity,瓶颈, NFR-anchored) for a banking workload; produce the perf review.

Each skill: frontmatter + per-skill metadata; embedded banking checklists (regulated-release, audit trail, dual-run windows, incident/comms); Banking pitfalls (silent SLO descoping, trace-gaps on regulated paths, cost-unwatched scale); Outputs (named); Related skills cross-linked — `../governance/production-readiness`, `../governance/operational-readiness`, `../architecture/nfr-checklist`. The CC onboarding effort's OTel-GenAI / traced-release / eval-harness notes are reusable worked context for **observability**.

Output = 5 skill files in `skills/devops/`. Resolution comment names files, close, Decisions-so-far pointer.

## Resolution
