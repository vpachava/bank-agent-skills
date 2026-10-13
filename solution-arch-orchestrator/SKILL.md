---
name: solution-arch-orchestrator
owner: Architectural Governance
version: 1.2.0
description: "Meta-skill: Receives a raw banking requirement, prompts the user to select their target country/regulatory jurisdiction (e.g., UAE, KSA, EU, USA, UK, Singapore), and maps it to the necessary subset of architectural skills with region-specific compliance overlays."
required-inputs:
  - Raw business requirement
  - Target country / regulatory jurisdiction
expected-deliverables:
  - Country-aware skill-mapping report
  - Actionable dependency workflow with regional guardrails
togaf-phases: [Phase A]
togaf-artifacts: [Architecture Vision]
bian-service-domains: [Customer Account.Origination]
---

# /solution-arch-orchestrator (Global Banking Edition)

## When to apply
Use as the universal entry point for *any* banking initiative worldwide. It acts as the global Wayfinder for the skills library, taking your raw prompt, executing a mandatory **Country/Jurisdiction Selection Grilling Session**, and tailoring the architectural workflow to local regulations.

## Inputs
- Raw business requirement
- Target country / jurisdiction (Prompted interactively: UAE, KSA, EU, UK, USA, SG, or Global)

## Process (Global Grilling Workflow)
1. **Jurisdiction Selection:** Prompt the user: *"Which country or regulatory jurisdiction is this solution targeting? (e.g., UAE / KSA / EU / UK / USA / Singapore)"*
2. **Regulatory Overlay Binding:** Automatically bind the corresponding policy files from `governance/policy/regional/` (e.g., CBUAE, SAMA, DORA/GDPR, FCA/PRA, OCC/Fed, MAS).
3. **Capability Mapping:** Map the requirements against BIAN service domains and TOGAF phases.
4. **Actionable Roadmap Generation:** Produce a tailored dependency roadmap embedding local data residency, cross-border, and security requirements.

## Outputs
- Country-scoped architectural workflow & artifact plan.
- Regional compliance matrix.

## Related skills
- [/governance/policy/regional/](../governance/policy/regional/)
- [/security/compliance](../security/compliance/SKILL.md)
- [/architecture/hld-generator](../architecture/hld-generator/SKILL.md)
