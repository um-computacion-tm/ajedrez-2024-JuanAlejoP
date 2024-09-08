import unittest
from game.pieces import Queen

class TestQueen(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Queen.

    Métodos:
        setUp(): Configura los objetos necesarios para las pruebas.
        test_queen_symbols(): Verifica que el símbolo de las reinas sea correcto.
        test_horizontal_vertical_move(): Prueba que la reina pueda moverse horizontal y verticalmente.
        test_diagonal_move(): Prueba que la reina pueda moverse diagonalmente.
        test_invalid_move(): Prueba que la reina no pueda realizar movimientos inválidos.
    """

    def setUp(self):
        """
        Configura los objetos Queen antes de cada prueba.

        Se crean una reina blanca y una negra.
        """
        self.white_queen = Queen('BLANCAS')
        self.black_queen = Queen('NEGRAS')

    def test_queen_symbols(self):
        """
        Verifica que el símbolo de la reina sea '♛' tanto para las piezas blancas como negras.
        """
        white_queen = Queen('BLANCAS')
        black_queen = Queen('NEGRAS')
        self.assertEqual(white_queen.symbol(), '♛')
        self.assertEqual(black_queen.symbol(), '♛')

    def test_horizontal_vertical_move(self):
        """
        Verifica que la reina pueda moverse horizontal y verticalmente.

        Se espera que los movimientos horizontales y verticales sean válidos para una reina.
        """
        self.assertTrue(self.white_queen.move(0, 0, 0, 7))
        self.assertTrue(self.black_queen.move(0, 0, 7, 0))

    def test_diagonal_move(self):
        """
        Verifica que la reina pueda moverse diagonalmente.

        Se espera que los movimientos diagonales sean válidos para una reina.
        """
        self.assertTrue(self.white_queen.move(0, 0, 7, 7))
        self.assertTrue(self.black_queen.move(7, 7, 0, 0))

    def test_invalid_move(self):
        """
        Verifica que los movimientos que no sean ni horizontales, verticales ni diagonales sean inválidos para la reina.
        """
        self.assertFalse(self.white_queen.move(0, 0, 2, 1))
        self.assertFalse(self.black_queen.move(7, 7, 5, 6))


if __name__ == '__main__':
    unittest.main()