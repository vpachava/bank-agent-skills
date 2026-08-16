---
name: idempotent-api
description: Use when designing API endpoints requiring idempotency to prevent duplicated transactions.
---

# /idempotent-api

## Overview
Ensures API operations are idempotent, preventing side effects from duplicate requests (e.g., retries due to network issues).

## When to Use
- Financial transactions (money transfers, limit increases).
- Critical state-changing operations where retries are possible.

## Core Pattern
1. **Deduplication Store:** Check for `idempotency-key` existence before processing.
2. **Conditional Processing:**
   - Key exists: Return cached/stored original response.
   - Key not exists: Process request, store result, and return.
3. **Transaction Rollback:** If processing fails, remove `idempotency-key` to allow subsequent retries.

## Implementation Example (Python concept)
```python
def process_request(idempotency_key, payload):
    # 1. Deduplication check
    cache = deduplication_store.get(idempotency_key)
    if cache:
        return cache

    # 2. Process and store
    try:
        result = perform_transaction(payload)
        deduplication_store.set(idempotency_key, result)
        return result
    except Exception:
        # 3. Rollback: remove key on failure to allow retry
        deduplication_store.delete(idempotency_key)
        raise
```
