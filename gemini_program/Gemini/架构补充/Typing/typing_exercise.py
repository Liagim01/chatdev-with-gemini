import random
import time
class TypingExercise:
  def __init__(self, progress_tracker):
    self.exercises = [
      "The quick brown fox jumps over the lazy dog.",
      "Programming is fun and challenging.",
      "Practice makes perfect.",
      "Typing speed matters in the digital world.",
      "I love coding in Python."
    ]
    self.progress_tracker = progress_tracker
  def start_exercise(self):
    exercise = random.choice(self.exercises)
    print("Exercise: ", exercise)
    user_input = input("Type the sentence: ")
    accuracy = self.calculate_accuracy(exercise, user_input)
    elapsed_time = time.time() - self.start_time
    speed = self.calculate_speed(user_input, elapsed_time)
    self.progress_tracker.record_performance(accuracy, speed)
  def calculate_accuracy(self, exercise, user_input):
    correct_chars = 0
    for i in range(len(exercise)):
      if exercise[i] == user_input[i]:
        correct_chars += 1
    accuracy = (correct_chars / len(exercise)) * 100
    return accuracy
  def calculate_speed(self, user_input, elapsed_time):
    speed = len(user_input) / elapsed_time
    return speed