'''
Search Module
This module provides the search functionality. Employees can easily find tasks and notes.
'''
import tkinter as tk
class Search(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.add_command(label="Search Tasks", command=self.search_tasks)
        self.add_command(label="Search Notes", command=self.search_notes)
    def search_tasks(self):
        # Implement the logic to search for tasks
        print("Searching for tasks...")
    def search_notes(self):
        # Implement the logic to search for notes
        print("Searching for notes...")