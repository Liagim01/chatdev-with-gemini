import pygame
class Level:
    def __init__(self):
        self.platforms = []
        self.obstacles = []
    def update(self):
        # Update the platforms
        for platform in self.platforms:
            platform.update()
        # Update the obstacles
        for obstacle in self.obstacles:
            obstacle.update()
    def draw(self, screen):
        # Draw the platforms
        for platform in self.platforms:
            platform.draw(screen)
        # Draw the obstacles
        for obstacle in self.obstacles:
            obstacle.draw(screen)