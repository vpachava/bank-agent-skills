---
name: idempotent-api
description: Use when designing API endpoints requiring idempotency to prevent duplicated transactions.
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
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

### Banking Context & Examples

#### (1) Fund Transfer Idempotency Example
**Scenario:** A customer initiates a transfer via the `Mobile-Banking-App`.
- **Architecture Lens Check:** The `idempotency-key` (UETR-compliant) is passed from the mobile client all the way to the core ledger. 
- **Sample Outcome:** "If a network timeout occurs and the mobile app retries the same UETR, the API immediately returns the cached success response of the originally initiated transfer."
- **Common Pitfall:** Ignoring the `idempotency-key` in backend services, causing a retry to initiate a second deduction of funds from the customer account, leading to reconciliation errors (and customer dissatisfaction).

#### (2) Sharia-Loan Disbursement Example
**Scenario:** Disbursing funds to a loan account.
- **Architecture Lens Check:** Verification that the `idempotency-key` is used to prevent double-disbursement of loan capital, which would violate Sharia-contract principles regarding specific, certified loan amounts.
- **Common Pitfall:** Failing to handle the retry scenario for disbursement; the system issues the loan funds twice to the same account due to network retry, violating Sharia Board product definitions.

#### (3) AECB Data Fetching Example
**Scenario:** Fetching an AECB credit report via API.
- **Architecture Lens Check:** Using an `idempotency-key` to avoid double-charging the bank's account for repeated AECB credit report fetches when a network error occurs.
- **Common Pitfall:** Treating the read-operation as non-idempotent; retrying the fetch incurs redundant costs for the bank and risks triggering AECB-side throttling due to excessive request rates on the same customer.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management


