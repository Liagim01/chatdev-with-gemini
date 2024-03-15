'''
This file contains the Piece class which represents a Tetris piece.
'''
import random
from builtins import reversed
class Piece:
    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y
    def rotate(self):
        return list(zip(*reversed(self.shape)))