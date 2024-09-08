import unittest
from unittest.mock import patch, MagicMock
from game.console_io import ConsoleIO, Fore

class TestConsoleIO(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase ConsoleIO en el módulo console_io.

    Métodos:
        setUp(): Configura un nuevo objeto ConsoleIO.
        test_input_move(): Verifica la conversión de movimientos en notación algebraica a índices.
        test_algebraic_to_index(): Verifica la conversión de coordenadas algebraicas a índices de tablero.
        test_output_turn(): Verifica la salida del turno actual.
        test_output_error(): Verifica la salida de mensajes de error.
        test_output_board(): Verifica la salida del tablero de juego.
        test_choose_colour_scheme_valid_option(): Verifica la selección de un esquema de colores válido.
        test_choose_colour_scheme_invalid_option(): Verifica la selección de un esquema de colores inválido.
        test_prompt_draw_agreement(): Verifica la solicitud de empate cuando se acepta.
        test_prompt_draw_one_accept(): Verifica la solicitud de empate cuando solo uno acepta.
        test_prompt_draw_disagreement(): Verifica la solicitud de empate cuando ninguno acepta.
    """
    
    def setUp(self):
        """
        Configura un nuevo objeto ConsoleIO.

        Se inicializa el objeto ConsoleIO para ser usado en las pruebas.
        """
        self.console_io = ConsoleIO()

    @patch('builtins.input', side_effect=['e2', 'e4'])
    def test_input_move(self, mock_input):
        """
        Verifica la conversión de movimientos en notación algebraica a índices.

        Se simula una entrada de movimiento en notación algebraica y se verifica que se convierta correctamente
        a índices de tablero.
        """
        from_row, from_col, to_row, to_col = self.console_io.input_move()
        self.assertEqual((from_row, from_col), (1, 4))
        self.assertEqual((to_row, to_col), (3, 4))

    def test_algebraic_to_index(self):
        """
        Verifica la conversión de coordenadas algebraicas a índices de tablero.

        Se verifica la conversión de varias coordenadas algebraicas a índices correspondientes del tablero.
        """
        self.assertEqual(self.console_io.algebraic_to_index('a1'), (0, 0))
        self.assertEqual(self.console_io.algebraic_to_index('h8'), (7, 7))
        self.assertEqual(self.console_io.algebraic_to_index('c5'), (4, 2))

    @patch('builtins.print')
    @patch('game.pieces.King')
    def test_output_turn(self, mock_king, mock_print):
        """
        Verifica la salida del turno actual.

        Se simula la visualización del turno actual con el símbolo del rey correspondiente y se verifica
        que el mensaje se imprima correctamente.
        """
        mock_king_instance = MagicMock()
        mock_king_instance.coloured_symbol.return_value = '♚'
        mock_king.return_value = mock_king_instance
        
        self.console_io.output_turn('BLANCAS', mock_king_instance)
        mock_print.assert_called_once_with('TURNO: BLANCAS ♚')

    @patch('builtins.print')
    def test_output_error(self, mock_print):
        """
        Verifica la salida de mensajes de error.

        Se simula la impresión de un mensaje de error y se verifica que se imprima correctamente.
        """
        self.console_io.output_error('Movimiento inválido')
        mock_print.assert_called_once_with('\n¡ERROR! Movimiento inválido')

    @patch('builtins.print')
    def test_output_board(self, mock_print):
        """
        Verifica la salida del tablero de juego.

        Se simula la impresión del tablero de juego y se verifica que el tablero se imprima correctamente.
        """
        board = 'tablero de ejemplo'
        self.console_io.output_board(board)
        mock_print.assert_called_once_with(board)

    @patch('builtins.input', side_effect=['1'])
    def test_choose_colour_scheme_valid_option(self, mock_input):
        """
        Verifica la selección de un esquema de colores válido.

        Se simula la selección de una opción válida para los colores y se verifica que se devuelvan los colores
        correspondientes.
        """
        colours = self.console_io.choose_colour_scheme()
        self.assertEqual(colours, (Fore.WHITE, Fore.BLACK))

    @patch('builtins.input', side_effect=['4'])
    def test_choose_colour_scheme_invalid_option(self, mock_input):
        """
        Verifica la selección de un esquema de colores inválido.

        Se simula la selección de una opción inválida para los colores y se verifica que se devuelva None.
        """
        colours = self.console_io.choose_colour_scheme()
        self.assertIsNone(colours)

    @patch('builtins.input', side_effect=['Y', 'Y'])
    def test_prompt_draw_agreement(self, mock_input):
        """
        Verifica la solicitud de empate cuando se acepta.

        Se simula la aceptación de un empate por ambos jugadores y se verifica que el método devuelva True.
        """
        result = self.console_io.prompt_draw()
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['Y', 'N'])
    def test_prompt_draw_one_accept(self, mock_input):
        """
        Verifica la solicitud de empate cuando solo uno acepta.

        Se simula la aceptación de un empate por un jugador y el rechazo por el otro, y se verifica que
        el método devuelva False.
        """
        result = self.console_io.prompt_draw()
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['N', 'N'])
    def test_prompt_draw_disagreement(self, mock_input):
        """
        Verifica la solicitud de empate cuando ninguno acepta.

        Se simula el rechazo del empate por ambos jugadores y se verifica que el método devuelva False.
        """
        result = self.console_io.prompt_draw()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()