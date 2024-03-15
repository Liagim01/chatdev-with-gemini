import random
import tkinter as tk
class Maze:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.maze = [[0] * self.cols for _ in range(self.rows)]
        self.player_row = 0
        self.player_col = 0
        self.goal_row = self.rows - 1
        self.goal_col = self.cols - 1
        self.generate_maze()
    def generate_maze(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if row == 0 or col == 0 or row == self.rows - 1 or col == self.cols - 1:
                    self.maze[row][col] = 1
                else:
                    self.maze[row][col] = 0
        self.maze[self.player_row][self.player_col] = 0
        self.maze[self.goal_row][self.goal_col] = 0
        self.create_path(self.player_row, self.player_col)
    def create_path(self, row, col):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if new_row >= 0 and new_row < self.rows and new_col >= 0 and new_col < self.cols and self.maze[new_row][new_col] == 1:
                self.maze[new_row][new_col] = 0
                self.create_path(new_row, new_col)
    def move_player(self, direction):
        if direction == "Up" and self.player_row > 0 and self.maze[self.player_row - 1][self.player_col] == 0:
            self.player_row -= 1
        elif direction == "Down" and self.player_row < self.rows - 1 and self.maze[self.player_row + 1][self.player_col] == 0:
            self.player_row += 1
        elif direction == "Left" and self.player_col > 0 and self.maze[self.player_row][self.player_col - 1] == 0:
            self.player_col -= 1
        elif direction == "Right" and self.player_col < self.cols - 1 and self.maze[self.player_row][self.player_col + 1] == 0:
            self.player_col += 1