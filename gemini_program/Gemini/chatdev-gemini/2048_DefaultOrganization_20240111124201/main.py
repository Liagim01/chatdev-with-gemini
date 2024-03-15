import tkinter as tk
from game import Game
def main():
    """
    The main function of the program.
    """
    # Create the main window.
    window = tk.Tk()
    window.title("2048")
    # Create the game object.
    game = Game(window)
    # Start the game.
    game.start()
    # Main loop.
    window.mainloop()
if __name__ == "__main__":
    main()