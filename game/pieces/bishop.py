from .a_piece import *

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__(colour)
    
    def valid_move(self, from_row, from_col, to_row, to_col):
        if (to_row - from_row) != (to_col - from_col):
                raise ValueError('La pieza Alfil solo puede moverse en diagonal.')