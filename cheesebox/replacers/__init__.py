"""
This module imports all shared replacers: numbers, symbols, fractions
"""

from cheesebox.replacers.numbers import number_replacers
from cheesebox.replacers.symbols import symbol_replacers
from cheesebox.replacers.fractions import fraction_replacers

shared_replacers = {
    **number_replacers,
    **symbol_replacers,
    **fraction_replacers
}
