'''This module contains the Expense class.'''
class Expense:
    def __init__(self):
        self._expense = 0
    def get_expense(self):
        return self._expense
    def set_expense(self, expense):
        self._expense = expense