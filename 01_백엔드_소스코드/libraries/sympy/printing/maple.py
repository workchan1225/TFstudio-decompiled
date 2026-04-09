# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: maple.pyc (Python 3.11)

__doc__ = '\nMaple code printer\n\nThe MapleCodePrinter converts single SymPy expressions into single\nMaple expressions, using the functions defined in the Maple objects where possible.\n\n\nFIXME: This module is still under actively developed. Some functions may be not completed.\n'
from sympy.core import S
from sympy.core.numbers import Integer, IntegerConstant, equal_valued
from sympy.printing.codeprinter import CodePrinter
from sympy.printing.precedence import precedence, PRECEDENCE
import sympy
_known_func_same_name = ('sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'sinh', 'cosh', 'tanh', 'sech', 'csch', 'coth', 'exp', 'floor', 'factorial', 'bernoulli', 'euler', 'fibonacci', 'gcd', 'lcm', 'conjugate', 'Ci', 'Chi', 'Ei', 'Li', 'Si', 'Shi', 'erf', 'erfc', 'harmonic', 'LambertW', 'sqrt')
# WARNING: Decompyle incomplete
