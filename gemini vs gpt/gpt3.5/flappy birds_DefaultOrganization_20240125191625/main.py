'''
This is the main file of the Flappy Bird game. It initializes the game and handles the game loop.
'''
import pygame
import sys
from bird import Bird
from pipe import Pipe
# Initialize the game
pygame.init()
# Set up the display
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()
# Set up the game objects
bird = Bird()
pipe = Pipe()
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
    bird.update()
    pipe.update()
    # Check for collisions
    if bird.collides_with(pipe):
        # Game over
        pygame.quit()
        sys.exit()
    # Draw the game objects
    screen.fill((0, 0, 0))
    bird.draw(screen)
    pipe.draw(screen)
    pygame.display.flip()
    clock.tick(60)