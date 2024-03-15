import pygame
import random
# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PingPong")

# Define the colors
BLACK = (0, 0,
0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

# Define the ball
BALL_RADIUS = 10
BALL_SPEED = 10

# Create the paddles
paddle1 = pygame.Rect(10, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(SCREEN_WIDTH - 10 - PADDLE_WIDTH, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(SCREEN_WIDTH / 2 - BALL_RADIUS / 2, SCREEN_HEIGHT / 2 - BALL_RADIUS
/ 2, BALL_RADIUS, BALL_RADIUS)

# Set up the game variables
running = True
score1 = 0
score2 = 0

# The main game loop
while running:

  # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1.y -= PADDLE_SPEED
            elif event.key == pygame.K_s:
                paddle1.y += PADDLE_SPEED
            elif event.key == pygame.K_UP:
                paddle2.y -= PADDLE_SPEED

        elif event.key == pygame.K_DOWN:
            paddle2.y += PADDLE_SPEED

    # Update the game logic
    # Update the ball's position
    ball.x += BALL_SPEED * random.choice([-1, 1])
    ball.y += BALL_SPEED * random.choice([-1, 1])

    # Check for collisions with the paddles
    if ball.colliderect(paddle1):
        BALL_SPEED *= -1
    elif ball.colliderect(paddle2):
        BALL_SPEED *= -1

    # Check for collisions with the walls
    if ball.top < 0 or ball.bottom > SCREEN_HEIGHT:
        BALL_SPEED *= -1
    elif ball.left < 0:
        score2 += 1
        ball.x = SCREEN_WIDTH / 2 - BALL_RADIUS / 2
        ball.y = SCREEN_HEIGHT / 2 - BALL_RADIUS / 2
        BALL_SPEED = 10

    elif ball.right > SCREEN_WIDTH:
        score1 += 1
        ball.x = SCREEN_WIDTH / 2 - BALL_RADIUS / 2
        ball.y = SCREEN_HEIGHT / 2 - BALL_RADIUS / 2
        BALL_SPEED = 10

    # Draw the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.circle(screen, WHITE, (ball.x, ball.y), BALL_RADIUS)
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT), 1)
    pygame.display.update()

    # Clock tick
    clock.tick(FPS)

# Quit pygame
pygame.quit()