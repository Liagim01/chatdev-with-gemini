'''Color palette class for the virtual painting studio app.'''
import tkinter as tk
from canvas import Canvas
from brush import Brush
class ColorPalette(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        for color in self.colors:
            button = tk.Button(self, text=color, bg=color, command=lambda c=color: self.set_color(c))
            button.pack(side=tk.LEFT)
        self.window = tk.Tk()
        self.window.title("Virtual Painting Studio")
        self.window.geometry("800x600")
        self.canvas = Canvas(self.window)
        self.canvas.pack(side=tk.LEFT)
        self.brush = Brush(self.canvas)
    def set_color(self, color):
        self.brush.color = color
