
def add_expense(expenses, name, amount, category):
    if not name or not category:
        raise ValueError("Name and category are required")

    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Amount must be numeric")

    if not 0 < amount < float("inf"):
        raise ValueError("Amount must be positive and finite")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    return expenses


def remove_expense(expenses, index):
    if isinstance(index, bool) or not isinstance(index, int):
        raise ValueError("Invalid index")

    if index < 0 or index >= len(expenses):
        raise ValueError("Invalid index")

    expenses.pop(index)
    return expenses
