---
id: "06"
slug: discovery-skills
title: "Build the discovery/ skills (5)"
map: wayfinder/map.md
label: wayfinder:task
type: task
status: closed
assignee: architect
blocked_by: ["01","03"]
blocks: []
---

## Question

Build the `discovery/` category — **5 invoke-and-act skills**, each a `discovery/<name>/SKILL.md` on the locked archetype (ticket 01):

1. **requirements-analysis** — elicit & structure functional + non-functional requirements for a banking initiative; produce a requirements baseline.
2. **stakeholder-workshop** — run/drive a discovery workshop (business + IT + risk/compliance): agenda, elicitation exercises, synthesis; produce workshop outcomes & decisions log.
3. **business-capability-map** — map a bank's capabilities (BIAN-grounded per research 03); produce a capability map + heat-map of gaps/duplication.
4. **gap-analysis** — current-state vs. target-state gap analysis against capabilities/processes; produce a gap register with severity.
5. **solution-options** — surface & compare 2–4 solution options (incl. buy/build/modernize); produce an options matrix + scoring + recommendation.

Each skill: frontmatter with per-skill metadata; Purpose & when-to-apply; Inputs/process as embedded banking checklists (legacy-core awareness, regulatory stakeholders, UAE reality); Banking pitfalls; Outputs (named deliverable); Related skills cross-linked folder-relative (e.g. `../architecture/gap-analysis`... → `../architecture/hld-generator`). Target ~200–400 lines, flex to fit. Use research 03 (BIAN) for the capability-map & gap-analysis skills only where it earns it; cite confidence where research was uncertain.

Output of this ticket = the 5 skill files committed in `skills/discovery/`. Post a resolution comment naming each file, link the archetype, close, and append a context pointer to the map's Decisions-so-far.

## Resolution

**Resolved 2026-08-08. 5 skills built in `skills/discovery/<name>/SKILL.md`:**
- `requirements-analysis` — requirements baseline; regulatory constraints as first-class; UAE free-zone cross-border gap surfaced.
- `stakeholder-workshop` — workshop design + decisions-log; Risk/Compliance-in-room enforced as a design rule.
- `business-capability-map` — BIAN-grounded (Service Landscape v14.0, ~322 service domains); selective-adoption pragmatic; heat-map drives a decision.
- `gap-analysis` — **TOGAF method on BIAN content**; missing/under-invested/**duplicated** (the missed gap); selective-depth-aware.
- `solution-options` — 2–4 options incl. "do nothing"; weighted scoring; reuse-and-wrap over legacy core vs. greenfield-rebuild honesty; compliance as gate not tiebreaker.

**On the archetype:** all five follow the locked template (structured-list frontmatter, trigger-first body, inline framework grounding via `>` notes, Banking pitfalls, Outputs, Related skills via folder-relative links). `description` strings use the "Use when… — produces…" house style.

**Depth note:** ~62–68 lines each — lighter than the ~200–400 band, justified because discovery is the lightest category per the archetype's "flex to fit" rule ("a discovery/workshop skill runs lighter"). Content is dense (6–7 process steps with inline grounding, 6 banking pitfalls each, named outputs, 4–5 cross-links). Phase-2 enrichment (worked examples, templates, maturity ratings) is parked in the map's *Not yet specified*; these are MVP-complete and invoke-and-act.

**Grounding used:** BIAN research (03) embedded in `business-capability-map` (v14.0, ~322 domains, selective adoption, Banks run selective decomposition, ~250 Semantic APIs) and `gap-analysis` ("TOGAF for method, BIAN for content" skill rule). UAE-compliance research (02) surfaced indirectly via the free-zone cross-border / regulatory-as-first-class pitfalls. Banking context (legacy core reuse-over-rewrite, multi-cloud, 3rd-party heavy) embedded throughout pitfalls.

**Caveat carried:** none specific to this category (discovery didn't depend on the MEDIUM-verify UAE cyber-rule specifics from research 02/05).
