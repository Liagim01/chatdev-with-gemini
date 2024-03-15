import datetime
from playsound import playsound
import random

# Initialize the app
running = True
while running:
    # Get the current time
    now = datetime.datetime.now()

    # Check if it's time for a hydration reminder
    if now.minute % 60 == 0:
        playsound('water.mp3')  # Play a sound to remind the user to drink water

    # Check if it's time for a break reminder
    if now.hour % 2 == 0 and now.minute == 0:
        playsound('break.mp3')  # Play a sound to remind the user to take a break

    # Check if it's time for a conversation topic suggestion
    if now.hour % 4 == 0 and now.minute == 0:
        topics = ['How was your day?', 'What are your favorite hobbies?', 'What's the most interesting thing you've learned recently?']
        topic = random.choice(topics)
        print(f"Conversation topic: {topic}")  # Print a conversation topic suggestion

    # Check for user input
    command = input()
    if command =='quit':
        running = False

# Print a goodbye message
print("Goodbye!")