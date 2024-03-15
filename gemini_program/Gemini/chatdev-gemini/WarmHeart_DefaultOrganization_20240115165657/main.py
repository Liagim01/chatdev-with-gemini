import tkinter as tk
from reminder_window import ReminderWindow
def main():
    '''Create the main window and start the app.'''
    root = tk.Tk()
    root.title("Reminder App")
    ReminderWindow(root)
    root.mainloop()
if __name__ == "__main__":
    main()