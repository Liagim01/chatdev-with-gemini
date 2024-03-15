'''
This file contains the TypingTutor class, which provides real-time feedback on typing accuracy and speed.
'''
import time
class TypingTutor:
    def __init__(self, interface):
        self.interface = interface
        self.start_time = None
        self.end_time = None
    def get_exercise_text(self):
        # This method should return a string that the user will type.
        # For simplicity, we're returning a static string.
        # In a real application, this would probably pull from a database of exercises.
        return "The quick brown fox jumps over the lazy dog."
    def start_timing(self):
        # Start the timer for the typing exercise
        self.start_time = time.time()
    def end_timing(self):
        # End the timer for the typing exercise
        self.end_time = time.time()
    def calculate_speed(self, typed_text):
        # Calculate typing speed in words per minute (WPM)
        elapsed_time = self.end_time - self.start_time
        words_typed = len(typed_text.split())
        # Calculate words per minute
        speed = (words_typed / elapsed_time) * 60
        return speed
    def calculate_accuracy(self, typed_text, target_text):
        # Calculate typing accuracy as a percentage
        typed_words = typed_text.split()
        target_words = target_text.split()
        correct_words = sum(t_word == typed_word for t_word, typed_word in zip(target_words, typed_words))
        accuracy = (correct_words / len(target_words)) * 100
        return accuracy
    def evaluate_typing(self, typed_text, target_text):
        # Evaluate the typing accuracy and speed
        self.end_timing()
        speed = self.calculate_speed(typed_text)
        accuracy = self.calculate_accuracy(typed_text, target_text)
        return accuracy, speed
    def display_feedback(self, accuracy, speed):
        # Display real-time typing feedback to the user
        feedback_message = f"Accuracy: {accuracy:.2f}% | Speed: {speed:.2f} WPM"
        self.interface.display_feedback(feedback_message)