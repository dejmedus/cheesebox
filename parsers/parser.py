import re

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
        shared_replacers = {
            "plus": "+",
            "minus": "-",
            "times": "*",
            "divided by": "/",
            "equals": "=",
            "cup": "c",
            **self.replacers
        }
                
        for word, symbol in shared_replacers.items():
            expression = expression.replace(word, symbol)

        # if re.match(self.regex, expression):
        if re.search(self.regex, expression):
            print(f"Using {self.name} parser")
            return self.function(expression)
        return None

