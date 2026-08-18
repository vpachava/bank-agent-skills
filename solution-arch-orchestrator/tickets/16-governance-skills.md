---
id: "16"
slug: governance-skills
title: "Build the governance/ skills (6)"
map: solution-arch-orchestrator/map.md
label: wayfinder:task
type: task
status: open
blocked_by: ["01","02"]
blocks: []
---

## Question

Build the `governance/` category — **6 invoke-and-act skills**, each `governance/<name>/SKILL.md` on the locked archetype (ticket 01):

1. **architecture-board** — run/prepare an architecture board review (submission, lenses, gating) for a banking solution; produce a board pack + decision.
2. **solution-review** — run a solution review (end-to-end fitness for purpose) for a banking initiative; produce the solution-review report.
3. **design-review** — run a design review (vs. standards/patterns/NFRs) for a banking component; produce the design-review report.
4. **production-readiness** — gate production readiness (go-live: release, ops, DR, security, monitoring) for a banking solution; produce the readiness verdict.
5. **dr-review** — review DR posture (RTO/RPO, failover, runbook, test cadence) for a banking service; produce the DR review.
6. **operational-readiness** — gate operational readiness (runbooks, on-call, SLOs, support model) for a banking service; produce the ops-readiness verdict.

Each skill: frontmatter + per-skill metadata; embedded banking checklists (CBUAE resilience direction per research 02, regulated freeze, dual-sign-off audit); Banking pitfalls (readiness theater, DR untested, SLO/audit mismatch); Outputs (named); Related skills cross-linked — governance is the *gate* layer; cross-link heavily: `../devops/release-readiness`, `../devops/sre-review`, `../security/security-architecture-review`, `../migration/cutover-plan`, `../cloud/landing-zone-review`. Ground UAE compliance posture (research 02) for resilience/security direction.

Output = 6 skill files in `skills/governance/`. Resolution comment names files, close, Decisions-so-far pointer.

## Resolution
