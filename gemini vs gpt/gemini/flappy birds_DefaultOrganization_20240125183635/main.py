'''This is the main file for the Flappy Bird game.'''
import pygame
import sys
import random
# Initialize the game engine
pygame.init()
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)zz
# Set the height and width of the screen
size = [500, 700]
screen = pygame.display.set_mode(size)
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
# Speed in pixels per second
x_speed = 5
y_speed = 5
# Current position
x_coord = 100
y_coord = 50
# Create a surface for the bird
bird = pygame.Surface((20, 20))
bird.fill(BLUE)
# Create a surface for the pipe
pipe = pygame.Surface((50, 500))
pipe.fill(GREEN)
# Create a surface for the ground
ground = pygame.Surface((500, 100))
ground.fill(RED)
# Put the bird on the screen
screen.blit(bird, (x_coord, y_coord))
# Put the pipe on the screen
screen.blit(pipe, (400, 100))
# Put the ground on the screen
screen.blit(ground, (0, 600))
# Flip the display
pygame.display.flip()
# -------- Main Program Loop -----------
while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    # Move the bird
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    # Move the pipe
    pipe_x = pipe_x - 5
    # If the bird hits the pipe, stop the game
    if bird.colliderect(pipe):
        done = True
    # If the bird hits the ground, stop the game
    if bird.colliderect(ground):
        done = True
    # Put the bird on the screen
    screen.blit(bird, (x_coord, y_coord))
    # Put the pipe on the screen
    screen.blit(pipe, (pipe_x, 100))
    # Put the ground on the screen
    screen.blit(ground, (0, 600))
    # Flip the display
    pygame.display.flip()
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()