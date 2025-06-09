import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

from csv_handler import CSV  # Uses your original CSV class & data file

FORMAT = "%d-%m-%Y"  # date format for validation

class ExpenseTrackerGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("500x400")

        # --------------------------- Heading ---------------------------- #
        heading = tk.Label(
            root,
            text="Expense Tracker",
            font=("Helvetica", 20, "bold"),
            pady=20,
        )
        heading.pack()

        # --------------------------- Main Buttons ----------------------- #
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=30)

        add_btn = tk.Button(
            btn_frame,
            text="Add New Transaction",
            width=25,
            command=self.open_add_form,
            bg="#4CAF50",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        add_btn.grid(row=0, column=0, padx=10, pady=5)

        view_btn = tk.Button(
            btn_frame,
            text="View Transactions",
            width=25,
            command=self.open_view_window,
            bg="#2196F3",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        view_btn.grid(row=1, column=0, padx=10, pady=5)

        exit_btn = tk.Button(
            btn_frame,
            text="Exit",
            width=25,
            command=self.root.quit,
            bg="#f44336",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        exit_btn.grid(row=2, column=0, padx=10, pady=5)

    # --------------------------- Add Form ----------------------------- #
    def open_add_form(self):
        form = tk.Toplevel(self.root)
        form.title("Add Transaction")
        form.geometry("350x300")

        # Form labels + entries
        tk.Label(form, text="Date (dd-mm-yyyy):").grid(row=0, column=0, padx=10, pady=8, sticky="e")
        date_entry = tk.Entry(form)
        date_entry.insert(0, datetime.today().strftime(FORMAT))
        date_entry.grid(row=0, column=1, padx=10, pady=8)

        tk.Label(form, text="Amount:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
        amount_entry = tk.Entry(form)
        amount_entry.grid(row=1, column=1, padx=10, pady=8)

        tk.Label(form, text="Category (Income/Expense):").grid(row=2, column=0, padx=10, pady=8, sticky="e")
        category_entry = tk.Entry(form)
        category_entry.insert(0, "Expense")
        category_entry.grid(row=2, column=1, padx=10, pady=8)

        tk.Label(form, text="Description:").grid(row=3, column=0, padx=10, pady=8, sticky="e")
        desc_entry = tk.Entry(form)
        desc_entry.grid(row=3, column=1, padx=10, pady=8)

        # Submit handler
        def submit():
            date = date_entry.get()
            amt = amount_entry.get()
            cat = category_entry.get().title()
            desc = desc_entry.get()

            try:
                datetime.strptime(date, FORMAT)
                amt = float(amt)
                if cat not in ["Income", "Expense"]:
                    raise ValueError("Category must be Income or Expense")
            except ValueError as e:
                messagebox.showerror("Invalid Input", str(e), parent=form)
                return

            CSV.add_entry(date, amt, cat, desc)
            messagebox.showinfo("Success", "Transaction added!", parent=form)
            form.destroy()

        tk.Button(form, text="Submit", bg="#4CAF50", fg="white", command=submit).grid(
            row=4, column=0, columnspan=2, pady=15
        )

    # --------------------------- View Window -------------------------- #
    def open_view_window(self):
        start_date = simpledialog.askstring("Start Date", "Enter start date (dd-mm-yyyy):", parent=self.root)
        end_date = simpledialog.askstring("End Date", "Enter end date (dd-mm-yyyy):", parent=self.root)

        if not start_date or not end_date:
            return  # user cancelled

        df = CSV.get_transactions(start_date, end_date)
        if df is None or df.empty:
            messagebox.showinfo("No Data", "No transactions in that range.")
            return

        # New window for table + graph button
        view_win = tk.Toplevel(self.root)
        view_win.title("Transactions")
        view_win.geometry("700x400")

        # ----------------- Table ----------------- #
        tree = ttk.Treeview(view_win, columns=df.columns.tolist(), show="headings")
        for col in df.columns:
            tree.heading(col, text=col.title())
            tree.column(col, width=100, anchor="center")
        for _, row in df.iterrows():
            tree.insert("", "end", values=list(row))
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # ----------------- Graph Button ---------- #
        def plot_graph():
            local_df = df.copy()
            local_df.set_index("date", inplace=True)
            income = local_df[local_df["category"] == "Income"]["amount"].resample("D").sum()
            expense = local_df[local_df["category"] == "Expense"]["amount"].resample("D").sum()
            plt.figure(figsize=(10, 5))
            plt.plot(income.index, income.values, label="Income")
            plt.plot(expense.index, expense.values, label="Expense")
            plt.title("Income vs Expense")
            plt.xlabel("Date")
            plt.ylabel("Amount")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        graph_btn = tk.Button(view_win, text="Show Graph", bg="#2196F3", fg="white", command=plot_graph)
        graph_btn.pack(pady=10)


if __name__ == "__main__":
    CSV.initialize_csv()  # ensure data file exists
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()



