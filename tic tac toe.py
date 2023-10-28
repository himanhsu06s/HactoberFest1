class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-'*5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move! Try again.")

    def check_win(self):
        for i in range(3):
            # Check rows and columns
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def start_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while True:
            self.print_board()
            row = int(input(f"Player {self.current_player}, enter the row (0-2): "))
            col = int(input(f"Player {self.current_player}, enter the column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                self.make_move(row, col)
                if self.check_win():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                elif self.check_draw():
                    self.print_board()
                    print("It's a draw!")
                    break
            else:
                print("Invalid input! Try again.")

            # Option to play again
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == 'yes':
                self.board = [[' ' for _ in range(3)] for _ in range(3)]
                self.current_player = 'X'
            else:
                print("Thank you for playing!")
                break


# Start the game
if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
