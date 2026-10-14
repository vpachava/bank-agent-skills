---
id: "13"
slug: cloud-skills
title: "Build the cloud/ skills (6)"
map: solution-arch-orchestrator/map.md
label: wayfinder:task
type: task
status: open
blocked_by: ["01","02","04"]
blocks: []
---

## Question

Build the `cloud/` category — **6 invoke-and-act skills**, each `cloud/<name>/SKILL.md` on the locked archetype (ticket 01):

1. **aws-review** — run an AWS Well-Architected review (banking lens) for a workload; produce a WAF review report with prioritized findings.
2. **azure-review** — run an Azure Well-Architected review (banking lens) mirroring aws-review structure; produce the review report.
3. **gcp-review** — run a GCP Well-Architected-equivalent review for parity; produce the review report.
4. **kubernetes** — design/review Kubernetes platform topology (banking: multi-tenant, secrets, GitOps, policy); produce the design/review.
5. **terraform** — design/review Terraform / IaC posture (modules, state, policy guardrails, landing-zone IaC) for a bank; produce the design/review.
6. **landing-zone-review** — review a cloud landing zone (AWS/Azure + UAE residency constraint from research 02/04) for regulated banking; produce the landing-zone review.

Each skill: frontmatter + per-skill metadata; embedded banking checklists (residency, regulated-load, DR pairing, cost guardrails); Banking pitfalls (cross-cloud drift, policy gaps, key sprawl); Outputs (named); Related skills cross-linked — `../security/zero-trust`, `../migration/cloud-migration`, `../devops/cicd-review`. Ground vendor WAF pillars + landing zones (research 04) and UAE residency (research 02) where they earn it. These are heavier skills — use `references/` for per-provider detail if a SKILL.md would otherwise blow past the depth band.

Output = 6 skill files in `skills/cloud/`. Resolution comment names files, close, Decisions-so-far pointer.

## Resolution
