'''
This file contains the TypingInterface class, which is responsible for the user interface of the typing practice software.
'''
import tkinter as tk
from tkinter import messagebox
from typing_tutor import TypingTutor
from user_progress import UserProgress
from settings_manager import SettingsManager
from statistics import StatisticsViewer
from datetime import datetime
class TypingInterface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("ChatDev Typing Practice")
        self.pack(fill="both", expand=True)
        self.create_widgets()
        self.typing_tutor = TypingTutor(self)
        self.user_progress = UserProgress()
        self.settings_manager = SettingsManager()
        self.statistics_viewer = StatisticsViewer()
    def create_widgets(self):
        # Add buttons, text fields, and other UI elements here
        self.start_button = tk.Button(self, text="Start Exercise", command=self.start_exercise)
        self.start_button.pack(side="top")
        self.stats_button = tk.Button(self, text="Show Statistics", command=self.show_statistics)
        self.stats_button.pack(side="top")
        self.settings_button = tk.Button(self, text="Settings", command=self.update_settings)
        self.settings_button.pack(side="top")
        self.text_display = tk.Text(self, height=10, width=50)
        self.text_display.pack(side="top")
        self.entry = tk.Entry(self)
        self.entry.pack(side="top", fill="x", expand=True)
        self.entry.bind("<Return>", self.record_progress)
    def start_exercise(self):
        # Start a typing exercise
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, self.typing_tutor.get_exercise_text())
        self.entry.focus_set()
        self.typing_tutor.start_timing()  # Start the timer
    def show_statistics(self):
        # Display user typing statistics
        self.statistics_viewer.display_statistics()
    def update_settings(self):
        # Update typing exercise settings
        # This is a placeholder for settings update functionality
        messagebox.showinfo("Settings", "Settings would be implemented here.")
    def record_progress(self, event):
        # Record the user's progress
        typed_text = self.entry.get()
        target_text = self.text_display.get(1.0, tk.END).strip()
        accuracy, speed = self.typing_tutor.evaluate_typing(typed_text, target_text)
        if accuracy is not None and speed is not None:
            current_timestamp = datetime.now().isoformat()  # Get the current timestamp in ISO format
            self.user_progress.update_progress(accuracy, speed, current_timestamp)
            self.statistics_viewer.update_statistics(accuracy, speed, current_timestamp)
            self.entry.delete(0, tk.END)
            self.start_exercise()  # Restart the exercise for continuous practice
    def display_feedback(self, message):
        # Display a feedback message to the user
        messagebox.showinfo("Feedback", message)