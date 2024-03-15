'''
This file contains the Game class that manages the game logic and rendering.
'''
import pygame
from player import Player
from enemy import Enemy
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.enemies = [Enemy(100, 100), Enemy(200, 100), Enemy(300, 100)]  # Example enemy positions
    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.update()
            self.draw()
            pygame.display.flip()
            clock.tick(60)
    def update(self):
        # Update game objects
        self.player.update()
        for enemy in self.enemies:
            enemy.update(1)  # Example speed
    def draw(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))
        # Draw game objects
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)