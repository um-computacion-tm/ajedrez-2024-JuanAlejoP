from .a_piece import *

class Bishop(Piece):

    def symbol(self):
        return '♗' if self.colour == 'WHITE' else '♝'

    def move(self, from_row, from_col, to_row, to_col):
        return MovementValidator.is_diagonal(from_row, from_col, to_row, to_col)