class Game:
  def __init__(self):
    self.board = [['' for _ in range(3)] for _ in range(3)]
    self.current_player = 'X'
  def make_move(self, row, col):
    if self.board[row][col] == '':
      self.board[row][col] = self.current_player
      self.current_player = 'O' if self.current_player == 'X' else 'X'
      return True
    return False
  def is_game_over(self):
    return self.is_winner('X') or self.is_winner('O') or self.is_board_full()
  def is_winner(self, player):
    # Check rows
    for row in range(3):
      if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
        return True
    # Check columns
    for col in range(3):
      if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
        return True
    # Check diagonals
    if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
      return True
    if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
      return True
    return False
  def is_board_full(self):
    for row in range(3):
      for col in range(3):
        if self.board[row][col] == '':
          return False
    return True
  def get_winner(self):
    if self.is_winner('X'):
      return 'X'
    elif self.is_winner('O'):
      return 'O'
    return None