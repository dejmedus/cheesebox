"""
This module imports all parsers and creates two lists: all_parsers and completion_words.

The all_parsers list contains all imported parsers.

The completion_words list contains all autocompletes from all parsers, sorted alphabetically.
"""

from .math import math_parser
from .measurements import measurement_parser


all_parsers = [math_parser, measurement_parser]

completion_words = []
for parser in all_parsers:
    completion_words.extend(parser.autocomplete)

completion_words.sort()