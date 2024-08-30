from .a_piece import *

class Queen(Piece):

    def symbol(self):
        return '♕' if self.colour == 'WHITE' else '♛'

    def move(self, from_row, from_col, to_row, to_col):
        return MovementValidator.is_straight_line(from_row, from_col, to_row, to_col) or \
               MovementValidator.is_diagonal(from_row, from_col, to_row, to_col)