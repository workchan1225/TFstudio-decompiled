# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fractions.pyc (Python 3.11)

'''Fraction, infinite-precision, rational numbers.'''
from decimal import Decimal
import math
import numbers
import operator
import re
import sys
__all__ = [
    'Fraction']
_PyHASH_MODULUS = sys.hash_info.modulus
_PyHASH_INF = sys.hash_info.inf
_RATIONAL_FORMAT = re.compile('\n    \\A\\s*                                  # optional whitespace at the start,\n    (?P<sign>[-+]?)                        # an optional sign, then\n    (?=\\d|\\.\\d)                            # lookahead for digit or .digit\n    (?P<num>\\d*|\\d+(_\\d+)*)                # numerator (possibly empty)\n    (?:                                    # followed by\n       (?:/(?P<denom>\\d+(_\\d+)*))?         # an optional denominator\n    |                                      # or\n       (?:\\.(?P<decimal>\\d*|\\d+(_\\d+)*))?  # an optional fractional part\n       (?:E(?P<exp>[-+]?\\d+(_\\d+)*))?      # and optional exponent\n    )\n    \\s*\\Z                                  # and optional whitespace to finish\n', re.VERBOSE | re.IGNORECASE)

class Fraction(numbers.Rational):
    pass
# WARNING: Decompyle incomplete
