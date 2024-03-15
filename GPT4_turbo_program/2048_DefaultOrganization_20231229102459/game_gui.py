'''
This module contains the graphical user interface for the 2048 game with a 10x10 grid.
'''
import tkinter as tk
import tkinter.messagebox as messagebox
class GameGUI:
    def __init__(self, master, game_logic):
        self.master = master
        self.game_logic = game_logic
        self.master.title('2048 Game')
        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack()
        self.size = game_logic.size
        self.tiles = {}
        self.colors = {
            0: 'lavender',
            2: '#eee4da',
            4: '#ede0c8',
            8: '#f2b179',
            16: '#f59563',
            32: '#f67c5f',
            64: '#f65e3b',
            128: '#edcf72',
            256: '#edcc61',
            512: '#edc850',
            1024: '#edc53f',
            2048: '#edc22e',
            # Add more colors if tiles can go beyond 2048
        }
        self.init_grid()
        # Bind key events to game moves
        self.master.bind("<Left>", lambda event: self.move('left'))
        self.master.bind("<Right>", lambda event: self.move('right'))
        self.master.bind("<Up>", lambda event: self.move('up'))
        self.master.bind("<Down>", lambda event: self.move('down'))
    def init_grid(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                tile = tk.Label(self.grid_frame, text='', bg='lavender', width=4, height=2)
                tile.grid(row=i, column=j, padx=5, pady=5)
                row.append(tile)
            self.tiles[i] = row
        self.update_grid()
    def update_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                value = self.game_logic.get_grid()[i][j]
                tile = self.tiles[i][j]
                tile['text'] = str(value) if value > 0 else ''
                tile['bg'] = self.colors.get(value, 'black')  # Default to black if value not in colors
    def move(self, direction):
        self.game_logic.move(direction)
        self.update_grid()
        if self.game_logic.is_game_over():
            messagebox.showinfo("Game Over", "No more moves available! Game Over!")
    def start(self):
        self.update_grid()