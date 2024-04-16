"""
This module imports all shared replacers: numbers, symbols
"""

from .numbers import number_replacers
from .symbols import symbol_replacers
from .fractions import fraction_replacers

shared_replacers = {
    **number_replacers,
    **symbol_replacers,
    **fraction_replacers
}
