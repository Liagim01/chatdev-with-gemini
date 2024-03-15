'''This is the main file for the running game.'''
import pygame
import sys
import random
# Initialize pygame
pygame.init()
# Set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the title of the game
pygame.display.set_caption("Running Game")
# Create the player
player = pygame.sprite.Sprite()
player.image = pygame.Surface((20, 20))
player.image.fill((255, 0, 0))
player.rect = player.image.get_rect()
player.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)
# Create the obstacles
obstacles = pygame.sprite.Group()
# Create the score counter
score = 0
score_font = pygame.font.SysFont("Arial", 30)
# Create the game over panel
game_over_panel = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
game_over_panel.fill((0, 0, 0))
game_over_text = score_font.render("Game Over", True, (255, 255, 255))
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
# Set the game state
game_state = "running"
# The main game loop
while game_state == "running":
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.rect.y -= 50
    # Update the player
    player.update()
    # Update the obstacles
    obstacles.update()
    # Check for collisions between the player and the obstacles
    if pygame.sprite.spritecollideany(player, obstacles):
        game_state = "game_over"
    # Draw the screen
    screen.fill((255, 255, 255))
    screen.blit(player.image, player.rect)
    screen.blit(obstacles, obstacles.rect)
    # Draw the score
    score_text = score_font.render("Score: " + str(score), True, (0, 0, 0))
    score_text_rect = score_text.get_rect()
    score_text_rect.topleft = (10, 10)
    screen.blit(score_text, score_text_rect)
    # If the game is over, draw the game over panel
    if game_state == "game_over":
        screen.blit(game_over_panel, (0, 0))
        screen.blit(game_over_text, game_over_text_rect)
    # Update the display
    pygame.display.update()
# Quit pygame
pygame.quit()