
import pytest
from expenses import add_expense, remove_expense


def test_add_expense():
    expenses = []
    result = add_expense(expenses, "Lunch", 40, "Food")
    assert result[0]["amount"] == 40
    assert result[0]["category"] == "Food"


def test_remove_expense():
    expenses = [
        {"name": "Taxi", "amount": 20, "category": "Transport"}
    ]
    result = remove_expense(expenses, 0)
    assert result == []


def test_negative_amount():
    with pytest.raises(ValueError):
        add_expense([], "Lunch", -5, "Food")


def test_zero_amount():
    with pytest.raises(ValueError):
        add_expense([], "Coffee", 0, "Food")


def test_invalid_index():
    with pytest.raises(ValueError):
        remove_expense([], 0)
