# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tensorflow.pyc (Python 3.11)

from sympy.external.importtools import version_tuple
from collections.abc import Iterable
from sympy.core.mul import Mul
from sympy.core.singleton import S
from sympy.codegen.cfunctions import Sqrt
from sympy.external import import_module
from sympy.printing.precedence import PRECEDENCE
from sympy.printing.pycode import AbstractPythonCodePrinter, ArrayPrinter
import sympy
tensorflow = import_module('tensorflow')

class TensorflowPrinter(AbstractPythonCodePrinter, ArrayPrinter):
    pass
# WARNING: Decompyle incomplete


def tensorflow_code(expr, **settings):
    printer = TensorflowPrinter(settings)
    return printer.doprint(expr)
