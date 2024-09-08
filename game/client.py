from game.chess import Chess
from game.console_io import ConsoleIO
from colorama import init

init(autoreset=True)

class Game:
    """
    Clase que representa el flujo principal del juego de ajedrez.

    Atributos:
        chess (Chess): Instancia del juego de ajedrez.
        io_handler (ConsoleIO): Manejador de entrada/salida para la interacción con el usuario.
        king (dict): Diccionario que contiene los reyes de cada jugador para mostrar su símbolo durante el turno.

    Métodos:
        play(): Ejecuta una jugada del juego, procesando la entrada del jugador y gestionando los movimientos.
        request_draw(): Solicita un empate a los jugadores y finaliza el juego si ambos están de acuerdo.
        configure_colours(): Permite al usuario configurar los colores de las piezas en el tablero.
        main_menu(): Muestra el menú principal donde el usuario puede elegir entre jugar, configurar colores o salir del juego.
    """
    
    def __init__(self, chess: Chess, io_handler: ConsoleIO):
        """
        Inicializa una nueva instancia de la clase Game.

        Args:
            chess (Chess): Instancia del juego de ajedrez.
            io_handler (ConsoleIO): Instancia del manejador de entrada/salida para la interacción con el usuario.
        """
        self.chess = chess
        self.io_handler = io_handler
        self.king = self.chess.kings

    def play(self):
        """
        Ejecuta una jugada, mostrando el tablero, el turno y solicitando la entrada del jugador.
        Si el jugador solicita un empate, se gestiona la petición.
        """
        try:
            self.io_handler.output_board(self.chess.board)
            self.io_handler.output_turn(self.chess.turn, self.king[self.chess.turn])
            move_input = self.io_handler.input_move()

            if move_input[0] == 'empate':
                self.request_draw()
            else:
                from_row, from_col, to_row, to_col = move_input
                self.chess.move(from_row, from_col, to_row, to_col)

        except Exception as e:
            self.io_handler.output_error(str(e))

    def request_draw(self):
        """
        Solicita a ambos jugadores si desean declarar un empate.
        Finaliza el juego si ambos jugadores están de acuerdo.
        """
        draw_request = self.io_handler.prompt_draw()
        if draw_request:
            self.chess.end_game('\n¡El juego terminó en empate por acuerdo mutuo!')
        else:
            print('\n¡No hubo acuerdo, el juego continúa!')

    def configure_colours(self):
        """
        Permite al usuario elegir un esquema de colores para las piezas del tablero.
        Los colores se aplican dependiendo de la elección del usuario.
        """
        print('1. Blanco/Negro')
        print('2. Azul/Rojo')
        print('3. Amarillo/Morado')
        print('4. Volver al menú principal')

        colour_scheme = self.io_handler.choose_colour_scheme()

        if colour_scheme:
            for row in range(8):
                for col in range(8):
                    piece = self.chess.board.get_piece(row, col)
                    if piece:
                        piece.display_colour = colour_scheme[0] if piece.colour == 'BLANCAS' else \
                        colour_scheme[1]

    def main_menu(self):
        """
        Muestra el menú principal del juego, donde el usuario puede elegir jugar, configurar colores o salir del juego.
        """
        while True:
            print('1. Jugar')
            print('2. Configurar colores')
            print('3. Salir del juego')
            choice = input(f'\nElegí una opción: ')

            if choice == '1':
                while True:
                    self.play()
                    if self.chess.game_over:
                        break
                self.io_handler.output_board(self.chess.board)
                break
            elif choice == '2':
                self.configure_colours()
            elif choice == '3':
                print('\nSaliendo...\n')
                break

def main():
    """
    Función principal que inicializa el juego de ajedrez y la interfaz de entrada/salida.
    Luego, inicia el menú principal del juego.
    """
    chess = Chess()
    io_handler = ConsoleIO()
    game = Game(chess, io_handler)
    game.main_menu()

if __name__ == '__main__':
    main()