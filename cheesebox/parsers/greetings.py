import re
from cheesebox.parsers.parser import ParserData
from cheesebox.helpers.exception_handler import exception_handler

@exception_handler
def greet_back(expression: str) -> str:
    if expression == "cheese":
        return "🧀"
    else:
        return "🐭💬"

greetings = ["hi", "hello", "hey", "hiya", "cheese"]

greetings_parser = ParserData(
    name="greetings",
    replacers={},
    regex= re.compile("|".join(greetings)),
    autocomplete=[],
    function=greet_back
)