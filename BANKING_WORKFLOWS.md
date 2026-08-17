# Banking Workflow Catalog

This catalog defines standardized skill sequences for common banking architectural scenarios.

## 1. Greenfield Project
Setup a brand new software system from scratch with C4 modeling, high level design, and low level design.
- **Sequence:**
  1. `architecture/c4-model` (Vision)
  2. `architecture/hld-generator` (High Level Design)
  3. `architecture/lld-generator` (Low Level Design)

## 2. Legacy Modernization
Assess a legacy component and produce modernization roadmap and high level design.
- **Sequence:**
  1. `modernization/legacy-assessment` (Assess)
  2. `architecture/hld-generator` (New Design)

## 3. Cloud Migration
Plan wave-based migration of resources to hyperscaler and design deployment zones.
- **Sequence:**
  1. `migration/cloud-migration` (Assess)
  2. `architecture/deployment-diagrams` (Deployment Setup)

## 4. API Design
Architect high performance and idempotent APIs with strong design patterns.
- **Sequence:**
  1. `integration/api-design` (Design API)
  2. `integration/idempotent-api` (Idempotence Guarantee)

## 5. Security Review
Audit architecture for compliance and threats.
- **Sequence:**
  1. `security/threat-model` (Identify Threats)
  2. `security/compliance` (Audit Standards)

## 6. Data Migration
Process and migrate core data between datastores safely.
- **Sequence:**
  1. `migration/database-migration` (Data Map)
  2. `integration/etl` (Migration Pipelines)

## 7. Microservices Decomposition
Assess monolithic system and break down into microservices and event-driven patterns.
- **Sequence:**
  1. `modernization/impact-analysis` (Evaluate Blast Radius)
  2. `integration/event-driven` (Establish Publish/Subscribe)

## 8. DevOps Transformation
Build automated deployments and establish validation controls.
- **Sequence:**
  1. `devops/cicd-review` (Assess CI/CD pipeline)
  2. `devops/release-readiness` (Production Sign-off)

## 9. Multi-cloud Strategy
Configure target infrastructure across several cloud environments.
- **Sequence:**
  1. `cloud/landing-zone-review` (Structure Landing Zones)
  2. `cloud/terraform` (Deploy Infrastructure)

## 10. AI/ML Integration
Introduce ML pipelines and operational governance checks.
- **Sequence:**
  1. `governance/ai-model-governance` (Assess model risks)
  2. `governance/ai-governance` (Audit AI systems)

All 10 workflows are validated against the composition taxonomy.
