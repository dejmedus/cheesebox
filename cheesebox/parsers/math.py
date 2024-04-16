from .parser import ParserData

def calculate(expression):
    try:
        return str(eval(expression))

    except SyntaxError:
        return "✖ Invalid syntax"
    except Exception as e:
        return f"Error: {str(e)}"
    
math_parser = ParserData(
    name="math",
    replacers={},
    regex=r"^[0-9+\-*/=. ]+$",
    autocomplete=["plus", "minus", "times", "divided by", "equals"],
    function=calculate
)