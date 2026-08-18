# Diagram Templates Repository

This directory contains standardized diagram-as-code templates for generating the visual layer of UAE Retail-Bank Architecture Skills outputs.

## Governance Rule: Orphan Diagram Prevention
All generated diagrams **MUST** include metadata linking them to the process execution that created them. This is primarily done using JSON Frontmatter or YAML configuration blocks natively inside the diagram file to provide evidence tracing.

Any Mermaid payload must start with the following frontmatter metadata block:

```mermaid
---
title: "[Diagram Name]"
config:
  metadata:
    artifact_id: "[UNIQUE_SKILL_EXECUTION_ID]"
    generated_by: "[SKILL_NAME]"
    timestamp: "[ISO_8601]"
---
```

## Available Component Classes

Define banking platform nodes with standard classifications for consistent styling.

```mermaid
%% Class Definition Injectable Header
classDef coreBank fill:#f4f4f4,stroke:#333,stroke-width:2px;
classDef paymentHub fill:#d1e7dd,stroke:#0f5132,stroke-width:2px;
classDef iam fill:#cff4fc,stroke:#055160,stroke-width:2px;
classDef apiGateway fill:#fff3cd,stroke:#664d03,stroke-width:2px;
classDef cbuaeZone fill:#f8d7da,stroke:#842029,stroke-width:3px,stroke-dasharray: 5 5;
```
