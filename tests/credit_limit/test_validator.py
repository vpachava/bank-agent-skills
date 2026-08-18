import pytest
from src.credit_limit.validator import validate_limit_increase

def test_valid_increase():
    assert validate_limit_increase("card123", 40000) == (True, "Request valid.")

def test_too_high_limit():
    assert validate_limit_increase("card123", 60000) == (False, "Limit exceeds compliant cap for this pilot.")

def test_negative_limit():
    assert validate_limit_increase("card123", -100) == (False, "Requested limit must be positive.")
