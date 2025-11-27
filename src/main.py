import sys
from antlr4 import FileStream
from generated.SQLLexer import SQLLexer

from utils.error_listener import CollectingErrorListener, print_errors


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.sql>")
        return

    input_stream = FileStream(sys.argv[1], encoding='utf-8')

    lexer = SQLLexer(input_stream)

    # Attach custom error listener
    error_listener = CollectingErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    # Process tokens
    tokens = lexer.getAllTokens()
    for token in tokens:
        token_name = lexer.symbolicNames[token.type]
        print(f"{token_name:15} -> {token.text}")

    # Print all errors at the end
    print_errors(error_listener.errors)


if __name__ == "__main__":
    main()
