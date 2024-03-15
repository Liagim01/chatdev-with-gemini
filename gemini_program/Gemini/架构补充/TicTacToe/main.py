#main.py
'''
This is the main file of the tic-tac-toe game. It handles the game flow, user input, and GUI.
'''
import tkinter as tk
from tkinter import messagebox
from game import Game
class TicTacToeGUI:
  def __init__(self, master):
    self.master = master
    self.master.title("Tic-Tac-Toe")
    self.game = Game()
    self.buttons = []
    self.create_board()
  def create_board(self):
    for row in range(3):
      for col in range(3):
        button = tk.Button(self.master, text="", width=10, height=5, command=lambda row=row, col=col: self.button_click(row, col))
        button.grid(row=row, column=col)
        self.buttons.append(button)
  def button_click(self, row, col):
    if self.game.make_move(row, col):
      self.buttons[row * 3 + col].configure(text=self.game.current_player)
      if self.game.is_game_over():
        self.show_winner()
  def show_winner(self):
    winner = self.game.get_winner()
    if winner:
      messagebox.showinfo("Winner", f"{winner} has won the game!")
    else:
      messagebox.showinfo("Tie", "The game ended in a tie.")
    self.master.destroy()
if __name__ == "__main__":
  root = tk.Tk()
  gui = TicTacToeGUI(root)
  root.mainloop()