# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pythonmpq.pyc (Python 3.11)

'''
PythonMPQ: Rational number type based on Python integers.

This class is intended as a pure Python fallback for when gmpy2 is not
installed. If gmpy2 is installed then its mpq type will be used instead. The
mpq type is around 20x faster. We could just use the stdlib Fraction class
here but that is slower:

    from fractions import Fraction
    from sympy.external.pythonmpq import PythonMPQ
    nums = range(1000)
    dens = range(5, 1005)
    rats = [Fraction(n, d) for n, d in zip(nums, dens)]
    sum(rats) # <--- 24 milliseconds
    rats = [PythonMPQ(n, d) for n, d in zip(nums, dens)]
    sum(rats) # <---  7 milliseconds

Both mpq and Fraction have some awkward features like the behaviour of
division with // and %:

    >>> from fractions import Fraction
    >>> Fraction(2, 3) % Fraction(1, 4)
    1/6

For the QQ domain we do not want this behaviour because there should be no
remainder when dividing rational numbers. SymPy does not make use of this
aspect of mpq when gmpy2 is installed. Since this class is a fallback for that
case we do not bother implementing e.g. __mod__ so that we can be sure we
are not using it when gmpy2 is installed either.
'''
import operator
from math import gcd
from decimal import Decimal
from fractions import Fraction
import sys
from typing import Tuple as tTuple, Type
_PyHASH_MODULUS = sys.hash_info.modulus
_PyHASH_INF = sys.hash_info.inf

class PythonMPQ:
    pass
# WARNING: Decompyle incomplete

PythonMPQ._compatible_types = (PythonMPQ, int, Decimal, Fraction)
