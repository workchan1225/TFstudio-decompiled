# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fortran.pyc (Python 3.11)

__doc__ = '\nFortran code printer\n\nThe FCodePrinter converts single SymPy expressions into single Fortran\nexpressions, using the functions defined in the Fortran 77 standard where\npossible. Some useful pointers to Fortran can be found on wikipedia:\n\nhttps://en.wikipedia.org/wiki/Fortran\n\nMost of the code below is based on the "Professional Programmer\'s Guide to\nFortran77" by Clive G. Page:\n\nhttps://www.star.le.ac.uk/~cgp/prof77.html\n\nFortran is a case-insensitive language. This might cause trouble because\nSymPy is case sensitive. So, fcode adds underscores to variable names when\nit is necessary to make them different for Fortran.\n'
from __future__ import annotations
from typing import Any
from collections import defaultdict
from itertools import chain
import string
from sympy.codegen.ast import Assignment, Declaration, Pointer, value_const, float32, float64, float80, complex64, complex128, int8, int16, int32, int64, intc, real, integer, bool_, complex_, none, stderr, stdout
from sympy.codegen.fnodes import allocatable, isign, dsign, cmplx, merge, literal_dp, elemental, pure, intent_in, intent_out, intent_inout
from sympy.core import S, Add, N, Float, Symbol
from sympy.core.function import Function
from sympy.core.numbers import equal_valued
from sympy.core.relational import Eq
from sympy.sets import Range
from sympy.printing.codeprinter import CodePrinter
from sympy.printing.precedence import precedence, PRECEDENCE
from sympy.printing.printer import printer_context
from sympy.printing.codeprinter import fcode, print_fcode
# WARNING: Decompyle incomplete
