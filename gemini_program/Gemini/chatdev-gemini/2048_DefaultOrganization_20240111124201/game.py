import tkinter as tk
import random
class Game:
    """
    The game object.
    """
    def __init__(self, window):
        """
        Initialize the game.
        Args:
            window: The main window of the program.
        """
        # Set the window title.
        window.title("2048")
        # Create the game board.
        self.board = [[0 for _ in range(10)] for _ in range(10)]
        # Create the game grid.
        self.grid = tk.Frame(window)
        self.grid.pack()
        # Create the game tiles.
        self.tiles = {}
        for row in range(10):
            for column in range(10):
                tile = tk.Label(self.grid, text="", bg="white", font=("Helvetica", 24))
                tile.grid(row=row, column=column, sticky="nsew")
                self.tiles[(row, column)] = tile
        # Add a new tile to the board.
        self.add_tile()
        # Bind the arrow keys to the game.
        window.bind("<Key>", self.on_key_press)
    def start(self):
        """
        Start the game.
        """
        # Update the game board.
        self.update_board()
    def update_board(self):
        """
        Update the game board.
        """
        # Clear the game grid.
        for tile in self.tiles.values():
            tile.configure(text="")
        # Draw the game tiles.
        for row in range(10):
            for column in range(10):
                tile = self.tiles[(row, column)]
                if self.board[row][column] != 0:
                    tile.configure(text=str(self.board[row][column]), bg="blue")
    def add_tile(self):
        """
        Add a new tile to the board.
        """
        # Get a random empty cell.
        empty_cells = [(row, column) for row in range(10) for column in range(10) if self.board[row][column] == 0]
        random_cell = random.choice(empty_cells)
        # Add a new tile to the cell.
        self.board[random_cell[0]][random_cell[1]] = 2
        # Update the game board.
        self.update_board()
    def on_key_press(self, event):
        """
        Handle the key press event.
        Args:
            event: The key press event.
        """
        # Get the key that was pressed.
        key = event.keysym
        # Move the tiles in the direction of the key that was pressed.
        if key == "Up":
            self.move_tiles("up")
        elif key == "Down":
            self.move_tiles("down")
        elif key == "Left":
            self.move_tiles("left")
        elif key == "Right":
            self.move_tiles("right")
        # Add a new tile to the board.
        self.add_tile()
        # Update the game board.
        self.update_board()
    def move_tiles(self, direction):
        """
        Move the tiles in the direction of the given direction.
        Args:
            direction: The direction to move the tiles.
        """
        # Create a copy of the game board.
        board_copy = [[tile for tile in row] for row in self.board]
        # Move the tiles in the given direction.
        if direction == "up":
            for column in range(10):
                for row in range(1, 10):
                    if board_copy[row][column] != 0:
                        for i in range(row, 0, -1):
                            if board_copy[i - 1][column] == 0:
                                board_copy[i - 1][column] = board_copy[i][column]
                                board_copy[i][column] = 0
                            elif board_copy[i - 1][column] == board_copy[i][column]:
                                board_copy[i - 1][column] *= 2
                                board_copy[i][column] = 0
                                break
        elif direction == "down":
            for column in range(10):
                for row in range(8, -1, -1):
                    if board_copy[row][column] != 0:
                        for i in range(row, 9):
                            if board_copy[i + 1][column] == 0:
                                board_copy[i + 1][column] = board_copy[i][column]
                                board_copy[i][column] = 0
                            elif board_copy[i + 1][column] == board_copy[i][column]:
                                board_copy[i + 1][column] *= 2
                                board_copy[i][column] = 0
                                break
        elif direction == "left":
            for row in range(10):
                for column in range(1, 10):
                    if board_copy[row][column] != 0:
                        for i in range(column, 0, -1):
                            if board_copy[row][i - 1] == 0:
                                board_copy[row][i - 1] = board_copy[row][i]
                                board_copy[row][i] = 0
                            elif board_copy[row][i - 1] == board_copy[row][i]:
                                board_copy[row][i - 1] *= 2
                                board_copy[row][i] = 0
                                break
        elif direction == "right":
            for row in range(10):
                for column in range(8, -1, -1):
                    if board_copy[row][column] != 0:
                        for i in range(column, 9):
                            if board_copy[row][i + 1] == 0:
                                board_copy[row][i + 1] = board_copy[row][i]
                                board_copy[row][i] = 0
                            elif board_copy[row][i + 1] == board_copy[row][i]:
                                board_copy[row][i + 1] *= 2
                                board_copy[row][i] = 0
                                break
        # Update the game board.
        self.board = board_copy