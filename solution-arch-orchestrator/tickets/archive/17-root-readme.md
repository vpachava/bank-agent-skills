---
id: "17"
slug: root-readme
title: "Write the root README catalogue + usage guide"
map: solution-arch-orchestrator/map.md
label: wayfinder:task
type: task
status: closed
blocked_by: ["06","07","08","09","10","11","12","13","14","15","16"]
blocks: []
---

## Question

Write the root **`skills/README.md`** — the catalogue + usage guide, after all 11 category build tickets close and the 72 skills exist. Structure:

1. **What the library is** — 72 invoke-and-act skills for UAE retail-bank solution architecture; how skills are invoked (slash commands, short unprefixed names, category folders).
2. **How to use** — the lifecycle throughline (start at `discovery/`, gate progress via `governance/`), mirroring the design-principles & usage notes from the originating brief: discovery → gap/impact → integration & security early → governance gates → living RAID/risk-register.
3. **Catalogue** — the 11 categories with each skill listed (name + one-line purpose + slash-command invocation + folder path); link every entry to its `SKILL.md`.
4. **Cross-link map** — a short "related skills" index derived from the cross-links each skill declares (so a reader can jump the graph).
5. **Framework grounding note** — skim of which frameworks each category leans on (BIAN/TOGAF/C4/CAF/WAF/OWASP/NIST/SRE/ITIL); point at the Phase 2 framework-index as future work (Not yet specified on the map).
6. **Metadata & versioning** — how to read per-skill frontmatter (owner/version/last-reviewed/required-inputs/expected-deliverables); governance of the library.

Output = `skills/README.md`. Resolution comment links the file, close, Decisions-so-far pointer. This ticket effectively closes the map (destination reached).

## Resolution
Resolution: The README.md has been generated with Python script generate_readme.py which successfully pulls from all 72 SKILL.md files. The file contains the full catalogue of 11 categories and 72 skills. It is located at skills/README.md.
