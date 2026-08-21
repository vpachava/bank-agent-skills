# Global Banking Solution-Architect Skills Library

Welcome to the comprehensive, enterprise-grade **Global Banking Solution-Architect Skills Library**. This repository contains **95 invoke-and-act agentic skills** covering the complete solution-architecture lifecycle — from initial discovery and capability mapping through secure design, data architecture, AI/ML integration, and multi-jurisdictional compliance.

---

## 🦅 Bird's-Eye View for Fellow Architects

Building software for financial institutions requires navigating a complex labyrinth of legacy core integration, multi-cloud topologies, polyglot microservices, and stringent regulatory oversight. 

This library treats architecture as **Executable Code** rather than static documentation:
- **Interactive Grilling & Jurisdiction Selection:** When you invoke the entry-point `/solution-arch-orchestrator`, it interactively prompts you for your target country/jurisdiction (e.g., UAE, KSA, EU, UK, USA, Singapore) and binds the exact regulatory policy overlays.
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

The repository comprises **95 active skills** partitioned across **15 core architectural domains**:

| Category | Skill Count | Focus & Core Deliverables |
| :--- | :---: | :--- |
| **`solution-arch-orchestrator`** | 1 | Global Wayfinder & Jurisdiction Routing (UAE, KSA, EU, UK, USA, SG, Global) |
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
| **`governance`** | 11 | Architecture Boards, Evidence Gates, Dashboard Analytics, DR & Production Readiness |
| **`documentation`** | 6 | Executive Summaries, Design Documents, Project Charters, Risk Registers, RAID Logs |
| **`greenfield`** | 5 | Platform Selection, PoC Planning, Reference Architecture, Roadmap Formulation |

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
Invoke the global orchestrator to start any new banking initiative:
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

## 🛡️ Compliance & Regional Overlays

The engine includes built-in compliance modules under `governance/policy/regional/`:
- **UAE:** CBUAE Cybersecurity Framework, UAE PDPL (Federal Decree-Law No. 45 of 2021).
- **KSA:** SAMA Cyber Security Framework, KSA Personal Data Protection Law (SDAIA).
- **EU:** Digital Operational Resilience Act (DORA), GDPR, PSD2/PSD3 SCA.
- **Global Baselines:** Basel III/IV liquidity & capital standards, ISO 20022 messaging (`pacs.008`, `pain.001`), FATF AML/KYC guidelines, and PCI-DSS v4.0.

---

## 🛠️ Repository Synchronization & Testing
- **Test Suite:** `PYTHONPATH=. pytest tests/ -v` (17/17 passing unit tests).
- **CI/CD:** Validated automatically via GitHub Actions and GitLab CI (`.gitlab-ci.yml`).
- **Version:** `v1.0.1`
