'''This is the main file for the Greedy Snake game.'''
import tkinter as tk
from snake import Snake
from food import Food
from game_board import GameBoard
def main():
    window = tk.Tk()
    window.title("Greedy Snake")
    # Create the game board
    game_board = GameBoard(window)
    # Create the snake
    snake = Snake(game_board)
    # Create the food
    food = Food(game_board)
    # Start the game
    game_board.start()
    # Bind the arrow keys to the snake's movement
    window.bind("<Up>", snake.move_up)
    window.bind("<Down>", snake.move_down)
    window.bind("<Left>", snake.move_left)
    window.bind("<Right>", snake.move_right)
    # Start the main loop
    window.mainloop()
if __name__ == "__main__":
    main()