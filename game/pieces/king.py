from .a_piece import *

class King(Piece):
    """Clase que representa al rey en el juego de ajedrez."""

    def symbol(self):
        """Devuelve el símbolo del rey.

        Returns:
            str: El símbolo '♚' que representa al rey.
        """
        return '♚'

    def move(self, from_row, from_col, to_row, to_col):
        """Valida si el movimiento realizado es válido para un rey.

        Un rey se mueve una casilla en cualquier dirección (horizontal, vertical o diagonal).

        Args:
            from_row (int): Fila de origen del movimiento.
            from_col (int): Columna de origen del movimiento.
            to_row (int): Fila de destino del movimiento.
            to_col (int): Columna de destino del movimiento.

        Returns:
            bool: True si el movimiento es válido para un rey, False en caso contrario.
        """
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1