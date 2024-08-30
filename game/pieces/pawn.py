from .a_piece import *

class Pawn(Piece):

    def symbol(self):
        return '♙' if self.colour == 'WHITE' else '♟'

    def move(self, from_row, from_col, to_row, to_col):
        direction = 1 if self.colour == 'WHITE' else -1
        if from_col == to_col:
            if to_row == from_row + direction or (from_row in [1, 6] and to_row == from_row + 2 * direction):
                return True
        return False