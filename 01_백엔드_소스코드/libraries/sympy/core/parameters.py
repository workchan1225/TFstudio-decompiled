# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parameters.pyc (Python 3.11)

'''Thread-safe global parameters'''
from cache import clear_cache
from contextlib import contextmanager
from threading import local

class _global_parameters(local):
    pass
# WARNING: Decompyle incomplete

global_parameters = _global_parameters(evaluate = True, distribute = True, exp_is_pow = False)

class evaluate:
    ''' Control automatic evaluation

    Explanation
    ===========

    This context manager controls whether or not all SymPy functions evaluate
    by default.

    Note that much of SymPy expects evaluated expressions.  This functionality
    is experimental and is unlikely to function as intended on large
    expressions.

    Examples
    ========

    >>> from sympy import evaluate
    >>> from sympy.abc import x
    >>> print(x + x)
    2*x
    >>> with evaluate(False):
    ...     print(x + x)
    x + x
    '''
    
    def __init__(self, x):
        self.x = x
        self.old = []

    
    def __enter__(self):
        self.old.append(global_parameters.evaluate)
        global_parameters.evaluate = self.x

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        global_parameters.evaluate = self.old.pop()


distribute = (lambda x: pass# WARNING: Decompyle incomplete
)()
_exp_is_pow = (lambda x: pass# WARNING: Decompyle incomplete
)()
