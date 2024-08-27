from .a_piece import *

class King(Piece):

    def symbol(self):
        return '♔' if self.colour == 'WHITE' else '♚'
    
    def move(self, from_row, from_col, to_row, to_col):
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1