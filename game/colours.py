from colorama import Fore, Style

class ColourScheme:
    def __init__(self, colour1, colour2):
        self.colour1 = colour1
        self.colour2 = colour2

    def colorize(self, symbol):
        from colorama import Fore, Style
        if symbol == '♙':
            return f"{Fore.WHITE}{symbol}{Style.RESET_ALL}"
        elif symbol == '♟':
            return f"{Fore.BLACK}{symbol}{Style.RESET_ALL}"
        else:
            return symbol
