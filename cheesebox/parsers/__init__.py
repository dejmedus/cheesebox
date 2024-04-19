"""
This module imports all parsers [math_parser, measurement_parser].

The all_parsers list contains all imported parsers.

The completion_words list contains all autocompletes from all parsers, sorted alphabetically.
"""

from cheesebox.parsers.math import math_parser
from cheesebox.parsers.measurements import measurement_parser

all_parsers = [math_parser, measurement_parser]

completion_words = []
for parser in all_parsers:
    completion_words.extend(parser.autocomplete)

completion_words.sort()