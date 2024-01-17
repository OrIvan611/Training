"""
Board - 3*3
Tow players, each of them pick a place to put his sign in.
Winning-
line, column, diagonal
Tie-
if the board is full, but no one won.
"""
# TODO: Add type hints everywhere.

from Player import Player
from Board import Board
from Play import Play
import check_board


def play(board: Board, player1: Player, player2: Player):
    board.print_board()
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


def game_over_message(player1: Player, player2: Player, game_over_reason: str) -> str:
    if player1.is_playing:
        winner = player2.name
    else:
        winner = player1.name

    if game_over_reason == "tie":
        message = "It's a TIE"
    else:
        message = f"{winner} is won!"
    return message


def check_board_status(board: Board, player1: Player, player2: Player) -> bool:
    line = check_board.CheckLine(board.board)
    column = check_board.CheckColumn(board.board)
    diagonal = check_board.CheckDiagonal(board.board)
    tie = check_board.CheckTie(board.board)

    for game_over_reason in [line, column, diagonal, tie]:
        if game_over_reason.check():
            print(board.print_board())
            print(game_over_message(player1, player2, str(game_over_reason)))
            return True
    return False


if __name__ == '__main__':
    board = Board(3, 3)
    player1 = Player('or', 'X', board.board, True)
    player2 = Player('mich', 'O', board.board, False)
    game_over = check_board_status(board, player1, player2)

    while not game_over:
        play(board, player1, player2)
        game_over = check_board_status(board, player1, player2)




