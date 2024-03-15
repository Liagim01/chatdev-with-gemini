import tkinter as tk
from reminder_entry import ReminderEntry
class ReminderWindow(tk.Frame):
    '''Main window for the reminder app.'''
    def __init__(self, root):
        '''Initialize the main window.'''
        super().__init__(root)
        self.root = root
        self.pack()
        # Create the reminder entries.
        self.reminder_entries = []
        for reminder in ["Drink water", "Avoid prolonged sitting", "Leave work at 9 PM"]:
            reminder_entry = ReminderEntry(self, reminder)
            reminder_entry.pack()
            self.reminder_entries.append(reminder_entry)
        # Create the button to add a new reminder.
        self.add_reminder_button = tk.Button(self, text="Add Reminder", command=self.add_reminder)
        self.add_reminder_button.pack()
    def add_reminder(self):
        '''Add a new reminder to the list.'''
        reminder = ReminderEntry(self, "")
        reminder.pack()
        self.reminder_entries.append(reminder)