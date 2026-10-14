# DOCS_INDEX.md — Domain Index

Quick-reference map of every top-level domain folder in this repository.
Agents: read this file to orient before exploring; it is a navigation pointer, not a spec.

---

| Domain | Folder | Core Skills / Artefacts |
|---|---|---|
| **Discovery** | `discovery/` | `business-capability-map`, `gap-analysis`, `requirements`, `solution-options`, `effort-estimation` |
| **Architecture** | `architecture/` | `c4-model`, `hld-generator`, `lld-generator`, `sequence-diagram`, `deployment-diagram`, `adr-writer`, `nfr-generator` |
| **Business Architecture** | `business-architecture/` | `value-stream`, `capability-model`, `business-case`, `org-design` |
| **Data Architecture** | `data-architecture/` | `data-model`, `data-governance`, `data-lineage`, `mdm`, `data-catalog` |
| **AI / ML Architecture** | `ai-ml-architecture/` | `ai-ethics`, `feature-store`, `mlops-pipeline`, `rag-pattern`, `model-governance` |
| **Modernisation** | `modernization/` | `legacy-assessment`, `impact-analysis`, `modernisation-roadmap`, `refactoring-plan` |
| **Migration** | `migration/` | `cloud-migration`, `db-migration`, `wave-plan`, `cutover-plan`, `rollback-plan` |
| **Integration** | `integration/` | `api-design`, `idempotent-api`, `event-driven`, `etl`, `data-sync`, `hybrid-orchestration` |
| **Security** | `security/` | `threat-model`, `zero-trust`, `iam-review`, `owasp`, `adverse-action-compliance` |
| **Cloud** | `cloud/` | `landing-zone`, `aws-well-architected`, `azure-well-architected`, `gcp-well-architected`, `terraform` |
| **DevOps / FinOps** | `devops/` | `cicd-review`, `sre`, `finops-strategy`, `performance`, `release-readiness` |
| **Governance** | `governance/` | `evidence-gate`, `staleness-detector`, `dashboard`, `adr-board`, `dr-plan`, `raid-log`, `quality-scorer` |
| **Documentation** | `documentation/` | `executive-summary`, `design-doc`, `project-charter`, `risk-register`, `raid-log` |
| **Greenfield** | `greenfield/` | `platform-selection`, `poc-plan`, `reference-architecture`, `roadmap` |
| **Industries** | `industries/` | `healthcare-hipaa`, `insurance-solvency2`, `retail-pcidss`, `government-nist`, `energy-nerc` |
| **Workflows** | `workflows/` | `ai-native-mobile.md` end-to-end playbook |
| **Multi-Agent** | `multi_agent/` | Parallel agent orchestration patterns |
| **Evaluation Suites** | `evaluation-suites/` | Skill correctness benchmarks |

---

## Regulatory Overlays

All overlays live under `governance/policy/regional/`:

| Jurisdiction | Standards covered |
|---|---|
| UAE | CBUAE Cybersecurity Framework, UAE PDPL |
| KSA | SAMA CSF, SDAIA PDPL |
| EU | DORA, GDPR, PSD2/PSD3 SCA, FAPI 2.0 |
| UK | FCA/PRA Supervisory Statements, UK GDPR |
| USA | OCC, FFIEC CAT, SOX §404, NYDFS 500 |
| Singapore | MAS TRM, SG PDPA |
| Australia | APRA CPS 234, Privacy Act 1988 |
| India | RBI Cyber Security Framework, DPDP Act 2023 |
| Global | Basel III/IV, ISO 20022, FATF AML/KYC, PCI-DSS v4 |

---

## Key Cross-Cutting Files

| File | Role |
|---|---|
| `GLOSSARY.md` | Canonical vocabulary — agents read before writing specs |
| `CODING_STANDARDS.md` | Reviewer-time rules (vocabulary, idempotency, cost metadata, ADR lifecycle) |
| `AGENTS.md` | Agent navigation pointers and standing directives |
| `BANKING_WORKFLOWS.md` | End-to-end workflow catalogue |
| `mcp-registry.json` | MCP server registry for external agent discovery |
| `.cursorrules` | Cursor / IDE agent governance rules |
| `.pre-commit-config.yaml` | Pre-commit hooks (ruff, whitespace, EOF) |
| `.github/workflows/ci.yml` | CI pipeline (validation, lint, JSON-schema check) |
