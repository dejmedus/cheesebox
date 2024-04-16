"""
This module imports all shared replacers: numbers, symbols
"""

from .numbers import number_replacers
from .symbols import symbol_replacers

shared_replacers = {
    **number_replacers,
    **symbol_replacers
}
