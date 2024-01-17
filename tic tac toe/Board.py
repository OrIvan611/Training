from check_board import CheckTie, CheckLine, CheckColumn, CheckDiagonal


class Board:
    def __init__(self, height: int, width: int):
        self.board = self._initialize_board(height, width)

    @staticmethod
    def _initialize_board(height: int, width: int) -> list:
        return [['_' for _ in range(height)] for _ in range(width)]

    def print_board(self):
        for lst in self.board:
            print(lst)