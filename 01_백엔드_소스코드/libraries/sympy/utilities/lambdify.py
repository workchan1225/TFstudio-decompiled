# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lambdify.pyc (Python 3.11)

__doc__ = '\nThis module provides convenient functions to transform SymPy expressions to\nlambda functions which can be used to calculate numerical values very fast.\n'
from __future__ import annotations
from typing import Any
import builtins
import inspect
import keyword
import textwrap
import linecache
from sympy.external import import_module
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.utilities.decorator import doctest_depends_on
from sympy.utilities.iterables import is_sequence, iterable, NotIterable, flatten
from sympy.utilities.misc import filldedent
__doctest_requires__ = {
    ('lambdify',): [
        'numpy',
        'tensorflow'] }
MATH_DEFAULT: 'dict[str, Any]' = { }
MPMATH_DEFAULT: 'dict[str, Any]' = { }
NUMPY_DEFAULT: 'dict[str, Any]' = {
    'I': (0+1j) }
SCIPY_DEFAULT: 'dict[str, Any]' = {
    'I': (0+1j) }
CUPY_DEFAULT: 'dict[str, Any]' = {
    'I': (0+1j) }
JAX_DEFAULT: 'dict[str, Any]' = {
    'I': (0+1j) }
TENSORFLOW_DEFAULT: 'dict[str, Any]' = { }
SYMPY_DEFAULT: 'dict[str, Any]' = { }
NUMEXPR_DEFAULT: 'dict[str, Any]' = { }
MATH = MATH_DEFAULT.copy()
MPMATH = MPMATH_DEFAULT.copy()
NUMPY = NUMPY_DEFAULT.copy()
SCIPY = SCIPY_DEFAULT.copy()
CUPY = CUPY_DEFAULT.copy()
JAX = JAX_DEFAULT.copy()
TENSORFLOW = TENSORFLOW_DEFAULT.copy()
SYMPY = SYMPY_DEFAULT.copy()
NUMEXPR = NUMEXPR_DEFAULT.copy()
MATH_TRANSLATIONS = {
    'ceiling': 'ceil',
    'E': 'e',
    'ln': 'log' }
# WARNING: Decompyle incomplete
