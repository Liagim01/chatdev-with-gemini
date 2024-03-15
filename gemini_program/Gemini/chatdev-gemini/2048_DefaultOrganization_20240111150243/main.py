import tkinter as tk
from game import Game
def main():
    """
    The main function of the 2048 game.
    """
    # Create the game window
    window = tk.Tk()
    window.title("2048")
    # Create the game object
    game = Game(window)
    # Start the game
    game.start()
    # Main event loop
    window.mainloop()
if __name__ == "__main__":
    main()