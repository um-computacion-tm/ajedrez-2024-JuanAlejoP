from game.chess import Chess
from game.console_io import ConsoleIO
from colorama import init

init(autoreset=True)

class Game:
    def __init__(self, chess: Chess, io_handler: ConsoleIO):
        self.chess = chess
        self.io_handler = io_handler

    def play(self):
        try:
            self.io_handler.output_board(self.chess.board)
            self.io_handler.output_turn(self.chess.turn)
            move_input = self.io_handler.input_move()

            if move_input[0] == 'empate':
                self.request_draw()
            else:
                from_row, from_col, to_row, to_col = move_input
                self.chess.move(from_row, from_col, to_row, to_col)
        except Exception as e:
            self.io_handler.output_error(str(e))

    def request_draw(self):
        draw_request = self.io_handler.prompt_draw()
        if draw_request:
            self.chess.end_game("El juego terminó en empate por acuerdo mutuo.")

    def configure_colours(self):
        print("1. Blanco/Negro")
        print("2. Azul/Rojo")
        print("3. Amarillo/Morado")
        print("4. Volver al menú principal")

        colour_scheme = self.io_handler.choose_colour_scheme()
        
        if colour_scheme:
            for row in range(8):
                for col in range(8):
                    piece = self.chess.board.get_piece(row, col)
                    if piece:
                        piece.display_colour = colour_scheme[0] if piece.colour == "WHITE" else colour_scheme[1]

    def main_menu(self):
        while True:
            print("1. Jugar")
            print("2. Configurar colores")
            print("3. Salir")
            choice = input("Elige una opción: ")

            if choice == "1":
                while True:
                    self.play()
                    if self.chess.game_over:
                        break
                self.io_handler.output_board(self.chess.board)
                break
            elif choice == "2":
                self.configure_colours()
            elif choice == "3":
                print("¡Gracias por jugar!")
                break

def main():
    chess = Chess()
    io_handler = ConsoleIO()
    game = Game(chess, io_handler)
    game.main_menu()

if __name__ == '__main__':
    main()