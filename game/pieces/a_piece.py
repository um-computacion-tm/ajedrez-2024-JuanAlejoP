class Piece:
    def __init__(self, colour):
        self.__colour__ = colour

    def valid_move(self, from_row, from_col, to_row, to_col):
        return True

    def within_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8