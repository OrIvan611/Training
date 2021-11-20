from consts import *
from utils import *

"""
This program simulates a rabbits farm. The game is initialized with const.NUMBER_OF_RABBITS random rabbits.
Each turn shows tow stages. At the first stage pregnant rabbits are giving birth and a new rabbit is being placed
somewhere around his mother. At the second stage all the rabbits getting older, step randomly one blank, 
all the girl rabbits who surrounded by boy rabbit are getting pregnant & all the rabbits who turned
eleven years old are dead.
The girls printed in red color, the boys in blue & the pregnant girls in yellow.
"""

rabbits, board = initialize_board()

for iteration in range(ITERATIONS):
    # Rabbits giving birth.
    rabbits_born = []
    for rabbit in rabbits:
        if rabbit.is_pregnant:
            new_rabbit = rabbit.give_birth(board)
            if new_rabbit:
                rabbits_born.append(new_rabbit)
    rabbits = rabbits + rabbits_born

    # Printing the board after rabbits gave birth.
    print(f'iteration {iteration}: \ngirl= {red}, boy= {blue}, pregnant= {yellow} \nAfter giving birth:')
    print_board(board)

    # Rabbits getting older.
    for rabbit in rabbits:
        rabbit.get_old()

    # Rabbits death.
    old_rabbits = []
    for rabbit in rabbits:
        if rabbit.age > DEATH_AGE:
            rabbit.death(board)
            old_rabbits.append(rabbit)

    # Removing dead rabbits from the game.
    for rabbit in old_rabbits:
        rabbits.remove(rabbit)

    # Rabbits getting pregnant.
    for rabbit in rabbits:
        rabbit.get_pregnant(board)

    # Rabbits step randomly.
    for rabbit in rabbits:
        rabbit.step_randomly(board)

    print(f'iteration {iteration}:\nAfter getting pregnant, getting older & moving 1 step randomly: ')
    print_board(board)