from utils import *
from player import Player

is_game_over = False
player = Player()
print_rules()
board = create_board()


while not is_game_over:
    print_board(board)

    is_game_over, board, text = player.movement_and_changing_player_place(board)

print(text)

