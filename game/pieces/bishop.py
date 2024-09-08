from .a_piece import *

class Bishop(Piece):
    """Clase que representa el alfil en el juego de ajedrez."""

    def symbol(self):
        """Devuelve el símbolo del alfil.

        Returns:
            str: El símbolo '♝' que representa al alfil.
        """
        return '♝'

    def move(self, from_row, from_col, to_row, to_col):
        """Valida si el movimiento realizado es válido para un alfil.

        Un alfil se mueve en diagonal, lo que significa que el número de filas y columnas
        que se mueve deben ser iguales.

        Args:
            from_row (int): Fila de origen del movimiento.
            from_col (int): Columna de origen del movimiento.
            to_row (int): Fila de destino del movimiento.
            to_col (int): Columna de destino del movimiento.

        Returns:
            bool: True si el movimiento es válido para un alfil, False en caso contrario.
        """
        return abs(from_row - to_row) == abs(from_col - to_col)