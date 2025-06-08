# import tkinter as tk
# from tkinter import messagebox, ttk

# # Global expenses list
# expenses = []

# # Function to add expense
# def add_expense():
#     month = month_entry.get().strip()
#     amount = amount_entry.get()
#     category = category_entry.get()

#     if not month:
#         messagebox.showerror("Error", "Month cannot be empty! (e.g., May2025)")
#         return

#     try:
#         amount = float(amount)
#         if not category:
#             messagebox.showerror("Error", "Category cannot be empty!")
#             return

#         expense = {'amount': amount, 'category': category}
#         expenses.append(expense)
#         messagebox.showinfo("Success", f"Added expense: ₹{amount:.2f} in '{category}'")
#         amount_entry.delete(0, tk.END)
#         category_entry.delete(0, tk.END)
#         refresh_expense_list()
#         update_total()
#     except ValueError:
#         messagebox.showerror("Error", "Please enter a valid amount!")

# # Function to refresh expense list
# def refresh_expense_list():
#     expense_list.delete(*expense_list.get_children())
#     for i, expense in enumerate(expenses, start=1):
#         expense_list.insert('', 'end', values=(i, f"₹{expense['amount']:.2f}", expense['category']))

# # Function to update total expenses
# def update_total():
#     total = sum(exp['amount'] for exp in expenses)
#     total_label.config(text=f"Total Expenses: ₹{total:.2f}")

# # Function to filter by category
# def filter_by_category():
#     category = filter_entry.get()
#     filtered = [exp for exp in expenses if exp['category'].lower() == category.lower()]

#     expense_list.delete(*expense_list.get_children())
#     for i, expense in enumerate(filtered, start=1):
#         expense_list.insert('', 'end', values=(i, f"₹{expense['amount']:.2f}", expense['category']))

# # Function to submit all expenses to month file
# def submit_month_expenses():
#     month = month_entry.get().strip()
#     if not month:
#         messagebox.showerror("Error", "Month cannot be empty! (e.g., May2025)")
#         return

#     if not expenses:
#         messagebox.showwarning("Warning", "No expenses to submit for this month!")
#         return

#     filename = f"{month}.txt"
#     with open(filename, "a", encoding="utf-8") as file:  # <-- Added encoding
#         file.write(f"--- Expenses for {month} ---\n")
#         for exp in expenses:
#             line = f"₹{exp['amount']:.2f} - {exp['category']}\n"
#             file.write(line)
#         file.write("\n")

#     messagebox.showinfo("Submitted", f"All expenses saved to {filename}!")
#     expenses.clear()
#     refresh_expense_list()
#     update_total()


#     messagebox.showinfo("Submitted", f"All expenses saved to {filename}!")
#     expenses.clear()
#     refresh_expense_list()
#     update_total()

# # Initialize GUI
# root = tk.Tk()
# root.title("💸 Expense Tracker")
# root.geometry("600x600")
# root.config(bg="#f0f8ff")

# # Title
# title = tk.Label(root, text="Expense Tracker", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#2e8b57")
# title.pack(pady=10)

# # Input frame
# input_frame = tk.Frame(root, bg="#f0f8ff")
# input_frame.pack(pady=10)

# tk.Label(input_frame, text="Month (e.g., May2025):", bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=5)
# month_entry = tk.Entry(input_frame)
# month_entry.grid(row=0, column=1, padx=5, pady=5)

# tk.Label(input_frame, text="Amount (₹):", bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=5)
# amount_entry = tk.Entry(input_frame)
# amount_entry.grid(row=1, column=1, padx=5, pady=5)

# tk.Label(input_frame, text="Category:", bg="#f0f8ff").grid(row=2, column=0, padx=5, pady=5)
# category_entry = tk.Entry(input_frame)
# category_entry.grid(row=2, column=1, padx=5, pady=5)

# add_button = tk.Button(input_frame, text="Add Expense", command=add_expense, bg="#2e8b57", fg="white")
# add_button.grid(row=3, column=0, columnspan=2, pady=10)

# # Filter frame
# filter_frame = tk.Frame(root, bg="#f0f8ff")
# filter_frame.pack(pady=5)

# tk.Label(filter_frame, text="Filter by Category:", bg="#f0f8ff").grid(row=0, column=0, padx=5)
# filter_entry = tk.Entry(filter_frame)
# filter_entry.grid(row=0, column=1, padx=5)
# filter_button = tk.Button(filter_frame, text="Filter", command=filter_by_category, bg="#4682b4", fg="white")
# filter_button.grid(row=0, column=2, padx=5)

# # Expense list table
# columns = ('#', 'Amount', 'Category')
# expense_list = ttk.Treeview(root, columns=columns, show='headings')
# for col in columns:
#     expense_list.heading(col, text=col)
# expense_list.pack(pady=10, fill='x')

# # Total label
# total_label = tk.Label(root, text="Total Expenses: ₹0.00", font=("Helvetica", 14, "bold"), bg="#f0f8ff", fg="#ff4500")
# total_label.pack(pady=10)

# # Submit Month button
# submit_button = tk.Button(root, text="✅ Submit All Expenses for Month", command=submit_month_expenses, bg="#ff6347", fg="white", font=("Helvetica", 12, "bold"))
# submit_button.pack(pady=15)

# # Run the app
# root.mainloop()


# import pandas as pd
# import csv
# from datetime import datetime

# class CSV: 
#     CSV_FILE = "finance_data.csv"

#     @classmethod
#     def initialize_csv(cls):
#         try:
#             pd.read_csv(cls.CSV_FILE)
#         except FileNotFoundError:
#             df = pd.DataFrame(columns=cls.COLUMNS)
#             df.to_csv(cls.CSV_FILE, index=False)

    
#     @classmethod
#     def add_entry(cls, date, amount, category, description):
#         new_entry = {
#             "date": date,
#             "amount": amount,
#             "category": category,
#             "description": description,
#         }
#         with open(cls.CSV_FILE, "a", newline="") as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
#             writer.writerow(new_entry)
#         print("Entry added successfully")



# CSV.initialize_csv()
# CSV.add_entry("20-07-2024", 125.65, "Income", "Salary")


import os
import csv
import pandas as pd
from datetime import datetime  
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS  = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        """Create the CSV (with headers) the first time you run the program."""
        if not os.path.exists(cls.CSV_FILE):
            # create an empty file with the correct header row
            pd.DataFrame(columns=cls.COLUMNS).to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        """Append one row to the CSV (auto-creates the file if needed)."""
        cls.initialize_csv()          # ensure the file exists

        # —optional— enforce ISO date format for consistency
        # date = datetime.strptime(date, "%d-%m-%Y").strftime("%Y-%m-%d")

        new_entry = {
            "date":        date,
            "amount":      amount,
            "category":    category,
            "description": description,
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)

        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df['date'], format= CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print('No transactions found in the given date range')
            return None
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\n Summary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")
            return filtered_df

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

def plot_transactions(df):
    df.set_index("date", inplace=True)

    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
        )
    
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
        )
    
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title('Income and Expenses Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm- yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date,end_date)
            if df is not None and not df.empty:
                if input("Do you want to see a plot? (y/n)").lower() == "y":
                    plot_transactions(df)
        elif choice == "3":
            print("Existing...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()


