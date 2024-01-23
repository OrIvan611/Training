from const import constants
Squares = constants["Squares"]


class Player:
    def __init__(self, name: str, sign: str, board: Squares, is_playing: bool):
        self.sign = sign
        self.name = name
        self.is_playing = is_playing
        self._board = board