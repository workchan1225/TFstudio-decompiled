# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: c.pyc (Python 3.11)

__doc__ = '\nC code printer\n\nThe C89CodePrinter & C99CodePrinter converts single SymPy expressions into\nsingle C expressions, using the functions defined in math.h where possible.\n\nA complete code generator, which uses ccode extensively, can be found in\nsympy.utilities.codegen. The codegen module can be used to generate complete\nsource code files that are compilable without further modifications.\n\n\n'
from __future__ import annotations
from typing import Any
from functools import wraps
from itertools import chain
from sympy.core import S
from sympy.core.numbers import equal_valued, Float
from sympy.codegen.ast import Assignment, Pointer, Variable, Declaration, Type, real, complex_, integer, bool_, float32, float64, float80, complex64, complex128, intc, value_const, pointer_const, int8, int16, int32, int64, uint8, uint16, uint32, uint64, untyped, none
from sympy.printing.codeprinter import CodePrinter, requires
from sympy.printing.precedence import precedence, PRECEDENCE
from sympy.sets.fancysets import Range
from sympy.printing.codeprinter import ccode, print_ccode
# WARNING: Decompyle incomplete
