'''
This file contains the UserProgress class, which tracks and records the user's performance over time.
'''
import json
import os
class UserProgress:
    def __init__(self):
        self.progress_data = {
            'accuracy': [],
            'speed': [],
            'timestamps': []
        }
        self.progress_file = 'user_progress.json'
        self.load_progress()
    def update_progress(self, accuracy, speed, timestamp):
        # Update the user's progress with the latest accuracy and speed
        self.progress_data['accuracy'].append(accuracy)
        self.progress_data['speed'].append(speed)
        self.progress_data['timestamps'].append(timestamp)
        self.save_progress()
    def get_progress(self):
        # Return the user's progress data
        return self.progress_data
    def save_progress(self):
        # Save the progress data to a file
        with open(self.progress_file, 'w') as file:
            json.dump(self.progress_data, file, indent=4)
    def load_progress(self):
        # Load the progress data from a file
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as file:
                self.progress_data = json.load(file)
        else:
            self.save_progress()  # Create the file if it doesn't exist
    def clear_progress(self):
        # Clear all progress data
        self.progress_data = {
            'accuracy': [],
            'speed': [],
            'timestamps': []
        }
        self.save_progress()