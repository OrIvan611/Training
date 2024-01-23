"""
Board - 3*3
Tow players, each of them pick a place to put his sign in.
Winning-
line, column, diagonal
Tie-
if the board is full, but no one won.
"""

from player import Player
from board import Board
from manage_gmae import ManageGame


if __name__ == '__main__':
    board = Board(3, 3)
    player1 = Player('or', 'X', board.board, True)
    player2 = Player('mich', 'O', board.board, False)
    is_game_over = ManageGame.check_board_status(board.board, player1, player2)
    ManageGame.run_the_game(board.board, is_game_over, player1, player2)






