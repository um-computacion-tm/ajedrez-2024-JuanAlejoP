from game.pieces import *

class Board:
    """Representa el tablero de ajedrez con las posiciones de las piezas."""

    def __init__(self):
        """Inicializa un tablero vacío de 8x8."""
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

    def get_piece(self, row, col):
        """Obtiene la pieza en la posición dada.

        Args:
            row (int): Fila de la pieza.
            col (int): Columna de la pieza.

        Returns:
            Piece | None: La pieza en la posición o None si está vacía.
        """
        return self.__positions__[row][col]

    def place_piece(self, piece: Piece, row, col):
        """Coloca una pieza en una posición del tablero.

        Args:
            piece (Piece): La pieza a colocar.
            row (int): Fila donde se colocará la pieza.
            col (int): Columna donde se colocará la pieza.
        """
        self.__positions__[row][col] = piece

    def is_occupied(self, row, col):
        """Verifica si una casilla está ocupada.

        Args:
            row (int): Fila de la casilla.
            col (int): Columna de la casilla.

        Returns:
            bool: True si la casilla está ocupada, False si está vacía.
        """
        return self.get_piece(row, col) is not None

    def within_bounds(self, row, col):
        """Verifica si una posición está dentro de los límites del tablero.

        Args:
            row (int): Fila de la casilla.
            col (int): Columna de la casilla.

        Returns:
            bool: True si está dentro de los límites, False si no lo está.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def has_pieces(self, colour):
        """Verifica si hay piezas de un color en el tablero.

        Args:
            colour (str): Color de las piezas ('BLANCAS' o 'NEGRAS').

        Returns:
            bool: True si hay piezas de ese color, False si no.
        """
        for row in self.__positions__:
            for piece in row:
                if piece and piece.colour == colour:
                    return True
        return False

    def is_path_blocked(self, from_row, from_col, to_row, to_col):
        """Verifica si el camino entre dos casillas está bloqueado.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el camino está bloqueado, False si está libre.
        """
        if from_row == to_row:
            return self.horizontal_path_blocked(from_row, from_col, to_col)
        elif from_col == to_col:
            return self.vertical_path_blocked(from_row, from_col, to_row)
        elif abs(from_row - to_row) == abs(from_col - to_col):
            return self.diagonal_path_blocked(from_row, from_col, to_row, to_col)
        return False

    def horizontal_path_blocked(self, row, from_col, to_col):
        """Verifica si el camino horizontal entre dos casillas está bloqueado.

        Args:
            row (int): Fila de las casillas.
            from_col (int): Columna de origen.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el camino está bloqueado, False si está libre.
        """
        step = 1 if from_col < to_col else -1
        for col in range(from_col + step, to_col, step):
            if self.is_occupied(row, col):
                return True
        return False

    def vertical_path_blocked(self, from_row, col, to_row):
        """Verifica si el camino vertical entre dos casillas está bloqueado.

        Args:
            from_row (int): Fila de origen.
            col (int): Columna de las casillas.
            to_row (int): Fila de destino.

        Returns:
            bool: True si el camino está bloqueado, False si está libre.
        """
        step = 1 if from_row < to_row else -1
        for row in range(from_row + step, to_row, step):
            if self.is_occupied(row, col):
                return True
        return False

    def diagonal_path_blocked(self, from_row, from_col, to_row, to_col):
        """Verifica si el camino diagonal entre dos casillas está bloqueado.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el camino está bloqueado, False si está libre.
        """
        row_step = 1 if from_row < to_row else -1
        col_step = 1 if from_col < to_col else -1
        for row, col in zip(range(from_row + row_step, to_row, row_step),
                            range(from_col + col_step, to_col, col_step)):
            if self.is_occupied(row, col):
                return True
        return False

    def move_piece(self, from_row, from_col, to_row, to_col):
        """Mueve una pieza de una casilla a otra.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Raises:
            ValueError: Si el destino está fuera de los límites.
        """
        piece = self.get_piece(from_row, from_col)

        if not self.within_bounds(to_row, to_col):
            raise ValueError('Movimiento fuera de los límites.')

        self.place_piece(piece, to_row, to_col)
        self.__positions__[from_row][from_col] = None

    def __str__(self):
        """Genera una representación en cadena del tablero de ajedrez.

        Returns:
            str: Representación visual del tablero.
        """
        board_str = '    a   b   c   d   e   f   g   h  \n'
        board_str += '  ' + '-' * 33 + '\n'
        for i, row in enumerate(self.__positions__):
            row_str = f'{i+1} |'
            for piece in row:
                if piece is None:
                    row_str += '   |'
                else:
                    row_str += f' {piece.coloured_symbol()} |'
            board_str += row_str + f' {i+1}\n'
            board_str += '  ' + '-' * 33 + '\n'
        board_str += '    a   b   c   d   e   f   g   h  \n'
        return board_str

class BoardInitializer:
    """Inicializa las piezas en sus posiciones iniciales en el tablero."""

    def __init__(self):
        """Crea las filas traseras de las piezas para las BLANCAS y las NEGRAS."""
        self.white_back_row = [
            Rook('BLANCAS'), Knight('BLANCAS'), Bishop('BLANCAS'),
            Queen('BLANCAS'), King('BLANCAS'), Bishop('BLANCAS'),
            Knight('BLANCAS'), Rook('BLANCAS')
        ]
        self.black_back_row = [
            Rook('NEGRAS'), Knight('NEGRAS'), Bishop('NEGRAS'),
            Queen('NEGRAS'), King('NEGRAS'), Bishop('NEGRAS'),
            Knight('NEGRAS'), Rook('NEGRAS')
        ]

    def initialize(self, board: Board):
        """Coloca todas las piezas en sus posiciones iniciales en el tablero.

        Args:
            board (Board): El tablero donde se colocarán las piezas.
        """
        # Colocar la fila trasera de las blancas
        for col, piece in enumerate(self.white_back_row):
            board.place_piece(piece, 0, col)

        # Colocar los peones blancos
        for col in range(8):
            board.place_piece(Pawn('BLANCAS'), 1, col)

        # Colocar los peones negros
        for col in range(8):
            board.place_piece(Pawn('NEGRAS'), 6, col)

        # Colocar la fila trasera de las negras
        for col, piece in enumerate(self.black_back_row):
            board.place_piece(piece, 7, col)