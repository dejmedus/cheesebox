import re
from fractions import Fraction

from cheesebox.parsers.parser import ParserData
from cheesebox.helpers.exception_handler import exception_handler

unit_conversions = {
    "tsp": {
        "tbsp": 1/3,
        "c": 1/48,
        "fl oz": 1/6,
        "ml": 4.929,
        "l": 4.929/1000,
        "pt": 1/96,
        "qt": 1/192,
        "gal": 1/768,
        "g": 4.929,
        "kg": 4.929/1000,
        "oz": 1/6,
        "lb": 1/96,
    },
    "tbsp": {
        "tsp": 3,
        "c": 1/16,
        "fl oz": 1/2,
        "ml": 14.787,
        "l": 14.787/1000,
        "pt": 1/32,
        "qt": 1/64,
        "gal": 1/256,
        "g": 14.787,
        "kg": 14.787/1000,
        "oz": 1/2,
        "lb": 1/32,
    },
    "c": {
        "tsp": 48,
        "tbsp": 16,
        "fl oz": 8,
        "ml": 236.588,
        "l": 236.588/1000,
        "pt": 1/2,
        "qt": 1/4,
        "gal": 1/16,
        "g": 236.588,
        "kg": 236.588/1000,
        "oz": 8,
        "lb": 1/2,
    },
    "fl oz": {
        "tsp": 6,
        "tbsp": 2,
        "c": 1/8,
        "ml": 29.5735,
        "l": 29.5735/1000,
        "pt": 1/16,
        "qt": 1/32,
        "gal": 1/128,
        "g": 29.5735,
        "kg": 29.5735/1000,
        "oz": 1,
        "lb": 1/16,
    },
    "ml": {
        "tsp": 0.202884,
        "tbsp": 0.067628,
        "c": 0.004227,
        "fl oz": 0.033814,
        "l": 0.001,
        "pt": 0.002113,
        "qt": 0.001057,
        "gal": 0.000264,
        "g": 1,
        "kg": 0.001,
        "oz": 0.035274,
        "lb": 0.00220462,
    },
    "l": {
        "tsp": 202.884,
        "tbsp": 67.628,
        "c": 4.227,
        "fl oz": 33.814,
        "ml": 1000,
        "pt": 2.11338,
        "qt": 1.05669,
        "gal": 0.264172,
        "g": 1000,
        "kg": 1,
        "oz": 35.274,
        "lb": 2.20462,
    },
    "pt": {
        "tsp": 96,
        "tbsp": 32,
        "c": 2,
        "fl oz": 16,
        "ml": 473.176,
        "l": 473.176/1000,
        "qt": 1/2,
        "gal": 1/8,
        "g": 473.176,
        "kg": 473.176/1000,
        "oz": 16,
        "lb": 1,
    },
    "qt": {
        "tsp": 192,
        "tbsp": 64,
        "c": 4,
        "fl oz": 32,
        "ml": 946.353,
        "l": 946.353/1000,
        "pt": 2,
        "gal": 1/4,
        "g": 946.353,
        "kg": 946.353/1000,
        "oz": 32,
        "lb": 2,
    },
    "gal": {
        "tsp": 768,
        "tbsp": 256,
        "c": 16,
        "fl oz": 128,
        "ml": 3785.41,
        "l": 3.78541,
        "pt": 8,
        "qt": 4,
        "g": 3785.41,
        "kg": 3.78541,
        "oz": 128,
        "lb": 8,
    },
    "g": {
        "tsp": 0.202884,
        "tbsp": 0.067628,
        "c": 0.004227,
        "fl oz": 0.033814,
        "ml": 1,
        "l": 0.001,
        "pt": 0.002113,
        "qt": 0.001057,
        "gal": 0.000264,
        "kg": 0.001,
        "oz": 0.035274,
        "lb": 0.00220462,
    },
    "kg": {
        "tsp": 202.884,
        "tbsp": 67.628,
        "c": 4.227,
        "fl oz": 33.814,
        "ml": 1000,
        "l": 1,
        "pt": 2.11338,
        "qt": 1.05669,
        "gal": 0.264172,
        "g": 1000,
        "oz": 35.274,
        "lb": 2.20462,
    },
    "oz": {
        "tsp": 6,
        "tbsp": 2,
        "c": 1/8,
        "fl oz": 1,
        "ml": 29.5735,
        "l": 29.5735/1000,
        "pt": 1/16,
        "qt": 1/32,
        "gal": 1/128,
        "g": 28,
        "kg": 28/1000,
        "lb": 1/16,
    },
    "lb": {
        "tsp": 96,
        "tbsp": 32,
        "c": 2,
        "fl oz": 16,
        "ml": 473.176,
        "l": 473.176/1000,
        "pt": 1/2,
        "qt": 1/4,
        "gal": 1/8,
        "g": 453.592,
        "kg": 453.592/1000,
        "oz": 16,
    },
}
units = ["c", "tbsp", "tsp", "lb", "oz", "g", "ml", "l", "pt", "qt", "gal"]

def convert(quantity, original_unit, unit):
    if original_unit == unit:
        return quantity

    conversion = unit_conversions[original_unit][unit]
    return quantity * conversion

def find_unit(expression):
    regex = r'\d+\s*((?:' + '|'.join(units) + r'))\s+to\s+((?:' + '|'.join(units) + r'))(?=\s|\b)'
    match = re.search(regex, expression)
    if match:
        return match.group(1), match.group(2)
    else:
        return None

@exception_handler
def calculate(expression: str) -> str:
    original_unit, unit = find_unit(expression)
    expression = re.sub(r'[a-zA-Z]', '', expression)
    result = eval(expression)

    result = convert(result, original_unit, unit)

    whole_part = int(result)
    fraction_part = Fraction(result - whole_part).limit_denominator(16)

    if fraction_part:
        if whole_part == 0:
            return f'{fraction_part} {unit}'
        else:
            return f'{whole_part} {fraction_part} {unit}'
    else:
        return f'{whole_part} {unit}'
    
    
conversion_parser = ParserData(
    name="unit conversion",
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
    regex = r'(\d+\s*(?:' + '|'.join(units) + r'))\s+to\s+((?:' + '|'.join(units) + r'))(?=\s|\b)',
    autocomplete=["cup", "tablespoon", "tbsp", "teaspoon", "tsp", "pound", "lb", "ounce", "oz", "gram", "milliliter", "ml", "liter", "l", "pint", "pt", "quart", "qt", "gallon", "gal"],
    function=calculate
)
