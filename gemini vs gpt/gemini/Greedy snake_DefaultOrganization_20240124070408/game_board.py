'''This is the class for the game board.'''
import tkinter as tk
from snake import Snake
from food import Food
import random
class GameBoard:
    def __init__(self, window):
        self.window = window
        # The game board's width and height are initially set to 20
        self.width = 20
        self.height = 20
        # The game board's cell size is initially set to 10
        self.cell_size = 10
        # Create the canvas for the game board
        self.canvas = tk.Canvas(self.window, width=self.width * self.cell_size, height=self.height * self.cell_size)
        self.canvas.pack()
        # Create the snake and the food
        self.snake = Snake(self)
        self.food = Food(self)
        # Start the game
        self.start()
    def start(self):
        # Draw the snake and the food on the game board
        self.draw_snake()
        self.draw_food()
        # Start the game loop
        self.game_loop()
    def game_loop(self):
        # Move the snake
        self.snake.move()
        # Check if the game is over
        if self.snake.has_collided(self.snake.get_next_position()):
            self.end_game()
            return
        # Draw the snake and the food on the game board
        self.draw_snake()
        self.draw_food()
        # Schedule the next game loop iteration
        self.window.after(1000 // self.snake.speed, self.game_loop)
    def end_game(self):
        # Display a message to the player that the game is over
        tk.messagebox.showinfo("Game Over", "Game Over!")
        # Stop the game loop
        self.window.after_cancel(self.game_loop)
    def draw_snake(self):
        # Clear the canvas
        self.canvas.delete("all")
        # Draw the snake's body
        for segment in self.snake.body:
            self.canvas.create_rectangle(segment[0] * self.cell_size, segment[1] * self.cell_size,
                                           (segment[0] + 1) * self.cell_size, (segment[1] + 1) * self.cell_size,
                                           fill="green")
    def draw_food(self):
        # Draw the food
        self.canvas.create_rectangle(self.food.position[0] * self.cell_size, self.food.position[1] * self.cell_size,
                                       (self.food.position[0] + 1) * self.cell_size, (self.food.position[1] + 1) * self.cell_size,
                                       fill="red")