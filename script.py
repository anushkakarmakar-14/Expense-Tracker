# Expense Tracker Application

# Function to add an expense
def add_expense(expenses, amount, category):
    """
    Adds a new expense to the list of expenses.

    Parameters:
    expenses (list): The list of expenses.
    amount (float): The amount of the expense.
    category (str): The category of the expense.

    Returns:
    None
    """
    expenses.append({'amount': amount, 'category': category})
    print("Expense added successfully!")

# Function to display all expenses
def print_expenses(expenses):
    """
    Prints all expenses in a user-friendly format.

    Parameters:
    expenses (list): The list of expenses.

    Returns:
    None
    """
    if not expenses:
        print("No expenses recorded.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: {expense['amount']:.2f}, Category: {expense['category']}")

# Function to calculate the total expenses
def total_expenses(expenses):
    """
    Calculates the total amount of all expenses.

    Parameters:
    expenses (list): The list of expenses.

    Returns:
    float: The total amount of expenses.
    """
    return sum(expense['amount'] for expense in expenses)

# Function to filter expenses by category
def filter_expenses_by_category(expenses, category):
    """
    Filters and returns expenses by the specified category.

    Parameters:
    expenses (list): The list of expenses.
    category (str): The category to filter by.

    Returns:
    list: A list of expenses matching the category.
    """
    return [expense for expense in expenses if expense['category'].lower() == category.lower()]

# Main function to run the application
def main():
    """
    The main function to manage the Expense Tracker application.

    Returns:
    None
    """
    expenses = []  # List to store all expenses

    while True:
        # User-friendly menu
        print("\n======== Expense Tracker ========")
        print("1. Add an Expense")
        print("2. List All Expenses")
        print("3. Show Total Expenses")
        print("4. Filter Expenses by Category")
        print("5. Exit")
        print("=================================")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':  # Add an expense
            try:
                amount = float(input("Enter the expense amount: "))
                category = input("Enter the expense category: ").strip()
                if not category:
                    print("Category cannot be empty!")
                else:
                    add_expense(expenses, amount, category)
            except ValueError:
                print("Invalid amount! Please enter a number.")

        elif choice == '2':  # List all expenses
            print("\nAll Recorded Expenses:")
            print_expenses(expenses)

        elif choice == '3':  # Show total expenses
            print("\nTotal Expenses: {:.2f}".format(total_expenses(expenses)))

        elif choice == '4':  # Filter expenses by category
            category = input("Enter the category to filter: ").strip()
            if not category:
                print("Category cannot be empty!")
            else:
                filtered_expenses = filter_expenses_by_category(expenses, category)
                print(f"\nExpenses in category '{category}':")
                print_expenses(filtered_expenses)

        elif choice == '5':  # Exit the program
            print("Thank you for using the Expense Tracker. Goodbye!")
            break

        else:  # Invalid choice
            print("Invalid choice! Please enter a number between 1 and 5.")

# Run the Expense Tracker
if __name__ == "__main__":
    main()
