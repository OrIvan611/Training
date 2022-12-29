from const import *
import random
import copy


def print_board(board):
    for line in board:
        print(line)


def create_board():

    difficulty = input("Choose difficulty: 'E'(easy)/'M'(medium)/'H'(hard): ").upper()

    valid_board = False
    while not valid_board:
        board = [[BOARD_START_SIGN for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        board[BOARD_SIZE - 1][0] = PLAYER_SIGN
        row, column, board_with_treasure = create_treasure_place(board)
        final_board = create_obstacle(board_with_treasure, difficulty)
        final_valid_board = copy.deepcopy(final_board)
        valid_list = check_path([(row, column)], final_board)
        if True in valid_list:
            return final_valid_board


def create_obstacle(board, difficulty):
    obstacle_amount = difficulty_levels[difficulty]

    while obstacle_amount != 0:
        obstacle_row = random.randint(0, BOARD_SIZE - 1)
        obstacle_column = random.randint(0, BOARD_SIZE - 1)

        if board[obstacle_row][obstacle_column] == BOARD_START_SIGN:
            board[obstacle_row][obstacle_column] = OBSTICALE_SIGN
            obstacle_amount -= 1
    return board


def create_treasure_place(board):
    valid_place = False
    while not valid_place:
        treasure_place = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
        if board[treasure_place[0]][treasure_place[1]] == BOARD_START_SIGN:
            valid_place = True
            board[treasure_place[0]][treasure_place[1]] = TREASURE_SIGN
    return treasure_place[0], treasure_place[1], board


def print_rules():
    print("Welcome to the treasure game!\n"
          f"Your goal is to reach the treasure by get to the {TREASURE_SIGN} sign\n"
          "You can move by using:\n"
          f"{UP_DIRECTION} for UP\n{DOWN_DIRECTION} for DOWN\n{RIGHT_DIRECTION} for right\n{LEFT_DIRECTION} for left\n"
          f"You can't hit the {OBSTICALE_SIGN} sign and you can't exit from the board boundaries. \nGood Luck!")


def check_by_direction(row, column, board, new_points):
    valid_way = False
    if row != BOARD_SIZE and row >= 0 and column != BOARD_SIZE and column >= 0:
        if board[row][column] == BOARD_START_SIGN:
            # It means that there is a new point that we need to check
            board[row][column] = 1
            new_points.append((row, column))
        elif board[row][column] == PLAYER_SIGN:
            valid_way = True
    return board, new_points, valid_way


def check_path(points, board):
    new_points = []
    new_valids = []

    for point in points:
        if board[point[0]][point[1]] != OBSTICALE_SIGN:

            for direction in directions:
                board, new_points, valid_way = check_by_direction(point[0] + change_by_direction[direction]["row_value"],
                                                                  point[1] + change_by_direction[direction]["column_value"],
                                                                  board,
                                                                  new_points)
                new_valids.append(valid_way)

    if new_points:
        new_valids += check_path(new_points, board)

    return new_valids

