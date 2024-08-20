from .a_piece import *

class Queen(Piece):
    def __init__(self, colour):
        super().__init__(colour)
    
    def valid_move(self, from_row, from_col, to_row, to_col):
        if to_row or to_col not in range(0, 7):
            raise ValueError('La pieza no debe salir del tablero.')