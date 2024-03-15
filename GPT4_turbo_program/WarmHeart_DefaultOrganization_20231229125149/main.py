'''
This is the main file for the Reminder Application. It sets up the GUI and handles the reminder notifications.
The reminders are set to notify the user to drink water every hour, stand up and stretch every 30 minutes,
and leave work at 9 PM daily. Additionally, when it's time to leave work, a conversation topic is provided.
'''
import tkinter as tk
from datetime import datetime, timedelta
import threading
import random
import sched
import time
class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.reminder_events = {}  # Dictionary to keep track of scheduled events
        self.create_gui()
        self.set_reminders()
        self.start_scheduler()  # Start the scheduler loop
    def create_gui(self):
        self.root.title("Reminder App")
        self.root.geometry("300x200")
        tk.Label(self.root, text="Reminder App", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text="Stay healthy and connected!").pack(pady=10)
    def set_reminders(self):
        # Set reminders for drinking water and avoiding prolonged sitting
        self.schedule_reminder("Drink Water", timedelta(hours=1))  # Every 1 hour
        self.schedule_reminder("Stand Up and Stretch", timedelta(minutes=30))  # Every 30 minutes
        # Set a reminder to leave work at 9 PM daily
        leave_work_time = datetime.now().replace(hour=21, minute=0, second=0, microsecond=0)
        self.schedule_daily_reminder("Leave Work", leave_work_time, True)
    def start_scheduler(self):
        def run_scheduler():
            while True:
                self.scheduler.run()
                time.sleep(1)
        self.scheduler_thread = threading.Thread(target=run_scheduler)
        self.scheduler_thread.daemon = True  # Daemonize thread to ensure it exits when the main program does
        self.scheduler_thread.start()
    def schedule_reminder(self, message, interval, conversation_topic=False):
        def reminder():
            show_reminder(message)
            if not conversation_topic:
                # Reschedule the reminder
                event = self.scheduler.enter(interval.total_seconds(), 1, reminder)
                self.reminder_events[message] = event
        event = self.scheduler.enter(interval.total_seconds(), 1, reminder)
        self.reminder_events[message] = event
    def schedule_daily_reminder(self, message, target_time, conversation_topic=False):
        def reminder():
            show_reminder(message)
            if conversation_topic:
                topics = get_conversation_topics()
                show_reminder("Talk about: " + topics)
            # Schedule the next reminder for the following day
            next_target_time = datetime.now().replace(hour=target_time.hour, minute=target_time.minute, second=0, microsecond=0) + timedelta(days=1)
            self.scheduler.enterabs(time.mktime(next_target_time.timetuple()), 1, reminder)
        # Schedule the first reminder
        now = datetime.now()
        if now.hour >= target_time.hour and now.minute >= target_time.minute:
            # If it's already past the target time, schedule for the next day
            target_time += timedelta(days=1)
        self.scheduler.enterabs(time.mktime(target_time.timetuple()), 1, reminder)
    def stop_scheduler(self):
        # This method should be called to stop the scheduler thread when the application is closed
        self.scheduler_thread.join()
        for event in self.reminder_events.values():
            self.scheduler.cancel(event)  # Cancel all scheduled events
def show_reminder(message):
    # This function will show the reminder notification to the user
    reminder_window = tk.Toplevel()
    reminder_window.title("Reminder")
    tk.Label(reminder_window, text=message, font=("Arial", 12)).pack(pady=20)
    tk.Button(reminder_window, text="OK", command=reminder_window.destroy).pack(pady=10)
def get_conversation_topics():
    # This function will return a string of conversation topics
    topics = [
        "the latest tech news",
        "upcoming company events",
        "any recent personal achievements",
        "popular TV shows or movies",
        "local sports events"
    ]
    return random.choice(topics)
if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.protocol("WM_DELETE_WINDOW", app.stop_scheduler)  # Stop the scheduler when the window is closed
    root.mainloop()