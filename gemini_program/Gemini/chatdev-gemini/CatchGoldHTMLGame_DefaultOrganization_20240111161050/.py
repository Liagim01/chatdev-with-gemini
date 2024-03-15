# Filename: coin_catcher.py
# Language: Python
'''
This is a simple coin catcher game developed using Pygame.
The objective of the game is to catch as many coins as possible before the timer runs out.
The player controls a container at the bottom of the screen and must move it left and right to catch the falling coins.
The coins are worth different amounts of points, and the player's score is displayed at the top of the screen.
The game ends when the timer reaches 0, and the player's final score is displayed.
'''
import pygame
import random
import sys
# Initialize Pygame
pygame.init()
# Set the screen size
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the title of the game
pygame.display.set_caption("Coin Catcher")
# Create the player
player = pygame.sprite.Sprite()
player.image = pygame.Surface((50, 50))
player.image.fill((0, 255, 0))
player.rect = player.image.get_rect()
player.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
# Create the coins
coins = pygame.sprite.Group()
for i in range(10):
    coin = pygame.sprite.Sprite()
    coin.image = pygame.Surface((20, 20))
    coin.image.fill((255, 255, 0))
    coin.rect = coin.image.get_rect()
    coin.rect.x = random.randint(0, SCREEN_WIDTH - coin.rect.width)
    coin.rect.y = random.randint(0, SCREEN_HEIGHT - coin.rect.height)
    coins.add(coin)
# Create the score
score = 0
# Create the timer
timer = 15
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= 5
            elif event.key == pygame.K_RIGHT:
                player.rect.x += 5
    # Update the game state
    coins.update()
    timer -= 1
    # Check for collisions between the player and the coins
    for coin in coins:
        if player.rect.colliderect(coin.rect):
            score += coin.value
            coin.kill()
    # Check if the timer has run out
    if timer <= 0:
        running = False
    # Draw the game state
    screen.fill((0, 0, 0))
    coins.draw(screen)
    player.draw(screen)
    pygame.display.flip()
# Display the final score
print("Your score is:", score)
# Quit Pygame
pygame.quit()
sys.exit()