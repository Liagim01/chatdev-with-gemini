'''
This is the main file for the Water Reminder application. It uses tkinter to create a GUI where users can input their work start and end times, and the interval for water breaks. It calculates the schedule for water breaks and updates a countdown timer for the next break. The application now correctly handles work hours that span over midnight and includes input validation to ensure a robust user experience.
'''
import tkinter as tk
import tkinter.messagebox
from datetime import datetime, timedelta
class WaterReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Reminder App")
        self.create_gui()
        self.schedule = []
        self.timer_running = False
    def create_gui(self):
        # Create and place GUI components here
        self.start_time_label = tk.Label(self.root, text="Start Time (HH:MM):")
        self.start_time_label.grid(row=0, column=0)
        self.start_time_entry = tk.Entry(self.root)
        self.start_time_entry.grid(row=0, column=1)
        self.end_time_label = tk.Label(self.root, text="End Time (HH:MM):")
        self.end_time_label.grid(row=1, column=0)
        self.end_time_entry = tk.Entry(self.root)
        self.end_time_entry.grid(row=1, column=1)
        self.interval_label = tk.Label(self.root, text="Interval (minutes):")
        self.interval_label.grid(row=2, column=0)
        self.interval_entry = tk.Entry(self.root)
        self.interval_entry.grid(row=2, column=1)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.on_submit)
        self.submit_button.grid(row=3, column=0, columnspan=2)
        self.schedule_label = tk.Label(self.root, text="Water Break Schedule:")
        self.schedule_label.grid(row=4, column=0, columnspan=2)
        self.countdown_label = tk.Label(self.root, text="Next Water Break Countdown: --:--")
        self.countdown_label.grid(row=5, column=0, columnspan=2)
    def calculate_schedule(self, start_time, end_time, interval):
        # Calculate the schedule for water breaks
        current_time = start_time
        while current_time < end_time:
            self.schedule.append(current_time)
            current_time += timedelta(minutes=interval)
        self.update_schedule_display()
    def update_schedule_display(self):
        # Update the schedule display on the GUI
        schedule_str = "\n".join(t.strftime("%H:%M") for t in self.schedule)
        self.schedule_label.config(text=f"Water Break Schedule:\n{schedule_str}")
    def update_countdown(self):
        # Update the countdown display on the GUI
        now = datetime.now()
        self.schedule = [t for t in self.schedule if t > now]  # Remove past break times
        if self.schedule:
            next_break = self.schedule[0]
            countdown = next_break - now
            # Format the countdown as HH:MM:SS
            countdown_str = str(countdown).split('.')[0]  # Remove microseconds
            self.countdown_label.config(text=f"Next Water Break Countdown: {countdown_str}")
            self.root.after(1000, self.update_countdown)  # Schedule the next update
        else:
            self.countdown_label.config(text="No more water breaks scheduled.")
            self.timer_running = False  # Stop the timer as there are no more breaks
    def start_timer(self):
        # Start the countdown timer
        if not self.timer_running:
            self.timer_running = True
            self.update_countdown()
    def on_submit(self):
        # Handle the submit action
        try:
            start_time_str = self.start_time_entry.get()
            end_time_str = self.end_time_entry.get()
            interval_str = self.interval_entry.get()
            # Validate interval input
            if not interval_str.isdigit() or int(interval_str) <= 0:
                raise ValueError("Interval must be a positive integer.")
            # Validate time format and convert to datetime objects
            start_time = datetime.strptime(start_time_str, "%H:%M")
            end_time = datetime.strptime(end_time_str, "%H:%M")
            # Check if the end time is on the following day
            if end_time <= start_time:
                end_time += timedelta(days=1)
            interval = int(interval_str)
            self.schedule = []  # Clear previous schedule
            self.calculate_schedule(start_time, end_time, interval)
            self.start_timer()
        except ValueError as e:
            # Display error message to the user
            tk.messagebox.showerror("Input Error", str(e))
def main():
    root = tk.Tk()
    app = WaterReminderApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()