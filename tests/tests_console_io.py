import unittest
from unittest.mock import patch
from game.console_io import ConsoleIO

class TestConsoleIO(unittest.TestCase):
    
    def setUp(self):
        self.console_io = ConsoleIO()

    @patch('builtins.input', side_effect=['e2', 'e4'])
    def test_input_move(self, mock_input):
        from_row, from_col, to_row, to_col = self.console_io.input_move()
        self.assertEqual((from_row, from_col), (1, 4))
        self.assertEqual((to_row, to_col), (3, 4))

    def test_algebraic_to_index(self):
        self.assertEqual(self.console_io.algebraic_to_index('a1'), (0, 0))
        self.assertEqual(self.console_io.algebraic_to_index('h8'), (7, 7))
        self.assertEqual(self.console_io.algebraic_to_index('c5'), (4, 2))

    @patch('builtins.print')
    def test_output_turn(self, mock_print):
        self.console_io.output_turn('Blancas')
        mock_print.assert_called_once_with('Turno: Blancas')

    @patch('builtins.print')
    def test_output_error(self, mock_print):
        self.console_io.output_error('Movimiento inválido')
        mock_print.assert_called_once_with('ERROR!', 'Movimiento inválido')

    @patch('builtins.print')
    def test_output_board(self, mock_print):
        board = 'tablero de ejemplo'
        self.console_io.output_board(board)
        mock_print.assert_called_once_with(board)

if __name__ == '__main__':
    unittest.main()