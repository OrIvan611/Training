BOARD_SIZE = 5
BOARD_START_SIGN = "_"
UP_DIRECTION = "U"
RIGHT_DIRECTION = "K"
DOWN_DIRECTION = "J"
LEFT_DIRECTION = "H"
OBSTICALE_SIGN = "X"
TREASURE_SIGN = "T"
PLAYER_SIGN = "P"

change_by_direction = {
    UP_DIRECTION: {
        "row_value": -1,
        "column_value": 0
    },
    DOWN_DIRECTION: {
        "row_value": +1,
        "column_value": 0
    },
    RIGHT_DIRECTION: {
        "row_value": 0,
        "column_value": +1
    },
    LEFT_DIRECTION: {
        "row_value": 0,
        "column_value": -1
    }
}

place_not_valid = "You exited from the board boundaries"
hitting_an_obstacle = "You hit an obstacle"
winning_text = "You won!!!"

difficulty_levels = {
    "E": 5,
    "M": 7,
    "H": 10
}

directions = [UP_DIRECTION, DOWN_DIRECTION, RIGHT_DIRECTION, LEFT_DIRECTION]