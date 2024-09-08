import unittest
from game.pieces import Pawn

class TestPawn(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Pawn.

    Métodos:
        setUp(): Configura los objetos necesarios para las pruebas.
        test_pawn_symbols(): Verifica que el símbolo de los peones sea correcto.
        test_pawn_initial_double_step(): Prueba que el peón pueda realizar el movimiento doble inicial.
        test_pawn_single_step(): Prueba que el peón pueda realizar un movimiento simple.
        test_pawn_invalid_move(): Prueba que los movimientos inválidos para el peón sean correctamente identificados.
    """

    def setUp(self):
        """
        Configura los objetos Pawn antes de cada prueba.

        Se crean un peón blanco y uno negro.
        """
        self.white_pawn = Pawn('BLANCAS')
        self.black_pawn = Pawn('NEGRAS')

    def test_pawn_symbols(self):
        """
        Verifica que el símbolo del peón sea '♟' tanto para las piezas blancas como negras.
        """
        white_pawn = Pawn('BLANCAS')
        black_pawn = Pawn('NEGRAS')
        self.assertEqual(white_pawn.symbol(), '♟')
        self.assertEqual(black_pawn.symbol(), '♟')

    def test_pawn_initial_double_step(self):
        """
        Verifica que el peón pueda realizar el movimiento doble en su primer movimiento.
        
        El peón blanco y el peón negro deben poder avanzar dos casillas en su primer movimiento.
        """
        self.assertTrue(self.white_pawn.move(1, 0, 3, 0))
        self.assertTrue(self.black_pawn.move(6, 0, 4, 0))

    def test_pawn_single_step(self):
        """
        Verifica que el peón pueda realizar un movimiento simple de una casilla.
        
        El peón blanco y el peón negro deben poder avanzar una casilla.
        """
        self.assertTrue(self.white_pawn.move(2, 0, 3, 0))
        self.assertTrue(self.black_pawn.move(5, 0, 4, 0))

    def test_pawn_invalid_move(self):
        """
        Verifica que los movimientos no válidos para el peón sean correctamente identificados.
        
        El peón no debe poder moverse diagonalmente o avanzar en columnas incorrectas.
        """
        self.assertFalse(self.white_pawn.move(1, 0, 3, 1))
        self.assertFalse(self.black_pawn.move(6, 0, 4, 1))


if __name__ == '__main__':
    unittest.main()