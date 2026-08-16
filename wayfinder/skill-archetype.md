# Skill Archetype — UAE Retail-Bank Solution-Architect Skills Library

The canonical shape every skill in this library follows. **Build tickets (06–16) point here.** Two parts: (A) the locked conventions, (B) a filled canonical example + empty skeleton to copy.

Locked in ticket 01's grilling (2026-08-06 → 07). Do not re-litigate; raise a new ticket to amend.

---

## A. Locked conventions

### A1. What a skill IS here
Each skill is an **invoke-and-act** Claude Code skill — triggered as its own slash command (e.g. `/threat-model`) and running a *process* that produces a concrete *deliverable*. Banking/UAE checklists & pitfalls are **the steps**, not a reference appendix. Industry-framework grounding (BIAN, TOGAF, C4, AWS/Azure Well-Architected, OWASP, NIST, SRE, ITIL 4) is **inline and actionable**, woven into the process where it earns it — never a separate reference section that bloats the skill.

### A2. Naming & location
- Each `name` is **short & unprefixed** → its own slash command. The **category folder** groups the catalogue, not the name.
- Path: `skills/<category>/<name>/SKILL.md` (one folder per skill, room for `references/`).
- 11 categories: `discovery/`, `architecture/`, `greenfield/`, `modernization/`, `migration/`, `integration/`, `security/`, `cloud/`, `devops/`, `documentation/`, `governance/`.

### A3. Frontmatter schema (structured-list metadata)
Every skill carries this frontmatter. `required-inputs` and `expected-deliverables` are **YAML lists** (machine-readable for a future Phase-2 framework index / catalogue generator). `owner`/`version`/`last-reviewed` are governance metadata for the library, inert to the harness.

```yaml
---
name: <short-kebab-name>          # the slash command, unprefixed
owner: <team / capability area>  # e.g. "Security Architecture"
version: <semver>                # start 0.1.0; bump on content change
last-reviewed: <ISO date>        # YYYY-MM-DD
description: "<see A4>"
required-inputs:
  - <thing you need before starting>
expected-deliverables:
  - <named artifact the skill produces>
---
```

### A4. `description` house style (the auto-discovery trigger)
The harness reads `description` to decide auto-apply, so it leads with the **trigger condition**, not a definition. House pattern, in one sentence:

> **"Use when <trigger condition> — produces <deliverable> (method / scope) with <what it yields>."**

- Start with **"Use when…"** + the situation that triggers it.
- Name the **deliverable** concretely (the threat model, the ADR, the risk register).
- Parenthesize the **method/scope** so a reader scanning `/help` groks it fast.
- One sentence; no trailing "Use during…" tacked on.

### A5. Body section order (trigger-first, grounding inline)
Fixed order. Framework grounding lives **inline as a boxed note (`> …`) inside the process** where it earns it — never its own section.

```
# /<name>
## When to apply      ← the trigger (purpose is already in frontmatter; don't restate it as a section)
## Inputs             ← list; what you need before starting (mirrors required-inputs, can expand)
## Process            ← numbered; the checklists ARE the steps; inline > boxed framework notes
## Banking pitfalls   ← the UAE/retail-bank-specific failure modes (NOT generic best-practice)
## Outputs            ← named deliverables (mirrors expected-deliverables)
## Related skills     ← folder-relative links to cross-linked skills
```

### A6. Depth policy — flex to fit
Target **~200–400 lines** per `SKILL.md`. A thick cloud/security/checklist skill can run heavier; a discovery/workshop skill runs lighter. **Consistency is in the structure (A5), not the line count.** If a skill's reference material would blow past the band, factor it into a per-skill `references/` folder the main `SKILL.md` points at ("see `references/<topic>.md`"), and keep the main file action-shaped. Use `references/` only where a skill *earns* it (not reflexively) — most skills stay single-file.

### A7. Cross-link format
Folder-relative paths, so links survive moving the library:
- Same category: `[other-skill](./other-skill/SKILL.md)` or just `[/other-skill](./other-skill/SKILL.md)`.
- Other category: `[gap-analysis](../discovery/gap-analysis/SKILL.md)`.

### A8. Diagram skills
The `c4-model`, `sequence-diagrams`, and `deployment-diagrams` skills delegate rendering to the **`/archify`** skill (polished explorable HTML/SVG architecture & sequence diagrams) rather than hand-rolling Mermaid. Their `## Process` invokes `/archify` with the right input type; the skill itself owns *what* to draw and the banking conventions for each view.

### A9. Banking context every skill assumes
Legacy core + modern platforms coexisting; multi-cloud (AWS + Azure + Oracle/private); heavy 3rd-party & core-banking integration; AI-native mobile on existing REST APIs; UAE/CBUAE regulatory perimeter (data-residency, free-zone divergence, cyber-resilience). Skills embed this as pitfalls/grounding, not re-explain it each time.

---

## B. Canonical example + skeleton

### B1. Filled example — `/threat-model` (the canonical reference shape every skill copies)

```markdown
---
name: threat-model
owner: Security Architecture
version: 0.1.0
last-reviewed: 2026-08-07
description: "Use when designing or reviewing a banking component's security posture — produces a threat model (STRIDE/PASTA, trust boundaries, data-flow) with findings, severities, and mitigation owners."
required-inputs:
  - Component scope & data-flow sketch
  - Trust boundaries (internal / partner / public)
  - NFRs relevant to security (availability, integrity, PII)
expected-deliverables:
  - Threat model document (per in-scope component)
  - Findings register with STRIDE category & severity
  - Mitigation owners & residual-risk notes
---

# /threat-model

## When to apply
Use whenever a banking component is being designed or materially changed, or when an existing component enters a security review. Especially load-bearing for anything crossing a trust boundary (customer-facing, partner/fintech, core-banking) or handling PII/biometrics/payment data. Closes a gap the lighter `/owasp-review` doesn't — this is the *structural* threat surface, not the vuln checklist.

## Inputs
- **Component scope** — the in-scope system boundary and what's explicitly out of scope.
- **Data-flow sketch** — where data enters, moves, and persists;标注 PII / payment / biometric flows.
- **Trust boundaries** — internal / partner-fintech / public / CBUAE-regulated zone.
- **Security-relevant NFRs** — availability (RTO/RPO targets), integrity (audit/provenance), confidentiality (PII, residency).
- **Existing controls inventory** — what's already in place so you don't re-mitigate.

## Process
1. **Scope & draw the data-flow.** Bound the component; mark data stores, flows, and external actors. Call out PII/payment/biometric flows explicitly.
   > Per OWASP, the attacker's first lever is the boundary data crosses — get the boundaries right before enumerating threats.

2. **Draw trust boundaries.** Internal / partner / public / the CBUAE-regulated data zone. Every boundary crossing is a threat surface.

3. **Enumerate threats — STRIDE across each boundary & flow.**
   - **Spoofing** — who can impersonate an actor on this flow? (esp. fintech/partner identity, UAE Pass assertions)
   - **Tampering** — can data in flight or at rest be modified? (payment amounts, KYC verdicts, provenance ledger)
   - **Repudiation** — can an action be denied? (audit trails, dual-sign-off ceremonies)
   - **Information disclosure** — PII/biometric/payment leakage; cross-border/residency exposure
   - **Denial of service** — availability attack on a regulated path
   - **Elevation of privilege** — can a role step up? (the silent privilege-creep failure mode below)

4. **(Where useful) layer PASTA** for risk-anchored decomposition — but STRIDE is the default; don't inflate.

5. **Severity & owner each finding.** Likelihood × impact against the bank's risk appetite; assign a mitigation owner; note residual risk after controls.

6. **Capture mitigations & residual risk.** Map each finding to a control (existing or new), owner, and a residual-risk statement for the risk register.
   > NIST CSF lens: each finding lands in Identify / Protect / Detect / Respond / Recover — useful for the compliance mapping, but STRIDE drives the enumeration.

## Banking pitfalls
- **Silent privilege creep across clouds** — IAM drifts as AWS/Azure accounts proliferate; least-privilege rots fast. Review IAM at every threat-model refresh, not just at design.
- **Key custody split across providers** — secrets divided across clouds become unauditable; prefer a single custody plane + per-cloud delegation.
- **Provider-plugin trust** — third-party IDV/KYC SDKs (UAE Pass / EFR / UAEKYC) are trust boundaries *inside* your scope, not external-safe; model the SDK→your-app boundary explicitly.
- **Audit/provenance as an afterthought** — field-level provenance (who/what produced a value) must be a threat you model, not a logging detail.
- **Residency leakage via logs/traces** — observability pipelines can exfiltrate PII across regions faster than the data store; model the telemetry path as a flow.
- **Regenerated, not living** — a threat model written at design and never refreshed is worse than none; tie refresh to the change-advisory path (`/governance`).

## Outputs
- **Threat model document** — per in-scope component: scope, data-flow, trust boundaries, threat-by-threat findings.
- **Findings register** — STRIDE category, severity, owner, mitigation, residual risk (feeds `/risk-register`).
- **Mitigation owners & residual-risk notes** — handoff to the risk/governance track.

## Related skills
- [owasp-review](./owasp-review/SKILL.md) — the vuln-list review that pairs with this structural model.
- [zero-trust](./zero-trust/SKILL.md) — posture design this model informs.
- [iam-review](./iam-review/SKILL.md) — the privilege-creep pitfall, operationalized.
- [security-architecture-review](./security-architecture-review/SKILL.md) — the broader review this feeds.
- [risk-register](../documentation/risk-register/SKILL.md) — where findings & residual risk land.
```

### B2. Empty skeleton to copy

```markdown
---
name: <short-kebab-name>
owner: <team / capability area>
version: 0.1.0
last-reviewed: <YYYY-MM-DD>
description: "Use when <trigger condition> — produces <deliverable> (<method / scope>) with <what it yields>."
required-inputs:
  - <input 1>
  - <input 2>
expected-deliverables:
  - <deliverable 1>
  - <deliverable 2>
---

# /<name>

## When to apply
Use <when the situation triggering this skill arises>. Especially load-bearing for <the banking context where it matters most>. <One line on what it closes / pairs with vs. adjacent skills.>

## Inputs
- **<input>** — <what it is / why needed>
- **<input>** — …

## Process
1. **<step>** — <what to do>.
   > <optional inline framework grounding note — BIAN/TOGAF/OWASP/etc. — only where it earns it>
2. **<step>** — …
   <!-- checklists ARE the steps; framework grounding woven in as boxed notes, not a separate section -->

## Banking pitfalls
- **<pitfall>** — <the UAE/retail-bank-specific failure mode; not generic best-practice>
- **<pitfall>** — …

## Outputs
- **<deliverable>** — <named artifact>
- **<deliverable>** — …

## Related skills
- [related](<folder-relative path>/SKILL.md) — <why>
- [related](../<category>/<name>/SKILL.md) — <why>
```
