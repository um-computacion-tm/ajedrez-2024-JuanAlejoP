from game.board import *

class Chess:
    """Clase principal para manejar el juego de ajedrez.

    Args:
        board_initializer (BoardInitializer, optional): Inicializa el tablero si no se proporciona uno.
    """
    
    def __init__(self, board_initializer=None):
        self.__board__ = Board()
        if board_initializer is None:
            board_initializer = BoardInitializer()
        board_initializer.initialize(self.__board__)
        self.kings = {
            'BLANCAS': self.__board__.__positions__[0][4],
            'NEGRAS': self.__board__.__positions__[7][4]
            }
        self.__turn__ = 'BLANCAS'
        self.game_over = False

    @property
    def board(self):
        """Obtiene el tablero actual.

        Returns:
            Board: El tablero del juego.
        """
        return self.__board__

    @property
    def turn(self):
        """Obtiene el turno actual (BLANCAS o NEGRAS).

        Returns:
            str: El turno actual.
        """
        return self.__turn__

    def move(self, from_row, from_col, to_row, to_col):
        """Realiza un movimiento en el tablero.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Raises:
            ValueError: Si el movimiento es inválido.
        """
        piece = self.__board__.get_piece(from_row, from_col)
        target_piece = self.__board__.get_piece(to_row, to_col)

        if piece is None:
            raise ValueError('No hay pieza en esa posición.')
        if not self.is_valid_move(piece, from_row, from_col, to_row, to_col):
            raise ValueError('Movimiento inválido para esa pieza.')
        if not isinstance(piece, Knight) and \
            self.__board__.is_path_blocked(from_row, from_col, to_row, to_col):
            raise ValueError('El camino está bloqueado por otra pieza.')
        if piece.colour != self.__turn__:
            raise ValueError(f'Es turno de las {self.turn}.')
        if target_piece and target_piece.colour == piece.colour:
            raise ValueError('No podés capturar piezas de tu mismo color.')
        if not self.__board__.has_pieces(self.__turn__):
            self.end_game(f'\n¡No quedan piezas {self.__turn__}!')
            self.change_turn()
            print(f'¡Ganan las {self.__turn__}!')
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        if isinstance(target_piece, King):
            self.end_game(f'\n¡El rey de las {target_piece.colour} ha sido capturado!')
            print(f'¡Ganan las {self.__turn__}!')
        else:
            self.change_turn()

    def is_valid_move(self, piece, from_row, from_col, to_row, to_col):
        """Valida si un movimiento es correcto para la pieza dada.

        Args:
            piece (Piece): La pieza a mover.
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        if isinstance(piece, Pawn):
            return self.is_valid_pawn_move(piece, from_row, from_col, to_row, to_col)
        if not piece.move(from_row, from_col, to_row, to_col):
            return False
        return True

    def is_valid_pawn_move(self, pawn, from_row, from_col, to_row, to_col):
        """Valida el movimiento de un peón.

        Args:
            pawn (Pawn): Peón a mover.
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        direction = 1 if pawn.colour == 'BLANCAS' else -1
        
        if from_col == to_col:
            if to_row == from_row + direction and not self.__board__.is_occupied(to_row, to_col):
                return True
            if (from_row == 1 or from_row == 6) and to_row == from_row + 2 * direction and not \
                self.__board__.is_occupied(to_row, to_col):
                return True
        elif abs(from_col - to_col) == 1 and to_row == from_row + direction:
            if self.__board__.is_occupied(to_row, to_col) and \
                self.__board__.get_piece(to_row, to_col).colour != pawn.colour:
                return True
        return False

    def change_turn(self):
        """Cambia el turno entre BLANCAS y NEGRAS."""
        self.__turn__ = 'NEGRAS' if self.__turn__ == 'BLANCAS' else 'BLANCAS'

    def end_game(self, message):
        """Finaliza el juego con un mensaje.

        Args:
            message (str): Mensaje a mostrar al finalizar el juego.
        """
        self.game_over = True
        print(message)