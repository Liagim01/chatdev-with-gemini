from datetime import datetime, time
import schedule
import conversation_topics # Add this import statement
def remind_leave_work(app):
  '''
  This function reminds the user to leave work at 9 PM.
  '''
  # Get the current time.
  now = datetime.now()
  # Check if it is 9 PM.
  if now.time() == time(21, 0):
    # Get conversation topics.
    conversation_topics = get_conversation_topics()
    # Set the reminder label.
    app.reminder_label.config(text="Leave work now! Here are some conversation topics for tomorrow: {}".format(', '.join(conversation_topics)))