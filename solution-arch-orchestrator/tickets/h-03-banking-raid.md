---
id: h-03-banking-raid
title: "Automate Banking RAID Registry"
label: wayfinder:task
status: closed
blocks: []
blocked_by: ["h-01-idempotent-protocol"]
---

## Question
Establish a central `/governance/raid-log.json` and force all skills to contribute identified risks into this global store.

## Resolution
Defined schema at `/governance/raid-log-schema.json`. Risk appending logic follows standard JSON structure updating ensuring idempotent storage keys.
