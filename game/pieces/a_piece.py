from abc import ABC, abstractmethod
from colorama import Fore, Style

class Piece(ABC):
    def __init__(self, colour, display_colour=None):
        self.__colour__ = colour
        self.__display_colour__ = display_colour or self.default_display_colour()

    @property
    def colour(self):
        return self.__colour__

    @abstractmethod
    def move(self, from_row, from_col, to_row, to_col):
        pass

    @abstractmethod
    def symbol(self):
        pass

    def default_display_colour(self):
        if self.colour == 'WHITE':
            return Fore.WHITE
        elif self.colour == 'BLACK':
            return Fore.BLACK

    @property
    def display_colour(self):
        return self.__display_colour__

    @display_colour.setter
    def display_colour(self, value):
        self.__display_colour__ = value

    def coloured_symbol(self):
        return f"{self.display_colour}{self.symbol()}{Style.RESET_ALL}"