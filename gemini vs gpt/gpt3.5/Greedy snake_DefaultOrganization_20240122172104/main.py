'''
Greedy Snake Game
'''
import pygame
import random
# Initialize the game
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Greedy Snake Game")
# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
# Define game variables
snake_size = 20
snake_speed = 15
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)
def display_score(score):
    '''
    Display the score on the screen
    '''
    value = score_font.render("Score: " + str(score), True, white)
    window.blit(value, [10, 10])
def draw_snake(snake_size, snake_list):
    '''
    Draw the snake on the screen
    '''
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_size, snake_size])
def game_loop():
    '''
    Main game loop
    '''
    game_over = False
    game_close = False
    # Initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2
    # Initial movement direction of the snake
    x1_change = 0
    y1_change = 0
    # Create the snake list
    snake_list = []
    snake_length = 1
    # Initial position of the food
    food_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
    while not game_over:
        while game_close:
            window.fill(black)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            window.blit(message, [window_width / 6, window_height / 3])
            display_score(snake_length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        draw_snake(snake_size, snake_list)
        display_score(snake_length - 1)
        pygame.display.update()
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
            snake_length += 1
        clock.tick(snake_speed)
    pygame.quit()
game_loop()