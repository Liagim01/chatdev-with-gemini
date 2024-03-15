'''
This file defines the Bird class.
'''
import pygame
class Bird:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.velocity = 0
        self.gravity = 0.5
    def jump(self):
        self.velocity = -10
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), 20)
    def collides_with(self, pipe):
        bird_rect = pygame.Rect(self.x - 20, self.y - 20, 40, 40)
        pipe_rect = pygame.Rect(pipe.x, pipe.y, pipe.width, pipe.height)
        return bird_rect.colliderect(pipe_rect)