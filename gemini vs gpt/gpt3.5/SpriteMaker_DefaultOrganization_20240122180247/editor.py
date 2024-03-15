'''
This is the editor module for the pixel art editor application.
'''
import tkinter as tk
class Editor:
    def __init__(self, root):
        self.root = root
        self.current_color = "black"
        self.create_gui()
    def create_gui(self):
        # Create a frame to hold the GUI elements
        frame = tk.Frame(self.root)
        frame.pack()
        # Create a color palette with buttons for selecting colors
        colors = ["black", "white", "red", "green", "blue"]  # Add more colors as needed
        for color in colors:
            button = tk.Button(frame, bg=color, width=2, command=lambda c=color: self.set_color(c))
            button.pack(side=tk.LEFT)
        # Create a canvas for drawing
        canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        canvas.pack()
        # Add more GUI elements for coloring, shading, and animation frames as required
        # Set the initial color
        self.set_color("black")
    def set_color(self, color):
        self.current_color = color
    # Add more methods for coloring, shading, and animation frames