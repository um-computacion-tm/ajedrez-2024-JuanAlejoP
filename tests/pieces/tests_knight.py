import unittest
from game.pieces import Knight

class TestKnight(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Knight.

    Métodos:
        setUp(): Configura los objetos necesarios para las pruebas.
        test_knight_symbols(): Verifica que el símbolo de los caballos sea correcto.
        test_l_shape_move(): Prueba que el caballo pueda moverse en forma de 'L'.
        test_invalid_move(): Prueba que el caballo no pueda realizar movimientos inválidos.
    """

    def setUp(self):
        """
        Configura los objetos Knight antes de cada prueba.

        Se crean un caballo blanco y uno negro.
        """
        self.white_knight = Knight('BLANCAS')
        self.black_knight = Knight('NEGRAS')

    def test_knight_symbols(self):
        """
        Verifica que el símbolo del caballo sea '♞' tanto para las piezas blancas como negras.
        """
        white_knight = Knight('BLANCAS')
        black_knight = Knight('NEGRAS')
        self.assertEqual(white_knight.symbol(), '♞')
        self.assertEqual(black_knight.symbol(), '♞')

    def test_l_shape_move(self):
        """
        Verifica que el caballo pueda moverse en forma de 'L'.
        
        El movimiento en forma de 'L' es característico del caballo.
        """
        self.assertTrue(self.white_knight.move(1, 0, 2, 2))
        self.assertTrue(self.black_knight.move(7, 1, 5, 2))

    def test_invalid_move(self):
        """
        Verifica que los movimientos que no sigan la forma de 'L' sean inválidos para el caballo.
        """
        self.assertFalse(self.white_knight.move(0, 1, 0, 0))
        self.assertFalse(self.black_knight.move(7, 1, 0, 0))


if __name__ == '__main__':
    unittest.main()