#!/usr/bin/env python3

import os
import readline

from .parsers import *
from .helpers.completer import completer


if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")


def main():
    readline.set_completer(completer)

    def welcome_message():
        print("Welcome to \U0001FAA4")
        print('Type ".help" for more')

    def exit_message():
        print("\n\U0001F42D\U0001F44B")
        

    welcome_message()

    while True:
        try:
            expression = input(">>> ")

            if expression.lower() == 'exit':
                exit_message()
                break
            elif expression.lower() == 'clear':
                os.system('clear')
                welcome_message()
            elif expression.strip() == '.help':
                print("\U0001FAA4 Help:")
                print("- Enter a mathematical expression to calculate.")
                print("- Type 'exit' to quit.")
            else:
                for parser in all_parsers:
                    result = parser.parse(expression)
                    if result is not None:
                        print(f"{result}")
                        break
                if result is None:
                     print("No parser found")

        except KeyboardInterrupt:
            exit_message()
            break


if __name__ == "__main__":
    main()
