# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lambdarepr.pyc (Python 3.11)

from pycode import PythonCodePrinter, MpmathPrinter
from numpy import NumPyPrinter
from sympy.core.sorting import default_sort_key
__all__ = [
    'PythonCodePrinter',
    'MpmathPrinter',
    'NumPyPrinter',
    'LambdaPrinter',
    'NumPyPrinter',
    'IntervalPrinter',
    'lambdarepr']

class LambdaPrinter(PythonCodePrinter):
    pass
# WARNING: Decompyle incomplete


class NumExprPrinter(LambdaPrinter):
    pass
# WARNING: Decompyle incomplete


class IntervalPrinter(LambdaPrinter, MpmathPrinter):
    pass
# WARNING: Decompyle incomplete

for k in NumExprPrinter._numexpr_functions:
    setattr(NumExprPrinter, '_print_%s' % k, NumExprPrinter._print_Function)
    
    def lambdarepr(expr, **settings):
        '''
    Returns a string usable for lambdifying.
    '''
        return LambdaPrinter(settings).doprint(expr)

    return None
