'''
This file defines the Pipe class.
'''
import pygame
import random
class Pipe:
    def __init__(self):
        self.x = 400
        self.y = random.randint(200, 400)
        self.width = 80
        self.height = 400
        self.speed = 5
    def update(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.x = 400
            self.y = random.randint(200, 400)
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))