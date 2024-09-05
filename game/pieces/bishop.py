from .a_piece import *

class Bishop(Piece):

    def symbol(self):
        return '♝'

    def move(self, from_row, from_col, to_row, to_col):
        return abs(from_row - to_row) == abs(from_col - to_col)