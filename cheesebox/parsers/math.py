from .parser import ParserData

def calculate(expression):
    try:
        result = eval(expression)
        result = float(result)
        return f"{format(result, '.2f').rstrip('0').rstrip('.')}"

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