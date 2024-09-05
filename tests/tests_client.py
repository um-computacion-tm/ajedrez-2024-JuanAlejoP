import unittest
from unittest.mock import MagicMock, patch
from game.client import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.mock_chess = MagicMock()
        self.mock_io_handler = MagicMock()
        self.game = Game(self.mock_chess, self.mock_io_handler)

    def test_play_successful_move(self):
        self.mock_io_handler.input_move.return_value = (0, 0, 1, 0)
        self.mock_io_handler.output_turn = MagicMock()
        
        self.game.play()

        self.mock_io_handler.output_board.assert_called_once_with(self.mock_chess.board)
        self.mock_io_handler.output_turn.assert_called_once_with(self.mock_chess.turn, self.mock_chess.kings[self.mock_chess.turn])
        self.mock_io_handler.input_move.assert_called_once()
        self.mock_chess.move.assert_called_once_with(0, 0, 1, 0)
        self.mock_io_handler.output_error.assert_not_called()

    def test_play_with_exception(self):
        self.mock_io_handler.input_move.return_value = (0, 0, 1, 0)
        self.mock_chess.move.side_effect = Exception('Invalid move')
        
        self.game.play()

        self.mock_io_handler.output_board.assert_called_once_with(self.mock_chess.board)
        self.mock_io_handler.output_turn.assert_called_once_with(self.mock_chess.turn, self.mock_chess.kings[self.mock_chess.turn])
        self.mock_io_handler.input_move.assert_called_once()
        self.mock_chess.move.assert_called_once_with(0, 0, 1, 0)
        self.mock_io_handler.output_error.assert_called_once_with('Invalid move')

    def test_request_draw_agreement(self):
        self.mock_io_handler.prompt_draw.return_value = True
        
        self.game.request_draw()
        
        self.mock_io_handler.prompt_draw.assert_called_once()
        self.mock_chess.end_game.assert_called_once_with('\n¡El juego terminó en empate por acuerdo mutuo!')

    def test_request_draw_disagreement(self):
        self.mock_io_handler.prompt_draw.return_value = False
        
        with patch('builtins.print') as mock_print:
            self.game.request_draw()
            mock_print.assert_called_once_with('\n¡No hubo acuerdo, el juego continúa!')

    def test_configure_colours(self):
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
        with patch('builtins.input', side_effect=['1']):
            with patch('builtins.print') as mock_print:
                self.mock_chess.game_over = True
                self.game.play = MagicMock()
                
                self.game.main_menu()
                
                self.game.play.assert_called()
                self.mock_io_handler.output_board.assert_called_once_with(self.mock_chess.board)
                mock_print.assert_called_with('3. Salir del juego')

    def test_exit_option(self):
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