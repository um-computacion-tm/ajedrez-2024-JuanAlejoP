from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, colour):
        self.__colour__ = colour

    @property
    def colour(self):
        return self.__colour__

    @abstractmethod
    def move(self, from_row, from_col, to_row, to_col):
        pass

    @abstractmethod
    def symbol(self):
        pass

class MovementValidator:
    
    @staticmethod
    def is_straight_line(from_row, from_col, to_row, to_col):
        return from_row == to_row or from_col == to_col

    @staticmethod
    def is_diagonal(from_row, from_col, to_row, to_col):
        return abs(from_row - to_row) == abs(from_col - to_col)

    @staticmethod
    def is_knight_move(from_row, from_col, to_row, to_col):
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)