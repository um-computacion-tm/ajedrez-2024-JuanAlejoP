import unittest
from game.chess import Chess
from game.pieces import Pawn, King, Knight

class TestChess(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Chess.

    Métodos:
        setUp(): Configura un nuevo juego de ajedrez antes de cada prueba.
        test_initial_turn(): Verifica que el turno inicial sea de las blancas.
        test_move(): Verifica que un movimiento válido cambie la posición de la pieza y el turno.
        test_invalid_move_empty_square(): Verifica que se lance una excepción al intentar mover a una casilla vacía.
        test_invalid_move_blocked_path(): Verifica que se lance una excepción si el camino está bloqueado.
        test_capture(): Verifica que una pieza puede capturar a otra correctamente.
        test_invalid_capture_same_color(): Verifica que se lance una excepción al intentar capturar una pieza del mismo color.
        test_pawn_double_step(): Verifica que el movimiento de dos casillas de un peón sea válido.
        test_pawn_diagonal_capture(): Verifica que el movimiento en diagonal para captura de un peón sea válido.
        test_knight_move(): Verifica que el movimiento de un caballo sea válido.
        test_turn_change(): Verifica que el turno cambie correctamente entre los jugadores.
        test_capture_king(): Verifica que el juego termine cuando se capture al rey.
    """

    def setUp(self):
        """
        Configura un nuevo juego de ajedrez antes de cada prueba.

        Se crea un objeto Chess que representa el juego de ajedrez.
        """
        self.chess = Chess()

    def test_initial_turn(self):
        """
        Verifica que el turno inicial sea de las blancas.

        Se espera que el turno inicial esté asignado a 'BLANCAS'.
        """
        self.assertEqual(self.chess.turn, 'BLANCAS')

    def test_move(self):
        """
        Verifica que un movimiento válido cambie la posición de la pieza y el turno.

        Se mueve un peón de (1, 0) a (3, 0), y se espera que el peón esté en la nueva posición,
        la posición original esté vacía, y el turno cambie a 'NEGRAS'.
        """
        self.chess.move(1, 0, 3, 0)
        self.assertIsInstance(self.chess.board.get_piece(3, 0), Pawn)
        self.assertIsNone(self.chess.board.get_piece(1, 0))
        self.assertEqual(self.chess.turn, 'NEGRAS')

    def test_invalid_move_empty_square(self):
        """
        Verifica que se lance una excepción al intentar mover a una casilla vacía.

        Se espera que se lance una excepción ValueError si se intenta mover a una casilla vacía.
        """
        with self.assertRaises(ValueError):
            self.chess.move(3, 3, 4, 3)

    def test_invalid_move_blocked_path(self):
        """
        Verifica que se lance una excepción si el camino está bloqueado.

        Se espera que se lance una excepción ValueError si el camino entre dos casillas está bloqueado por otras piezas.
        """
        with self.assertRaises(ValueError):
            self.chess.move(0, 0, 0, 3)

    def test_capture(self):
        """
        Verifica que una pieza puede capturar a otra correctamente.

        Se mueve un peón para capturar una pieza enemiga y se espera que la pieza capturada sea un peón blanco
        en la nueva posición de la pieza capturadora.
        """
        self.chess.move(1, 0, 3, 0)
        self.chess.move(6, 1, 4, 1)
        self.chess.move(3, 0, 4, 1)
        self.assertIsInstance(self.chess.board.get_piece(4, 1), Pawn)
        self.assertEqual(self.chess.board.get_piece(4, 1).colour, 'BLANCAS')

    def test_invalid_capture_same_color(self):
        """
        Verifica que se lance una excepción al intentar capturar una pieza del mismo color.

        Se espera que se lance una excepción ValueError si se intenta capturar una pieza del mismo color.
        """
        with self.assertRaises(ValueError):
            self.chess.move(0, 0, 0, 1)

    def test_pawn_double_step(self):
        """
        Verifica que el movimiento de dos casillas de un peón sea válido.

        Se espera que el movimiento de un peón dos casillas hacia adelante desde su posición inicial sea válido,
        y que un movimiento de tres casillas no lo sea.
        """
        self.assertTrue(self.chess.is_valid_pawn_move(self.chess.board.get_piece(1, 0), 1, 0, 3, 0))
        self.assertFalse(self.chess.is_valid_pawn_move(self.chess.board.get_piece(1, 0), 1, 0, 4, 0))

    def test_pawn_diagonal_capture(self):
        """
        Verifica que el movimiento en diagonal para captura de un peón sea válido.

        Se mueve un peón para capturar en diagonal y se espera que el movimiento sea válido.
        """
        self.chess.move(1, 0, 3, 0)
        self.chess.move(6, 1, 4, 1)
        self.assertTrue(self.chess.is_valid_pawn_move(self.chess.board.get_piece(3, 0), 3, 0, 4, 1))

    def test_knight_move(self):
        """
        Verifica que el movimiento de un caballo sea válido.

        Se espera que el movimiento en forma de 'L' del caballo sea válido y cualquier otro movimiento no lo sea.
        """
        knight = self.chess.board.get_piece(0, 1)
        self.assertTrue(self.chess.is_valid_move(knight, 0, 1, 2, 2))
        self.assertFalse(self.chess.is_valid_move(knight, 0, 1, 3, 3))

    def test_turn_change(self):
        """
        Verifica que el turno cambie correctamente entre los jugadores.

        Se espera que el turno cambie de 'BLANCAS' a 'NEGRAS' y viceversa con cada llamada a change_turn().
        """
        self.assertEqual(self.chess.turn, 'BLANCAS')
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, 'NEGRAS')
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, 'BLANCAS')

    def test_capture_king(self):
        """
        Verifica que el juego termine cuando se capture al rey.

        Se realizan una serie de movimientos que llevan a la captura del rey. Se espera que el juego se marque como terminado.
        """
        self.chess.move(1, 3, 3, 3)
        self.chess.move(6, 5, 5, 5)
        self.chess.move(0, 3, 2, 3)
        self.chess.move(7, 4, 6, 5)
        self.chess.move(2, 3, 5, 6)
        self.chess.move(6, 5, 7, 4)
        self.chess.move(5, 6, 7, 4)
        self.assertTrue(self.chess.game_over)


if __name__ == '__main__':
    unittest.main()