import tkinter as tk
class TaskList(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Create the task list label
        self.task_list_label = tk.Label(self, text="Task List")
        self.task_list_label.pack()
        # Create the task list box
        self.task_list_box = tk.Listbox(self)
        self.task_list_box.pack()
        # Create the add task button
        self.add_task_button = tk.Button(self, text="Add Task")
        self.add_task_button.pack()
        # Create the edit task button
        self.edit_task_button = tk.Button(self, text="Edit Task")
        self.edit_task_button.pack()
        # Create the mark task as completed button
        self.mark_task_as_completed_button = tk.Button(self, text="Mark Task as Completed")
        self.mark_task_as_completed_button.pack()
        # Create the delete task button
        self.delete_task_button = tk.Button(self, text="Delete Task")
        self.delete_task_button.pack()