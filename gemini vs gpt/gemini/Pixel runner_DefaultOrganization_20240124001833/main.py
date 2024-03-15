import pygame
import sys
from player import Player
from level import Level
def main():
    pygame.init()
    # Set up the screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Retro Runner")
    # Create the player
    player = Player()
    # Create the level
    level = Level()
    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Update the game state
        player.update()
        level.update()
        # Draw the game state
        screen.fill((0, 0, 0))
        level.draw(screen)
        player.draw(screen)
        # Flip the display
        pygame.display.flip()
if __name__ == "__main__":
    main()