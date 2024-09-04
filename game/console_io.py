from colorama import Fore

class ConsoleIO:

    def input_move(self):
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
        confirm1 = input('¿Jugador 1 desea declarar empate? (Y/N): ').strip().upper()
        confirm2 = input('¿Jugador 2 desea declarar empate? (Y/N): ').strip().upper()
        return confirm1 == 'Y' and confirm2 == 'Y'

    def algebraic_to_index(self, pos):
        col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        col = col_map[pos[0]]
        row = int(pos[1]) - 1
        return row, col

    def output_turn(self, turn):
        print(f'TURNO: {turn}')

    def output_error(self, error_message):
        print(f'\n¡ERROR! {error_message}')

    def output_board(self, board):
        print(board)

    def choose_colour_scheme(self):
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