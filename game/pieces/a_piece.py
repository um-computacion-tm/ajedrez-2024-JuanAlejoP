from abc import ABC, abstractmethod
from colorama import Fore, Style

class Piece(ABC):
    """Clase base abstracta para representar una pieza de ajedrez.

    Esta clase define la interfaz y los métodos comunes que deben implementar
    todas las piezas de ajedrez.

    Args:
        colour (str): El color de la pieza ('BLANCAS' o 'NEGRAS').
        display_colour (Fore, opcional): Color de la pieza para mostrar en la consola.
            Si no se especifica, se asigna un color por defecto basado en el color de la pieza.

    Attributes:
        __colour__ (str): El color interno de la pieza.
        __display_colour__ (Fore): El color de la pieza para mostrar en la consola.
    """

    def __init__(self, colour, display_colour=None):
        """Inicializa una nueva pieza de ajedrez con un color y un color de visualización."""
        self.__colour__ = colour
        self.__display_colour__ = display_colour or self.default_display_colour()

    @property
    def colour(self):
        """Obtiene el color de la pieza.

        Returns:
            str: El color de la pieza ('BLANCAS' o 'NEGRAS').
        """
        return self.__colour__

    @property
    def display_colour(self):
        """Obtiene el color de visualización de la pieza.

        Returns:
            Fore: El color de visualización en la consola.
        """
        return self.__display_colour__

    @abstractmethod
    def symbol(self):
        """Obtiene el símbolo de la pieza en formato unicode.

        Returns:
            str: El símbolo unicode que representa la pieza.
        """
        pass

    @abstractmethod
    def move(self, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento es válido para esta pieza.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        pass

    def default_display_colour(self):
        """Determina el color de visualización por defecto de la pieza según su color.

        Returns:
            Fore: El color por defecto (blanco para 'BLANCAS', negro para 'NEGRAS').
        """
        if self.colour == 'BLANCAS':
            return Fore.WHITE
        elif self.colour == 'NEGRAS':
            return Fore.BLACK

    def coloured_symbol(self):
        """Genera el símbolo de la pieza coloreado para mostrar en la consola.

        Returns:
            str: El símbolo de la pieza con su color correspondiente.
        """
        return f'{self.display_colour}{self.symbol()}{Style.RESET_ALL}'

    @display_colour.setter
    def display_colour(self, value):
        """Establece el color de visualización de la pieza.

        Args:
            value (Fore): El nuevo color de visualización.
        """
        self.__display_colour__ = value