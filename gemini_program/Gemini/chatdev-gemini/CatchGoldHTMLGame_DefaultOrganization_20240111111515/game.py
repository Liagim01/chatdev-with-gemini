# game.py
import pygame
import random
class Game:
    """
    The main game class.
    """
    def __init__(self, screen):
        """
        Initialize the game.
        Args:
            screen: The pygame screen object.
        """
        # Set the screen
        self.screen = screen
        # Set the game state
        self.game_over = False
        self.score = 0
        self.time_left = 15
        # Create the container
        self.container = pygame.Rect(screen_width / 2 - 50, screen_height - 50, 100, 20)
        # Create the coins
        self.coins = []
        for i in range(10):
            coin_type = random.choice([1, 10, 100])
            coin = pygame.Rect(random.randint(0, screen_width - 20), 0, 20, 20)
            coin.value = coin_type
            self.coins.append(coin)
        # Set the font
        self.font = pygame.font.SysFont("Arial", 20)
    def update(self):
        """
        Update the game state.
        """
        # Update the time left
        self.time_left -= 1
        # Check if the game is over
        if self.time_left <= 0:
            self.game_over = True
        # Move the coins
        for coin in self.coins:
            coin.y += 5
            # Check if the coin has reached the bottom of the screen
            if coin.y > screen_height:
                # Remove the coin from the list
                self.coins.remove(coin)
                # Create a new coin
                coin_type = random.choice([1, 10, 100])
                coin = pygame.Rect(random.randint(0, screen_width - 20), 0, 20, 20)
                coin.value = coin_type
                self.coins.append(coin)
        # Check if the container has collided with any coins
        for coin in self.coins:
            if self.container.colliderect(coin):
                # Remove the coin from the list
                self.coins.remove(coin)
                # Add the coin's value to the score
                self.score += coin.value
    def draw(self):
        """
        Draw the game screen.
        """
        # Fill the screen with black
        self.screen.fill((0, 0, 0))
        # Draw the container
        pygame.draw.rect(self.screen, (255, 255, 255), self.container)
        # Draw the coins
        for coin in self.coins:
            pygame.draw.rect(self.screen, (255, 255, 0), coin)
        # Draw the score
        score_text = self.font.render("Score: {}".format(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        # Draw the time left
        time_left_text = self.font.render("Time Left: {}".format(self.time_left), True, (255, 255, 255))
        self.screen.blit(time_left_text, (10, 30))
        # Draw the game over message
        if self.game_over:
            game_over_text = self.font.render("Game Over", True, (255, 255, 255))
            self.screen.blit(game_over_text, (screen_width / 2 - 50, screen_height / 2 - 10))
    def move_container_left(self):
        """
        Move the container to the left.
        """
        # Check if the container is at the left edge of the screen
        if self.container.x <= 0:
            return
        # Move the container to the left
        self.container.x -= 5
    def move_container_right(self):
        """
        Move the container to the right.
        """
        # Check if the container is at the right edge of the screen
        if self.container.x >= screen_width - self.container.width:
            return
        # Move the container to the right
        self.container.x += 5