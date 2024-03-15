'''
This file contains the Maze class which is responsible for generating and drawing the maze.
'''
import pygame
import random
class Maze:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = []
        self.start_pos = (0, 0)
        self.goal_pos = (width - 1, height - 1)
        self.generate_maze()
    def generate_maze(self):
        # Initialize all cells as walls
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
        # Random starting point
        start_x, start_y = (0, 0)
        self.start_pos = (start_x, start_y)
        # Stack for backtracking
        stack = [(start_x, start_y)]
        visited = set((start_x, start_y))
        while stack:
            x, y = stack[-1]
            self.grid[y][x] = 0  # Mark the current cell as a path
            # Find unvisited neighbors
            neighbors = []
            directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in visited:
                    neighbors.append((nx, ny))
            if neighbors:
                # Choose a random neighboring cell
                nx, ny = random.choice(neighbors)
                visited.add((nx, ny))
                # Remove the wall between the current cell and the chosen cell
                self.grid[(ny + y) // 2][(nx + x) // 2] = 0
                # Push the chosen cell to the stack
                stack.append((nx, ny))
            else:
                # Backtrack
                stack.pop()
        # Set the goal position
        self.goal_pos = (self.width - 2, self.height - 2)
        self.grid[self.goal_pos[1]][self.goal_pos[0]] = 0  # Ensure the goal position is a path
    def draw(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))