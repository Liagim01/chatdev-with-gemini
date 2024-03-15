'''Tetris game implementation in Python.'''
import tkinter as tk
import random
# Constants
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLOCK_SIZE = 25
# Colors
COLORS = {
    'I': 'cyan',
    'O': 'yellow',
    'T': 'purple',
    'S': 'green',
    'Z': 'red',
    'J': 'blue',
    'L': 'orange'
}
# Shapes
SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'J': [[1, 0, 0],
          [1, 1, 1]],
    'L': [[0, 0, 1],
          [1, 1, 1]]
}
# Game class
class Tetris:
    def __init__(self):
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_block = self.get_random_block()
        self.current_x = BOARD_WIDTH // 2 - len(self.current_block[0]) // 2
        self.current_y = 0
        self.score = 0
    def get_random_block(self):
        return random.choice(list(SHAPES.keys()))
    def draw_board(self):
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.board[y][x] == 1:
                    tk.Canvas.create_rectangle(self.canvas, x * BLOCK_SIZE, y * BLOCK_SIZE,
                                              (x + 1) * BLOCK_SIZE, (y + 1) * BLOCK_SIZE,
                                              fill=COLORS[self.current_block])
    def move_block_left(self):
        if self.current_x > 0 and self.is_valid_move(self.current_block, self.current_x - 1, self.current_y):
            self.current_x -= 1
    def move_block_right(self):
        if self.current_x < BOARD_WIDTH - len(self.current_block[0]) and self.is_valid_move(self.current_block, self.current_x + 1, self.current_y):
            self.current_x += 1
    def move_block_down(self):
        if self.current_y < BOARD_HEIGHT - len(self.current_block) and self.is_valid_move(self.current_block, self.current_x, self.current_y + 1):
            self.current_y += 1
        else:
            self.add_block_to_board()
            self.current_block = self.get_random_block()
            self.current_x = BOARD_WIDTH // 2 - len(self.current_block[0]) // 2
            self.current_y = 0
    def add_block_to_board(self):
        for y in range(len(self.current_block)):
            for x in range(len(self.current_block[0])):
                if self.current_block[y][x] == 1:
                    self.board[self.current_y + y][self.current_x + x] = 1
    def is_valid_move(self, block, x, y):
        for y_block in range(len(block)):
            for x_block in range(len(block[0])):
                if block[y_block][x_block] == 1 and (x + x_block < 0 or x + x_block >= BOARD_WIDTH or
                                                    y + y_block >= BOARD_HEIGHT or self.board[y + y_block][x + x_block] == 1):
                    return False
        return True
    def check_for_completed_lines(self):
        for y in range(BOARD_HEIGHT):
            if all(self.board[y]):
                self.score += 1
                for y_above in range(y, 0, -1):
                    self.board[y_above] = self.board[y_above - 1]
                self.board[0] = [0 for _ in range(BOARD_WIDTH)]
    def start_game(self):
        self.canvas.bind('<Left>', lambda event: self.move_block_left())
        self.canvas.bind('<Right>', lambda event: self.move_block_right())
        self.canvas.bind('<Down>', lambda event: self.move_block_down())
        self.update_game()
    def update_game(self):
        self.draw_board()
        self.check_for_completed_lines()
        self.move_block_down()
        self.canvas.after(1000, self.update_game)
# Main function
def main():
    tetris = Tetris()
    tetris.canvas = tk.Canvas(width=BOARD_WIDTH * BLOCK_SIZE, height=BOARD_HEIGHT * BLOCK_SIZE)
    tetris.canvas.pack()
    tetris.start_game()
if __name__ == '__main__':
    main()