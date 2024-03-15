'''Main file for the virtual painting studio app.'''
import tkinter as tk
from canvas import Canvas
from color_palette import ColorPalette
from brush import Brush
class VirtualPaintingStudio:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Virtual Painting Studio")
        self.window.geometry("800x600")
        self.canvas = Canvas(self.window)
        self.canvas.pack(side=tk.LEFT)
        self.color_palette = ColorPalette(self.window)
        self.color_palette.pack(side=tk.RIGHT)
        self.brush = Brush(self.canvas)
        self.window.mainloop()
if __name__ == "__main__":
    VirtualPaintingStudio()