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


import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

try:
    from tkcalendar import DateEntry
    CALENDAR_AVAILABLE = True
except ImportError:
    CALENDAR_AVAILABLE = False

CSV_FILE = "finance_data.csv"
COLUMNS = ["date", "amount", "category", "description"]
FORMAT = "%d-%m-%Y"

def initialize_csv():
    if not os.path.exists(CSV_FILE):
        pd.DataFrame(columns=COLUMNS).to_csv(CSV_FILE, index=False)

def add_entry(date, amount, category, description):
    initialize_csv()
    new_entry = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description,
    }
    with open(CSV_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COLUMNS)
        writer.writerow(new_entry)

def plot_transactions(start_date, end_date):
    df = pd.read_csv(CSV_FILE)
    df["date"] = pd.to_datetime(df['date'], format=FORMAT)
    df.set_index("date", inplace=True)

    try:
        start = datetime.strptime(start_date, FORMAT)
        end = datetime.strptime(end_date, FORMAT)
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter valid start and end dates in dd-mm-yyyy format.")
        return

    filtered_df = df.loc[(df.index >= start) & (df.index <= end)]

    if filtered_df.empty:
        messagebox.showinfo("No Data", "No transactions found in the given date range.")
        return

    income_df = filtered_df[filtered_df["category"] == "Income"].resample("D").sum().reindex(filtered_df.index, fill_value=0)
    expense_df = filtered_df[filtered_df["category"] == "Expense"].resample("D").sum().reindex(filtered_df.index, fill_value=0)

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="green")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="red")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense Over Selected Time Period")
    plt.legend()
    plt.grid(True)
    plt.show()

def save_transaction():
    try:
        date = date_entry.get()
        datetime.strptime(date, FORMAT)  # validate format
        amount = float(amount_entry.get())
        category = category_combobox.get()
        description = description_entry.get()

        add_entry(date, amount, category, description)
        messagebox.showinfo("Success", "Transaction saved successfully!")

        # clear inputs
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        category_combobox.set("Expense")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values.")

def open_chart():
    start_date = chart_start_date.get()
    end_date = chart_end_date.get()
    plot_transactions(start_date, end_date)

# ---------------- GUI Layout ----------------
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x500")
root.configure(bg="white")

style = ttk.Style()
style.configure("TLabel", background="white", font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10, "bold"))

frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

tt_label = ttk.Label(frame, text="Enter Your Transaction Details", font=("Helvetica", 14, "bold"))
tt_label.pack(pady=10)

# Date
ttk.Label(frame, text="Date (dd-mm-yyyy):").pack(anchor="w")
if CALENDAR_AVAILABLE:
    date_entry = DateEntry(frame, date_pattern='dd-mm-yyyy')
else:
    date_entry = ttk.Entry(frame)
    date_entry.insert(0, datetime.today().strftime(FORMAT))
date_entry.pack(fill="x", pady=5)

# Amount
ttk.Label(frame, text="Amount:").pack(anchor="w")
amount_entry = ttk.Entry(frame)
amount_entry.pack(fill="x", pady=5)

# Category
ttk.Label(frame, text="Category:").pack(anchor="w")
category_combobox = ttk.Combobox(frame, values=["Income", "Expense"], state="readonly")
category_combobox.set("Expense")
category_combobox.pack(fill="x", pady=5)

# Description
ttk.Label(frame, text="Description:").pack(anchor="w")
description_entry = ttk.Entry(frame)
description_entry.pack(fill="x", pady=5)

# Save Button
save_button = ttk.Button(frame, text="💾 Save Transaction", command=save_transaction)
save_button.pack(pady=10)

# Chart Section
ttk.Label(frame, text="Chart Start Date (dd-mm-yyyy):").pack(anchor="w")
chart_start_date = ttk.Entry(frame)
chart_start_date.insert(0, datetime.today().strftime(FORMAT))
chart_start_date.pack(fill="x", pady=2)

ttk.Label(frame, text="Chart End Date (dd-mm-yyyy):").pack(anchor="w")
chart_end_date = ttk.Entry(frame)
chart_end_date.insert(0, datetime.today().strftime(FORMAT))
chart_end_date.pack(fill="x", pady=2)

chart_button = ttk.Button(frame, text="📈 View Chart", command=open_chart)
chart_button.pack(pady=10)

root.mainloop()
