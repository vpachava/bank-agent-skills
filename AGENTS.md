# AGENTS.md — Navigation Pointers

This file is read by every AI agent working in this repository.
Keep it **sparse**: navigation pointers only. Full detail lives in the files pointed to.

---

## Standing Directives (apply to every task)

- Before any architectural change, confirm a ticket exists in `solution-arch-orchestrator/tickets/`.
- Always check `GLOSSARY.md` for canonical term definitions before writing specs or skill docs.
- Always check `governance/policy/regional/` for applicable regulatory overlays before touching payment, identity, or data-residency skills.
- All mobile-to-core calls MUST traverse the BFF seam (ADR: `architecture/docs/adr/0002-bff-pattern-seam.md`).
- All transactional API handlers MUST include an `Idempotency-Key` header.
- Run `python scripts/validate_skill_readiness.py` before committing new or modified skills.
- Full coding standards for review-time judgement calls → `CODING_STANDARDS.md`.

---

## Persona Entry Points

| Persona | Start here |
|---|---|
| **Enterprise Architect** | `solution-arch-orchestrator/SKILL.md` → `architecture/c4-model/` |
| **Solution Architect** | `architecture/hld-generator/` → `architecture/lld-generator/` → `archify` |
| **Domain Architect** | `discovery/business-capability-map/` |
| **Technical Architect** | `architecture/database-design/` → `cloud/terraform/` |
| **Integration Architect** | `integration/api-design/` → `integration/event-driven/` → `integration/idempotent-api/` |
| **Security Architect** | `security/threat-model/` → `security/zero-trust/` → `security/compliance/` |
| **Product Owner / AI PM** | `discovery/effort-estimation/` → `workflows/ai-native-mobile.md` |
| **Scrum Master / Head of IT** | `discovery/effort-estimation/` → `devops/release-readiness/` → `governance/operational-readiness/` |
| **FinOps / Cost Optimisation** | `devops/finops-strategy/` → `CODING_STANDARDS.md §3` |
| **Data Architect** | `data-architecture/` → `GLOSSARY.md` |
| **AI/ML Architect** | `ai-ml-architecture/` → `GLOSSARY.md` |
| **Modernisation Lead** | `modernization/` → `migration/` |
| **Cloud Architect** | `cloud/` → `cloud/terraform/` |

---

## Domain Map

| Domain folder | What's inside |
|---|---|
| `discovery/` | Business-capability mapping, gap analysis, requirements, effort estimation |
| `architecture/` | C4, HLD/LLD, sequence/deployment diagrams, ADRs, NFRs |
| `business-architecture/` | Value streams, capability models, org design |
| `data-architecture/` | Data modelling, governance, lineage, MDM |
| `ai-ml-architecture/` | AI ethics, feature stores, MLOps, RAG, model governance |
| `modernization/` | Legacy assessment, impact analysis, modernisation roadmaps |
| `migration/` | Cloud/DB migration, wave planning, cutover & rollback |
| `integration/` | API design, idempotent APIs, event-driven, ETL, data sync |
| `security/` | STRIDE/PASTA threat models, zero-trust, IAM, OWASP |
| `cloud/` | Landing zones, AWS/Azure/GCP Well-Architected, Terraform |
| `devops/` | CI/CD, SRE, FinOps, performance, release readiness |
| `governance/` | Architecture boards, evidence gates, dashboards, DR, RAID |
| `documentation/` | Executive summaries, design docs, risk registers |
| `greenfield/` | Platform selection, PoC planning, reference architecture |
| `industries/` | Healthcare, Insurance, Retail, Government, Energy verticals |
| `workflows/` | End-to-end workflow playbooks (e.g., AI-native mobile) |

---

## Key Reference Files

| File | Purpose |
|---|---|
| `GLOSSARY.md` | Canonical term definitions — read before writing any spec |
| `CODING_STANDARDS.md` | Reviewer-time judgement-call rules |
| `BANKING_WORKFLOWS.md` | Full workflow catalogue with skill sequences |
| `DOCS_INDEX.md` | Domain index with folder descriptions |
| `mcp-registry.json` | MCP server endpoints for external agent discovery |
| `.cursorrules` | IDE agent governance rules |
| `governance/scripts/governance_engine.py` | Unified deep-module governance adapter |
| `scripts/validate_skill_readiness.py` | Pre-commit skill validation |
