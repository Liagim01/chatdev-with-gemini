import datetime
import threading

class WaterBreakScheduler:

    def __init__(self, work_hours, break_interval):

        self.work_hours = work_hours
        self.break_interval = break_interval
        self.timer = None

    def start(self):
        self.timer = threading.Timer(self.break_interval, self.notify_break)
        self.timer.start()

    def notify_break(self):
        print("Water break time!")
        self.timer = threading.Timer(self.break_interval, self.notify_break)
        self.timer.start()

    def stop(self):

     self.timer.cancel()

# Example usage:
work_hours = (8, 17)  # 8 am to 5 pm
break_interval = 60 * 60  # 1 hour in seconds

scheduler = WaterBreakScheduler(work_hours, break_interval)
scheduler.start()

# Keep the app running until the user closes it
try:
    while True:

     pass
except KeyboardInterrupt:
    scheduler.stop()