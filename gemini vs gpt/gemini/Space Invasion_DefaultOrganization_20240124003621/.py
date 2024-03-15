import pygame
import sys
import random
# Initialize Pygame
pygame.init()
# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')
# Set up the player
player = pygame.sprite.Sprite()
player.image = pygame.Surface((50, 50))
player.image.fill((255, 0, 0))
player.rect = player.image.get_rect()
player.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
# Set up the aliens
aliens = pygame.sprite.Group()
for i in range(10):
    alien = pygame.sprite.Sprite()
    alien.image = pygame.Surface((50, 50))
    alien.image.fill((0, 255, 0))
    alien.rect = alien.image.get_rect()
    alien.rect.x = random.randint(0, SCREEN_WIDTH - 50)
    alien.rect.y = random.randint(0, SCREEN_HEIGHT / 2)
    aliens.add(alien)
# Set up the bullets
bullets = pygame.sprite.Group()
# Set up the score
score = 0
# Set up the clock
clock = pygame.time.Clock()
# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= 5
            elif event.key == pygame.K_RIGHT:
                player.rect.x += 5
            elif event.key == pygame.K_SPACE:
                bullet = pygame.sprite.Sprite()
                bullet.image = pygame.Surface((10, 10))
                bullet.image.fill((255, 255, 0))
                bullet.rect = bullet.image.get_rect()
                bullet.rect.center = player.rect.center
                bullets.add(bullet)
    # Update the game state
    player.update()
    aliens.update()
    bullets.update()
    # Check for collisions
    for bullet in bullets:
        for alien in aliens:
            if bullet.rect.colliderect(alien.rect):
                alien.kill()
                bullet.kill()
                score += 1
    # Check for game over
    if len(aliens) == 0:
        running = False
    # Draw the game state
    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    aliens.draw(screen)
    bullets.draw(screen)
    # Display the score
    font = pygame.font.SysFont('Arial', 30)
    text = font.render('Score: {}'.format(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    # Update the display
    pygame.display.update()
    # Limit the frame rate
    clock.tick(60)
# Quit Pygame
pygame.quit()
sys.exit()