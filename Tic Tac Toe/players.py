# TODO : remove this module
class Players:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def play(self, board):
        # TODO: Why so many Play*()
        location = int(input(f'{self.name}, Pick a place between 0-8: '))

        board[int(location/3)][location%3] = self.sign












