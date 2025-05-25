import tkinter as tk
from tkinter import messagebox, ttk

# Global expenses list
expenses = []

# Function to add expense
def add_expense():
    month = month_entry.get().strip()
    amount = amount_entry.get()
    category = category_entry.get()

    if not month:
        messagebox.showerror("Error", "Month cannot be empty! (e.g., May2025)")
        return

    try:
        amount = float(amount)
        if not category:
            messagebox.showerror("Error", "Category cannot be empty!")
            return

        expense = {'amount': amount, 'category': category}
        expenses.append(expense)
        messagebox.showinfo("Success", f"Added expense: ₹{amount:.2f} in '{category}'")
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        refresh_expense_list()
        update_total()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount!")

# Function to refresh expense list
def refresh_expense_list():
    expense_list.delete(*expense_list.get_children())
    for i, expense in enumerate(expenses, start=1):
        expense_list.insert('', 'end', values=(i, f"₹{expense['amount']:.2f}", expense['category']))

# Function to update total expenses
def update_total():
    total = sum(exp['amount'] for exp in expenses)
    total_label.config(text=f"Total Expenses: ₹{total:.2f}")

# Function to filter by category
def filter_by_category():
    category = filter_entry.get()
    filtered = [exp for exp in expenses if exp['category'].lower() == category.lower()]

    expense_list.delete(*expense_list.get_children())
    for i, expense in enumerate(filtered, start=1):
        expense_list.insert('', 'end', values=(i, f"₹{expense['amount']:.2f}", expense['category']))

# Function to submit all expenses to month file
def submit_month_expenses():
    month = month_entry.get().strip()
    if not month:
        messagebox.showerror("Error", "Month cannot be empty! (e.g., May2025)")
        return

    if not expenses:
        messagebox.showwarning("Warning", "No expenses to submit for this month!")
        return

    filename = f"{month}.txt"
    with open(filename, "a", encoding="utf-8") as file:  # <-- Added encoding
        file.write(f"--- Expenses for {month} ---\n")
        for exp in expenses:
            line = f"₹{exp['amount']:.2f} - {exp['category']}\n"
            file.write(line)
        file.write("\n")

    messagebox.showinfo("Submitted", f"All expenses saved to {filename}!")
    expenses.clear()
    refresh_expense_list()
    update_total()


    messagebox.showinfo("Submitted", f"All expenses saved to {filename}!")
    expenses.clear()
    refresh_expense_list()
    update_total()

# Initialize GUI
root = tk.Tk()
root.title("💸 Expense Tracker")
root.geometry("600x600")
root.config(bg="#f0f8ff")

# Title
title = tk.Label(root, text="Expense Tracker", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#2e8b57")
title.pack(pady=10)

# Input frame
input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Month (e.g., May2025):", bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=5)
month_entry = tk.Entry(input_frame)
month_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Amount (₹):", bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Category:", bg="#f0f8ff").grid(row=2, column=0, padx=5, pady=5)
category_entry = tk.Entry(input_frame)
category_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Expense", command=add_expense, bg="#2e8b57", fg="white")
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Filter frame
filter_frame = tk.Frame(root, bg="#f0f8ff")
filter_frame.pack(pady=5)

tk.Label(filter_frame, text="Filter by Category:", bg="#f0f8ff").grid(row=0, column=0, padx=5)
filter_entry = tk.Entry(filter_frame)
filter_entry.grid(row=0, column=1, padx=5)
filter_button = tk.Button(filter_frame, text="Filter", command=filter_by_category, bg="#4682b4", fg="white")
filter_button.grid(row=0, column=2, padx=5)

# Expense list table
columns = ('#', 'Amount', 'Category')
expense_list = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    expense_list.heading(col, text=col)
expense_list.pack(pady=10, fill='x')

# Total label
total_label = tk.Label(root, text="Total Expenses: ₹0.00", font=("Helvetica", 14, "bold"), bg="#f0f8ff", fg="#ff4500")
total_label.pack(pady=10)

# Submit Month button
submit_button = tk.Button(root, text="✅ Submit All Expenses for Month", command=submit_month_expenses, bg="#ff6347", fg="white", font=("Helvetica", 12, "bold"))
submit_button.pack(pady=15)

# Run the app
root.mainloop()





