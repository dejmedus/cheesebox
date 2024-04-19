from cheesebox.parsers.parser import ParserData
from cheesebox.helpers.exception_handler import exception_handler
from cheesebox.helpers.extended_eval import extended_eval

@exception_handler
def calculate(expression):
    result = extended_eval(expression)
    result = float(result)
    return f"{format(result, '.2f').rstrip('0').rstrip('.')}"
    
math_parser = ParserData(
    name="math",
    replacers={},
    regex=r"^[0-9+\-*/=.() ]+$",
    autocomplete=["plus", "minus", "times", "divided by", "equals"],
    function=calculate
)