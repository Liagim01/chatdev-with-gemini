'''This is the main file for the personal budget app.'''
import tkinter as tk
from income import Income
from expense import Expense
from report import Report
def main():
    window = tk.Tk()
    window.title("Personal Budget App")
    # Create the income, expense, and report objects.
    income = Income()
    expense = Expense()
    report = Report()
    # Create the main window.
    main_frame = tk.Frame(window)
    main_frame.pack()
    # Create the income entry form.
    income_label = tk.Label(main_frame, text="Income:")
    income_label.grid(row=0, column=0)
    income_entry = tk.Entry(main_frame)
    income_entry.grid(row=0, column=1)
    # Create the expense entry form.
    expense_label = tk.Label(main_frame, text="Expense:")
    expense_label.grid(row=1, column=0)
    expense_entry = tk.Entry(main_frame)
    expense_entry.grid(row=1, column=1)
    # Create the submit button.
    submit_button = tk.Button(main_frame, text="Submit", command=lambda: report.generate_report(income.get_income(), expense.get_expense()))
    submit_button.grid(row=2, column=1)
    # Create the report display area.
    report_display = tk.Text(main_frame)
    report_display.grid(row=3, column=0, columnspan=2)
    # Start the main loop.
    window.mainloop()
if __name__ == "__main__":
    main()