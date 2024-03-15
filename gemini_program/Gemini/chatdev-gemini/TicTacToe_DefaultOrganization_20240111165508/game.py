# game.py
import tkinter as tk
class Game:
    """
    The game object for the tic-tac-toe game.
    """
    def __init__(self):
        """
        Initialize the game object.
        """
        # The current player.
        self.player = 1
        # The game board.
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        # The status of the game.
        self.status = "ongoing"
    def start(self):
        """
        Start the game.
        """
        # Reset the game board.
        for i in range(3):
            for j in range(3):
                self.board[i][j] = 0
        # Set the current player to player 1.
        self.player = 1
        # Set the status of the game to "ongoing".
        self.status = "ongoing"
    def move(self, row, col):
        """
        Make a move on the game board.
        Args:
            row: The row of the move.
            col: The column of the move.
        """
        # Check if the move is valid.
        if self.board[row][col] != 0 or self.status != "ongoing":
            return
        # Make the move.
        self.board[row][col] = self.player
        # Check if the game is over.
        self.check_game_over()
        # Switch the current player.
        self.player = 3 - self.player
    def check_game_over(self):
        """
        Check if the game is over.
        """
        # Check for a win.
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.status = "win"
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.status = "win"
                return
        # Check for a tie.
        if all(all(cell != 0 for cell in row) for row in self.board):
            self.status = "tie"
            return
        # The game is still ongoing.
        self.status = "ongoing"