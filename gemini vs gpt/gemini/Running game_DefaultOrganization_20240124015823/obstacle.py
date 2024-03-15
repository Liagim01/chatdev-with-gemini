'''This is the class for the obstacles.'''
import pygame
import random
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Set the image and rect of the obstacle
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
    def update(self):
        # Move the obstacle down the screen
        self.rect.y += 5
        # If the obstacle goes off the screen, reset its position
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)