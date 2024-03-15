'''This module contains the Report class.'''
import matplotlib.pyplot as plt
class Report:
    def __init__(self):
        self._income = 0
        self._expense = 0
    def generate_report(self, income, expense):
        self._income = income
        self._expense = expense
        # Create the pie chart.
        labels = ['Income', 'Expense']
        sizes = [self._income, self._expense]
        colors = ['green', 'red']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.title('Income and Expense Report')
        plt.show()