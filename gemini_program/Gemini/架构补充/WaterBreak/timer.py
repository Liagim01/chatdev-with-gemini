import tkinter as tk
from datetime import datetime, date
class CountdownTimer:
  def __init__(self, schedule):
    self.schedule = schedule
    self.current_index = 0
    self.remaining_time = 0
    self.timer_label = None
  def start(self):
    self.update_timer()
  def update_timer(self):
    if self.current_index >= len(self.schedule):
      self.timer_label.config(text="All breaks completed!")
      return
    self.remaining_time = self.schedule[self.current_index] - datetime.now()
    self.timer_label.config(text="Next break in: " + str(self.remaining_time))
    self.timer_label.after(1000, self.update_timer)
  def set_timer_label(self, timer_label):
    self.timer_label = timer_label