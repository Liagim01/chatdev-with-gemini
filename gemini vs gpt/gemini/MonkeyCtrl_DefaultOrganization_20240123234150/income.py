'''This module contains the Income class.'''
class Income:
    def __init__(self):
        self._income = 0
    def get_income(self):
        return self._income
    def set_income(self, income):
        self._income = income