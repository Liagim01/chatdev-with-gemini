import pygame
class Player:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.width = 50
        self.height = 50
        self.speed = 5
        self.is_jumping = False
        self.is_sliding = False
    def update(self):
        # Handle keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
        if keys[pygame.K_DOWN] and not self.is_sliding:
            self.is_sliding = True
        # Update the player's position
        if self.is_jumping:
            self.y -= self.speed
            if self.y <= 0:
                self.is_jumping = False
                self.y = 0
        elif self.is_sliding:
            self.y += self.speed
            if self.y >= 600 - self.height:
                self.is_sliding = False
                self.y = 600 - self.height
        else:
            self.y += self.speed
            if self.y >= 600 - self.height:
                self.y = 600 - self.height
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))