'''
This file contains the Raindrop class which represents a raindrop falling down the screen.
'''
class Raindrop:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = self.canvas.create_image(0, 0, anchor='nw')
    def fall(self):
        # Implement the logic for the raindrop falling down the screen
        x, y = self.canvas.coords(self.image)
        self.canvas.coords(self.image, x, y + 1)
    def is_under_umbrella(self, umbrella):
        # Implement the logic to check if the raindrop is under the umbrella
        umbrella_coords = self.canvas.coords(umbrella.image)
        raindrop_coords = self.canvas.coords(self.image)
        umbrella_x1, umbrella_y1, umbrella_x2, umbrella_y2 = umbrella_coords
        raindrop_x1, raindrop_y1, raindrop_x2, raindrop_y2 = raindrop_coords
        return (raindrop_x1 >= umbrella_x1 and raindrop_x2 <= umbrella_x2 and
                raindrop_y1 >= umbrella_y1 and raindrop_y2 <= umbrella_y2)
    def stop(self):
        # Implement the logic to stop the raindrop from falling
        self.canvas.delete(self.image)