---
id: "01"
slug: skill-archetype
title: "Pin the SKILL.md section template & metadata frontmatter (the archetype)"
map: wayfinder/map.md
label: wayfinder:grilling
type: grilling
status: closed
assignee: architect
blocked_by: []
blocks: ["06","07","08","09","10","11","12","13","14","15","16","17"]
---

## Question

The single decision that every build ticket inherits: the **canonical SKILL.md shape**. Run a `/grilling` + `/domain-modeling` session to pin exactly:

1. **Frontmatter schema** — `name`, `description` (with trigger phrasing), plus metadata: `owner`, `version`, `last-reviewed`, `required-inputs`, `expected-deliverables`. Set the exact keys, types, and a house style for the `description` (so each skill surfaces well under `/help`).
2. **Section order & intent** — Purpose & when-to-apply · Inputs/process (banking-specific checklists **embedded as the steps**, not appended) · Banking/UAE pitfalls · Outputs (the concrete deliverable, named) · Related skills (folder-relative links). Decide whether a "Framework grounding" sub-block sits inside the process or as its own short section.
3. **Depth policy in practice** — confirm the "flex to fit (~200–400 lines)" rule and when a skill earns a `references/` folder vs. inlining. Produce a one-line rubric builders apply.
4. **Deliverable of this ticket** — a concrete **archetype artifact** at `wayfinder/skill-archetype.md`: (a) a fully filled-in canonical example skill, and (b) an empty section skeleton builders copy. This file is what the build tickets point at; it locks the template.

Ground the archetype in how installed skills here are shaped (e.g. `graphify` SKILL.md — single-file, frontmatter + action sections + optional `references/`) and Claude Code's skill model (trigger description → action), so library skills are real, invocable skills — not topic pages.

## Resolution

**Resolved 2026-08-07. The archetype is pinned at `wayfinder/skill-archetype.md`** (the artifact all build tickets 06–16 point at). Three locked decisions + their fill:

1. **Frontmatter — structured-list metadata.** Every skill carries `name`, `owner`, `version`, `last-reviewed`, `description`, `required-inputs` (YAML list), `expected-deliverables` (YAML list). `required-inputs`/`expected-deliverables` are YAML lists (machine-readable for a future Phase-2 framework index). `owner`/`version`/`last-reviewed` are governance metadata, inert to the harness. *(Chose structured-list over free-form metadata and over minimal-frontmatter-with-body-sections — list form is tool-parsable for the catalogue generator and stays compact.)*

2. **Body template — trigger-first, grounding inline.** Fixed order: `## When to apply` → `## Inputs` → `## Process` (checklists *are* the steps; framework grounding woven in as inline `>` boxed notes where it earns it, **never** a separate section) → `## Banking pitfalls` (UAE/retail-bank-specific failure modes, not generic best-practice) → `## Outputs` → `## Related skills` (folder-relative links). Purpose is *not* restated as a section — it already lives in frontmatter `description`. *(Chose trigger-first+inline grounding over a dedicated `## Framework grounding` section and over maximal reference sections — keeps skills action-shaped, consistent with the "practical not catalogue" goal.)*

3. **`description` house style — "Use when" + deliverable.** Pattern: `"Use when <trigger condition> — produces <deliverable> (<method / scope>) with <what it yields>."` Leads with the trigger condition the harness matches for auto-apply, names the concrete deliverable. One sentence, no trailing clause. *(Chose "Use when…"-lead over action-verb-lead and noun-lead descriptions — best match for skill auto-discovery.)*

**Also locked into the archetype (carried from charter, confirmed):**
- *Depth* — flex to fit, ~200–400 lines; structure is consistent, line-count is not. `references/` folder used only where a skill earns it (most stay single-file).
- *Naming* — short unprefixed `name` = slash command; category folder groups.
- *Diagram skills* (`c4-model`, `sequence-diagrams`, `deployment-diagrams`) delegate rendering to the **`/archify`** skill rather than hand-rolling Mermaid.
- *Banking context every skill assumes* — legacy core + modern coexistence; multi-cloud AWS/Azure/Oracle/private; heavy 3rd-party/core integration; AI-native mobile on existing REST APIs; UAE/CBUAE regulatory perimeter.

**Creeked downstream:** tickets 06–16 (the 11 category builds) are now unblocked on this decision and inherit `skill-archetype.md` verbatim. Ticket 17 (README) is unblocked once all builds close. The "maturity rating" enhancement stays parked (Not yet specified / Phase 2) — confirmed out of the archetype.
