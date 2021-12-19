import random

# In this project we have a board that contains numbers. Each number simulates minutes.
# We calculate the shortest "time" to get from the first point to the last point whit the condition that we
# can move only down and right.

BOARD_SIZE = 4
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 10
board = [[random.randint(LOWEST_NUMBER, HIGHEST_NUMBER) for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board):
    for line in board:
        print(line)


def find_shortest_path(board):
    """
    This function finds the shortest path from each pixel to the end point, using dynamic programing.
    """
    for j in range(1, BOARD_SIZE + 1):
        # Each iteration we start from the diagonal. From the end point to the start point.
        line = BOARD_SIZE - j
        column = BOARD_SIZE - j

        # Other than the end point, we check the diagonal's right and down.
        if line < BOARD_SIZE - 1:
            check_right_and_down(board, line, column)

        for i in range(1, BOARD_SIZE - j + 1):
            if j == 1:
                # Here we are on the boundary of the board so we only have one way to go.
                board[line - i][column] += board[line - i + 1][column]
                board[line][column - i] += board[line][column - i + 1]
            else:
                check_right_and_down(board, line - i, column)
                check_right_and_down(board, line, column - i)


def check_right_and_down(board, line, column):
    """
    This function changes the number to the sum of itself and the minimum number between the number on his right
    and the number below it.
    """
    check_line = line + 1
    check_column = column + 1
    if board[check_line][column] < board[line][check_column]:
        board[line][column] += board[check_line][column]
    else:
        board[line][column] += board[line][check_column]


print_board(board)
find_shortest_path(board)
print('The result:')
print_board(board)
print(f'The shortest path: {board[0][0]}')