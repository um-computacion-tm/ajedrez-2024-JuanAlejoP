import unittest
from game.pieces import Rook

class TestRook(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Rook.

    Métodos:
        setUp(): Configura los objetos necesarios para las pruebas.
        test_rook_symbols(): Verifica que el símbolo de las torres sea correcto.
        test_horizontal_move(): Prueba que la torre pueda moverse horizontalmente.
        test_vertical_move(): Prueba que la torre pueda moverse verticalmente.
        test_invalid_move(): Prueba que la torre no pueda realizar movimientos inválidos.
    """

    def setUp(self):
        """
        Configura los objetos Rook antes de cada prueba.

        Se crean una torre blanca y una negra.
        """
        self.white_rook = Rook('BLANCAS')
        self.black_rook = Rook('NEGRAS')

    def test_rook_symbols(self):
        """
        Verifica que el símbolo de la torre sea '♜' tanto para las piezas blancas como negras.
        """
        white_rook = Rook('BLANCAS')
        black_rook = Rook('NEGRAS')
        self.assertEqual(white_rook.symbol(), '♜')
        self.assertEqual(black_rook.symbol(), '♜')

    def test_horizontal_move(self):
        """
        Verifica que la torre pueda moverse horizontalmente.

        Se espera que los movimientos horizontales sean válidos para una torre.
        """
        self.assertTrue(self.white_rook.move(0, 0, 0, 7))
        self.assertFalse(self.white_rook.move(0, 0, 1, 7))

    def test_vertical_move(self):
        """
        Verifica que la torre pueda moverse verticalmente.

        Se espera que los movimientos verticales sean válidos para una torre.
        """
        self.assertTrue(self.black_rook.move(0, 0, 7, 0))
        self.assertFalse(self.black_rook.move(0, 0, 7, 1))

    def test_invalid_move(self):
        """
        Verifica que los movimientos que no sean ni horizontales ni verticales sean inválidos para la torre.
        """
        self.assertFalse(self.white_rook.move(0, 0, 7, 7))
        self.assertFalse(self.black_rook.move(0, 0, 1, 2))


if __name__ == '__main__':
    unittest.main()