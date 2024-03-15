'''This is a simple ping pong game written in Python using the Pygame library.'''
import pygame
import sys
import random
# Initialize pygame
pygame.init()
# Set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the title of the window
pygame.display.set_caption("Ping Pong")
# Create the paddles
paddle_left = pygame.Rect(30, 200, 20, 100)
paddle_right = pygame.Rect(750, 200, 20, 100)
# Create the ball
ball = pygame.Rect(400, 300, 20, 20)
# Set the speed of the ball
ball_speed_x = 5
ball_speed_y = 5
# Set the scores
score_left = 0
score_right = 0
# Create the font for the score
font = pygame.font.SysFont("Arial", 32)
# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_left.y -= 10
            elif event.key == pygame.K_s:
                paddle_left.y += 10
            elif event.key == pygame.K_UP:
                paddle_right.y -= 10
            elif event.key == pygame.K_DOWN:
                paddle_right.y += 10
    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # Check if the ball has hit the left or right wall
    if ball.x < 0 or ball.x > SCREEN_WIDTH:
        ball_speed_x = -ball_speed_x
    # Check if the ball has hit the top or bottom wall
    if ball.y < 0 or ball.y > SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y
    # Check if the ball has hit the left paddle
    if ball.colliderect(paddle_left):
        ball_speed_x = -ball_speed_x
    # Check if the ball has hit the right paddle
    if ball.colliderect(paddle_right):
        ball_speed_x = -ball_speed_x
    # Check if the ball has gone off the screen
    if ball.x < 0:
        score_right += 1
        ball.x = 400
        ball.y = 300
        ball_speed_x = 5
        ball_speed_y = 5
    elif ball.x > SCREEN_WIDTH:
        score_left += 1
        ball.x = 400
        ball.y = 300
        ball_speed_x = -5
        ball_speed_y = -5
    # Draw the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle_left)
    pygame.draw.rect(screen, (255, 255, 255), paddle_right)
    pygame.draw.rect(screen, (255, 255, 255), ball)
    # Draw the score
    score_left_text = font.render(str(score_left), True, (255, 255, 255))
    screen.blit(score_left_text, (100, 100))
    score_right_text = font.render(str(score_right), True, (255, 255, 255))
    screen.blit(score_right_text, (700, 100))
    # Update the display
    pygame.display.update()