'''
This file contains the Umbrella class which represents the umbrella controlled by the mouse cursor.
'''
class Umbrella:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = self.canvas.create_image(0, 0, anchor='nw')
        self.canvas.bind('<Motion>', self.move)
    def move(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.image, x, y)