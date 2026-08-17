# UAE Retail-Bank Solution-Architect Skills Library

Welcome to the comprehensive skills library for UAE retail-bank solution architecture. This repository contains **invoke-and-act** Claude Code skills covering the complete solution-architecture lifecycle — from initial discovery through operational readiness.

## What is this library?

This library is a collection of 64+ concrete, executable skills. Unlike static reference documentation, these are **active processes**. Each skill is invoked as a slash command (e.g., `/threat-model`) which triggers an interactive assessment or generation process.

Each skill features:
- **Embedded Checklists & Pitfalls:** Banking-specific and UAE-specific constraints, common anti-patterns, and step-by-step checklists.
- **Industry-framework Grounding:** Inline and actionable alignment with BIAN, TOGAF, C4, AWS Well-Architected, Azure CAF, OWASP, NIST, SRE, and ITIL 4 frameworks.
- **Concrete Deliverables:** Every skill produces an explicit artifact (e.g., a high-level design document, a risk register, a platform evaluation report).

## How to Use

Skills are designed to be invoked sequentially through the structural lifecycle phases of architecture. You can invoke them using their short, unprefixed names (e.g., `/solution-options`).

**The Lifecycle Throughline:**
1. **Discovery & Assessment (`discovery/`, `modernization/`, `greenfield/`)** -> Understand the landscape. Map capabilities, assess legacy tech debt, and evaluate candidate target platforms.
2. **Planning & Strategy (`migration/`, `architecture/`)** -> Establish the blueprints and transition roadmaps. Map high-level/low-level designs, target non-functional requirements (NFRs), and sequence migration waves.
3. **Secure & Integrate Early (`security/`, `integration/`)** -> Front-load risk. Enforce enterprise zero-trust, IAM best practices, API designs, and messaging models before any coding happens.
4. **Platform & Validation (`cloud/`, `devops/`)** -> Ensure continuous quality and readiness. Verify well-architected cloud footprint, CI/CD checks, and release gates.
5. **Governance Gates & Tracking (`governance/`, `documentation/`)** -> Manage lifecycle status. Present to architecture boards, gate production releases, and continuously maintain RAID logs and risk registers.

## Catalogue

### Discovery
- **[business-capability-map](discovery/business-capability-map/SKILL.md)** — `No description provided.` Invoke with: `/business-capability-map`
- **[gap-analysis](discovery/gap-analysis/SKILL.md)** — `No description provided.` Invoke with: `/gap-analysis`
- **[requirements-analysis](discovery/requirements-analysis/SKILL.md)** — `No description provided.` Invoke with: `/requirements-analysis`
- **[solution-options](discovery/solution-options/SKILL.md)** — `No description provided.` Invoke with: `/solution-options`
- **[stakeholder-workshop](discovery/stakeholder-workshop/SKILL.md)** — `No description provided.` Invoke with: `/stakeholder-workshop`

### Architecture
- **[architecture-decision-records](architecture/architecture-decision-records/SKILL.md)** — `No description provided.` Invoke with: `/architecture-decision-records`
- **[architecture-review](architecture/architecture-review/SKILL.md)** — `No description provided.` Invoke with: `/architecture-review`
- **[c4-model](architecture/c4-model/SKILL.md)** — `No description provided.` Invoke with: `/c4-model`
- **[database-design](architecture/database-design/SKILL.md)** — `No description provided.` Invoke with: `/database-design`
- **[deployment-diagrams](architecture/deployment-diagrams/SKILL.md)** — `No description provided.` Invoke with: `/deployment-diagrams`
- **[hld-generator](architecture/hld-generator/SKILL.md)** — `No description provided.` Invoke with: `/hld-generator`
- **[lld-generator](architecture/lld-generator/SKILL.md)** — `No description provided.` Invoke with: `/lld-generator`
- **[nfr-checklist](architecture/nfr-checklist/SKILL.md)** — `No description provided.` Invoke with: `/nfr-checklist`
- **[sequence-diagrams](architecture/sequence-diagrams/SKILL.md)** — `No description provided.` Invoke with: `/sequence-diagrams`

### Greenfield
- **[platform-selection](greenfield/platform-selection/SKILL.md)** — `No description provided.` Invoke with: `/platform-selection`
- **[poc-planning](greenfield/poc-planning/SKILL.md)** — `No description provided.` Invoke with: `/poc-planning`
- **[reference-architecture](greenfield/reference-architecture/SKILL.md)** — `No description provided.` Invoke with: `/reference-architecture`
- **[roadmap](greenfield/roadmap/SKILL.md)** — `No description provided.` Invoke with: `/roadmap`
- **[technology-evaluation](greenfield/technology-evaluation/SKILL.md)** — `No description provided.` Invoke with: `/technology-evaluation`

### Modernization
- **[impact-analysis](modernization/impact-analysis/SKILL.md)** — `No description provided.` Invoke with: `/impact-analysis`
- **[legacy-assessment](modernization/legacy-assessment/SKILL.md)** — `No description provided.` Invoke with: `/legacy-assessment`
- **[modernization-roadmap](modernization/modernization-roadmap/SKILL.md)** — `No description provided.` Invoke with: `/modernization-roadmap`
- **[refactoring-plan](modernization/refactoring-plan/SKILL.md)** — `No description provided.` Invoke with: `/refactoring-plan`
- **[technical-debt](modernization/technical-debt/SKILL.md)** — `No description provided.` Invoke with: `/technical-debt`

### Migration
- **[application-migration](migration/application-migration/SKILL.md)** — `No description provided.` Invoke with: `/application-migration`
- **[cloud-migration](migration/cloud-migration/SKILL.md)** — `No description provided.` Invoke with: `/cloud-migration`
- **[cutover-plan](migration/cutover-plan/SKILL.md)** — `No description provided.` Invoke with: `/cutover-plan`
- **[database-migration](migration/database-migration/SKILL.md)** — `No description provided.` Invoke with: `/database-migration`
- **[migration-wave-planning](migration/migration-wave-planning/SKILL.md)** — `No description provided.` Invoke with: `/migration-wave-planning`
- **[rollback-plan](migration/rollback-plan/SKILL.md)** — `No description provided.` Invoke with: `/rollback-plan`

### Integration
- **[api-design](integration/api-design/SKILL.md)** — `No description provided.` Invoke with: `/api-design`
- **[data-sync](integration/data-sync/SKILL.md)** — `No description provided.` Invoke with: `/data-sync`
- **[etl](integration/etl/SKILL.md)** — `No description provided.` Invoke with: `/etl`
- **[event-driven](integration/event-driven/SKILL.md)** — `No description provided.` Invoke with: `/event-driven`
- **[idempotent-api](integration/idempotent-api/SKILL.md)** — `No description provided.` Invoke with: `/idempotent-api`
- **[integration-patterns](integration/integration-patterns/SKILL.md)** — `No description provided.` Invoke with: `/integration-patterns`
- **[messaging](integration/messaging/SKILL.md)** — `No description provided.` Invoke with: `/messaging`

### Security
- **[compliance](security/compliance/SKILL.md)** — `No description provided.` Invoke with: `/compliance`
- **[iam-review](security/iam-review/SKILL.md)** — `No description provided.` Invoke with: `/iam-review`
- **[owasp-review](security/owasp-review/SKILL.md)** — `No description provided.` Invoke with: `/owasp-review`
- **[security-architecture-review](security/security-architecture-review/SKILL.md)** — `No description provided.` Invoke with: `/security-architecture-review`
- **[threat-model](security/threat-model/SKILL.md)** — `No description provided.` Invoke with: `/threat-model`
- **[zero-trust](security/zero-trust/SKILL.md)** — `No description provided.` Invoke with: `/zero-trust`

### Cloud
- **[aws-review](cloud/aws-review/SKILL.md)** — `No description provided.` Invoke with: `/aws-review`
- **[azure-review](cloud/azure-review/SKILL.md)** — `No description provided.` Invoke with: `/azure-review`
- **[gcp-review](cloud/gcp-review/SKILL.md)** — `No description provided.` Invoke with: `/gcp-review`
- **[kubernetes](cloud/kubernetes/SKILL.md)** — `No description provided.` Invoke with: `/kubernetes`
- **[landing-zone-review](cloud/landing-zone-review/SKILL.md)** — `No description provided.` Invoke with: `/landing-zone-review`
- **[terraform](cloud/terraform/SKILL.md)** — `No description provided.` Invoke with: `/terraform`

### DevOps
- **[cicd-review](devops/cicd-review/SKILL.md)** — `No description provided.` Invoke with: `/cicd-review`
- **[finops-strategy](devops/finops-strategy/SKILL.md)** — `No description provided.` Invoke with: `/finops-strategy`
- **[observability](devops/observability/SKILL.md)** — `No description provided.` Invoke with: `/observability`
- **[performance-review](devops/performance-review/SKILL.md)** — `No description provided.` Invoke with: `/performance-review`
- **[release-readiness](devops/release-readiness/SKILL.md)** — `No description provided.` Invoke with: `/release-readiness`
- **[sre-review](devops/sre-review/SKILL.md)** — `No description provided.` Invoke with: `/sre-review`

### Documentation
- **[design-document](documentation/design-document/SKILL.md)** — `No description provided.` Invoke with: `/design-document`
- **[executive-summary](documentation/executive-summary/SKILL.md)** — `No description provided.` Invoke with: `/executive-summary`
- **[project-charter](documentation/project-charter/SKILL.md)** — `No description provided.` Invoke with: `/project-charter`
- **[proposal](documentation/proposal/SKILL.md)** — `No description provided.` Invoke with: `/proposal`
- **[raid-log](documentation/raid-log/SKILL.md)** — `No description provided.` Invoke with: `/raid-log`
- **[risk-register](documentation/risk-register/SKILL.md)** — `No description provided.` Invoke with: `/risk-register`

### Governance
- **[ai-governance](governance/ai-governance/SKILL.md)** — `No description provided.` Invoke with: `/ai-governance`
- **[ai-model-governance](governance/ai-model-governance/SKILL.md)** — `No description provided.` Invoke with: `/ai-model-governance`
- **[architecture-board](governance/architecture-board/SKILL.md)** — `No description provided.` Invoke with: `/architecture-board`
- **[design-review](governance/design-review/SKILL.md)** — `No description provided.` Invoke with: `/design-review`
- **[dr-review](governance/dr-review/SKILL.md)** — `No description provided.` Invoke with: `/dr-review`
- **[operational-readiness](governance/operational-readiness/SKILL.md)** — `No description provided.` Invoke with: `/operational-readiness`
- **[production-readiness](governance/production-readiness/SKILL.md)** — `No description provided.` Invoke with: `/production-readiness`
- **[security-nfr-baseline-check](governance/security-nfr-baseline-check/SKILL.md)** — `No description provided.` Invoke with: `/security-nfr-baseline-check`
- **[solution-review](governance/solution-review/SKILL.md)** — `No description provided.` Invoke with: `/solution-review`

### Wayfinder (Orchestration)
- **[orchestrator](wayfinder/orchestrator/SKILL.md)** — `No description provided.` Invoke with: `/orchestrator`

### Tooling & CI/CD
- **[tdd-documentation](.claude/tdd-documentation/SKILL.md)** — `Use when authoring or refactoring skills (SKILL.md) to ensure disciplined, TDD-based construction.` Invoke with: `/tdd-documentation`

## Cross-Link Navigation

Each `.md` document includes a "Related Skills" or "Inputs/Outputs" section in its frontmatter metadata enabling navigation across the graph. 
For example, you might flow from `/gap-analysis` -> `/solution-options` -> `/architecture-board`.

**Core Orchestration:** Use `/orchestrator` located in `wayfinder/` to orchestrate agents automatically executing these sequences.
