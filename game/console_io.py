from colorama import Fore
from game.pieces import King

class ConsoleIO:
    """Gestor de entrada y salida para la interacción del usuario en consola."""

    def input_move(self):
        """Solicita al usuario ingresar las posiciones de origen y destino para mover una pieza.

        Returns:
            tuple: Una tupla con las posiciones (from_row, from_col, to_row, to_col) o un 
            comando de empate si el usuario lo ingresa.

        Raises:
            ValueError: Si no se ingresó un movimiento válido.
        """
        from_pos = input('Mover pieza desde: ').strip().lower()
        if from_pos == 'empate':
            return 'empate', None, None, None
        to_pos = input('Hacia casilla: ').strip().lower()
        if not from_pos or not to_pos:
            raise ValueError('No ingresaste un movimiento.')

        from_row, from_col = self.algebraic_to_index(from_pos)
        to_row, to_col = self.algebraic_to_index(to_pos)
        return from_row, from_col, to_row, to_col

    def prompt_draw(self):
        """Solicita a los jugadores confirmar si desean declarar empate.

        Returns:
            bool: True si ambos jugadores confirman el empate, False en caso contrario.
        """
        confirm1 = input('¿Jugador 1 desea declarar empate? (Y/N): ').strip().upper()
        confirm2 = input('¿Jugador 2 desea declarar empate? (Y/N): ').strip().upper()
        return confirm1 == 'Y' and confirm2 == 'Y'

    def algebraic_to_index(self, pos):
        """Convierte una notación algebraica (e.g., 'a2') a índices de fila y columna.

        Args:
            pos (str): Notación algebraica.

        Returns:
            tuple: Índices de fila y columna correspondientes a la posición.
        """
        col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        col = col_map[pos[0]]
        row = int(pos[1]) - 1
        return row, col

    def output_turn(self, turn, king):
        """Muestra el turno actual y el rey del color correspondiente.

        Args:
            turn (str): El color del turno actual ('BLANCAS' o 'NEGRAS').
            king (King): La pieza de rey del color correspondiente.
        """
        print(f'TURNO: {turn} {king.coloured_symbol()}')

    def output_error(self, error_message):
        """Muestra un mensaje de error en la consola.

        Args:
            error_message (str): El mensaje de error a mostrar.
        """
        print(f'\n¡ERROR! {error_message}')

    def output_board(self, board):
        """Muestra el tablero de ajedrez en la consola.

        Args:
            board (Board): El tablero a mostrar.
        """
        print(board)

    def choose_colour_scheme(self):
        """Permite al usuario elegir un esquema de colores para las piezas.

        Returns:
            tuple | None: Los colores seleccionados para las piezas blancas y negras, o None
            si no se seleccionó una opción válida.
        """
        choice = input(f'\nElegí colores para las piezas BLANCAS/NEGRAS: ')

        if choice == '1':
            print('Elegiste colores Blanco/Negro')
            return Fore.WHITE, Fore.BLACK
        elif choice == '2':
            print('Elegiste colores Azul/Rojo')
            return Fore.BLUE, Fore.RED
        elif choice == '3':
            print('Elegiste colores Amarillo/Morado')
            return Fore.YELLOW, Fore.MAGENTA
        else:
            return None