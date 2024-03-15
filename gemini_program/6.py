import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]
        self.generate_maze()

    def generate_maze(self):

     # Create a stack to store the current cell and its neighbors
        stack = []

        # Start at the top-left corner
        current_cell = (0, 0)

        # While there are still unvisited cells
        while len(stack) > 0 or self.has_unvisited_cells():
            # If the current cell has any unvisited neighbors
            if self.has_unvisited_neighbors(current_cell):
                # Choose a random unvisited neighbor
                neighbor = self.get_random_unvisited_neighbor(current_cell)

                # Add the current cell to the stack
                stack.append(current_cell)

                # Remove the wall between the current cell and its neighbor
                self.remove_wall(current_cell, neighbor)

                # Set the neighbor as the current cell
                current_cell = neighbor

   # If the current cell has no unvisited neighbors
            else:
                # Pop the current cell from the stack
                current_cell = stack.pop()

    def has_unvisited_cells(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col] == 0:
                    return True
        return False

    def has_unvisited_neighbors(self, cell):
        row, col = cell
        if row > 0 and self.cells[row - 1][col] == 0:
            return True
        if row < self.height - 1 and self.cells[row + 1][col] == 0:
            return True
        if col > 0 and self.cells[row][col - 1] == 0:
            return True

        if col < self.width - 1 and self.cells[row][col + 1] == 0:
            return True
        return False

    def get_random_unvisited_neighbor(self, cell):
        row, col = cell
        neighbors = []
        if row > 0 and self.cells[row - 1][col] == 0:
            neighbors.append((row - 1, col))
        if row < self.height - 1 and self.cells[row + 1][col] == 0:
            neighbors.append((row + 1, col))

        if col > 0 and self.cells[row][col - 1] == 0:
            neighbors.append((row, col - 1))
        if col < self.width - 1 and self.cells[row][col + 1] == 0:
            neighbors.append((row, col + 1))
        return random.choice(neighbors)

    def remove_wall(self, cell1, cell2):
        row1, col1 = cell1
        row2, col2 = cell2
        if row1 == row2:
            self.cells[row1][max(col1, col2)] = 1

        else:
            self.cells[max(row1, row2)][col1] = 1

    def is_valid_move(self, cell, direction):
        row, col = cell
        if direction == "up" and row > 0 and self.cells[row - 1][col] == 1:
            return True
        if direction == "down" and row < self.height - 1 and self.cells[row + 1][col] == 1:
            return True
        if direction == "left" and col > 0 and self.cells[row][col - 1] == 1:
            return True
        if direction == "right" and col < self.width - 1 and self.cells[row][col + 1] == 1:
            return True
        return False

    def move(self, cell, direction):
        if self.is_valid_move(cell, direction):
            row, col = cell

            if direction == "up":
                return (row - 1, col)
            if direction == "down":
                return (row + 1, col)
            if direction == "left":
                return (row, col - 1)
            if direction == "right":
                return (row, col + 1)
        return cell

    def __str__(self):
        maze_str = ""
        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col] == 1:
                    maze_str += "#"
                else:

                    maze_str += " "
            maze_str += "\n"
        return maze_str


def play_game(maze):
    current_cell = (0, 0)

    while True:
        print(maze)
        print("Current cell:", current_cell)
        direction = input("Enter a direction (up, down, left, right): ")
        current_cell = maze.move(current_cell, direction)


if __name__ == "__main__":
    width = int(input("Enter the width of the maze: "))
    height = int(input("Enter the height of the maze: "))
    maze = Maze(width, height)
    play_game(maze)