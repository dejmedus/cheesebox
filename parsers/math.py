from .parser import ParserData

def calculate(expression):
    try:
        return eval(expression)

    except Exception as e:
        return f"Error: {str(e)}"
    
math_parser = ParserData(
    name="math",
    replacers={
        "plus": "+",
        "minus": "-",
        "times": "*",
        "divided by": "/",
        "equals": "="
    },
    regex=r"^[0-9+\-*/= ]+$",
    autocomplete=["plus", "minus", "times", "divided by", "equals"],
    function=calculate
)