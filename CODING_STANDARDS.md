# CODING_STANDARDS.md

This file defines **judgement-call** standards enforced during code review.
Mechanical rules (lint, formatting, idempotency header presence) are enforced automatically via `.pre-commit-config.yaml` and CI — do not duplicate them here.

---

## 1. Deep-Module Vocabulary

Use these terms exactly across all specifications, skills, diagrams, and documentation.
Never substitute "component", "service", "API", or "boundary" — use the precise term from the list below.

| Correct Term | Prohibited Synonyms | Meaning |
|---|---|---|
| **module** | component, service, unit | Anything with an interface and an implementation |
| **interface** | API, signature | Everything a caller must know: types, invariants, ordering, errors |
| **seam** | boundary, layer boundary | The location at which a module's interface lives |
| **adapter** | plugin, connector, bridge | A concrete thing that satisfies an interface at a seam |
| **depth** | richness, complexity | Amount of behaviour per unit of interface |
| **leverage** | reuse, DRY | What callers gain from depth |
| **locality** | single-source-of-truth, cohesion | What maintainers gain from depth |

**Reviewer rule**: Flag any PR that uses "component", "service", "boundary", or "API" where one of the above terms applies.

---

## 2. Idempotency

Every HTTP handler in a transactional workflow MUST:
- Accept an `Idempotency-Key` request header.
- Return a `409 Conflict` (not `200`) if a duplicate key is detected with a different payload.
- Document the idempotency contract in the skill's `SKILL.md` under an `## Idempotency` section.

**This is also mechanically enforced** by the CI job `validate_skill_readiness.py`. The reviewer's role is to check that the *contract is documented correctly* (e.g., correct status codes, key TTL mentioned).

---

## 3. Cost Estimation Metadata

Every skill that touches cloud infrastructure MUST include a `## Cost Estimation` section in its `SKILL.md` with at minimum:

```markdown
## Cost Estimation
- **Cloud Run**: ~$X / month at Y RPS
- **Storage**: ~$X / GB / month
- **ML Inference** (if applicable): ~$X / 1M tokens
```

**Reviewer rule**: Flag any infrastructure-touching skill PR that omits this section.

---

## 4. Regulatory Overlay Citation

Any skill touching payments, identity, or data residency MUST cite the applicable regulatory overlays from `governance/policy/regional/` in its `SKILL.md` under a `## Compliance` section.

**Reviewer rule**: Flag missing `## Compliance` sections in payment, identity, and data-residency skills.

---

## 5. Skill File Structure

Every skill directory MUST contain:
- `SKILL.md` — with valid YAML frontmatter (`name`, `description`)
- `tests/` — at least one test stub

The CI job `validate_skill_readiness.py` enforces this mechanically.
The reviewer's role is to check that tests verify **behaviour**, not implementation internals.

---

## 6. ADR Lifecycle

ADRs in `*/docs/adr/` are immutable once merged. To change an architectural decision:
1. Create a new ADR superseding the old one.
2. Add `superseded-by: NNNN-<title>.md` to the superseded ADR's frontmatter.

**Reviewer rule**: Flag any PR that edits an existing ADR body rather than superseding it.
