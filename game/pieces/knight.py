from .a_piece import *

class Knight(Piece):

    def symbol(self):
        return '♘' if self.colour == 'WHITE' else '♞'

    def move(self, from_row, from_col, to_row, to_col):
        return MovementValidator.is_knight_move(from_row, from_col, to_row, to_col)