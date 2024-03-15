import schedule
from datetime import datetime, timedelta
def remind_avoid_sitting(app):
  '''
  This function reminds the user to avoid prolonged sitting.
  '''
  # Get the current time.
  now = datetime.now()
  # Schedule a reminder to avoid sitting for every 30 minutes.
  schedule.every(30).minutes.do(lambda: app.reminder_label.config(text="Get up and move around!"))
  # Schedule a reminder to avoid sitting for every 60 minutes.
  schedule.every(60).minutes.do(lambda: app.reminder_label.config(text="Take a break from sitting!"))