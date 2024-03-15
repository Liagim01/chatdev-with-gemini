'''
This file contains the Player class that represents the player character.
'''
import pygame
class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 375
        self.y = 500
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))