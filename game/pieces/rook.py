from .a_piece import *

class Rook(Piece):

    def symbol(self):
        return '♖' if self.colour == 'WHITE' else '♜'

    def move(self, from_row, from_col, to_row, to_col):
        return from_row == to_row or from_col == to_col