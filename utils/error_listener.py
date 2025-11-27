from antlr4.error.ErrorListener import ErrorListener

class CollectingErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append((line, column, msg))
from utils.colors import Color

def print_errors(errors):
    if not errors:
        print(f"\n{Color.INFO}No lexer errors.{Color.RESET}")
        return

    print(f"\n{Color.ERROR}=== LEXER ERRORS ==={Color.RESET}")
    for line, col, msg in errors:
        print(f"{Color.ERROR}Line {line}, Col {col}:{Color.RESET} {msg}")
