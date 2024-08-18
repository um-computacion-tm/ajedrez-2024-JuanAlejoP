class Piece:
    def __init__(self, colour):
        self.__colour__ = colour

class Pawn(Piece):
    def __init__(self, colour):
        super().__init__(colour)

class Rook(Piece):
    def __init__(self, colour):
        super().__init__(colour)

    def valid_move(self, from_row, from_col, to_row, to_col):
        return from_row == to_row or from_col == to_col

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__(colour)

class Knight(Piece):
    def __init__(self, colour):
        super().__init__(colour)

class Queen(Piece):
    def __init__(self, colour):
        super().__init__(colour)

class King(Piece):
    def __init__(self, colour):
        super().__init__(colour)