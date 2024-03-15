'''This module contains the BriefNote class.'''
import tkinter as tk
class BriefNote(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Create the brief note label
        self.brief_note_label = tk.Label(self, text="Brief Note")
        self.brief_note_label.pack()
        # Create the brief note text box
        self.brief_note_text_box = tk.Text(self)
        self.brief_note_text_box.pack()
        # Create the save brief note button
        self.save_brief_note_button = tk.Button(self, text="Save Brief Note")
        self.save_brief_note_button.pack()