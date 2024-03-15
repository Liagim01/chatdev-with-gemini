import tkinter as tk
import random
class Game:
    """
    The 2048 game class.
    """
    def __init__(self, window):
        """
        Initialize the game.
        Args:
            window: The tkinter window object.
        """
        # Set the game window
        self.window = window
        # Set the game size
        self.size = 10
        # Create the game board
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        # Create the game score
        self.score = 0
        # Create the game over flag
        self.game_over = False
        # Create the game canvas
        self.canvas = tk.Canvas(window, width=self.size * 100, height=self.size * 100)
        self.canvas.pack()
        # Create the game tiles
        self.tiles = {}
        for i in range(self.size):
            for j in range(self.size):
                self.tiles[(i, j)] = tk.Label(window, text="", bg="white", font=("Arial", 20))
                self.tiles[(i, j)].place(x=i * 100, y=j * 100, width=100, height=100)
        # Bind the key press event
        window.bind("<Key>", self.on_key_press)
        # Start the game
        self.start()
    def start(self):
        """
        Start the game.
        """
        # Add two random tiles to the board
        self.add_random_tile()
        self.add_random_tile()
        # Update the game board
        self.update_board()
    def on_key_press(self, event):
        """
        Handle the key press event.
        Args:
            event: The key press event object.
        """
        # Check if the game is over
        if self.game_over:
            return
        # Get the key that was pressed
        key = event.keysym
        # Move the tiles
        if key == "Up":
            self.move_tiles("up")
        elif key == "Down":
            self.move_tiles("down")
        elif key == "Left":
            self.move_tiles("left")
        elif key == "Right":
            self.move_tiles("right")
        # Update the game board
        self.update_board()
        # Check if the game is over
        self.check_game_over()
    def move_tiles(self, direction):
        """
        Move the tiles in the given direction.
        Args:
            direction: The direction to move the tiles.
        """
        # Check if the direction is valid
        if direction not in ["up", "down", "left", "right"]:
            raise ValueError("Invalid direction: {}".format(direction))
        # Move the tiles in the given direction
        if direction == "up":
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] != 0:
                        k = i - 1
                        while k >= 0 and self.board[k][j] == 0:
                            self.board[k][j] = self.board[k + 1][j]
                            self.board[k + 1][j] = 0
                            k -= 1
                        if k >= 0 and self.board[k][j] == self.board[k + 1][j]:
                            self.board[k][j] *= 2
                            self.board[k + 1][j] = 0
                            self.score += self.board[k][j]
        elif direction == "down":
            for i in range(self.size - 1, -1, -1):
                for j in range(self.size):
                    if self.board[i][j] != 0:
                        k = i + 1
                        while k < self.size and self.board[k][j] == 0:
                            self.board[k][j] = self.board[k - 1][j]
                            self.board[k - 1][j] = 0
                            k += 1
                        if k < self.size and self.board[k][j] == self.board[k - 1][j]:
                            self.board[k][j] *= 2
                            self.board[k - 1][j] = 0
                            self.score += self.board[k][j]
        elif direction == "left":
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] != 0:
                        k = j - 1
                        while k >= 0 and self.board[i][k] == 0:
                            self.board[i][k] = self.board[i][k + 1]
                            self.board[i][k + 1] = 0
                            k -= 1
                        if k >= 0 and self.board[i][k] == self.board[i][k + 1]:
                            self.board[i][k] *= 2
                            self.board[i][k + 1] = 0
                            self.score += self.board[i][k]
        elif direction == "right":
            for i in range(self.size):
                for j in range(self.size - 1, -1, -1):
                    if self.board[i][j] != 0:
                        k = j + 1
                        while k < self.size and self.board[i][k] == 0:
                            self.board[i][k] = self.board[i][k - 1]
                            self.board[i][k - 1] = 0
                            k += 1
                        if k < self.size and self.board[i][k] == self.board[i][k - 1]:
                            self.board[i][k] *= 2
                            self.board[i][k - 1] = 0
                            self.score += self.board[i][k]
    def update_board(self):
        """
        Update the game board.
        """
        # Clear the canvas
        self.canvas.delete("all")
        # Draw the tiles
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != 0:
                    self.tiles[(i, j)].configure(text=str(self.board[i][j]))
                    self.tiles[(i, j)].place(x=i * 100, y=j * 100, width=100, height=100)
        # Update the score
        self.window.title("2048 - Score: {}".format(self.score))
    def check_game_over(self):
        """
        Check if the game is over.
        """
        # Check if there are any empty tiles
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return
        # Check if there are any adjacent tiles that can be merged
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.board[i][j] == self.board[i][j + 1]:
                    return
        for i in range(self.size - 1):
            for j in range(self.size):
                if self.board[i][j] == self.board[i + 1][j]:
                    return
        # The game is over
        self.game_over = True
        # Display the game over message
        self.canvas.create_text(self.size * 100 / 2, self.size * 100 / 2, text="Game Over!", font=("Arial", 50))
    def add_random_tile(self):
        """
        Add a random tile to the board.
        """
        # Get a list of all the empty tiles
        empty_tiles = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    empty_tiles.append((i, j))
        # Choose a random tile from the list of empty tiles
        random_tile = random.choice(empty_tiles)
        # Set the value of the random tile to 2 or 4
        self.board[random_tile[0]][random_tile[1]] = 2 if random.random() < 0.9 else 4