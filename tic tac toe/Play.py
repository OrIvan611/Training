from Board import Board


class Play:
    def __init__(self, board: Board, name: str, sign: str):
        self.board = board
        self._name = name
        self._sign = sign

    def _valid_movement(self, line: int, column: int) -> bool:
        return self.board.board[line][column] == "_"

    @staticmethod
    def _valid_input(user_input: int):
        return 1 <= user_input <= 9

    def _movement(self, line: int, column: int):
        self.board.board[line][column] = self._sign

    def play(self) -> bool:
        location = int(input(f"{self._name}, Pick a place between 1-9: "))
        if self._valid_input(location):
            if location < 4:  # First line
                if self._valid_movement(line=0, column=location-1):
                    self._movement(line=0, column=location-1)
                    return True

            elif location < 7:  # Second line
                if self._valid_movement(line=1, column=location-4):
                    self._movement(line=1, column=location-7)
                    return True

            else:  # Third line:
                if self._valid_movement(line=2, column=location-7):
                    self._movement(line=2, column=location-7)
                    return True
        return False