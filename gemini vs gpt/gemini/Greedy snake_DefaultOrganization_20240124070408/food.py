'''This is the class for the food.'''
import tkinter as tk
import random
class Food:
    def __init__(self, game_board):
        self.game_board = game_board
        # The food's position is initially set to a random location on the game board
        self.position = self.get_random_position()
    def get_random_position(self):
        # Generate a random position for the food
        while True:
            position = (random.randint(0, self.game_board.width - 1), random.randint(0, self.game_board.height - 1))
            # Check if the position is not occupied by the snake
            if position not in self.game_board.snake.body:
                return position
    def eaten(self):
        # Generate a new random position for the food
        self.position = self.get_random_position()
        # Increase the snake's speed
        self.game_board.snake.speed += 1
    def draw(self):
        # Draw the food on the game board
        self.game_board.canvas.create_rectangle(self.position[0] * self.game_board.cell_size, self.position[1] * self.game_board.cell_size,
                                               (self.position[0] + 1) * self.game_board.cell_size, (self.position[1] + 1) * self.game_board.cell_size,
                                               fill="red")