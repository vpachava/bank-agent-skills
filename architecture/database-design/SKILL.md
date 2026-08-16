---
name: database-design
description: Use when designing database schemas and infrastructure, including vector database integration for AI-native workloads.
---

# /database-design

## Overview
Standards for relational and non-relational database design, with specific focus on high-performance, resilient, and AI-native vector requirements.

## When to Use
- Designing schemas for core banking domains.
- Integrating vector databases for AI-native workloads.
- Infrastructure choices (RDBMS vs NoSQL vs Vector).

## Core Principles
1. **Schema Integrity:** Normalization vs De-normalization balance based on read/write patterns.
2. **Resilience & Availability:** Replication, sharding, and backup/recovery strategies.
3. **AI-Native Integration (Vector):** Design patterns for vector embedding persistence and retrieval.
4. **Data Sovereignty:** Alignment with regional data residency requirements.

## Vector Database Integration Patterns
1. **Embedding Storage:** Structured storage for high-dimensional vector embeddings with associated metadata.
2. **Retrieval Strategy:** Hybrid search enablement (vector similarity + metadata filtering).
3. **Synchronization:** Ensuring embedding updates maintain consistency with source transaction data.

## Mandatory Compliance Block
Any ADR referencing a database design MUST include: 
- **Data Classification:** [Public/Internal/Restricted/Confidential]
- **Residency Requirement:** [Onshore/Cloud-Regional/None]
- **Performance Expectation:** [IOPS/Latency/Throughput]

## Related Skills
- [data-governance](../../governance/data-governance/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
