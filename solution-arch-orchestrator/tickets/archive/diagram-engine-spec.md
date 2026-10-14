## Objective:
Extend all 91 skills to support programmatic visual generation of architectural state.

## Implementation Tasks (Add to hardening map):
1. [ ] **TICKET: Canonical Mermaid Definitions**
   - Establish the standard Mermaid syntax for all banking components (Core Banking, Payment Hub, IAM, API Gateway).
2. [ ] **TICKET: Archify Post-Processor Implementation**
   - Create the `/archify` skill that takes raw `design.json` (from any other skill) and maps it to standardized templates.
3. [ ] **TICKET: Template Repository Creation (`diagram-templates/`)**
   - Populate with standardized banking patterns (C4 Context, Sequence Flows for ISO20022, Deployment Zones).
4. [ ] **TICKET: Pipeline Integration**
   - Update `ci.yml` to fail if a skill claims to produce a design but lacks the corresponding Mermaid/PlantUML export.

## Governance Rule:
Every diagram must be tagged with a unique `artifact_id` in its metadata that links back to the specific architectural skill/version that generated it. This prevents "orphan diagrams" that were drawn manually and no longer reflect the code.
