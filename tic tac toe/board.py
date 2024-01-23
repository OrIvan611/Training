from const import constants
Squares = constants["Squares"]


class Board:
    def __init__(self, height: int, width: int):
        self.board = self._initialize_board(height, width)

    @staticmethod
    def _initialize_board(height: int, width: int) -> Squares:
        return [['_' for _ in range(height)] for _ in range(width)]

    def __str__(self):
        lines = []
        for lst in self.board:
            lines.append("  " + ", ".join(map(str, lst)) + "\n")
        return "".join(lines)