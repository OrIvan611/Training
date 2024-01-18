from check_board import CheckTie, CheckLine, CheckColumn, CheckDiagonal
#TODO: Remove not used imports: ctrl + alt + o (i want you to learn also about ctrl + alt + l)
#TODO: Every module name should be in lower case and separated by underscore. For example: check_board.py
#TODO: Read about PEP8

#TODO: Squares = list[list[str]]

class Board:
    def __init__(self, height: int, width: int):
        self.board = self._initialize_board(height, width)

    @staticmethod
    def _initialize_board(height: int, width: int):  # #TODO: list[list[str]]
        return [['_' for _ in range(height)] for _ in range(width)]

    # TODO: use __str__


    def print_board(self):
        for lst in self.board:
            print(lst)