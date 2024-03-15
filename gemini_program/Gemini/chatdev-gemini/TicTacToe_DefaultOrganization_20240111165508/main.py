import tkinter as tk
from game import Game
def main():
    """
    The main function of the tic-tac-toe game.
    """
    # Create the main window.
    window = tk.Tk()
    window.title("Tic-Tac-Toe")
    # Create the game object.
    game = Game()
    # Create the game board.
    board = tk.Frame(window)
    board.pack()
    # Create the buttons for the game board.
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(board, text=" ", command=lambda row=i, col=j: game.move(row, col))
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)
    # Create the status bar.
    status_bar = tk.Label(window, text="Player 1's turn")
    status_bar.pack()
    # Start the game.
    game.start()
    # Main loop.
    window.mainloop()
if __name__ == "__main__":
    main()