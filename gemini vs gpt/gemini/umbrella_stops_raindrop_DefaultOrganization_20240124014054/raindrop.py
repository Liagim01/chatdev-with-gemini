'''This class represents a single raindrop.'''
import pygame
import random
class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class constructor
        super().__init__()
        # Set the raindrop's image
        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 0, 255))
        # Set the raindrop's position
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 600)
        # Set the raindrop's speed
        self.speed_x = 0
        self.speed_y = 5
    def update(self):
        # Move the raindrop
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # If the raindrop moves off the screen, reset its position
        if self.rect.y > 600:
            self.rect.x = random.randint(0, 800)
            self.rect.y = 0