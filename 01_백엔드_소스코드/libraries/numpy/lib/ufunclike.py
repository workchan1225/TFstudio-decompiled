# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ufunclike.pyc (Python 3.11)

'''
Module of functions that are like ufuncs in acting on arrays and optionally
storing results in an output array.

'''
__all__ = [
    'fix',
    'isneginf',
    'isposinf']

numeric
from numpy.core.overrides import array_function_dispatch
import numpy.core.numeric, core
import warnings
import functools

def _dispatcher(x, out = (None,)):
    return (x, out)

fix = (lambda x, out = (None,): res = nx.asanyarray(nx.ceil(x, out = out))res = nx.floor(x, out = res, where = nx.greater_equal(x, 0))# WARNING: Decompyle incomplete
)()
isposinf = (lambda x, out = (None,): is_inf = nx.isinf(x)try:
signbit = ~nx.signbit(x)nx.logical_and(is_inf, signbit, out)except TypeError:
e = Nonedtype = nx.asanyarray(x).dtyperaise TypeError(f'''This operation is not supported for {dtype} values because it would be ambiguous.'''), ee = Nonedel e)()
isneginf = (lambda x, out = (None,): is_inf = nx.isinf(x)try:
signbit = nx.signbit(x)nx.logical_and(is_inf, signbit, out)except TypeError:
e = Nonedtype = nx.asanyarray(x).dtyperaise TypeError(f'''This operation is not supported for {dtype} values because it would be ambiguous.'''), ee = Nonedel e)()
