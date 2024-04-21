#!/usr/bin/env python3

import os
import readline

from cheesebox.parsers import *
from cheesebox.helpers.completer import completer
from cheesebox.helpers.messages import *


if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")


def main():
    readline.set_completer(completer)
    os.system('clear')
    welcome_message()
    

    while True:
        try:
            expression = input("> ")
            cleaned_expression = expression.lower().strip()

            if cleaned_expression == 'exit' or cleaned_expression == 'quit()':
                exit_message()
                break
            elif cleaned_expression == 'clear':
                os.system('clear')
                welcome_message()
            elif cleaned_expression == 'help':
                os.system('clear')
                help_message()
            else:
                for parser in all_parsers:
                    result = parser.parse(expression)
                    if result is not None:
                        print(result)
                        break
                if result is None:
                    error_message()

        except KeyboardInterrupt:
            exit_message()
            break


if __name__ == "__main__":
    main()
