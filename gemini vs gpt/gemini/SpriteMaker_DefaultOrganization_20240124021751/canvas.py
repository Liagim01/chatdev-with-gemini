'''This is the file for the canvas widget.'''
import tkinter as tk
class Canvas(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.bind("<B1-Motion>", self.draw)
        self.bind("<Button-1>", self.start_draw)
        self.bind("<ButtonRelease-1>", self.end_draw)
        self.color = "black"
        self.size = 1
        self.drawing = False
    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            self.create_rectangle(x, y, x + self.size, y + self.size, fill=self.color)
    def start_draw(self, event):
        self.drawing = True
    def end_draw(self, event):
        self.drawing = False