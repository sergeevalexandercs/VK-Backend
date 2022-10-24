from custom_exceptions.exceptions import NotANumberError, OutOfRangeError, OccupiedCellError


class TicTacGame:

    def __init__(self):
        self.board = [i for i in range(0, 10)]
        self.iter = 0
        self.game_over = False
        self.X_moves = []
        self.O_moves = []

    def show_board(self):
        for i in range(3):
            print("--" * 7)
            print("|", self.board[3*i+1], "|", self.board[3*i + 2], "|", self.board[3*i+3], "|")
        print("--" * 7)

    def validate_input(self, player_input):

        if not str.isdigit(player_input):
            raise NotANumberError("It isn't a number")
        if int(player_input) not in [i for i in range(1, 10)]:
            raise OutOfRangeError("Number is out of range")
        if int(player_input) in (self.X_moves or self.O_moves):
            raise OccupiedCellError("Cell is occupied")

        return int(player_input)

    def start_game(self):
        self.show_board()
        while not self.game_over:
            player_number = self.iter % 2
            if player_number == 1:
                player_token = 'O'
            else:
                player_token = 'X'
            move = input(f"Player {player_number + 1}, choose a square on the board: ")

            try:
                self.board[self.validate_input(move)] = player_token
            except NotANumberError as error:
                print(error)
                continue
            except OutOfRangeError as error:
                print(error)
                continue
            except OccupiedCellError as error:
                print(error)
                continue
            print("Went through try except blog")
            move = self.validate_input(move)
            self.O_moves.append(move) if player_number else self.X_moves.append(move)
            self.iter += 1
            self.show_board()
            if self.iter > 4:
                if self.check_winner():
                    self.game_over = True
                elif self.iter == 9:
                    self.game_over = True

        if self.check_winner():
            print(f"Player {(self.iter-1) % 2 + 1} is the winner! Congratulations")
        else:
            print("Game ended level")

    def check_winner(self):
        winner = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                  [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        if sum([set(i).issubset(self.X_moves) for i in winner]) or \
                sum([set(i).issubset(self.O_moves) for i in winner]):
            return True
        else:
            return False


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
