from .a_piece import *

class Knight(Piece):

    def symbol(self):
        return '♘' if self.colour == 'WHITE' else '♞'

    def move(self, from_row, from_col, to_row, to_col):
        return self.is_knight_move(from_row, from_col, to_row, to_col)
    
    def is_knight_move(self, from_row, from_col, to_row, to_col):
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)