import unittest
from game.pieces import King

class TestKing(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase King.

    Métodos:
        setUp(): Configura los objetos necesarios para las pruebas.
        test_king_symbols(): Verifica que el símbolo de los reyes sea correcto.
        test_single_square_move(): Prueba que el rey pueda moverse una casilla en cualquier dirección.
        test_invalid_move(): Prueba que el rey no pueda realizar movimientos inválidos.
    """

    def setUp(self):
        """
        Configura los objetos King antes de cada prueba.

        Se crean un rey blanco y uno negro.
        """
        self.white_king = King('BLANCAS')
        self.black_king = King('NEGRAS')

    def test_king_symbols(self):
        """
        Verifica que el símbolo del rey sea '♚' tanto para las piezas blancas como negras.
        """
        white_king = King('BLANCAS')
        black_king = King('NEGRAS')
        self.assertEqual(white_king.symbol(), '♚')
        self.assertEqual(black_king.symbol(), '♚')

    def test_single_square_move(self):
        """
        Verifica que el rey pueda moverse una casilla en cualquier dirección.
        
        Se espera que los movimientos de una sola casilla sean válidos.
        """
        self.assertTrue(self.white_king.move(4, 4, 4, 5))
        self.assertTrue(self.black_king.move(4, 4, 5, 4))

    def test_invalid_move(self):
        """
        Verifica que los movimientos de más de una casilla no sean válidos para el rey.
        """
        self.assertFalse(self.white_king.move(4, 4, 6, 4))
        self.assertFalse(self.black_king.move(4, 4, 4, 6))


if __name__ == '__main__':
    unittest.main()