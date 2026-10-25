def total_spending(expenses):
    """Sum of all amounts. expenses = list of dicts {"name", "amount", "category"}."""
    return sum(e["amount"] for e in expenses)


def spending_by_category(expenses):
    """Return a dict {category: total}."""
    result = {}
    for e in expenses:
        result[e["category"]] = result.get(e["category"], 0) + e["amount"]
    return result


def highest_expense(expenses):
    """Return the biggest expense, or None if the list is empty."""
    if not expenses:
        return None
    return max(expenses, key=lambda e: e["amount"])


def remaining_budget(budget, expenses):
    """Budget minus spending. Raises ValueError if the budget is negative."""
    if budget < 0:
        raise ValueError("Budget cannot be negative")
    return budget - total_spending(expenses)


def is_overspending(budget, expenses):
    """True if spending is above the budget."""
    return total_spending(expenses) > budget