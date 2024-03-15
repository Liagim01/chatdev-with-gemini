import tkinter as tk
from tkinter import Canvas, Frame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Virtual Painting Studio")
        self.geometry("800x600")

        self.canvas = Canvas(self)
        self.canvas.pack(expand=True, fill="both")

        self.toolbar = Toolbar(self)
        self.toolbar.pack(side="left", fill="y")

class Canvas(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, bg="white")

        self.brush_size = 5
        self.brush_color = "black"

        self.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        self.create_oval(event.x - self.brush_size // 2,
        event.y - self.brush_size // 2,
        event.x + self.brush_size // 2,
        event.y + self.brush_size // 2,
        fill=self.brush_color)

class Toolbar(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.brush_size_label = tk.Label(self, text="Brush Size")
        self.brush_size_label.pack()

        self.brush_size_slider = tk.Scale(self, from_=1, to=20, orient="horizontal")
        self.brush_size_slider.set(5)
        self.brush_size_slider.pack()

        self.brush_color_label = tk.Label(self, text="Brush Color")
        self.brush_color_label.pack()

        self.brush_color_button = tk.Button(self, text="Choose Color", command=self.choose_color)
        self.brush_color_button.pack()

    def get_brush_size(self):
        return self.brush_size_slider.get()

    def get_brush_color(self):
        return self.brush_color

    def choose_color(self):
        color = tk.colorchooser.askcolor()[1]
        self.brush_color = color

if __name__ == "__main__":
    app = App()
    app.mainloop()