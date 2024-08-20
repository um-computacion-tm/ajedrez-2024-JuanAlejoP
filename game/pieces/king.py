from .a_piece import *

class King(Piece):
    def __init__(self, colour):
        super().__init__(colour)
    
    def valid_move(self, from_row, from_col, to_row, to_col):
        if (to_row - from_row) > 1 or (to_col - from_col) > 1:
            raise ValueError('La pieza Rey solo puede moverse 1 casilla.')