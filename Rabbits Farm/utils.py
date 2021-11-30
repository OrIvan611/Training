from termcolor import colored
from rabbit import Rabbit
import random
from consts import *
from termcolor import colored



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
            board[line][column] = rabbit
    return rabbits, board


def print_board(board):
    for line in board:
        for point in line:
            if point == BLANK:
                print(colored(point, 'white'), end=',')
            elif point.gender == 'boy':
                print(colored(point.age, 'blue'), end=',')
            elif point.gender == 'girl' and point.is_pregnant == False:
                print(colored(point.age, 'red'), end=',')
            elif point.is_pregnant:
                print(colored(point.age, 'yellow'), end=',')
        print()
