'''Brush class for the virtual painting studio app.'''
class Brush:
    def __init__(self, canvas):
        self.canvas = canvas
        self.color = "black"
        self.size = 1
    def set_color(self, color):
        self.color = color
    def set_size(self, size):
        self.size = size