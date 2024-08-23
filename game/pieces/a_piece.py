from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, colour):
        self.__colour__ = colour

    @abstractmethod
    def valid_move(self, from_row, from_col, to_row, to_col):
        pass
    
    @abstractmethod
    def symbol(self):
        pass