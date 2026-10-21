
import json
from datetime import date
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved expenses.")
    return []


def save_expenses(expenses):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)


def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    description = input("Enter description: ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date.today().isoformat()
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"{expense['amount']:.2f}"
        )


def show_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    total = sum(expense["amount"] for expense in expenses)
    today = date.today()
    monthly = [
        expense for expense in expenses
        if expense["date"][:7] == today.strftime("%Y-%m")
    ]

    print(f"Total expenses: {total:.2f}")
    print(f"This month's expenses: {sum(e['amount'] for e in monthly):.2f}")

    print("Spending by category:")
    categories = {}
    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]

    for category, amount in categories.items():
        print(f"{category}: {amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
