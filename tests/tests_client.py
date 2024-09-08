import unittest
from unittest.mock import MagicMock, patch
from game.client import Game

class TestGame(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Game en el módulo client.

    Métodos:
        setUp(): Configura un nuevo objeto Game con mocks para Chess y IOHandler.
        test_play_successful_move(): Verifica que se maneje correctamente un movimiento válido.
        test_play_with_exception(): Verifica que se maneje una excepción durante el movimiento.
        test_request_draw_agreement(): Verifica que se maneje correctamente un acuerdo de empate.
        test_request_draw_disagreement(): Verifica que se maneje correctamente un desacuerdo de empate.
        test_configure_colours(): Verifica que los colores de las piezas se configuren correctamente.
        test_play_option(): Verifica que la opción de jugar se maneje correctamente en el menú principal.
        test_exit_option(): Verifica que la opción de salir se maneje correctamente en el menú principal.
    """

    def setUp(self):
        """
        Configura un nuevo objeto Game con mocks para Chess y IOHandler.

        Se crean objetos MagicMock para el juego de ajedrez y el manejador de entrada/salida,
        y se inicializa el objeto Game con estos mocks.
        """
        self.mock_chess = MagicMock()
        self.mock_io_handler = MagicMock()
        self.game = Game(self.mock_chess, self.mock_io_handler)

    def test_play_successful_move(self):
        """
        Verifica que se maneje correctamente un movimiento válido.

        Se simula una entrada de movimiento válida y se verifica que el tablero y el turno se actualicen,
        que se llame al método de movimiento del juego, y que no se llame al método de error.
        """
        self.mock_io_handler.input_move.return_value = (0, 0, 1, 0)
        self.mock_io_handler.output_turn = MagicMock()
        
        self.game.play()

        self.mock_io_handler.output_board.assert_called_once_with(self.mock_chess.board)
        self.mock_io_handler.output_turn.assert_called_once_with(self.mock_chess.turn, self.mock_chess.kings[self.mock_chess.turn])
        self.mock_io_handler.input_move.assert_called_once()
        self.mock_chess.move.assert_called_once_with(0, 0, 1, 0)
        self.mock_io_handler.output_error.assert_not_called()

    def test_play_with_exception(self):
        """
        Verifica que se maneje una excepción durante el movimiento.

        Se simula una excepción al intentar realizar un movimiento y se verifica que se llame al método de error
        con el mensaje de la excepción.
        """
        self.mock_io_handler.input_move.return_value = (0, 0, 1, 0)
        self.mock_chess.move.side_effect = Exception('Invalid move')
        
        self.game.play()

        self.mock_io_handler.output_board.assert_called_once_with(self.mock_chess.board)
        self.mock_io_handler.output_turn.assert_called_once_with(self.mock_chess.turn, self.mock_chess.kings[self.mock_chess.turn])
        self.mock_io_handler.input_move.assert_called_once()
        self.mock_chess.move.assert_called_once_with(0, 0, 1, 0)
        self.mock_io_handler.output_error.assert_called_once_with('Invalid move')

    def test_request_draw_agreement(self):
        """
        Verifica que se maneje correctamente un acuerdo de empate.

        Se simula una respuesta afirmativa para un empate y se verifica que se llame al método de finalizar el juego
        con el mensaje adecuado.
        """
        self.mock_io_handler.prompt_draw.return_value = True
        
        self.game.request_draw()
        
        self.mock_io_handler.prompt_draw.assert_called_once()
        self.mock_chess.end_game.assert_called_once_with('\n¡El juego terminó en empate por acuerdo mutuo!')

    def test_request_draw_disagreement(self):
        """
        Verifica que se maneje correctamente un desacuerdo de empate.

        Se simula una respuesta negativa para un empate y se verifica que se imprima un mensaje de continuación.
        """
        self.mock_io_handler.prompt_draw.return_value = False
        
        with patch('builtins.print') as mock_print:
            self.game.request_draw()
            mock_print.assert_called_once_with('\n¡No hubo acuerdo, el juego continúa!')

    def test_configure_colours(self):
        """
        Verifica que los colores de las piezas se configuren correctamente.

        Se simula la selección de colores para las piezas y se verifica que los colores de visualización se configuren
        según la selección.
        """
        self.mock_io_handler.choose_colour_scheme.return_value = ('white', 'black')
        
        self.mock_chess.board.get_piece = MagicMock()
        piece_mock = MagicMock()
        self.mock_chess.board.get_piece.return_value = piece_mock
        piece_mock.colour = 'BLANCAS'
        
        self.game.configure_colours()
        
        piece_mock.display_colour = 'white'
        self.mock_chess.board.get_piece.assert_called()

        for piece in [self.mock_chess.board.get_piece.return_value] * 64:
            if piece.colour == 'BLANCAS':
                self.assertEqual(piece.display_colour, 'white')
            else:
                self.assertEqual(piece.display_colour, 'black')

    def test_play_option(self):
        """
        Verifica que la opción de jugar se maneje correctamente en el menú principal.

        Se simula la selección de la opción de jugar en el menú principal y se verifica que el juego comience
        y que se llame al método de salida correspondiente.
        """
        with patch('builtins.input', side_effect=['1']):
            with patch('builtins.print') as mock_print:
                self.mock_chess.game_over = True
                self.game.play = MagicMock()
                
                self.game.main_menu()
                
                self.game.play.assert_called()
                self.mock_io_handler.output_board.assert_called_once_with(self.mock_chess.board)
                mock_print.assert_called_with('3. Salir del juego')

    def test_exit_option(self):
        """
        Verifica que la opción de salir se maneje correctamente en el menú principal.

        Se simula la selección de la opción de salir en el menú principal y se verifica que el juego finalice
        y que se impriman los mensajes correspondientes.
        """
        with patch('builtins.input', side_effect=['3']):
            with patch('builtins.print') as mock_print:
                self.game.play = MagicMock()
                self.game.configure_colours = MagicMock()
                
                self.game.main_menu()
                
                mock_print.assert_called_with('\nSaliendo...\n')
                self.game.play.assert_not_called()
                self.game.configure_colours.assert_not_called()


if __name__ == '__main__':
    unittest.main()