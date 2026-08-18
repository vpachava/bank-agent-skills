---
id: h-02-evidence-gate
title: "Formalize Evidence-Gate Verification"
label: wayfinder:task
status: closed
blocks: ["h-04-adversarial-compliance", "h-05-packaging"]
blocked_by: ["h-01-idempotent-protocol"]
---

## Question
Create a new skill `/governance/evidence-gate` that tests architectural claims against real project repository state.

## Resolution
Created `/governance/evidence-gate/SKILL.md` forcing concrete validation on architectural prose using verification paths. Handled error states appropriately based on architectural handoffs schema.
