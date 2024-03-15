'''
This module contains the game logic for a 2048 game with a 10x10 grid.
'''
import random
class GameLogic:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[0] * self.size for _ in range(self.size)]
        self.add_new_tile()
        self.add_new_tile()
    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4
    def get_grid(self):
        return self.grid
    def compress(self, row):
        new_row = [i for i in row if i != 0]
        new_row += [0] * (self.size - len(new_row))
        return new_row
    def merge(self, row):
        for i in range(self.size - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row
    def move_left(self):
        for i in range(self.size):
            self.grid[i] = self.compress(self.grid[i])
            self.grid[i] = self.merge(self.grid[i])
            self.grid[i] = self.compress(self.grid[i])
    def move_right(self):
        for i in range(self.size):
            self.grid[i].reverse()
            self.grid[i] = self.compress(self.grid[i])
            self.grid[i] = self.merge(self.grid[i])
            self.grid[i] = self.compress(self.grid[i])
            self.grid[i].reverse()
    def move_up(self):
        self.grid = [list(x) for x in zip(*self.grid)]
        self.move_left()
        self.grid = [list(x) for x in zip(*self.grid)]
    def move_down(self):
        self.grid = [list(x) for x in zip(*self.grid)]
        self.move_right()
        self.grid = [list(x) for x in zip(*self.grid)]
    def move(self, direction):
        if direction == 'up':
            self.move_up()
        elif direction == 'down':
            self.move_down()
        elif direction == 'left':
            self.move_left()
        elif direction == 'right':
            self.move_right()
        self.add_new_tile()
    def is_game_over(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return False
                if i < self.size - 1 and self.grid[i][j] == self.grid[i + 1][j]:
                    return False
                if j < self.size - 1 and self.grid[i][j] == self.grid[i][j + 1]:
                    return False
        return True