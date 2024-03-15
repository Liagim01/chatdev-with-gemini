'''
This file contains the Obstacle class representing the obstacles in the game.
'''
import pygame
import random
from constants import *
class Obstacle:
    def __init__(self, width, height, color, window_width):
        self.width = width
        self.height = height
        self.color = color
        self.x = window_width
        self.y = window_height - self.height
        self.velocity = OBSTACLE_VELOCITY
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self):
        self.x -= self.velocity
        self.rect.x = self.x
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)