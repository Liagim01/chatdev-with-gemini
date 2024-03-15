import random
import sys

# Initialize the game board
board = [[0 for _ in range(10)] for _ in range(10)]

# Add two random tiles to the board
def add_random_tile():
    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)

        if board[row][col] == 0:
            board[row][col] = 2 if random.random() < 0.9 else 4
            break

add_random_tile()
add_random_tile()

# Print the game board
def print_board():
    for row in board:
        print(' '.join(str(tile) for tile in row))

# Handle player input
def get_input():
    while True:
        command = input("Enter a command (w/s/a/d): ")
        if command in ("w", "s", "a", "d"):
            return command
        else:
            print("Invalid input. Please enter w/s/a/d.")

# Move tiles in the given direction
def move(direction):
    # Move tiles up
    if direction == "w":
        for col in range(10):
            for row in range(1, 10):
                if board[row][col] != 0:
                    move_up(row, col)
    # Move tiles down
    elif direction == "s":

        for col in range(10):
            for row in range(8, -1, -1):
                if board[row][col] != 0:
                    move_down(row, col)
    # Move tiles left
    elif direction == "a":
        for row in range(10):
            for col in range(1, 10):
                if board[row][col] != 0:
                    move_left(row, col)
    # Move tiles right
    elif direction == "d":
        for row in range(10):
            for col in range(8, -1, -1):
                if board[row][col] != 0:
                    move_right(row, col)

# Move a tile up
def move_up(row, col):
    while row > 0 and board[row - 1][col] == 0:
        board[row - 1][col] = board[row][col]
        board[row][col] = 0
        row -= 1
    if row > 0 and board[row - 1][col] == board[row][col]:
        board[row - 1][col] *= 2
        board[row][col] = 0

# Move a tile down
def move_down(row, col):
    while row < 9 and board[row + 1][col] == 0:
        board[row + 1][col] = board[row][col]
        board[row][col] = 0
        row += 1
    if row < 9 and board[row + 1][col] == board[row][col]:
        board[row + 1][col] *=2
        board[row][col] = 0


# Move a tile left
def move_left(row, col):
    while col > 0 and board[row][col - 1] == 0:
        board[row][col - 1] = board[row][col]
        board[row][col] = 0
        col -= 1
    if col > 0 and board[row][col - 1] == board[row][col]:
        board[row][col - 1] *= 2
        board[row][col] = 0

# Move a tile right
def move_right(row, col):
    while col < 9 and board[row][col+ 1] == 0:
        board[row][col + 1] = board[row][col]
        board[row][col] = 0
        col += 1
    if col < 9 and board[row][col + 1]== board[row][col]:
        board[row][col + 1] *= 2
        board[row][col] = 0

# Check if the game is over
def is_game_over():
    # Check if there are any empty spaces on the board
    for row in board:
        for tile in row:
            if tile == 0:
                return False

    # Check if there are any moves left
    for direction in ["w", "s", "a", "d"]:
        temp_board = [[tile for tile in row] for row in board]
        move(direction)
        if temp_board != board:
            return False

    # No empty spaces and no moves left, game over
    return True

# Main game loop
while not is_game_over():
    # Print the game board
    print_board()

    # Get player
    input
    command = get_input()

    # Move tiles in the given direction
    move(command)

    # Add a new random tile
    add_random_tile()

# Game over
print("Game over!")

