from termcolor import colored
from rabbit import Rabbit
import random
from consts import *


def initialize_board():
    board = [(BOARD_PIXELS * [BLANK]) for i in range(BOARD_PIXELS)]

    rabbits = []
    rabbit_counter = 0
    while rabbit_counter < NUMBER_OF_RABBITS:
        line = random.randint(0, BOARD_PIXELS - 1)
        column = random.randint(0, BOARD_PIXELS - 1)

        if board[line][column] != BLANK:
            continue
        else:
            rabbit = Rabbit(age=random.randint(0,10), gender=random.choice(['boy', 'girl']), line=line, column=column)
            rabbits.append(rabbit)
            rabbit_counter += 1
            board[line][column] = (rabbit.age, rabbit.gender)
    return rabbits, board


colors = {'boy': 'blue', 'girl': 'red', 'Pregnant': 'yellow', BLANK: 'white'}


def print_board(board):
    for line in board:
        for character in line:
            if character == BLANK:
                print(colored(character, colors[character]), end=',')
            else:
                print(colored(character[0], colors[character[1]]), end=',')
        print()