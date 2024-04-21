
from readchar import readkey, key

from cheesebox.helpers.messages import colors
from cheesebox.parsers import completion_words


def extended_input():
    current_input = ""
    current_suffix = ""

    try:
        print_line('\033[?25l')
        while True:
            char = readkey()
            if char == key.ENTER and current_input:
                print_line('\033[K' + current_input + "\n")
                return current_input
            elif char == key.TAB:
                current_input = current_input + current_suffix
            elif char == key.BACKSPACE:
                if current_input:
                    current_input = current_input[:-1]
            else:
                current_input += char

            autocomplete = current_input and current_input[-1] != " " and get_autocomplete_suffix(current_input)
            if autocomplete:
                current_suffix = autocomplete
                print_line(current_input + colors["light_gray"] + autocomplete + colors["reset"])
            else:
                print_line(current_input)
    except KeyboardInterrupt:
        # we want the outer function to handle ctrl+c
        raise KeyboardInterrupt

def get_autocomplete_suffix(current_input):
    prefix = current_input.split(" ")[-1]
    if len(prefix) > 1:
        for word in completion_words:
            if word.startswith(prefix):
                return word[len(prefix):]
            
    return ""

def print_line(expression):
    print("> " + expression + ' ' * (len(expression) + 10), end='\r')
