'''Canvas class for the virtual painting studio app.'''
import tkinter as tk
class Canvas(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.bind("<B1-Motion>", self.draw)
    def draw(self, event):
        self.create_line(event.x, event.y, event.x+1, event.y+1, fill=self.brush.color, width=self.brush.size)