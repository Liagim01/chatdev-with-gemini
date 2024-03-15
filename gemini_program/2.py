import tkinter as tk
from PIL import Image, ImageDraw

class ArtCanvas(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        # Create a canvas for drawing
        self.canvas = tk.Canvas(self, width=500, height=500, bg="white")
        self.canvas.pack(side=tk.LEFT)

        # Create a toolbar for selecting brush size and color
        self.toolbar = tk.Frame(self)
        self.toolbar.pack(side=tk.RIGHT)

        # Add a label for brush size
        self.brush_size_label = tk.Label(self.toolbar, text="Brush Size")

        self.brush_size_label.pack()

        # Add a slider for selecting brush size
        self.brush_size_slider = tk.Scale(self.toolbar, from_=1, to=10, orient=tk.HORIZONTAL)
        self.brush_size_slider.pack()

        # Add a label for color selection
        self.color_label = tk.Label(self.toolbar, text="Color")
        self.color_label.pack()

        # Add a color picker for selecting color
        self.color_picker = tk.ColorChooser(self.toolbar)
        self.color_picker.pack()

        # Add a button for saving the artwork
        self.save_button= tk.Button(self.toolbar, text="Save", command=self.save_artwork)
        self.save_button.pack()

        # Add a button for loading the artwork
        self.load_button = tk.Button(self.toolbar, text="Load", command=self.load_artwork)
        self.load_button.pack()

    def bind_events(self):
        # Bind the mouse motion event to the canvas
        self.canvas.bind("<Motion>", self.on_mouse_motion)

    def on_mouse_motion(self, event):
        # Get the current brush size and color
        brush_size = self.brush_size_slider.get()
        color = self.color_picker.get()

        # Create an ImageDraw object for drawing on the canvas
        draw = ImageDraw.Draw(self.canvas.image)


      # Draw a circle at the current mouse position
        draw.ellipse((event.x - brush_size / 2, event.y - brush_size / 2, event.x + brush_size / 2, event.y + brush_size / 2), fill=color)       

        # Update the canvas with the new drawing
        self.canvas.update()

    def save_artwork(self):
        # Get the current canvas image
        image = self.canvas.image

        # Save the image to a file
        image.save("artwork.png")

    def load_artwork(self):
        # Load the image from a file
        image = Image.open("artwork.png")


# Update the canvas with the new image
        self.canvas.image = image
        self.canvas.update()

if __name__ == "__main__":
    root = tk.Tk()
    art_canvas = ArtCanvas(root)
    art_canvas.pack()
    root.mainloop()