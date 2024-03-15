'''This is the class for the snake.'''
import tkinter as tk
class Snake:
    def __init__(self, game_board):
        self.game_board = game_board
        # The snake's body is a list of tuples, where each tuple represents a segment of the snake's body
        self.body = [(4, 4), (3, 4), (2, 4)]
        # The snake's direction is initially set to right
        self.direction = "right"
        # The snake's speed is initially set to 1
        self.speed = 1
    def move(self):
        # Get the next position of the snake's head
        next_position = self.get_next_position()
        # Check if the snake has collided with itself or the game boundaries
        if self.has_collided(next_position):
            self.game_board.end_game()
            return
        # Move the snake's body to the new position
        self.body.insert(0, next_position)
        # Check if the snake has eaten the food
        if next_position == self.game_board.food.position:
            self.game_board.food.eaten()
            self.speed += 1
        else:
            # Remove the last segment of the snake's body
            self.body.pop()
        # Draw the snake on the game board
        self.game_board.draw_snake()
    def get_next_position(self):
        # Get the current position of the snake's head
        head_position = self.body[0]
        # Calculate the next position of the snake's head based on its direction
        if self.direction == "right":
            next_position = (head_position[0] + 1, head_position[1])
        elif self.direction == "left":
            next_position = (head_position[0] - 1, head_position[1])
        elif self.direction == "up":
            next_position = (head_position[0], head_position[1] - 1)
        elif self.direction == "down":
            next_position = (head_position[0], head_position[1] + 1)
        return next_position
    def has_collided(self, position):
        # Check if the snake has collided with itself
        for segment in self.body[1:]:
            if position == segment:
                return True
        # Check if the snake has collided with the game boundaries
        if position[0] < 0 or position[0] >= self.game_board.width or position[1] < 0 or position[1] >= self.game_board.height:
            return True
        return False
    def move_up(self, event):
        if self.direction != "down":
            self.direction = "up"
    def move_down(self, event):
        if self.direction != "up":
            self.direction = "down"
    def move_left(self, event):
        if self.direction != "right":
            self.direction = "left"
    def move_right(self, event):
        if self.direction != "left":
            self.direction = "right"