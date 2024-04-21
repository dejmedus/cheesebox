import os 

colors = {
    'red': '\033[91m',
    'gray': '\033[90m',
    'reset': '\033[0m',
}

def welcome_message():
    print(colors['gray'] + "Welcome to \U0001FAA4")
    print('Type "help" for more')
    print(colors["reset"])

def exit_message():
    # try/except loop so the executable doesn't error on ctrl+c 
    try:
        os.system('clear')
        print("\n\U0001F42D\U0001F44B")
    except KeyboardInterrupt:
        pass

def error_message():
    print("✖ Could not parse input")


def help_message():
    print(colors['gray'] + "\U0001FAA4 Help:")
    print(colors["reset"])

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
    