# CODING_STANDARDS.md

This file defines **judgement-call** standards enforced during code review.
Mechanical rules (lint, formatting, idempotency header presence) are enforced automatically via `.pre-commit-config.yaml` and CI — do not duplicate them here.

---

## 1. Deep-Module Vocabulary

Enforced mechanically by CI (ruff) — see `.github/workflows/ci.yml`.

**Reviewer judgement call**: Flag PRs where a term is used with the *wrong intent* — e.g., "module" applied to a UI widget rather than a behaviour-bearing unit with an interface. Mechanical lint cannot catch semantic misuse.

Canonical vocabulary → `GLOSSARY.md §Architectural Design Vocabulary`.

---

## 2. Idempotency

Enforced mechanically by CI (`validate_skill_readiness.py`) — see `.github/workflows/ci.yml`.

**Reviewer judgement call**: Check that the documented idempotency contract is *correct*, not just present:
- Status code on duplicate-key collision is `409 Conflict`, not `200` or `422`.
- Key TTL (expiry window) is stated explicitly in the `## Idempotency` section.
- Retry-safe behaviour is described (what the caller does on `5xx` vs `409`).

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

Enforced mechanically by CI (`validate_skill_readiness.py`) — see `.github/workflows/ci.yml`.

**Reviewer judgement call**: Check that tests verify **behaviour through the public interface**, not implementation internals. A test that mocks private methods or asserts internal state passes the mechanical check but fails this standard.

---

## 6. ADR Lifecycle

ADRs in `*/docs/adr/` are immutable once merged. To change an architectural decision:
1. Create a new ADR superseding the old one.
2. Add `superseded-by: NNNN-<title>.md` to the superseded ADR's frontmatter.

**Reviewer rule**: Flag any PR that edits an existing ADR body rather than superseding it.
