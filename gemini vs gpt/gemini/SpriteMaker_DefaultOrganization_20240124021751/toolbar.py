'''This is the file for the toolbar widget.'''
import tkinter as tk
class Toolbar(tk.Frame):
    def __init__(self, master, canvas):
        super().__init__(master)
        self.canvas = canvas
        self.color_button = tk.Button(self, text="Color", command=self.choose_color)
        self.size_button = tk.Button(self, text="Size", command=self.choose_size)
        self.color_button.pack(side=tk.LEFT)
        self.size_button.pack(side=tk.LEFT)
    def choose_color(self):
        color = tk.colorchooser.askcolor()[1]
        self.canvas.color = color
    def choose_size(self):
        size = tk.simpledialog.askinteger("Size", "Enter the size of the brush:")
        self.canvas.size = size