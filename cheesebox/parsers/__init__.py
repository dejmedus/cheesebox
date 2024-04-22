"""
This module imports all parsers [math_parser, measurement_parser].

The all_parsers list contains all imported parsers.

The completion_words list contains all autocompletes from all parsers, sorted alphabetically.
"""

from cheesebox.parsers.math import math_parser
from cheesebox.parsers.measurements import measurement_parser
from cheesebox.parsers.greetings import greetings_parser
from cheesebox.parsers.catch_all import catch_all_parser

all_parsers = [math_parser, measurement_parser, catch_all_parser, greetings_parser]

completion_words = []
for parser in all_parsers:
    parser.autocomplete.sort()
    completion_words.extend(parser.autocomplete)
