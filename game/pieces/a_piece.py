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