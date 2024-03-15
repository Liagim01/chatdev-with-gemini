'''
This is the main file for the Virtual Painting Studio app. It sets up the GUI and handles user interactions.
It includes functionality for choosing brush size, color, and an undo feature for better user experience.
'''
import tkinter as tk
from tkinter import colorchooser, Canvas
class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Virtual Painting Studio')
        self.color = 'black'
        self.brush_size = 2
        self.last_x, self.last_y = None, None
        self.undo_stack = []
        self.initUI()
    def initUI(self):
        self.canvas = CanvasArea(self.root, self)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.setupMenu()
    def setupMenu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        brush_menu = tk.Menu(menu)
        color_menu = tk.Menu(menu)
        edit_menu = tk.Menu(menu)
        menu.add_cascade(label='Brush Size', menu=brush_menu)
        menu.add_cascade(label='Colors', menu=color_menu)
        menu.add_cascade(label='Edit', menu=edit_menu)
        brush_menu.add_command(label='2px', command=lambda: self.selectBrushSize(2))
        brush_menu.add_command(label='5px', command=lambda: self.selectBrushSize(5))
        color_menu.add_command(label='Choose Color', command=self.selectColor)
        color_menu.add_command(label='Reset Canvas', command=self.resetCanvas)
        edit_menu.add_command(label='Undo', command=self.undo)
    def selectColor(self):
        color = colorchooser.askcolor(color=self.color)[1]
        if color:
            self.color = color
    def selectBrushSize(self, size):
        self.brush_size = size
    def resetCanvas(self):
        self.canvas.clear()
        self.undo_stack = []
    def startDrawing(self, event):
        self.last_x, self.last_y = event.x, event.y
    def draw(self, event):
        if self.last_x and self.last_y:
            line_id = self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                              width=self.brush_size, fill=self.color,
                                              capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
            self.undo_stack.append(line_id)
        self.last_x, self.last_y = event.x, event.y
    def undo(self):
        if self.undo_stack:
            line_id = self.undo_stack.pop()
            self.canvas.delete(line_id)
class CanvasArea(tk.Canvas):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.bind('<Button-1>', self.app.startDrawing)
        self.bind('<B1-Motion>', self.app.draw)
        self.config(bg='white', width=600, height=400)
    def clear(self):
        self.delete('all')
if __name__ == '__main__':
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()