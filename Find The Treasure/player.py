from const import *


class Player:
    def __init__(self):
        self.row = BOARD_SIZE - 1
        self.column = 0
        self.sign = PLAYER_SIGN

    @staticmethod
    def check_by_direction(row, column, board):
        if BOARD_SIZE - 1 < row or row < 0 or BOARD_SIZE - 1 < column or column < 0:
            return True, place_not_valid
        elif board[row][column] == OBSTICALE_SIGN:
            return True, hitting_an_obstacle
        elif board[row][column] == TREASURE_SIGN:
            return True, winning_text
        board[row][column] = PLAYER_SIGN
        return False, ""

    def check_valid_movement_and_winning(self, direction, board):
        """
        This function check if the direction that the user choose is valid.
        If it is, the function change the place of the player.
        If not(the player exited from the board boundaries/the player hit an obstacle), the function return an error
         message and the user lost.
        """

        is_game_over, text = self.check_by_direction(self.row + change_by_direction[direction]["row_value"],
                                                     self.column + change_by_direction[direction]["column_value"],
                                                     board)
        if is_game_over:
            return is_game_over, text, board
        else:
            board[self.row + change_by_direction[direction]["row_value"]][self.column + change_by_direction[direction]["column_value"]] = PLAYER_SIGN
            board[self.row][self.column] = BOARD_START_SIGN
            self.row = self.row + change_by_direction[direction]["row_value"]
            self.column = self.column + change_by_direction[direction]["column_value"]

        return False, "", board

    @staticmethod
    def get_valid_input_of_direction():
        valid_direction = False
        direction_options = [UP_DIRECTION, RIGHT_DIRECTION, DOWN_DIRECTION, LEFT_DIRECTION]

        while not valid_direction:
            direction_input = input("Pick direction: ").upper()
            if direction_input in direction_options:
                valid_direction = True
            else:
                print("Your input is invalid")
        return direction_input

    def movement_and_changing_player_place(self, board):
        """
        This function return True and the board if the player choose valid movement after change the place of the player
        on the board.
        If the player choose an invalid movement the function return text that fit to the player's error.
        """

        direction = self.get_valid_input_of_direction()
        valid_movement, text, new_board = self.check_valid_movement_and_winning(direction, board)

        if valid_movement and text == "":
            new_board[self.row][self.column] = self.sign
            return True, new_board, ""
        elif valid_movement and text != "":
            return True, new_board, text
        return False, new_board, text