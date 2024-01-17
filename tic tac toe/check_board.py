class CheckEqualList:
    def __init__(self, board: list):
        self._board = board

    @staticmethod
    def _check_if_all_equal(signs: list):
        if signs[0] != "_":
            if signs[0] == signs[1] == signs[2]:
                return True
        return False


class CheckLine(CheckEqualList):
    def check(self) -> bool:
        for line in self._board:
            signs = []
            signs.extend(line)
            if self._check_if_all_equal(signs):
                return True
        return False


class CheckColumn(CheckEqualList):
    def check(self) -> bool:
        for line in range(3):
            signs = []
            column = [self._board[0][line], self._board[1][line], self._board[2][line]]
            signs.extend(column)
            if self._check_if_all_equal(signs):
                return True
        return False


class CheckDiagonal(CheckEqualList):
    def check(self) -> bool:
        diagonal_1 = [self._board[0][0], self._board[1][1], self._board[2][2]]
        diagonal_2 = [self._board[0][2], self._board[1][1], self._board[2][0]]

        if self._check_if_all_equal(diagonal_1) or self._check_if_all_equal(diagonal_2):
            return True
        return False


class CheckTie(CheckEqualList):
    def check(self):
        for line in self._board:
            for cell in line:
                if cell == "_":
                    return False
        return True