---
id: "12"
slug: security-skills
title: "Build the security/ skills (6)"
map: wayfinder/map.md
label: wayfinder:task
type: task
status: closed
assignee: architect
blocked_by: ["01","02"]
blocks: []
---

## Question

Build the `security/` category — **6 invoke-and-act skills**, each `security/<name>/SKILL.md` on the locked archetype (ticket 01):

1. **threat-model** — produce a threat model (STRIDE/PASTA, data-flow, trust boundaries) for a banking component; produce the threat model.
2. **owasp-review** — run an OWASP (API/Open Top10 + LLM Top10 given the bank's AI-native surface) review; produce findings + remediation.
3. **zero-trust** — design a zero-trust posture (identity segmentation, mTLS, policy, micro-perimeters) for a banking estate; produce the design.
4. **iam-review** — review IAM (identity, roles, least-privilege, federation, UAE identity fabric — UAE Pass/EFR context from research 02) for a banking solution; produce the IAM review.
5. **compliance** — map a design to UAE/CBUAE + standard compliance (CBUAE cyber, DIFC/ADGM, ISO/NIST per research 02); produce a compliance assessment.
6. **security-architecture-review** — run a security architecture review across a banking solution; produce a review report with findings/severity.

Each skill: frontmatter + per-skill metadata; embedded banking checklists (PII/fraud, audit/provenance, CBUAE direction); Banking pitfalls (silent privilege creep, key custody across clouds, provider-plugin trust); Outputs (named); Related skills cross-linked — `../cloud/landing-zone-review`, `../governance/production-readiness`. Ground UAE compliance posture (research 02) heavily — this is the most UAE-bound category; cite sources/confidence.

Output = 6 skill files in `skills/security/`. Resolution comment names files, close, Decisions-so-far pointer.

## Resolution

**Built.** 6 skills in `skills/security/<name>/SKILL.md` (~73–92 lines): `threat-model` (STRIDE/PASTA trust-boundary modelling; cross-zone SCC/BCR as trust boundary; UAE Pass/EFR/UAEKYC modelled as internal trust boundaries; PDPL residency HIGH-confidence, DESC/NESA MEDIUM-verify), `owasp-review` (API Top 10 + LLM Top 10 for AI-native banking; BOPLA/IDOR consequence-weighted; prompt-injection + excessive-agency for bank AI; observability-path PII leakage; FAPI2 + sender-constraining for open-banking), `zero-trust` (NIST SP 800-207 framed; identity-anchored, micro-perimeter segmented, policy-as-code; UAE Pass as identity assertion not trust transfer; cross-zone as separate trust domain; SPIFFE/mTLS for workload identity), `iam-review` (cloud IAM + app RBAC/ABAC + federation + service accounts; UAE Pass assertion validation per-use; EFR/UAEKYC verdict integrity; cross-zone identity data with transfer-basis logging; break-glass auditing), `compliance` (UAE/CBUAE + international mapping: PDPL Decree-Law 45/2021, CBUAE SVF Art.10 + Retail-Payment Art.18, DIFC DPL 5/2020 + 2023 AI DPR, ADGM DPR 2021; cross-zone transfer-basis register as living artifact; MEDIUM-verify items explicitly flagged), `security-architecture-review` (capstone gate synthesizing all other security skills; gate verdict pass/conditional-pass/fail; residual-risk register; AI tier as first-class security surface). **⚠️ DESC / NESA→Cybersecurity Council / standalone CBUAE cyber-resilience specifics carried as MEDIUM-verify throughout (research 02 caveat); PDPL/CBUAE-sectoral/DIFC/ADGM laws = HIGH-confidence primary-verified.** All cross-linked to each other and to cloud/, governance/, documentation/, architecture/ skills. Verified clean — no garbled glyphs.