# Global Banking Solution-Architect Skills Library

Welcome to the comprehensive, enterprise-grade **Global Banking Solution-Architect Skills Library**. This repository contains **100 invoke-and-act agentic skills** partitioned across **16 structured architectural categories** covering the complete solution-architecture lifecycle — from initial discovery and capability mapping through secure design, data architecture, AI/ML integration, and multi-jurisdictional compliance.

---

## 🦅 Bird's-Eye View for Fellow Architects

Building software for financial institutions requires navigating a complex labyrinth of legacy core integration, multi-cloud topologies, polyglot microservices, and stringent regulatory oversight. 

This library treats architecture as **Executable Code** rather than static documentation:
- **Interactive Grilling & Jurisdiction Selection:** When you invoke the entry-point `/solution-arch-orchestrator`, it interactively prompts you for your target country/jurisdiction (e.g., UAE, KSA, EU, UK, USA, Singapore, Australia, India) and binds the exact regulatory policy overlays.
- **Evidence-Based Verification (`/governance/evidence-gate`):** Agents do not just generate markdown prose; they inspect your repository's actual infrastructure-as-code (Terraform, Kubernetes manifests) to prove compliance before architectural sign-off.
- **Diagram-as-Code (`/archify`):** Automatically compiles design artifacts into canonical **Mermaid.js** diagrams and renders an end-to-end architecture visual.
- **Spec & Tracker Export:** Seamlessly exports architectural schemas into **OpenAPI 3.1**, **AsyncAPI 3.0**, and pre-formatted **Jira/Linear** execution tickets.

---

## 🏛️ End-to-End Architecture Overview

Below is the end-to-end execution flow of the governance engine:

![Global Banking Architecture Overview](diagram-templates/architecture-overview.svg)

*(For detailed Mermaid syntax, inspect `diagram-templates/architecture-overview.mmd`)*

---

## 📊 Library Statistics & Categories

The repository comprises **100 active skills** partitioned across **16 core architectural domains**:

| Category | Skill Count | Focus & Core Deliverables |
| :--- | :---: | :--- |
| **`solution-arch-orchestrator`** | 1 | Global Wayfinder & Jurisdiction Routing (UAE, KSA, EU, UK, USA, SG, AU, IN, Global) |
| **`discovery`** | 5 | Business Capability Mapping, Gap Analysis, Requirements, Solution Options, Workshops |
| **`architecture`** | 9 | C4 Models, HLD/LLD Generators, Sequence Diagrams, Deployment Diagrams, ADRs, NFRs |
| **`business-architecture`** | 6 | Value Streams, Capability Models, Business Cases, Organizational Design |
| **`data-architecture`** | 6 | Data Modeling, Governance, Lineage, Master Data Management (MDM) |
| **`ai-ml-architecture`** | 6 | AI Ethics, Feature Stores, MLOps Pipelines, RAG Patterns, Model Governance |
| **`modernization`** | 5 | Legacy Assessment, Impact Analysis, Modernization Roadmaps, Refactoring Plans |
| **`migration`** | 6 | Cloud/Database Migration, Wave Planning, Cutover & Rollback Plans |
| **`integration`** | 7 | API Design, Idempotent APIs, Event-Driven Messaging, ETL, Data Sync |
| **`security`** | 7 | Threat Modeling (STRIDE/PASTA), Zero Trust, IAM Reviews, OWASP, Adversarial Compliance |
| **`cloud`** | 6 | Landing Zone Reviews, AWS/Azure/GCP Well-Architected Reviews, Terraform |
| **`devops`** | 6 | CI/CD Reviews, SRE, FinOps Strategy, Performance & Release Readiness |
| **`governance`** | 14 | Architecture Boards, Evidence Gates, Dashboard Analytics, DR, RAID Logs & Quality Scorer |
| **`documentation`** | 6 | Executive Summaries, Design Documents, Project Charters, Risk Registers, RAID Logs |
| **`greenfield`** | 5 | Platform Selection, PoC Planning, Reference Architecture, Roadmap Formulation |
| **`industries`** | 5 | Healthcare (HIPAA), Insurance (Solvency II), Retail (PCI-DSS), Government (NIST), Energy (NERC) |

---

## 🚀 Quick Start for Fellow Architects

### 1. Installation
Clone the repository and install the skills into your local agent environment (Hermes Agent or Claude Code CLI):
```bash
git clone https://github.com/vpachava/bank-agent-skills.git
cd bank-agent-skills
./install.sh
```

### 2. Execution Entry Point
Invoke the global orchestrator to start any new initiative:
```text
/solution-arch-orchestrator
```
*The orchestrator will prompt you for your initiative scope and target jurisdiction, generating a tailored, compliance-bound execution workflow.*

### 3. Local Quality Gates (Pre-commit hooks)
Ensure your architecture specs and code conform to repository standards:
```bash
python scripts/setup_hooks.py
```

---


---

## 👥 Persona-Based Entry Points

Whether you are governing enterprise tech stacks, designing microservices, or planning delivery sprints, find your entry point below:

### 🏛️ Architecture Personas
- **Enterprise Architect:** Use `/solution-arch-orchestrator` and `architecture/c4-model` to establish enterprise baselines and BIAN domain maps.
- **Solution Architect:** Use `architecture/hld-generator`, `architecture/lld-generator`, and `archify` to design and render end-to-end flows (e.g., dual-orchestration credit limit increases).
- **Domain Architect:** Use `discovery/business-capability-map` and domain-specific modeling skills.
- **Technical Architect:** Use `architecture/database-design` and `cloud/terraform` for deep technical realization.
- **Integration Architect:** Use `integration/api-design`, `integration/event-driven`, and `integration/idempotent-api` for reliable enterprise messaging.
- **Security & Infosec Architect:** Use `security/threat-model`, `security/zero-trust`, and `security/compliance` (CBUAE, SAMA, DORA, PCI-DSS v4).
- **API Governance Architect:** Use `integration/api-design` and OpenAPI/AsyncAPI verification rules.

### 🚀 Delivery & Product Personas (Effort Sizing & Execution)
- **Product Owner & AI PM:** Use `discovery/effort-estimation`, `discovery/solution-options`, and `workflows/ai-native-mobile.md` for feature sizing and AI-native mobile transformation.
- **Scrum Master & Head of IT:** Use `discovery/effort-estimation`, `devops/release-readiness`, and `governance/operational-readiness` for capacity planning, risk logs, and sprint governance.

## 🛡️ Compliance & Regional Overlays

The engine includes built-in compliance modules under `governance/policy/regional/`:
- **UAE:** CBUAE Cybersecurity Framework, UAE PDPL.
- **KSA:** SAMA Cyber Security Framework, SDAIA PDPL.
- **EU:** Digital Operational Resilience Act (DORA), GDPR, PSD2/PSD3 SCA.
- **UK:** FCA/PRA Supervisory Statements, UK GDPR.
- **USA:** OCC Risk Guidelines, FFIEC CAT, SOX Section 404, NYDFS 500.
- **Singapore:** MAS TRM Guidelines, SG PDPA.
- **Australia:** APRA CPS 234, Privacy Act 1988.
- **India:** RBI Cyber Security Framework, DPDP Act 2023.
- **Global Baselines:** Basel III/IV capital & liquidity standards, ISO 20022 messaging (`pacs.008`, `pain.001`, `camt.053`), FATF AML/KYC guidelines, and PCI-DSS v4.0.

---

## 🛠️ Repository Synchronization & Testing
- **Test Suite:** `PYTHONPATH=. pytest tests/ -v` (20/20 passing unit tests).
- **CI/CD:** Validated automatically via GitHub Actions and GitLab CI (`.gitlab-ci.yml`).
- **Version:** `v1.0.1`
