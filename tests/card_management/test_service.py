import pytest
from src.card_management.service import CardManagementService

def test_create_card():
    service = CardManagementService()
    assert service.create_card("123", "Alice") is True
    assert service.get_card("123") == {"holder_name": "Alice"}

def test_delete_card():
    service = CardManagementService()
    service.create_card("123", "Alice")
    assert service.delete_card("123") is True
    assert service.get_card("123") is None

def test_delete_nonexistent_card():
    service = CardManagementService()
    assert service.delete_card("999") is False
