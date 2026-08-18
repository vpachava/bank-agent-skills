---
id: "07"
slug: architecture-skills
title: "Build the architecture/ skills (8)"
map: solution-arch-orchestrator/map.md
label: wayfinder:task
type: task
status: closed
assignee: architect
blocked_by: ["01","03"]
blocks: []
---

## Question

Build the `architecture/` category — **8 invoke-and-act skills**, each `architecture/<name>/SKILL.md` on the locked archetype (ticket 01):

1. **hld-generator** — produce a High-Level Design doc (context, containers, key flows, NFRs at headline level) for a banking initiative.
2. **lld-generator** — produce a Low-Level Design (component APIs, data, sequences, deployment detail) from an HLD.
3. **c4-model** — generate C4-context/container/component/code diagrams (diagrams-as-text, Mermaid-ready) for a banking solution; structured by C4 levels.
4. **sequence-diagrams** — produce sequence diagrams for key flows; banking scenarios (core-banking calls, IDV, payments) where relevant.
5. **deployment-diagrams** — produce deployment diagrams (topology, regions, HA, DR pairing) for a bank's multi-cloud/private estate.
6. **architecture-review** — run a review against BIAN/TOGAF lenses + the bank's architecture standards; produce a review report with findings/severity.
7. **architecture-decision-records** — author an ADR (context, options, decision, consequences); produce a versioned ADR file.
8. **nfr-checklist** — drive NFR elicitation & a checklist (perf, scale, availability, security, compliance); produce an NFR baseline.

Each skill: frontmatter + per-skill metadata; Purpose & when-to-apply; Inputs/process as embedded banking checklists (legacy core + modern, multi-cloud); Banking pitfalls; Outputs (named deliverable); Related skills cross-linked folder-relative, and to `../greenfield/reference-architecture`, `../governance/architecture-review` (note potential overlap with ticket 06's architecture-review). Depth flex to fit — cloud-adjacent skills here can run heavier; diagram skills keep examples concise. Ground BIAN (research 03) where it earns it.

Output = 8 skill files in `skills/architecture/`. Resolution comment names files, links archetype, close, Decisions-so-far pointer.

## Resolution

**Resolved 2026-08-08. 8 skills built in `skills/architecture/<name>/SKILL.md` (~68–106 lines each; ADR-records longer for its embedded skeleton template):**
- `hld-generator` — context/containers/key-flows/headline-NFRs/reuse-vs-replace; open-questions handed to LLD.
- `lld-generator` — components + API contracts (idempotency named), data + residency, sequences to exception depth, resolved-or-escalated open questions, deployment view.
- `c4-model` — C4 levels on audience demand; **delegates rendering to `/archify`**; banking annotations (legacy-core band, residency perimeter, regulated gates, trust boundaries); selective-depth honesty.
- `sequence-diagrams` — actors-by-zone; happy path + separate exception fragments (retake/escalate/timeout/resume); regulated-gate + provenance + idempotency markers; **rendered by `/archify`**.
- `deployment-diagrams` — topology/regions/HA-DR pairing; **residency perimeter (onshore/DIFC/ADGM) + cross-zone SCC/BCR implication**是他的核心 lens; multi-cloud seams; renders via `/archify`.
- `architecture-review` — lens stack (BIAN-capability-fit, TOGAF-method-coherence, **NFR commitment, residency, integration, security, resilience, reuse-vs-replace**); severity discipline (no inflation); findings-with-paths.
- `architecture-decision-records` — standard template; **"do nothing" + rejected-with-appeal, not just winner**; honest consequences (gains + penalties + accepted-regulatory-exposure + reversibility cost); versioned supersede/amend (never silent edits); **embedded ADR skeleton in the skill**.
- `nfr-checklist` — measurable targets (no "high"/"robust"); **residency & compliance NFRs as first-class rows**; NFR-to-design trace map; tensions escalated to ADRs.

**On the archetype:** all 8 follow the locked template — structured-list frontmatter, trigger-first body (## When to apply → ## Inputs → ## Process [checklists-as-steps; inline `>` framework grounding] → ## Banking pitfalls → ## Outputs → ## Related skills [folder-relative]). `description` strings use the "Use when… — produces…" house style. The 3 diagram skills explicitly delegate rendering to **`/archify`** per the archetype's A8.

**Depth note:** ~68–106 lines — these land at the *light* end of the ~200–400 band. Justified: architecture skills are *process* skills with dense, tight steps (7–8 process steps + 6–7 banking pitfalls + named outputs + 5–6 cross-links each), not reference catalogues. The "flex to fit" rule allows lighter where the content earns it; the Phase-2 enrichment (worked examples, Mermaid/draw.io templates, maturity ratings) will bulk these out and is parked in *Not yet specified*.

**Grounding used:** BIAN research (03) — selective decomposition (don't manufacture gaps), "TOGAF for method, BIAN for content" in `architecture-review`; BIAN v14.0 in `c4-model`. UAE-compliance research (02) — the **free-zone cross-zone SCC/BCR obligation** is a named pitfall + a core lens in `deployment-diagrams`, `hld-generator`, `architecture-review`, `nfr-checklist` (residency as first-class NFR). Integration research (05) — idempotency-key (UETR-style), reconciliation, strangler-fig cited in `lld-generator`/`architecture-review`.

**Cloud-depth caveat:** cloud-adjacent skills (`hld-generator` deployment view, `deployment-diagrams` landing-zone detail) are at altitude here — research 04 (cloud WAF, still running at build time) was not folded in. If 04 lands material landing-zone/WAF detail, a follow-up enrichment to those two skills' `references/` may be warranted (Phase-2-style); the skills themselves are MVP-complete and invoke-and-act.
