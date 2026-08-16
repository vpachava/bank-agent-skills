import uuid
import logging

# Simple in-memory store for demonstration purposes
deduplication_store = {}

def perform_transaction(payload):
    # Simulated transaction logic
    logging.info(f"Processing transaction: {payload}")
    return {"status": "success", "transaction_id": str(uuid.uuid4())}

def process_idempotent_request(idempotency_key, payload):
    logging.info(f"Received request with key: {idempotency_key}")

    # 1. Deduplication check
    if idempotency_key in deduplication_store:
        logging.info(f"Returning cached response for key: {idempotency_key}")
        return deduplication_store[idempotency_key]

    # 2. Process and store
    try:
        logging.info("Executing new transaction")
        result = perform_transaction(payload)

        # Store result
        deduplication_store[idempotency_key] = result
        return result
    except Exception as e:
        # 3. Rollback: remove key on failure to allow retry
        logging.error(f"Transaction failed: {e}")
        if idempotency_key in deduplication_store:
            del deduplication_store[idempotency_key]
        raise

# Example Usage:
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    key = str(uuid.uuid4())
    payload = {"account_id": "123", "amount": 100}

    # First request
    print(process_idempotent_request(key, payload))

    # Second request (retry)
    print(process_idempotent_request(key, payload))
