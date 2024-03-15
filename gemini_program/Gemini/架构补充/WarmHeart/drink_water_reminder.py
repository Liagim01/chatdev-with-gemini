from datetime import datetime, timedelta
import schedule
from avoid_sitting_reminder import remind_avoid_sitting # Add this import statement
def remind_drink_water(app):
  '''
  This function reminds the user to drink water.
  '''
  # Get the current time.
  now = datetime.now()
  # Schedule a reminder to drink water for every 2 hours.
  schedule.every(2).hours.do(lambda: app.reminder_label.config(text="Drink some water!"))
