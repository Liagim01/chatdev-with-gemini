import keyboard
import time
class TypingTutor:
  def __init__(self, progress_tracker):
    self.current_sentence = ""
    self.errors = 0
    self.total_chars = 0
    self.progress_tracker = progress_tracker
    self.start_time = 0
  def start_tutor(self):
    self.current_sentence = "The quick brown fox jumps over the lazy dog."
    self.total_chars = len(self.current_sentence)
    self.start_time = time.time()
    keyboard.hook(self.check_typing)
  def check_typing(self, key):
    if key.name == "enter":
      self.calculate_accuracy()
      self.calculate_speed()
      self.progress_tracker.record_performance(self.accuracy, self.speed)
      keyboard.unhook_all()
    elif key.name == "backspace":
      if self.errors > 0:
        self.errors -= 1
    elif key.name == "space":
      self.total_chars += 1
    else:
      if key.name != self.current_sentence[self.errors]:
        self.errors += 1
      self.total_chars += 1
  def calculate_accuracy(self):
    self.accuracy = ((self.total_chars - self.errors) / self.total_chars) * 100
  def calculate_speed(self):
    elapsed_time = time.time() - self.start_time
    self.speed = self.total_chars / elapsed_time