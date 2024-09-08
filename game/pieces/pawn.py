from .a_piece import *

class Pawn(Piece):
    """Clase que representa un Peón en el juego de ajedrez."""

    def symbol(self):
        """Devuelve el símbolo que representa al Peón.

        Returns:
            str: El símbolo ♟ que representa al Peón.
        """
        return '♟'

    def move(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento es válido para un Peón.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        direction = 1 if self.colour == 'BLANCAS' else -1
        if from_col == to_col:
            if to_row == from_row + direction or (from_row in [1, 6] and \
            to_row == from_row + 2 * direction):
                return True
        return False