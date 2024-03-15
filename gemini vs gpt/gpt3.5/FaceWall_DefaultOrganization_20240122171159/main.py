'''
FaceWall - Memo Software for Company Employees
This is the main file of the FaceWall application. It initializes the GUI and starts the application.
'''
import tkinter as tk
from task_list import TaskList
from schedule import Schedule
from search import Search
from brief_note import BriefNote
class FaceWallApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FaceWall")
        # Create the main menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        # Create the sub-menus
        self.task_list = TaskList(self)
        self.schedule = Schedule(self)
        self.search = Search(self)
        self.brief_note = BriefNote(self)
        # Add sub-menus to the main menu
        self.menu.add_cascade(label="Task List", menu=self.task_list)
        self.menu.add_cascade(label="Schedule", menu=self.schedule)
        self.menu.add_cascade(label="Search", menu=self.search)
        self.menu.add_cascade(label="Brief Note", menu=self.brief_note)
if __name__ == "__main__":
    app = FaceWallApplication()
    app.mainloop()