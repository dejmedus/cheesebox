from cheesebox.parsers import completion_words

def completer(text, state):
    options = [word for word in completion_words if word.startswith(text)]

    if state < len(options):
        return options[state]
    else:
        return None