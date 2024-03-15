'''
This is the main file for the Maze Game. It initializes the game and contains the game loop.
'''
import pygame
import sys
from maze import Maze
from player import Player
# Initialize Pygame
pygame.init()
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")
# Clock to control the frame rate
clock = pygame.time.Clock()
# Create the maze and player instances
maze = Maze(20, 15, 40)  # 20x15 grid with 40px per cell
player = Player(maze.start_pos, maze.cell_size)
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move_up(maze)
                elif event.key == pygame.K_DOWN:
                    player.move_down(maze)
                elif event.key == pygame.K_LEFT:
                    player.move_left(maze)
                elif event.key == pygame.K_RIGHT:
                    player.move_right(maze)
        screen.fill((0, 0, 0))  # Fill the screen with black
        maze.draw(screen)
        player.draw(screen)
        pygame.display.flip()  # Update the full display Surface to the screen
        clock.tick(FPS)  # Control the frame rate
        if player.position == maze.goal_pos:
            print("Congratulations! You've reached the goal!")
            pygame.quit()
            sys.exit()
if __name__ == "__main__":
    game_loop()