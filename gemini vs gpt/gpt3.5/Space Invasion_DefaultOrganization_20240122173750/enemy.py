'''
This file contains the Enemy class that represents the enemy characters.
'''
import pygame
class Enemy:
    def __init__(self, x, y):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
    def update(self, speed):
        self.y += speed
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))