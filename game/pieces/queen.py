from .a_piece import *

class Queen(Piece):
    def __init__(self, colour):
        super().__init__(colour)
    
    def valid_move(self, from_row, from_col, to_row, to_col):
        pass