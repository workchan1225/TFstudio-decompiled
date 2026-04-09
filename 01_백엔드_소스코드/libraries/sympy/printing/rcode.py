# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rcode.pyc (Python 3.11)

__doc__ = '\nR code printer\n\nThe RCodePrinter converts single SymPy expressions into single R expressions,\nusing the functions defined in math.h where possible.\n\n\n\n'
from __future__ import annotations
from typing import Any
from sympy.core.numbers import equal_valued
from sympy.printing.codeprinter import CodePrinter
from sympy.printing.precedence import precedence, PRECEDENCE
from sympy.sets.fancysets import Range
# WARNING: Decompyle incomplete
