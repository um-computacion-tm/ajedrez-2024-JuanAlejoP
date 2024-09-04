from game.board import *

class Chess:
    def __init__(self, board_initializer=None):
        self.__board__ = Board()
        if board_initializer is None:
            board_initializer = BoardInitializer()
        board_initializer.initialize(self.__board__)
        self.__turn__ = 'WHITE'
        self.game_over = False

    @property
    def board(self):
        return self.__board__

    @property
    def turn(self):
        return self.__turn__

    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        target_piece = self.__board__.get_piece(to_row, to_col)

        if piece is None:
            raise ValueError('No hay pieza en esa posición.')
        if not self.is_valid_move(piece, from_row, from_col, to_row, to_col):
            raise ValueError('Movimiento inválido para esta pieza.')
        if not isinstance(piece, Knight) and self.__board__.is_path_blocked(from_row, from_col, to_row, to_col):
            raise ValueError('El camino está bloqueado por otra pieza.')
        if piece.colour != self.__turn__:
            raise ValueError(f'Es turno de las {self.turn}.')
        if target_piece and target_piece.colour == piece.colour:
            raise ValueError('No puedes capturar una pieza del mismo color.')
        
        if not self.__board__.has_pieces(self.__turn__):
            self.end_game(f"¡El jugador {self.__turn__} se quedó sin piezas! El otro jugador gana.")
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        if isinstance(target_piece, King):
            self.end_game(f'¡El rey {target_piece.colour} ha sido capturado! {self.__turn__} gana.')
        else:
            self.change_turn()

    def is_valid_move(self, piece, from_row, from_col, to_row, to_col):
        if isinstance(piece, Pawn):
            return self.is_valid_pawn_move(piece, from_row, from_col, to_row, to_col)
        if not piece.move(from_row, from_col, to_row, to_col):
            return False
        return True

    def is_valid_pawn_move(self, pawn, from_row, from_col, to_row, to_col):
        direction = 1 if pawn.colour == 'WHITE' else -1
        
        if from_col == to_col:
            if to_row == from_row + direction and not self.__board__.is_occupied(to_row, to_col):
                return True
            if (from_row == 1 or from_row == 6) and to_row == from_row + 2 * direction and not self.__board__.is_occupied(to_row, to_col):
                return True
        elif abs(from_col - to_col) == 1 and to_row == from_row + direction:
            if self.__board__.is_occupied(to_row, to_col) and self.__board__.get_piece(to_row, to_col).colour != pawn.colour:
                return True
        return False

    def change_turn(self):
        self.__turn__ = 'BLACK' if self.__turn__ == 'WHITE' else 'WHITE'

    def end_game(self, message):
        self.game_over = True
        print(message)