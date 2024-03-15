import pygame
import random
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
        self.radius = 10
    def update(self, paddle1, paddle2):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y < 0 or self.y > 400:
            self.speed_y *= -1
        if self.x < 0:
            self.speed_x *= -1
        if self.x > 800:
            self.speed_x *= -1
        if self.x > paddle1.x and self.x < paddle1.x + paddle1.width and self.y > paddle1.y and self.y < paddle1.y + paddle1.height:
            self.speed_x *= -1
        if self.x > paddle2.x and self.x < paddle2.x + paddle2.width and self.y > paddle2.y and self.y < paddle2.y + paddle2.height:
            self.speed_x *= -1
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
    def reset(self):
        self.x = 400
        self.y = 200
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)