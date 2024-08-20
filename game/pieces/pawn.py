from .a_piece import *

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