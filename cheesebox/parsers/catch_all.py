import re
from fractions import Fraction

from cheesebox.parsers.parser import ParserData
from cheesebox.helpers.exception_handler import exception_handler

def find_unit(expression):
    regex = r"(\d+|)\s*([a-zA-Z]+)\b"
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
        if whole_part == 0:
            return f'{fraction_part} {unit}'
        else:
            return f'{whole_part} {fraction_part} {unit}'
    else:
        return f'{whole_part} {unit}'
    

    
catch_all_parser = ParserData(
    name="catch all",
    replacers={},
    regex = r'(\d+\s+[a-zA-Z]+)(?=\s|\b)',
    autocomplete=[],
    function=calculate
)