'''
This is the main entry point for the 2048 game with a 10x10 grid.
'''
import tkinter as tk
from game_logic import GameLogic
from game_gui import GameGUI
def main():
    root = tk.Tk()
    game_logic = GameLogic()
    app = GameGUI(root, game_logic)
    app.start()
    root.mainloop()
if __name__ == '__main__':
    main()