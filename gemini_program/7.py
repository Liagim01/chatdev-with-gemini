import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 game board
        self.player1 = 'X'
        self.player2 = 'O'
        self.current_player = self.player1

    def print_board(self):

  # This function prints the current game board
        print('-------------')
        for i in range(3):
            print('|', self.board[i*3], '|', self.board[i*3+1], '|', self.board[i*3+2], '|')
        print('-------------')

    def check_win(self, player):

 # This function checks if the given player has won the game
        win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),      # Horizontal rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),      # Vertical columns
                        (0, 4, 8), (2, 4, 6))              # Diagonals
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == player:
                return True
        return False

    def check_draw(self):
        # This function checks if the game is a draw
        return ' ' not in self.board

    def switch_player(self):
        # This function switches the current player
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def get_player_move(self, player):
        # This function gets the player's move
        while True:
            try:
                move = int(input(f'{player} (1-9): ')) - 1

                if 0 <= move < 9 and self.board[move] == ' ':
                    return move
                else:
                    print("Invalid move, please try again.")
            except ValueError:
                print("Invalid move, please try again.")

    def start_game(self):
        # This function starts the game loop
        self.print_board()
        while True:
            move = self.get_player_move(self.current_player)
            self.board[move] = self.current_player
            self.print_board()
            if self.check_win(self.current_player):
                print(f'{self.current_player} wins!')
                break
            elif self.check_draw():
                print("It's a draw!")
                break
            else:
                self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()