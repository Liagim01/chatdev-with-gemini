import pygame
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 100
        self.speed = 5
    def move_up(self):
        if self.y > 0:
            self.y -= self.speed
    def move_down(self):
        if self.y < 400 - self.height:
            self.y += self.speed
    def update(self):
        pass
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))