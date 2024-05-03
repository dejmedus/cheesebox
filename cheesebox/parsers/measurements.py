import re
from fractions import Fraction

from cheesebox.parsers.parser import ParserData
from cheesebox.helpers.exception_handler import exception_handler


unit_conversion = {
    "tsp": {"next_unit": "tbsp", "conversion_factor": 3},
    "tbsp": {"next_unit": "c", "conversion_factor": 16},
    "c": {"next_unit": "qt", "conversion_factor": 4},
    "qt": {"next_unit": "gal", "conversion_factor": 4},
    "oz": {"next_unit": "lb", "conversion_factor": 16},
    "g": {"next_unit": "kg", "conversion_factor": 1000},
    "ml": {"next_unit": "l", "conversion_factor": 1000},
}

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

    while unit in unit_conversion and result >= unit_conversion[unit]["conversion_factor"]:
        result /= unit_conversion[unit]["conversion_factor"]
        unit = unit_conversion[unit]["next_unit"]

    whole_part = int(result)
    fraction_part = Fraction(result - whole_part).limit_denominator(16)

    if fraction_part:
        if whole_part == 0:
            return f'{fraction_part} {unit}'
        else:
            return f'{whole_part} {fraction_part} {unit}'
    else:
        return f'{whole_part} {unit}'
    
    
measurement_parser = ParserData(
    name="measurements",
    replacers={
        "cups": "c",
        "cup": "c",
        "tablespoon": "tbsp",
        "tablespoons": "tbsp",
        "tbsps": "tbsp",
        "teaspoon": "tsp",
        "teaspoons": "tsp",
        "tsps": "tsp",
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
    regex= r'(\d+\s+(?:' + 'c|tbsp|tsp|lb|oz|g|ml|l|pt|qt|gal' + r'))(?=\s|\b)',
    autocomplete=["cup", "tablespoon", "tbsp", "teaspoon", "tsp", "pound", "lb", "ounce", "oz", "gram", "milliliter", "ml", "liter", "l", "pint", "pt", "quart", "qt", "gallon", "gal"],
    function=calculate
)
