import random
class Game:
  def __init__(self):
    self.grid = [[0] * 10 for _ in range(10)]
    self.add_random_tile()
    self.add_random_tile()
  def add_random_tile(self):
    empty_spots = []
    for row in range(10):
      for col in range(10):
        if self.grid[row][col] == 0:
          empty_spots.append((row, col))
    if empty_spots:
      row, col = random.choice(empty_spots)
      self.grid[row][col] = random.choice([2, 4])
  def move_up(self):
    self.move_tiles("up")
    self.merge_tiles("up")
    self.move_tiles("up")
    self.add_random_tile()
  def move_down(self):
    self.move_tiles("down")
    self.merge_tiles("down")
    self.move_tiles("down")
    self.add_random_tile()
  def move_left(self):
    self.move_tiles("left")
    self.merge_tiles("left")
    self.move_tiles("left")
    self.add_random_tile()
  def move_right(self):
    self.move_tiles("right")
    self.merge_tiles("right")
    self.move_tiles("right")
    self.add_random_tile()
  def move_tiles(self, direction):
    if direction == "up":
      for col in range(10):
        self.move_column_up(col)
    elif direction == "down":
      for col in range(10):
        self.move_column_down(col)
    elif direction == "left":
      for row in range(10):
        self.move_row_left(row)
    elif direction == "right":
      for row in range(10):
        self.move_row_right(row)
  def move_column_up(self, col):
    for row in range(1, 10):
      self.move_tile(row, col, -1, 0)
  def move_column_down(self, col):
    for row in range(8, -1, -1):
      self.move_tile(row, col, 1, 0)
  def move_row_left(self, row):
    for col in range(1, 10):
      self.move_tile(row, col, 0, -1)
  def move_row_right(self, row):
    for col in range(8, -1, -1):
      self.move_tile(row, col, 0, 1)
  def move_tile(self, row, col, row_offset, col_offset):
    if self.grid[row][col] == 0:
      return
    next_row = row + row_offset
    next_col = col + col_offset
    if self.grid[next_row][next_col] == 0:
      self.grid[next_row][next_col] = self.grid[row][col]
      self.grid[row][col] = 0
    elif self.grid[next_row][next_col] == self.grid[row][col]:
      self.grid[next_row][next_col] *= 2
      self.grid[row][col] = 0
  def merge_tiles(self, direction):
    if direction == "up":
      for col in range(10):
        self.merge_column_up(col)
    elif direction == "down":
      for col in range(10):
        self.merge_column_down(col)
    elif direction == "left":
      for row in range(10):
        self.merge_row_left(row)
    elif direction == "right":
      for row in range(10):
        self.merge_row_right(row)
  def merge_column_up(self, col):
    for row in range(1, 10):
      if self.grid[row][col] == self.grid[row - 1][col]:
        self.grid[row - 1][col] *= 2
        self.grid[row][col] = 0
  def merge_column_down(self, col):
    for row in range(8, -1, -1):
      if self.grid[row][col] == self.grid[row + 1][col]:
        self.grid[row + 1][col] *= 2
        self.grid[row][col] = 0
  def merge_row_left(self, row):
    for col in range(1, 10):
      if self.grid[row][col] == self.grid[row][col - 1]:
        self.grid[row][col - 1] *= 2
        self.grid[row][col] = 0
  def merge_row_right(self, row):
    for col in range(8, -1, -1):
      if self.grid[row][col] == self.grid[row][col + 1]:
        self.grid[row][col + 1] *= 2
        self.grid[row][col] = 0
  def is_game_over(self):
    for row in range(10):
      for col in range(10):
        if self.grid[row][col] == 0:
          return False
    for row in range(1, 10):
      for col in range(10):
        if self.grid[row][col] == self.grid[row - 1][col]:
          return False
    for row in range(10):
      for col in range(1, 10):
        if self.grid[row][col] == self.grid[row][col - 1]:
          return False
    return True