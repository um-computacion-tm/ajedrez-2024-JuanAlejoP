import unittest
from game.pieces import Bishop

class TestBishop(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Bishop.

    Métodos:
        setUp(): Configura los objetos necesarios para las pruebas.
        test_bishop_symbols(): Verifica que el símbolo de los alfiles sea correcto.
        test_diagonal_move(): Prueba que el alfil pueda moverse en diagonal correctamente.
        test_invalid_move(): Prueba que el alfil no pueda realizar movimientos inválidos.
    """

    def setUp(self):
        """
        Configura los objetos Bishop antes de cada prueba.

        Se crean un alfil blanco y uno negro.
        """
        self.white_bishop = Bishop('BLANCAS')
        self.black_bishop = Bishop('NEGRAS')

    def test_bishop_symbols(self):
        """
        Verifica que el símbolo del alfil sea '♝' tanto para las piezas blancas como negras.
        """
        white_bishop = Bishop('BLANCAS')
        black_bishop = Bishop('NEGRAS')
        self.assertEqual(white_bishop.symbol(), '♝')
        self.assertEqual(black_bishop.symbol(), '♝')

    def test_diagonal_move(self):
        """
        Verifica que el alfil pueda moverse en diagonal.
        
        Se espera que los movimientos de tipo diagonal sean válidos.
        """
        self.assertTrue(self.white_bishop.move(0, 2, 3, 5))
        self.assertTrue(self.black_bishop.move(7, 2, 4, 5))

    def test_invalid_move(self):
        """
        Verifica que los movimientos no diagonales del alfil sean inválidos.
        
        Se espera que movimientos horizontales o verticales no sean válidos para un alfil.
        """
        self.assertFalse(self.white_bishop.move(0, 2, 0, 5))
        self.assertFalse(self.black_bishop.move(7, 2, 7, 0))


if __name__ == '__main__':
    unittest.main()