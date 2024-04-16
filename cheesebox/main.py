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

    def help_message():
        print("\U0001FAA4  Help:")
        print("Type 'exit' to quit.\n")
        print("Usage: ")

        print("\n1. Math:")
        print("   Perform basic math operations.\n")
        print("     two plus two ------------- 4")
        print("     2.5 + 1 ------------------ 3.5")
        print("     1/2 + 1 ------------------ 1.5")

        print("\n2. Measurements:")
        print("   Perform calculations with measurements of the same unit.\n")
        print("     one tsp times two -------- 2 tsp")
        print("     2 cups plus 2 ------------ 4 c")
        print("     2.5 tbsp * 2 ------------- 5 tbsp")
        print("     1/3 cup + 2 -------------- 2 1/3 c")
        print("\n")
        

    welcome_message()

    while True:
        try:
            expression = input(">>> ")
            cleaned_expression = expression.lower().strip()

            if cleaned_expression == 'exit' or cleaned_expression == 'quit()':
                exit_message()
                break
            elif cleaned_expression == 'clear':
                os.system('clear')
                welcome_message()
            elif cleaned_expression == '.help':
                os.system('clear')
                help_message()
            else:
                for parser in all_parsers:
                    result = parser.parse(expression)
                    if result is not None:
                        print(result)
                        break
                if result is None:
                     print("No parser found")

        except KeyboardInterrupt:
            exit_message()
            break


if __name__ == "__main__":
    main()
