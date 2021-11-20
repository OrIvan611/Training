import random
from consts import * 


class Rabbit():
    def __init__(self, age, gender, line, column):
        self.is_pregnant = False
        self.column = column
        self.line = line
        self.gender = gender
        self.age = age

    def step_randomly(self, world_board):
        direction = random.choice([UP, DOWN, LEFT, RIGHT])
        world_board[self.line][self.column] = BLANK

        if direction == UP:
            self.line -= 1
            if self.line == -1:
                self.line = BOARD_PIXELS - 1
            if world_board[self.line][self.column] != BLANK:
                self.line += 1
                if self.line == BOARD_PIXELS :
                    self.line = 0

        if direction == DOWN:
            self.line += 1
            if self.line == BOARD_PIXELS :
                self.line = 0
            if world_board[self.line][self.column] != BLANK:
                self.line -= 1
                if self.line == -1:
                    self.line = BOARD_PIXELS - 1

        if direction == RIGHT:
            self.column += 1
            if self.column == BOARD_PIXELS :
                self.column = 0
            if world_board[self.line][self.column] != BLANK:
                self.column -= 1
                if self.column == -1:
                    self.column = BOARD_PIXELS - 1

        if direction == LEFT:
            self.column -= 1
            if self.column == -1:
                self.column = BOARD_PIXELS - 1
            if world_board[self.line][self.column] != BLANK:
                self.column += 1
                if self.column == BOARD_PIXELS:
                    self.column = 0

        if self.is_pregnant:
            world_board[self.line][self.column] = (self.age, 'Pregnant')
        else:
            world_board[self.line][self.column] = (self.age, self.gender)

    def get_old(self):
        self.age += 1

    def death(self, world_board):
        world_board[self.line][self.column] = BLANK

    def check_if_boy_is_up(self, world_board):
        check_line = self.line - 1
        if check_line == -1:
            check_line = BOARD_PIXELS - 1
        if world_board[check_line][self.column] != BLANK:
            if world_board[check_line][self.column][1] == 'boy':
                return True

    def check_if_boy_is_down(self, world_board):
        check_line = self.line + 1
        if check_line == BOARD_PIXELS:
            check_line = 0
        if world_board[check_line][self.column] != BLANK:
            if world_board[check_line][self.column][1] == 'boy':
                return True

    def check_if_boy_is_right(self, world_board):
        check_column = self.column + 1
        if check_column == BOARD_PIXELS:
            check_column = 0
        if world_board[self.line][check_column] != BLANK:
            if world_board[self.line][check_column][1] == 'boy':
                return True

    def check_if_boy_is_left(self, board):
        check_column = self.column - 1
        if check_column == -1:
            check_column = BOARD_PIXELS - 1
        if board[self.line][check_column] != BLANK:
            if board[self.line][check_column][1] == 'boy':
                return True

    def check_if_pregnant(self, board):
        if self.gender == 'girl':
            if self.check_if_boy_is_up(board):
                return True
            if self.check_if_boy_is_left(board):
                return True
            if self.check_if_boy_is_right(board):
                return True
            if self.check_if_boy_is_down(board):
                return True

    def get_pregnant(self, board):
        if self.check_if_pregnant(board):
            self.is_pregnant = True

    def _give_birth(self, line, column, board):
        if board[line][column] == BLANK:
            new_rabbit = Rabbit(age=0, gender=random.choice(['boy', 'girl']), line=line, column=column)
            board[line][column] = (new_rabbit.age, new_rabbit.gender)
            self.is_pregnant = False
            return new_rabbit

    def give_birth(self, board):
        # Check Up
        check_line = self.line - 1
        if check_line == -1:
            check_line = BOARD_PIXELS - 1
        rabbit = self._give_birth(line=check_line, column=self.column, board=board)
        if rabbit:
            return rabbit

        # Check Down
        check_line = self.line + 1
        if check_line == BOARD_PIXELS:
            check_line = 0
        rabbit = self._give_birth(line=check_line, column=self.column, board=board)
        if rabbit:
            return rabbit

        # Check Left
        check_column = self.column - 1
        if check_column == -1:
            check_column = BOARD_PIXELS - 1
        rabbit = self._give_birth(line=self.line, column=check_column, board=board)
        if rabbit:
            return rabbit

        # Check Right
        check_column = self.column + 1
        if check_column == BOARD_PIXELS:
            check_column = 0
        rabbit = self._give_birth(line=self.line, column=check_column, board=board)
        if rabbit:
            return rabbit















