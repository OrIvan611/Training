from players import Players
import copy

line = ['_' for i in range(3)]
board = [copy.copy(line) for i in range(3)]


def print_board(board):
    for line in board:
        print(line)


player1 = Players(name=input('Hello player 1, What is your name? ').upper(), sign=input('Pick your sign X/O: ').upper())
if player1.sign == 'X':
    player2 = Players(name=input('Hello player 2, What is your name? ').upper(), sign='O')
else:
    player2 = Players(name=input('Hello player 2, What is your name? ').upper(), sign='X')


def wining(board):
    # check the lines:
    for line in board:
        if line[0] == line[1] == line[2] != '_':
            return line[0]

    # check columns: (036)(147)(258)
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return board[0][i]

    # check diagonals:
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]


def is_full(board):
    for line in board:
        if line[0] == '_' or line[1] == '_' or line[2] == '_':
            return False
    return True


x = True
while not wining(board) and not is_full(board):
    print_board(board)
    if x:
        player1.play(board)
        x = False
    else:
        player2.play(board)
        x = True

if wining(board):
    if wining(board) == player1.sign:
        print(f'{player1.name}, You won!')
    else:
        print(f'{player2.name}, You won!')

elif is_full(board):
    print("It's a tie..")

