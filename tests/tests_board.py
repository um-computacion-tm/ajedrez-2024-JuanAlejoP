import unittest
from game.board import Board, Pawn, Rook, Bishop, Knight, Queen, King, BoardInitializer

class TestBoard(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Board.

    Métodos:
        setUp(): Configura el tablero y lo inicializa antes de cada prueba.
        test_initial_setup(): Verifica la configuración inicial del tablero de ajedrez.
        test_get_piece(): Verifica la obtención de piezas en posiciones específicas.
        test_within_bounds(): Verifica que las coordenadas estén dentro de los límites del tablero.
        test_is_occupied(): Verifica si una casilla está ocupada por una pieza.
        test_is_path_blocked(): Verifica si el camino entre dos casillas está bloqueado por piezas.
        test_move_piece(): Verifica que una pieza se mueva correctamente de una casilla a otra.
    """

    def setUp(self):
        """
        Configura un nuevo tablero y lo inicializa antes de cada prueba.

        Se crea un objeto Board y se inicializa con las piezas usando BoardInitializer.
        """
        self.board = Board()
        initializer = BoardInitializer()
        initializer.initialize(self.board)

    def test_initial_setup(self):
        """
        Verifica que la configuración inicial del tablero sea correcta.

        Se espera que las piezas estén en sus posiciones iniciales correctas:
        - Las torres en las esquinas.
        - Los caballos junto a las torres.
        - Los alfiles junto a los caballos.
        - La reina y el rey en el centro.
        - Los peones en la segunda y séptima fila.
        - Las casillas vacías en la tercera y cuarta fila.
        """
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)

        for row in range(8):
            for col in range(8):
                if row == 1 or row == 6:
                    self.assertIsInstance(self.board.get_piece(row, col), Pawn)
                elif 2 <= row <= 5:
                    self.assertIsNone(self.board.get_piece(row, col))

        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        self.assertIsInstance(self.board.get_piece(7, 4), King)
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 6), Knight)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)

    def test_get_piece(self):
        """
        Verifica la obtención de una pieza en una posición específica.

        Se espera que la pieza en (0, 0) sea una torre blanca.
        """
        piece = self.board.get_piece(0, 0)
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.colour, 'BLANCAS')

    def test_within_bounds(self):
        """
        Verifica que las coordenadas estén dentro de los límites del tablero.

        Se espera que las coordenadas (0, 0) y (7, 7) estén dentro de los límites,
        mientras que las coordenadas (-1, 0) y (0, 8) no lo estén.
        """
        self.assertTrue(self.board.within_bounds(0, 0))
        self.assertTrue(self.board.within_bounds(7, 7))
        self.assertFalse(self.board.within_bounds(-1, 0))
        self.assertFalse(self.board.within_bounds(0, 8))

    def test_is_occupied(self):
        """
        Verifica si una casilla está ocupada por una pieza.

        Se espera que la casilla (0, 0) esté ocupada y la casilla (4, 4) esté vacía.
        """
        self.assertTrue(self.board.is_occupied(0, 0))
        self.assertFalse(self.board.is_occupied(4, 4))

    def test_is_path_blocked(self):
        """
        Verifica si el camino entre dos casillas está bloqueado por piezas.

        Se espera que el camino entre (0, 0) y (0, 7) esté bloqueado por una pieza,
        y que el camino entre (1, 0) y (3, 0) no esté bloqueado.
        """
        self.assertTrue(self.board.is_path_blocked(0, 0, 0, 7))
        self.assertTrue(self.board.is_path_blocked(7, 0, 7, 7))
        self.assertFalse(self.board.is_path_blocked(1, 0, 3, 0))
        self.assertFalse(self.board.is_path_blocked(4, 4, 4, 4))

    def test_move_piece(self):
        """
        Verifica que una pieza se mueva correctamente de una casilla a otra.

        Se mueve un peón de (1, 0) a (3, 0) y se espera que la pieza se haya movido
        a la nueva posición y la posición original esté vacía.
        """
        self.board.move_piece(1, 0, 3, 0)
        self.assertIsInstance(self.board.get_piece(3, 0), Pawn)
        self.assertIsNone(self.board.get_piece(1, 0))


if __name__ == '__main__':
    unittest.main()