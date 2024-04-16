import re
from fractions import Fraction
from ..replacers import shared_replacers


class ParserData:
    """
    A class used to represent a Parser for different types of data.

    ...

    Attributes
    ----------
    replacers : dict
        a dictionary mapping words to their corresponding symbols
    regex : str
        a regular expression used to validate the transformed expression
    autocomplete : list
        a list of words for autocomplete functionality
    function : callable
        a function that is applied to the transformed and validated expression

    Methods
    -------
    parse(expression):
        Transforms the expression using the replacers, validates it with the regex, 
        and applies the function to it.
    """
        
    def __init__(self, name, replacers, regex, autocomplete, function):
        self.name = name
        self.replacers = replacers
        self.regex = regex
        self.autocomplete = autocomplete
        self.function = function

    def parse(self, expression):
        all_replacers = {
            **shared_replacers,
            **self.replacers
        }

        sorted_replacers = sorted(all_replacers.items(), key=lambda item: len(item[0]), reverse=True)

        for word, symbol in sorted_replacers:
            expression = expression.replace(word, symbol)

        if re.search(self.regex, expression):
            expression = handle_fractions(expression)
            return self.function(expression)
        return None


def handle_fractions(expression):
    mixed_fractions = re.findall(r'\b\d+\s*\d*/\d+\b', expression)
    for fraction in mixed_fractions:
        parts = fraction.split()
        if len(parts) == 2:
            whole_number = int(parts[0])
            decimal = float(Fraction(parts[1]))
            expression = expression.replace(fraction, str(whole_number + decimal))
        else:
            decimal = float(Fraction(fraction))
            expression = expression.replace(fraction, str(decimal))
    return expression