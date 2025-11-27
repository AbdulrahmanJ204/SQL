from colorama import init, Fore, Style


init(autoreset=True)

class Color:
    KEYWORD = Fore.CYAN
    IDENTIFIER = Fore.GREEN
    LITERAL = Fore.MAGENTA
    OPERATOR = Fore.YELLOW
    ERROR = Fore.RED
    INFO = Fore.WHITE
    RESET = Style.RESET_ALL
