---
id: "02"
slug: uae-compliance-posture
title: "UAE/CBUAE regulatory, compliance & data-residency posture for a retail bank"
map: solution-arch-orchestrator/map.md
label: wayfinder:research
type: research
status: closed
assignee: research-agent
blocked_by: []
blocks: ["12","13","16"]
---

## Question

Gather the external facts that the **security**, **cloud**, and **governance** skills must embed — UAE-specific, not derivable from generic knowledge. Investigate (verify via web; mark confidence; cite authoritative sources — CBUAE, DIFC, ADGM, TDRA, UAE Data Protection Law; do not invent specifics):

1. **CBUAE regulatory perimeter** for retail banking — what CBUAE governs (licensing, consumer protection, AML/CFT, open banking/finance), and the compliance touchpoints an architect must design around.
2. **UAE data-residency & data-sovereignty obligations** — onshore vs. free-zone (DIFC/ADGM) data rules, cross-border data movement constraints, and their architectural implications for cloud landing zones and core-banking data.
3. **Free-zone financial-center regimes (DIFC, ADGM)** — where their rules diverge from onshore CBUAE and what that changes for cloud/security/IAM design.
4. **Key compliance frameworks/standards** architects cite in a UAE bank — UAE NESA / Dubai Electronic Security, CBUAE cyber-security & resilience standards, and how they map to NIST CSF / ISO 27001 / OWASP for skill grounding.
5. **Identity & KYC ecosystem context** (already integrated at most large UAE banks — Emirates Face Recognition, UAE KYC/eKYC, UAE Pass) — just enough so security/IAM skills reference the real identity fabric, not to re-research integration.

Capture findings to `solution-arch-orchestrator/research/uae-compliance-posture.md`. These facts feed the `compliance`, `security-architecture-review`, `zero-trust`, `iam-review`, `landing-zone-review`, and `production-readiness` / `operational-readiness` skills.

## Resolution

**Resolved 2026-08-08. Findings at `solution-arch-orchestrator/research/uae-compliance-posture.md` (284 lines).** HIGH-confidence primary-verified (WebFetch on DLA Piper federal/DIFC/ADGM, u.ae, Wikipedia for CBUAE/TDRA charters):
- **Federal PDPL** = Federal Decree-Law No. 45 of 2021 (cross-border restricted, adequacy TBD), backstopped by **Cybercrime Law 34/2021 Art. 13**.
- **CBUAE sectoral data-residency** — SVF Regulation (30 Sep 2020) Art. 10 + Retail-Payment-Services/Card-Schemes Regulation (6 Jun 2021) Art. 18: **in-country residency, 72-hour breach reporting, ~5-yr retention**; Consumer Protection Notices 444/1158 of 2021.
- **DIFC DPL** Law No. 5 of 2020 (2023 AI DPR update; Art. 27(4) hybrid-transfer flexibility; "as soon as practicable" breach clock; USD 10K–100K fines).
- **ADGM DPR** 2021 (72-hour breach; EU-2021-SCC-based SCCs; ROPA + fee).
- **UAE Pass** = TDRA-backed national digital identity / SSO layer for the bank identity fabric (context only; already integrated).
- **🔥 MOST ARCHITECTURALLY CONSEQUENTIAL FACT:** **both free zones treat onshore UAE as a Third Country** for transfers → intra-group **onshore ↔ DIFC ↔ ADGM** data flows require **SCCs/BCRs**. This changes landing-zone topology, cross-border data design, and the zero-trust posture. Dedicated section + `landing-zone-review` grounding block in the file.

**⚠️ CAVEAT for builders of tickets 12 (security), 13 (cloud), 16 (governance):** `WebSearch` did not run; agency sites failed (`www.desc.gov.ae` 403; `www.nesa.gov.ae` DNS NXDOMAIN — superseded; `centralbank.ae` 403; PIA/FSA rulebooks 403/404). So **DESC, the NESA→Cybersecurity Council transition, and any standalone CBUAE cyber-resilience/open-banking rule text are MEDIUM-synthesized — verify against a current primary publication before any checklist ships.** No law/notice numbers or dates were invented; a 7-item open-verifications list is in the file. The HIGH-confidence PDPL/DIFC/ADGM/CBUAE-sectoral facts above are embeddable now.

**Unblocks** build tickets **12 (security)**, **13 (cloud)**, and **16 (governance)** — but for UAE-cyber-rule specifics (DESC/CBUAE-standalone), those builds should cite this research as "MEDIUM-verify" or re-pin to a current CBUAE publication during build.
