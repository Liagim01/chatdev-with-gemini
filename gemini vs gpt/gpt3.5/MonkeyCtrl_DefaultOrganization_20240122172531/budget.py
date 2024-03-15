'''
This file contains the Budget class that handles income, expense tracking, and reporting.
'''
class Budget:
    def __init__(self):
        self.income = []
        self.expenses = []
    def add_income(self, amount):
        self.income.append(amount)
    def add_expense(self, amount):
        self.expenses.append(amount)
    def generate_report(self):
        total_income = sum(self.income)
        total_expenses = sum(self.expenses)
        balance = total_income - total_expenses
        report = {
            "Total Income": total_income,
            "Total Expenses": total_expenses,
            "Balance": balance
        }
        return report