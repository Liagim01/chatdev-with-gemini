'''
This is the main file that initializes the game and runs the game loop.
'''
import pygame
from game import Game
# Initialize Pygame
pygame.init()
# Create the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
# Create an instance of the Game class
game = Game(screen)
# Start the game loop
game.run()
# Quit Pygame
pygame.quit()