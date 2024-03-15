import pygame

# Define the dimensions of the maze.
WIDTH = 10
HEIGHT = 10

# Define the player's starting position.
PLAYER_START_X = 0
PLAYER_START_Y = 0

# Define the exit's position.
EXIT_X = WIDTH - 1
EXIT_Y = HEIGHT - 1

# Create a 2D array to represent the maze.
maze = [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Set the player's starting position in the maze.
maze[PLAYER_START_Y][PLAYER_START_X] = 'P'

# Set the exit's position in the maze.
maze[EXIT_Y][EXIT_X] = 'E'

# Create a Pygame window.
window = pygame.display.set_mode((WIDTH * 32, HEIGHT * 32))

# Set the window title.
pygame.display.set_caption("Maze Game")

# Create a clock object to control the game's frame rate.
clock = pygame.time.Clock()

# Create a player object.
player = pygame.sprite.Sprite()
player.image = pygame.Surface((32, 32))
player.image.fill((0, 255, 0))
player.rect = player.image.get_rect()
player.rect.center = (PLAYER_START_X * 32 + 16, PLAYER_START_Y * 32 + 16)

# Create a group to hold all of the sprites in the game.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create a group to hold all of the walls in the maze.
walls = pygame.sprite.Group()

# Loop through the maze and create a wall object for each '#' character.
for y, row in enumerate(maze):
    for x, char in enumerate(row):
        if char == '#':
            wall = pygame.sprite.Sprite()
            wall.image = pygame.Surface((32, 32))
            wall.image.fill((0, 0, 0))
            wall.rect = wall.image.get_rect()
            wall.rect.x = x * 32
            wall.rect.y = y * 32
            walls.add(wall)

# Add the walls to the all_sprites group.
all_sprites.add(walls)

# Set the game's frame rate.
FPS = 60

# Game loop.
running = True
while running:
    # Handle events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keyboard input.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.rect.y -= 32
            elif event.key == pygame.K_DOWN:
                player.rect.y += 32
            elif event.key == pygame.K_LEFT:
                player.rect.x -= 32
            elif event.key == pygame.K_RIGHT:
                player.rect.x += 32

    # Check for collisions between the player and the walls.
    if pygame.sprite.spritecollideany(player, walls):
        # If the player collides with a wall, move them back to their previous position.
        player.rect.x = player.rect.x
        player.rect.y = player.rect.y

    # Check if the player has reached the exit.
    if player.rect.colliderect(EXIT_X * 32, EXIT_Y * 32, 32, 32):
        # If the player has reached the exit, end the game.
        running = False

    # Update the game state.
    all_sprites.update()

    # Draw the game screen.
    window.fill((255, 255, 255))
    all_sprites.draw(window)

    # Flip the display.
    pygame.display.flip()

    # Limit the frame rate.
    clock.tick(FPS)

# Quit Pygame.
pygame.quit()