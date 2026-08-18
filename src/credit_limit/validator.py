def validate_limit_increase(card_id: str, requested_limit: float) -> (bool, str):
    """
    Validates credit limit increase request.
    Compliance: CBUAE-aligned rule (limit cap of 50,000 AED for pilot).
    """
    if requested_limit <= 0:
        return False, "Requested limit must be positive."

    # Simple CBUAE rule simulation
    if requested_limit > 50000:
        return False, "Limit exceeds compliant cap for this pilot."

    return True, "Request valid."
