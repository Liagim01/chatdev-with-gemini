'''
This is the main file for the Tic-Tac-Toe game. It sets up the GUI and handles the game logic.
The game allows two players to take turns to play Tic-Tac-Toe and determines the winner or a tie.
A "Restart Game" button has been added for user convenience to start a new game without reopening the application.
'''
import tkinter as tk
from tkinter import messagebox
class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = []
        self.create_board()
        self.create_restart_button()
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=' ', font=('normal', 40), height=1, width=2,
                                   command=lambda i=i, j=j: self.player_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    def create_restart_button(self):
        restart_button = tk.Button(self.root, text='Restart Game', font=('normal', 14), command=self.reset_game)
        restart_button.grid(row=3, column=1)
    def player_click(self, i, j):
        index = i * 3 + j
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
                return  # Exit the method after a win
            if ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
                return  # Exit the method after declaring a tie
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False
    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for row in self.buttons:  # Corrected from buttons to self.buttons
            for button in row:
                button.config(text=' ')
        self.current_player = 'X'
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()