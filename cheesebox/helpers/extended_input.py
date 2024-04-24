import sys
from readchar import readkey, key

from cheesebox.helpers.messages import colors
from cheesebox.parsers import completion_words

history = [""]
history_index = 0

def extended_input():
    global history_index, history
    current_input = ""
    current_suffix = ""
    cursor_x = 0

    try:
        print_line("", cursor_x)

        while True:
            char = readkey()
            if char == key.ENTER:
                current_input = current_input.strip()
                if current_input != "":
                    print_line(current_input + "\n", cursor_x=-3)
                    add_to_history(history, current_input)
                    history_index = 0
                    return current_input
            elif char == key.TAB:
                if current_suffix:
                    current_input = insert(current_input, current_suffix, cursor_x)
                    cursor_x += len(current_suffix)
                    current_suffix = ""
            elif char == key.BACKSPACE:
                if current_input and cursor_x > 0:
                    current_input = current_input[:cursor_x-1] + current_input[cursor_x:]
                    cursor_x = max(0, cursor_x - 1)
            elif char == key.RIGHT:
                cursor_x = min(len(current_input), cursor_x + 1)
            elif char == key.LEFT:
                cursor_x = max(0, cursor_x - 1)
            elif char == key.UP:
                if history_index < len(history) -1:
                    history_index += 1
                    current_input = history[history_index]
                    cursor_x = len(current_input)
            elif char == key.DOWN:
                if history_index > 0:
                    history_index -= 1
                    current_input = history[history_index]
                    cursor_x = len(current_input)
            elif char == key.CTRL_A:
                # jump to start
                cursor_x = 0
            elif char == key.CTRL_E:
                # jump to end
                cursor_x = len(current_input.strip())
            elif char == key.CTRL_W:
                # delete the word before the cursor
                word_before_cursor = current_input[:cursor_x].split(" ")[-1]
                word_start_index = cursor_x - len(word_before_cursor)
                current_input = current_input[:word_start_index] + current_input[cursor_x:]
                cursor_x = word_start_index
            elif char == key.CTRL_U:
                # delete everything before cursor
                current_input = current_input[cursor_x:]
                cursor_x = 0
            else:
                current_input = insert(current_input, char, cursor_x)
                cursor_x += 1

            autocomplete = current_input and (len(current_input) == 1 or len(current_input) > 1 and current_input[-1] != " ") and get_autocomplete_suffix(current_input, cursor_x)

            # isprintable prevents autocomplete on backspace/right/left keys
            if autocomplete and char.isprintable():
                current_suffix = autocomplete
                autocomplete_hint = insert(current_input, colors["light_gray"] + autocomplete + colors["reset"], cursor_x)
                print_line(autocomplete_hint, cursor_x)
            else:
                print_line(current_input, cursor_x)

    except KeyboardInterrupt:
        # we want the outer function to handle ctrl+c
        raise KeyboardInterrupt

def get_autocomplete_suffix(current_input, cursor_x):
    prefix = current_input[:cursor_x].split(" ")[-1]

    if len(prefix) > 1:
        for word in completion_words:
            if word.startswith(prefix):
                return word[len(prefix):]
            
    return ""

def add_to_history(history, str):
    history.pop(0)
    history.insert(0, "")
    history.insert(1, str)
           
def insert(current_input, str, cursor_x):
    return current_input[:cursor_x] + str + current_input[cursor_x:]

def print_line(expression, cursor_x):
    # problem: cant handle strings longer than line
    # columns, _ = shutil.get_terminal_size()
    # max_length = columns - 10

    clear_line = "\033[2K"
    return_to_start = "\r"

    print(clear_line, end='')
    print(return_to_start + "> " + expression, end='')
    # cursor_x + 3 to account for "> "
    print("\033[" + str(cursor_x + 3) + "G", end='')
    sys.stdout.flush()
