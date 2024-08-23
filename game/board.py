from game.pieces import *

class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece: Piece, row, col):
        self.__positions__[row][col] = piece

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def within_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def is_occupied(self, row, col):
        return self.get_piece(row, col) is not None

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if not self.within_bounds(to_row, to_col):
            raise ValueError('Movimiento fuera de los límites.')
        
        if piece is None:
            raise ValueError('No hay pieza en esa posición.')

        if not piece.valid_move(from_row, from_col, to_row, to_col):
            raise ValueError('Movimiento inválido para esta pieza.')

        if self.is_occupied(to_row, to_col) and (to_row != from_row + 1):
            raise ValueError('Casilla ocupada.')

        self.place_piece(piece, to_row, to_col)
        self.__positions__[from_row][from_col] = None

    def __str__(self):
        board_str = "    a   b   c   d   e   f   g   h  \n"
        board_str += "  " + "-" * 33 + "\n"
        for i, row in enumerate(self.__positions__):
            row_str = f"{i+1} |"
            for piece in row:
                if piece is None:
                    row_str += "   |"
                else:
                    row_str += f" {piece.symbol()} |"
            board_str += row_str + f" {i+1}\n"
            board_str += "  " + "-" * 33 + "\n"
        board_str += "    a   b   c   d   e   f   g   h  \n"
        return board_str
   
class BoardInitializer:
    def __init__(self):
        self.white_back_row = [
            Rook('WHITE'), Knight('WHITE'), Bishop('WHITE'), 
            King('WHITE'), Queen('WHITE'), Bishop('WHITE'), 
            Knight('WHITE'), Rook('WHITE')
        ]
        self.black_back_row = [
            Rook('BLACK'), Knight('BLACK'), Bishop('BLACK'), 
            King('BLACK'), Queen('BLACK'), Bishop('BLACK'), 
            Knight('BLACK'), Rook('BLACK')
        ]

    def initialize(self, board: Board):
        for col, piece in enumerate(self.white_back_row):
            board.place_piece(piece, 0, col)

        for col in range(8):
            board.place_piece(Pawn('WHITE'), 1, col)

        for col in range(8):
            board.place_piece(Pawn('BLACK'), 6, col)

        for col, piece in enumerate(self.black_back_row):
            board.place_piece(piece, 7, col)