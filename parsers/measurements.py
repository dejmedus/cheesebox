from .parser import ParserData

import re
import fractions


def find_unit(expression):
    regex = r"(\d+|)\s*(" + "c|tbsp|tsp|lb|oz|g|ml|l|pt|qt|gal" + r")\b"
    match = re.search(regex, expression)
    if match:
        return match.group(2)
    else:
        return None
    
def calculate(expression):
    try:
        unit = find_unit(expression)
        expression = expression.replace(unit, "")
        result = eval(expression)
        fraction = fractions.Fraction.from_float(result).limit_denominator()
        if fraction.denominator == 1:
            return f'{fraction.numerator} {unit}'
        else:
            return f'{fraction.numerator // fraction.denominator} {fraction.numerator % fraction.denominator}/{fraction.denominator} {unit}'

    except Exception as e:
        return f"Error: {str(e)}"
    
measurement_parser = ParserData(
    name="measurments",
     replacers={
        "tablespoon": "tbsp",
        "teaspoon": "tsp",
        "pound": "lb",
        "ounce": "oz",
        "gram": "g",
        "milliliter": "ml",
        "liter": "l",
        "pint": "pt",
        "quart": "qt",
        "gallon": "gal"
    },
    regex = "(\d+|)\s*(" + "c|tbsp|tsp|lb|oz|g|ml|l|pt|qt|gal" + r")\b",
    autocomplete=["cup", "tablespoon", "tbsp", "teaspoon", "tsp", "pound", "lb", "ounce", "oz", "gram", "milliliter", "ml", "liter", "l", "pint", "pt", "quart", "qt", "gallon", "gal"],
    function=calculate
)