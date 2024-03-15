'''This is the class for the player.'''
import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Set the image and rect of the player
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)
    def update(self):
        # Handle the player's movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 50
        # Keep the player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT