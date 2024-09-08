from .a_piece import *

class Queen(Piece):
    """Clase que representa una Reina en el juego de ajedrez."""

    def symbol(self):
        """Devuelve el símbolo que representa a la Reina.

        Returns:
            str: El símbolo ♛ que representa a la Reina.
        """
        return '♛'

    def move(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento es válido para una Reina.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        return (from_row == to_row or from_col == to_col) or \
               abs(from_row - to_row) == abs(from_col - to_col)