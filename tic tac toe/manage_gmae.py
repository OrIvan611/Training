from play import Play
from player import Player
from check_board import CheckTie, CheckLine, CheckColumn, CheckDiagonal
from const import constants
Squares = constants["Squares"]


class ManageGame:
    @staticmethod
    def play(board: Squares, player1: Player, player2: Player):
        print(board)
        if player1.is_playing:
            if Play(board, player1.name, player1.sign).play():
                player1.is_playing = False
                player2.is_playing = True
            else:
                print("Location not valid. Please try again. ")
        else:
            if Play(board, player2.name, player2.sign).play():
                player1.is_playing = True
                player2.is_playing = False

    @staticmethod
    def run_the_game(board: Squares, is_game_over: bool, player1: Player, player2: Player):
        while not is_game_over:
            ManageGame.play(board, player1, player2)
            is_game_over = ManageGame.check_board_status(board, player1, player2)

    @staticmethod
    def initialize_game_over_message(player1: Player, player2: Player, game_over_reason: str) -> str:
        winner = player2.name if player1.is_playing else player1.name
        message = "It's a TIE" if game_over_reason == "tie" else f"{winner} is won!"
        return message

    @staticmethod
    def check_board_status(board: Squares, player1: Player, player2: Player) -> bool:
        line = CheckLine()
        column = CheckColumn()
        diagonal = CheckDiagonal()
        tie = CheckTie()

        for game_over_reason in [line, column, diagonal, tie]:
            if game_over_reason.check(board):
                print(f"{ManageGame.initialize_game_over_message(player1, player2, str(game_over_reason))}")
                return True
        return False
