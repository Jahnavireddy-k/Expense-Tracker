import json
import os

FILENAME = "expenses.json"

def load_expenses():
    """Load expenses from the JSON file if it exists, otherwise return an empty list."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    """Save the list of expenses to the JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Prompt user for expense details and add it to the list."""
    title = input("Enter expense title: ").strip()
    try:
        amount = float(input("Enter amount (₹): "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    category = input("Enter category (e.g., Food, Transport, Utilities): ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!\n")

def view_expenses(expenses):
    """Display all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. Title: {exp['title']} | Amount: ₹{exp['amount']:.2f} | Category: {exp['category']} | Date: {exp['date']}")
    print()

def main():
    expenses = load_expenses()
    
    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Exiting tracker. Good luck with your project!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 3.\n")

if __name__ == "__main__":
    main()