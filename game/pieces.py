class Piece:
    def __init__(self, colour):
        self.__colour__ = colour

class Pawn(Piece):
    def __init__(self, colour):
        super().__init__(colour)

    #revisar
    def valid_move(self, from_row, to_row, to_col):
        if self.__colour__ == 'WHITE' and from_row == 1:
            if to_row <= 2:
                return to_row, to_col
        if self.__colour__ == 'BLACK' and from_row == 6:
            if to_row <= 2:
                return to_row, to_col
        else:
            if to_row != 1:
                raise ValueError('La pieza Peón solo puede moverse 1 lugar.')
                
class Rook(Piece):
    def __init__(self, colour):
        super().__init__(colour)

    def valid_move(self, from_row, from_col, to_row, to_col):
        return from_row == to_row or from_col == to_col

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__(colour)
    
    def valid_move(self, from_row, from_col, to_row, to_col):
        if (to_row - from_row) != (to_col - from_col):
                raise ValueError('La pieza Alfil solo puede moverse en diagonal.')

class Knight(Piece):
    def __init__(self, colour):
        super().__init__(colour)

class Queen(Piece):
    def __init__(self, colour):
        super().__init__(colour)

class King(Piece):
    def __init__(self, colour):
        super().__init__(colour)
    
    def valid_move(self, from_row, from_col, to_row, to_col):
        if (to_row - from_row) > 1 or (to_col - from_col) > 1:
            raise ValueError('La pieza Rey solo puede moverse 1 casilla.')