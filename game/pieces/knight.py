from .a_piece import *

class Knight(Piece):

    def symbol(self):
        return '♘' if self.colour == 'WHITE' else '♞'

    def move(self, from_row, from_col, to_row, to_col):
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)