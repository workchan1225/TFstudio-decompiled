# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: octave.pyc (Python 3.11)

__doc__ = '\nOctave (and Matlab) code printer\n\nThe `OctaveCodePrinter` converts SymPy expressions into Octave expressions.\nIt uses a subset of the Octave language for Matlab compatibility.\n\nA complete code generator, which uses `octave_code` extensively, can be found\nin `sympy.utilities.codegen`.  The `codegen` module can be used to generate\ncomplete source code files.\n\n'
from __future__ import annotations
from typing import Any
from sympy.core import Mul, Pow, S, Rational
from sympy.core.mul import _keep_coeff
from sympy.core.numbers import equal_valued
from sympy.printing.codeprinter import CodePrinter
from sympy.printing.precedence import precedence, PRECEDENCE
from re import search
known_fcns_src1 = [
    'sin',
    'cos',
    'tan',
    'cot',
    'sec',
    'csc',
    'asin',
    'acos',
    'acot',
    'atan',
    'atan2',
    'asec',
    'acsc',
    'sinh',
    'cosh',
    'tanh',
    'coth',
    'csch',
    'sech',
    'asinh',
    'acosh',
    'atanh',
    'acoth',
    'asech',
    'acsch',
    'erfc',
    'erfi',
    'erf',
    'erfinv',
    'erfcinv',
    'besseli',
    'besselj',
    'besselk',
    'bessely',
    'bernoulli',
    'beta',
    'euler',
    'exp',
    'factorial',
    'floor',
    'fresnelc',
    'fresnels',
    'gamma',
    'harmonic',
    'log',
    'polylog',
    'sign',
    'zeta',
    'legendre']
# WARNING: Decompyle incomplete
