class Piece:
    def __init__(self, colour):
        self.__colour__ = colour

class Pawn(Piece):
    def __init__(self, colour):
        super().__init__(colour)

class Rook(Piece):
    def __init__(self, colour):
        super().__init__(colour)

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