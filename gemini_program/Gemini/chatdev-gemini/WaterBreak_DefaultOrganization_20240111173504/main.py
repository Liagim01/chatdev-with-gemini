import tkinter as tk
from datetime import datetime
from waterreminder import WaterReminder
def main():
    """
    Create a GUI window and start the water reminder.
    """
    root = tk.Tk()
    root.title("Water Reminder")
    root.geometry("300x200")
    # Create a WaterReminder object.
    water_reminder = WaterReminder(root)
    # Start the water reminder.
    water_reminder.start()
    # Start the main loop.
    root.mainloop()
if __name__ == "__main__":
    main()