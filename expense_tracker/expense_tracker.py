import json
import os
from datetime import datetime

DATA_FILE = "data/expenses.json"

# Ensure data folder exists
if not os.path.exists("data"):
    os.makedirs("data")

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        expenses = json.load(f)
else:
    expenses = []

def save_expenses():
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Transport, etc.): ").title()
        description = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        if date == "":
            date = datetime.today().strftime("%Y-%m-%d")
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }
        expenses.append(expense)
        save_expenses()
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Amount must be a number.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nAll Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} - {exp['category']} - {exp['description']} - ${exp['amount']:.2f}")

def filter_by_category():
    category = input("Enter category to filter: ").title()
    filtered = [e for e in expenses if e["category"] == category]
    if not filtered:
        print(f"No expenses found in category: {category}")
        return
    print(f"\nExpenses in {category}:")
    for i, exp in enumerate(filtered, start=1):
        print(f"{i}. {exp['date']} - {exp['description']} - ${exp['amount']:.2f}")

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    monthly = [e for e in expenses if e["date"].startswith(month)]
    if not monthly:
        print(f"No expenses found for {month}")
        return
    total = sum(e["amount"] for e in monthly)
    print(f"\nMonthly Summary for {month}:")
    for e in monthly:
        print(f"{e['date']} - {e['category']} - {e['description']} - ${e['amount']:.2f}")
    print(f"Total spent: ${total:.2f}")

def main_menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
