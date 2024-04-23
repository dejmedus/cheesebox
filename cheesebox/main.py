#!/usr/bin/env python3

import os
import readline

from cheesebox.parsers import *
from cheesebox.helpers.messages import *
from cheesebox.helpers.extended_input import extended_input


def main():
    history = [""]
    history_index = 0
    os.system('clear')
    welcome_message()

    while True:
        try:
            expression = extended_input(history, history_index)
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
