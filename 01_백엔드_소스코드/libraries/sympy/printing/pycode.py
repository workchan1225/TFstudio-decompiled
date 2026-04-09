# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pycode.pyc (Python 3.11)

__doc__ = '\nPython code printers\n\nThis module contains Python code printers for plain Python as well as NumPy & SciPy enabled code.\n'
from collections import defaultdict
from itertools import chain
from sympy.core import S
from sympy.core.mod import Mod
from precedence import precedence
from codeprinter import CodePrinter
_kw = {
    'as',
    'if',
    'in',
    'is',
    'or',
    'and',
    'def',
    'del',
    'for',
    'not',
    'try',
    'None',
    'True',
    'elif',
    'else',
    'from',
    'pass',
    'with',
    'False',
    'break',
    'class',
    'raise',
    'while',
    'yield',
    'assert',
    'except',
    'global',
    'import',
    'lambda',
    'return',
    'finally',
    'continue',
    'nonlocal'}
_known_functions = {
    'Abs': 'abs',
    'Min': 'min',
    'Max': 'max' }
# WARNING: Decompyle incomplete
