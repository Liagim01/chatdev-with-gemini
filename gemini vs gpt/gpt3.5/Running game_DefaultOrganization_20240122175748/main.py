'''
This is the main file that handles the game loop.
'''
import pygame
from game import Game
# Initialize pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Running Game")
# Create a game instance
game = Game(window)
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.player.jump()
    # Update game state
    game.update()
    # Draw game objects
    game.draw()
    # Update the display
    pygame.display.update()
# Quit the game
pygame.quit()