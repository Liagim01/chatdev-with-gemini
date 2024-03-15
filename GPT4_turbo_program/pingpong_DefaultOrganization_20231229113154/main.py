'''
This is the main file for the pingpong game designed using Pygame. It contains the game loop, event handling, and rendering of game objects.
Before running this game, make sure to install Pygame by running 'pip install pygame' in your command line or terminal.
'''
import pygame
import sys
# Constants for the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
BALL_SIZE = 15
PADDLE_SPEED = 7
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PingPong Game')
# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    def move(self, y):
        self.rect.y += y
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
# Ball class
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y
    def move(self, game):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - BALL_SIZE:
            self.speed_y *= -1
        if self.rect.x <= 0:
            game.score2 += 1
            self.reset()
        elif self.rect.x >= SCREEN_WIDTH - BALL_SIZE:
            game.score1 += 1
            self.reset()
    def reset(self):
        self.rect.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        self.rect.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        self.speed_x *= -1
    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)
    def collide_with_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            # Check if collision is from top or bottom of the paddle
            if self.rect.centery < paddle.rect.top or self.rect.centery > paddle.rect.bottom:
                self.speed_y *= -1
            else:
                self.speed_x *= -1
            # Optional: Adjust speed_y based on where the ball hits the paddle for more dynamic gameplay
            offset = (paddle.rect.centery - self.rect.centery) / (PADDLE_HEIGHT / 2)
            self.speed_y -= offset
# Game class
class Game:
    def __init__(self):
        self.paddle1 = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.paddle2 = Paddle(SCREEN_WIDTH - 10 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2)
        self.score1 = 0
        self.score2 = 0
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.paddle1.move(-PADDLE_SPEED)
            if keys[pygame.K_s]:
                self.paddle1.move(PADDLE_SPEED)
            if keys[pygame.K_UP]:
                self.paddle2.move(-PADDLE_SPEED)
            if keys[pygame.K_DOWN]:
                self.paddle2.move(PADDLE_SPEED)
            self.ball.move(self)
            self.ball.collide_with_paddle(self.paddle1)
            self.ball.collide_with_paddle(self.paddle2)
            screen.fill(BLACK)
            self.paddle1.draw()
            self.paddle2.draw()
            self.ball.draw()
            # Display the score
            font = pygame.font.Font(None, 74)
            text = font.render(str(self.score1), 1, WHITE)
            screen.blit(text, (250, 10))
            text = font.render(str(self.score2), 1, WHITE)
            screen.blit(text, (SCREEN_WIDTH - 250, 10))
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        sys.exit()
# Main function
def main():
    game = Game()
    game.run()
if __name__ == '__main__':
    main()