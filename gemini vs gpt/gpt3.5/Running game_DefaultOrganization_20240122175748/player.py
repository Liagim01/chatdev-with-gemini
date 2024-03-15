'''
This file contains the Player class representing the main character.
'''
import pygame
from constants import *
class Player:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.x = 100
        self.y = window_height - self.height
        self.velocity = 0
        self.gravity = GRAVITY
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        if self.y > window_height - self.height:
            self.y = window_height - self.height
            self.velocity = 0
        self.rect.y = self.y
    def jump(self):
        if self.y == window_height - self.height:
            self.velocity -= JUMP_VELOCITY
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
    def reset(self):
        self.y = window_height - self.height
        self.velocity = 0
        self.rect.y = self.y