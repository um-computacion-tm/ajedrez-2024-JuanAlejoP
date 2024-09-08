from .a_piece import *

class Knight(Piece):
    """Clase que representa un Caballo en el juego de ajedrez."""

    def symbol(self):
        """Devuelve el símbolo que representa al Caballo.

        Returns:
            str: El símbolo ♞ que representa al Caballo.
        """
        return '♞'

    def move(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento es válido para un Caballo.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        return self.is_knight_move(from_row, from_col, to_row, to_col)

    def is_knight_move(self, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento sigue el patrón de un Caballo.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento cumple con el patrón de un Caballo, False en caso contrario.
        """
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)