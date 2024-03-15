import tkinter as tk
from maze import Maze
class MazeGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maze Game")
        self.geometry("400x400")
        self.maze = Maze()
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()
        self.draw_maze()
        self.bind("<KeyPress>", self.move_player)
        self.game_over = False
    def draw_maze(self):
        for row in range(self.maze.rows):
            for col in range(self.maze.cols):
                if self.maze.maze[row][col] == 1:
                    self.canvas.create_rectangle(col * 40, row * 40, (col + 1) * 40, (row + 1) * 40, fill="black")
        self.canvas.create_rectangle(self.maze.player_row * 40, self.maze.player_col * 40, (self.maze.player_row + 1) * 40, (self.maze.player_col + 1) * 40, fill="red")
        self.canvas.create_rectangle(self.maze.goal_row * 40, self.maze.goal_col * 40, (self.maze.goal_row + 1) * 40, (self.maze.goal_col + 1) * 40, fill="green")
    def move_player(self, event):
        if event.keysym == "Up" and self.maze.player_row > 0 and self.maze.maze[self.maze.player_row - 1][self.maze.player_col] == 0:
            self.maze.player_row -= 1
        elif event.keysym == "Down" and self.maze.player_row < self.maze.rows - 1 and self.maze.maze[self.maze.player_row + 1][self.maze.player_col] == 0:
            self.maze.player_row += 1
        elif event.keysym == "Left" and self.maze.player_col > 0 and self.maze.maze[self.maze.player_row][self.maze.player_col - 1] == 0:
            self.maze.player_col -= 1
        elif event.keysym == "Right" and self.maze.player_col < self.maze.cols - 1 and self.maze.maze[self.maze.player_row][self.maze.player_col + 1] == 0:
            self.maze.player_col += 1
        if self.maze.player_row == self.maze.goal_row and self.maze.player_col == self.maze.goal_col:
            self.game_over = True
        self.draw_maze()
        if self.game_over:
            self.canvas.create_text(200, 200, text="You win!", font=("Arial", 30), fill="blue")
if __name__ == "__main__":
    app = MazeGameApp()
    app.mainloop()