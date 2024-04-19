import re
from fractions import Fraction

from cheesebox.parsers.parser import ParserData
from cheesebox.helpers.exception_handler import exception_handler

def find_unit(expression):
    regex = r"(\d+|)\s*(" + "c|tbsp|tsp|lb|oz|g|ml|l|pt|qt|gal" + r")\b"
    match = re.search(regex, expression)
    if match:
        return match.group(2)
    else:
        return None

@exception_handler
def calculate(expression: str) -> str:
    unit = find_unit(expression)
    expression = expression.replace(unit, "")
    result = eval(expression)

    whole_part = int(result)
    fraction_part = Fraction(result - whole_part).limit_denominator(16)

    if fraction_part:
        return f'{whole_part} {fraction_part} {unit}'
    else:
        return f'{whole_part} {unit}'
    

units = ["c", "tbsp", "tsp", "lb", "oz", "g", "ml", "l", "pt", "qt", "gal"]
    
measurement_parser = ParserData(
    name="measurements",
    replacers={
        "cups": "c",
        "cup": "c",
        "tablespoon": "tbsp",
        "tablespoons": "tbsp",
        "teaspoon": "tsp",
        "teaspoons": "tsp",
        "pound": "lb",
        "pounds": "lb",
        "ounce": "oz",
        "ounces": "oz",
        "gram": "g",
        "grams": "g",
        "milliliter": "ml",
        "milliliters": "ml",
        "liter": "l",
        "liters": "l",
        "pint": "pt",
        "pints": "pt",
        "quart": "qt",
        "quarts": "qt",
        "gallon": "gal",
        "gallons": "gal"
    },
    regex= r'(\d+\s+(?:' + '|'.join(units) + r'))(?=\s|\b)',
    autocomplete=["cup", "tablespoon", "tbsp", "teaspoon", "tsp", "pound", "lb", "ounce", "oz", "gram", "milliliter", "ml", "liter", "l", "pint", "pt", "quart", "qt", "gallon", "gal"],
    function=calculate
)