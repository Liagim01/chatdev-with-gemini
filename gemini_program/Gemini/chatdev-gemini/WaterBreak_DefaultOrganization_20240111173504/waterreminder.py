import tkinter as tk
from datetime import datetime
import time
class WaterReminder:
    """
    A class that creates a water reminder GUI window and starts the water reminder.
    """
    def __init__(self, root):
        """
        Initialize the WaterReminder object.
        Args:
            root: The Tkinter root window.
        """
        self.root = root
        # Create a frame for the water reminder.
        self.frame = tk.Frame(root)
        self.frame.pack()
        # Create a label for the start time.
        self.start_time_label = tk.Label(self.frame, text="Start Time:")
        self.start_time_label.grid(row=0, column=0)
        # Create an entry for the start time.
        self.start_time_entry = tk.Entry(self.frame)
        self.start_time_entry.grid(row=0, column=1)
        # Create a label for the end time.
        self.end_time_label = tk.Label(self.frame, text="End Time:")
        self.end_time_label.grid(row=1, column=0)
        # Create an entry for the end time.
        self.end_time_entry = tk.Entry(self.frame)
        self.end_time_entry.grid(row=1, column=1)
        # Create a label for the water break interval.
        self.water_break_interval_label = tk.Label(self.frame, text="Water Break Interval (minutes):")
        self.water_break_interval_label.grid(row=2, column=0)
        # Create an entry for the water break interval.
        self.water_break_interval_entry = tk.Entry(self.frame)
        self.water_break_interval_entry.grid(row=2, column=1)
        # Create a button to start the water reminder.
        self.start_button = tk.Button(self.frame, text="Start", command=self.start)
        self.start_button.grid(row=3, column=0)
        # Create a button to stop the water reminder.
        self.stop_button = tk.Button(self.frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=3, column=1)
        # Create a label for the next water break time.
        self.next_water_break_time_label = tk.Label(self.frame, text="Next Water Break Time:")
        self.next_water_break_time_label.grid(row=4, column=0)
        # Create a label for the countdown timer.
        self.countdown_timer_label = tk.Label(self.frame, text="Countdown Timer:")
        self.countdown_timer_label.grid(row=5, column=0)
        # Initialize the water reminder variables.
        self.start_time = None
        self.end_time = None
        self.water_break_interval = None
        self.next_water_break_time = None
        self.countdown_timer = None
    def start(self):
        """
        Start the water reminder.
        """
        # Get the start time, end time, and water break interval from the user.
        self.start_time = datetime.strptime(self.start_time_entry.get(), "%H:%M")
        self.end_time = datetime.strptime(self.end_time_entry.get(), "%H:%M")
        self.water_break_interval = int(self.water_break_interval_entry.get())
        # Calculate the next water break time.
        self.next_water_break_time = self.start_time + datetime.timedelta(minutes=self.water_break_interval)
        # Start the countdown timer.
        self.countdown_timer = time.time()
        # Update the GUI.
        self.update_gui()
        # Start the main loop.
        self.root.mainloop()
    def stop(self):
        """
        Stop the water reminder.
        """
        # Stop the countdown timer.
        self.countdown_timer = None
        # Update the GUI.
        self.update_gui()
    def update_gui(self):
        """
        Update the GUI.
        """
        # Update the next water break time label.
        self.next_water_break_time_label.config(text="Next Water Break Time: {}".format(self.next_water_break_time))
        # Update the countdown timer label.
        if self.countdown_timer is not None:
            # Calculate the time remaining until the next water break.
            time_remaining = self.next_water_break_time - datetime.now()
            # Update the countdown timer label.
            self.countdown_timer_label.config(text="Countdown Timer: {}".format(time_remaining))
            # Schedule the next update.
            self.root.after(1000, self.update_gui)
        else:
            # The countdown timer is not running.
            self.countdown_timer_label.config(text="Countdown Timer: 00:00")