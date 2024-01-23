from const import constants
Squares = constants["Squares"]


class CheckEqualList:
    @staticmethod
    def _check_if_all_equal(signs: list):
        if signs[0] != "_":
            if signs[0] == signs[1] == signs[2]:
                return True
        return False


class CheckLine(CheckEqualList):
    def check(self, board: Squares) -> bool:
        for line in board:
            signs = []
            signs.extend(line)
            if self._check_if_all_equal(signs):
                return True
        return False


class CheckColumn(CheckEqualList):
    def check(self, board: Squares) -> bool:
        for line in range(3):
            signs = []
            column = [board[0][line], board[1][line], board[2][line]]
            signs.extend(column)
            if self._check_if_all_equal(signs):
                return True
        return False


class CheckDiagonal(CheckEqualList):
    def check(self, board: Squares) -> bool:
        diagonal_1 = [board[0][0], board[1][1], board[2][2]]
        diagonal_2 = [board[0][2], board[1][1], board[2][0]]

        if self._check_if_all_equal(diagonal_1) or self._check_if_all_equal(diagonal_2):
            return True
        return False


class CheckTie(CheckEqualList):
    @staticmethod
    def check(board: Squares):
        for line in board:
            for cell in line:
                if cell == "_":
                    return False
        return True