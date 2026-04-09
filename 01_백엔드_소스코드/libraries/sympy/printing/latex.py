# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: latex.pyc (Python 3.11)

__doc__ = '\nA Printer which converts an expression into its LaTeX equivalent.\n'
from __future__ import annotations
from typing import Any, Callable, TYPE_CHECKING
import itertools
from sympy.core import Add, Float, Mod, Mul, Number, S, Symbol, Expr
from sympy.core.alphabets import greeks
from sympy.core.containers import Tuple
from sympy.core.function import Function, AppliedUndef, Derivative
from sympy.core.operations import AssocOp
from sympy.core.power import Pow
from sympy.core.sorting import default_sort_key
from sympy.core.sympify import SympifyError
from sympy.logic.boolalg import true, BooleanTrue, BooleanFalse
from sympy.printing.precedence import precedence_traditional
from sympy.printing.printer import Printer, print_function
from sympy.printing.conventions import split_super_sub, requires_partial
from sympy.printing.precedence import precedence, PRECEDENCE
from mpmath.libmp.libmpf import prec_to_dps, to_str as mlib_to_str
from sympy.utilities.iterables import has_variety, sift
import re
if TYPE_CHECKING:
    from sympy.tensor.array import NDimArray
    from sympy.vector.basisdependent import BasisDependent
accepted_latex_functions = [
    'arcsin',
    'arccos',
    'arctan',
    'sin',
    'cos',
    'tan',
    'sinh',
    'cosh',
    'tanh',
    'sqrt',
    'ln',
    'log',
    'sec',
    'csc',
    'cot',
    'coth',
    're',
    'im',
    'frac',
    'root',
    'arg']
# WARNING: Decompyle incomplete
