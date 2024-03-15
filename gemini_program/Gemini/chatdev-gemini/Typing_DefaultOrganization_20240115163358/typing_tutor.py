
import tkinter as tk
from tkinter import * 
from tkinter.ttk import *

class TypingLessons:
    '''Typing lessons class.'''

    def __init__(self):
        '''Constructor.'''

        # Create the lessons.
        self.lessons = [
            "The quick brown fox jumps over the lazy dog.",
            "The five boxing wizards jump quickly.",
            "Pack my box with five dozen liquor jugs.",
            "The twelve blackbucks jumped over the quick zebra.",
            "The jay, pig, fox, zebra, and my wolves quack."
        ]

class TypingTutor:
    '''Typing tutor class.'''

    def __init__(self, root):
        '''Constructor.'''

        # Set the root window.
        self.root = root

        # Create the main frame.
        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        # Create the text area.
        self.text = tk.Text(self.main_frame, width=60, height=20)
        self.text.pack()

        # Create the lessons button.
        self.lessons_button = tk.Button(self.main_frame, text="Lessons", command=self.show_lessons)
        self.lessons_button.pack()

        # Create the start button.
        self.start_button = tk.Button(self.main_frame, text="Start", command=self.start_typing)
        self.start_button.pack()

        # Create the stop button.
        self.stop_button = tk.Button(self.main_frame, text="Stop", command=self.stop_typing)
        self.stop_button.pack()

        # Create the typing lessons.
        self.typing_lessons = TypingLessons()

        # Set the current lesson.
        self.current_lesson = 0

        # Set the typing speed.
        self.typing_speed = 0

        # Set the typing accuracy.
        self.typing_accuracy = 0

        # Set the typing time.
        self.typing_time = 0

        # Create the progress bar.
        self.progress_bar = Progressbar(self.main_frame, orient=tk.HORIZONTAL, length=200)
        self.progress_bar.pack()

        # Create the status bar.
        self.status_bar = tk.Label(self.main_frame, text="Ready")
        self.status_bar.pack()

    def show_lessons(self):
        '''Show the lessons.'''

        # Create the lessons window.
        lessons_window = tk.Toplevel(self.root)
        lessons_window.title("Lessons")

        # Create the lessons listbox.
        self.lessons_listbox = tk.Listbox(lessons_window)
        self.lessons_listbox.pack()

        # Insert the lessons into the listbox.
        for lesson in self.typing_lessons.lessons:
            self.lessons_listbox.insert(tk.END, lesson)

        # Create the select button.
        self.select_button = tk.Button(lessons_window, text="Select", command=self.select_lesson)
        self.select_button.pack()

    def select_lesson(self):
        '''Select the lesson.'''

        # Get the selected lesson.
        selected_lesson = self.lessons_listbox.get(tk.ACTIVE)

        # Set the current lesson.
        self.current_lesson = selected_lesson

        # Close the lessons window.
        self.lessons_window.destroy()

    def start_typing(self):
        '''Start typing.'''

        # Set the typing speed.
        self.typing_speed = 0

        # Set the typing accuracy.
        self.typing_accuracy = 0

        # Set the typing time.
        self.typing_time = 0

        # Set the progress bar.
        self.progress_bar.start()

        # Set the status bar.
        self.status_bar.config(text="Typing...")

        # Start the timer.
        self.timer_id = self.root.after(1000, self.update_timer)

    def stop_typing(self):
        '''Stop typing.'''

        # Stop the timer.
        self.root.after_cancel(self.timer_id)

        # Set the progress bar.
        self.progress_bar.stop()

        # Set the status bar.
        self.status_bar.config(text="Ready")

    def update_timer(self):
        '''Update the timer.'''

        # Increment the typing time.
        self.typing_time += 1

        # Update the progress bar.
        self.progress_bar['value'] = self.typing_time

        # Start the timer again.
        self.timer_id = self.root.after(1000, self.update_timer)