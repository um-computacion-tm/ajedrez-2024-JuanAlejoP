from .a_piece import *

class Rook(Piece):
    """Clase que representa una Torre en el juego de ajedrez."""

    def symbol(self):
        """Devuelve el símbolo que representa a la Torre.

        Returns:
            str: El símbolo ♜ que representa a la Torre.
        """
        return '♜'

    def move(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento es válido para una Torre.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        return from_row == to_row or from_col == to_col