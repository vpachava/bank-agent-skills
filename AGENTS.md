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
- For new files or rewrites >50% of existing content, use `write_file`. For targeted edits, use `patch`. Never `read_file` + `patch` on a file you are rewriting wholesale.

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

## Domain map, key files, and regulatory overlays → `DOCS_INDEX.md`
