import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from analysis import (
    total_spending,
    spending_by_category,
    highest_expense,
    remaining_budget,
    is_overspending,
)

EXPENSES = [
    {"name": "Lunch", "amount": 10, "category": "food"},
    {"name": "Bus", "amount": 5, "category": "transport"},
    {"name": "Dinner", "amount": 20, "category": "food"},
]


def test_total_spending_normal():
    assert total_spending(EXPENSES) == 35


def test_spending_by_category():
    assert spending_by_category(EXPENSES) == {"food": 30, "transport": 5}


def test_highest_expense_empty_list():
    # edge case: empty list
    assert highest_expense([]) is None


def test_remaining_budget_negative_budget():
    # error case: invalid input
    with pytest.raises(ValueError):
        remaining_budget(-10, EXPENSES)


def test_remaining_budget_invalid_types():
    # error case: budget or amounts that are not numbers
    with pytest.raises(ValueError):
        remaining_budget("100", EXPENSES)
    with pytest.raises(ValueError):
        remaining_budget(100, [{"name": "X", "amount": "abc", "category": "food"}])