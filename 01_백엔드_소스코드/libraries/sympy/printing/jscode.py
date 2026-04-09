# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: jscode.pyc (Python 3.11)

__doc__ = '\nJavascript code printer\n\nThe JavascriptCodePrinter converts single SymPy expressions into single\nJavascript expressions, using the functions defined in the Javascript\nMath object where possible.\n\n'
from __future__ import annotations
from typing import Any
from sympy.core import S
from sympy.core.numbers import equal_valued
from sympy.printing.codeprinter import CodePrinter
from sympy.printing.precedence import precedence, PRECEDENCE
# WARNING: Decompyle incomplete
