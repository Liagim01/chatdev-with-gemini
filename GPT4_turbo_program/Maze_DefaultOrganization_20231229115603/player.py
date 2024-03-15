'''
This file contains the Player class which handles the player's movement and drawing.
'''
import pygame
class Player:
    def __init__(self, start_pos, cell_size):
        self.position = start_pos
        self.size = 20  # Smaller than the cell size to fit within the maze paths
        self.cell_size = cell_size
    def move_up(self, maze):
        if self.position[1] > 0 and maze.grid[self.position[1] - 1][self.position[0]] == 0:
            self.position = (self.position[0], self.position[1] - 1)
    def move_down(self, maze):
        if self.position[1] < maze.height - 1 and maze.grid[self.position[1] + 1][self.position[0]] == 0:
            self.position = (self.position[0], self.position[1] + 1)
    def move_left(self, maze):
        if self.position[0] > 0 and maze.grid[self.position[1]][self.position[0] - 1] == 0:
            self.position = (self.position[0] - 1, self.position[1])
    def move_right(self, maze):
        if self.position[0] < maze.width - 1 and maze.grid[self.position[1]][self.position[0] + 1] == 0:
            self.position = (self.position[0] + 1, self.position[1])
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0] * self.cell_size + (self.cell_size - self.size) / 2, self.position[1] * self.cell_size + (self.cell_size - self.size) / 2, self.size, self.size))