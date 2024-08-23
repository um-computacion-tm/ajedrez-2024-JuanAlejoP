from .a_piece import *

class Pawn(Piece):
    def __init__(self, colour):
        super().__init__(colour)

    def symbol(self):
        return '♙' if self.colour == 'WHITE' else '♟'

    def valid_move(self, from_row, from_col, to_row, to_col):
        direction = 1 if self.colour == 'WHITE' else -1
        if from_col == to_col:
            #Movimiento hacia adelante
            if to_row == from_row + direction:
                return True
            #Movimiento de dos casillas desde la posición inicial
            if (from_row == 1 or from_row == 6) and to_row == from_row + 2 * direction:
                return True
        elif abs(from_col - to_col) == 1 and to_row == from_row + direction:
            #Captura en diagonal
            return True
        return False