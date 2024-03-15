# main.py
import pygame
import sys
import random
from game import Game
def main():
    """
    The main function of the game.
    """
    # Initialize pygame
    pygame.init()
    # Set the screen size
    screen_width = 400
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Set the game title
    pygame.display.set_caption("Coin Catcher")
    # Create a new game object
    game = Game(screen)
    # Start the game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_container_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_container_right()
        # Update the game state
        game.update()
        # Draw the game screen
        game.draw()
        # Flip the display
        pygame.display.flip()
    # Quit pygame
    pygame.quit()
if __name__ == "__main__":
    main()