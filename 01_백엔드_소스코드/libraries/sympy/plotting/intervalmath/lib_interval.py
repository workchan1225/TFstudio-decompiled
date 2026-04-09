# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lib_interval.pyc (Python 3.11)

''' The module contains implemented functions for interval arithmetic.'''
from functools import reduce
from sympy.plotting.intervalmath import interval
from sympy.external import import_module

def Abs(x):
    if isinstance(x, (int, float)):
        return interval(abs(x))
    if None(x, interval):
        if x.start < 0 and x.end > 0:
            return interval(0, max(abs(x.start), abs(x.end)), is_valid = x.is_valid)
        return None(abs(x.start), abs(x.end))
    raise None


def exp(x):
    '''evaluates the exponential of an interval'''
    np = import_module('numpy')
    if isinstance(x, (int, float)):
        return interval(np.exp(x), np.exp(x))
    if None(x, interval):
        return interval(np.exp(x.start), np.exp(x.end), is_valid = x.is_valid)
    raise None


def log(x):
    '''evaluates the natural logarithm of an interval'''
    np = import_module('numpy')
    if isinstance(x, (int, float)):
        if x <= 0:
            return interval(-(np.inf), np.inf, is_valid = False)
        return None(np.log(x))
    if None(x, interval):
        if not x.is_valid:
            return interval(-(np.inf), np.inf, is_valid = x.is_valid)
        if None.end <= 0:
            return interval(-(np.inf), np.inf, is_valid = False)
        if None.start <= 0:
            return interval(-(np.inf), np.inf, is_valid = None)
        return None(np.log(x.start), np.log(x.end))
    raise None


def log10(x):
    '''evaluates the logarithm to the base 10 of an interval'''
    np = import_module('numpy')
    if isinstance(x, (int, float)):
        if x <= 0:
            return interval(-(np.inf), np.inf, is_valid = False)
        return None(np.log10(x))
    if None(x, interval):
        if not x.is_valid:
            return interval(-(np.inf), np.inf, is_valid = x.is_valid)
        if None.end <= 0:
            return interval(-(np.inf), np.inf, is_valid = False)
        if None.start <= 0:
            return interval(-(np.inf), np.inf, is_valid = None)
        return None(np.log10(x.start), np.log10(x.end))
    raise None


def atan(x):
    '''evaluates the tan inverse of an interval'''
    np = import_module('numpy')
    if isinstance(x, (int, float)):
        return interval(np.arctan(x))
    if None(x, interval):
        start = np.arctan(x.start)
        end = np.arctan(x.end)
        return interval(start, end, is_valid = x.is_valid)
    raise None


def sin(x):
    '''evaluates the sine of an interval'''
    np = import_module('numpy')
    if isinstance(x, (int, float)):
        return interval(np.sin(x))
    if None(x, interval):
        if not x.is_valid:
            return interval(-1, 1, is_valid = x.is_valid)
        (na, __) = None(x.start, np.pi / 2)
        (nb, __) = divmod(x.end, np.pi / 2)
        start = min(np.sin(x.start), np.sin(x.end))
        end = max(np.sin(x.start), np.sin(x.end))
        if nb - na > 4:
            return interval(-1, 1, is_valid = x.is_valid)
        if None == nb:
            return interval(start, end, is_valid = x.is_valid)
        if (None - 1) // 4 != (nb - 1) // 4:
            end = 1
        if (na - 3) // 4 != (nb - 3) // 4:
            start = -1
        return interval(start, end)
    raise None


def cos(x):
    '''Evaluates the cos of an interval'''
    np = import_module('numpy')
    if isinstance(x, (int, float)):
        return interval(np.sin(x))
    if None(x, interval):
        if not np.isfinite(x.start) or np.isfinite(x.end):
            return interval(-1, 1, is_valid = x.is_valid)
        (na, __) = None(x.start, np.pi / 2)
        (nb, __) = divmod(x.end, np.pi / 2)
        start = min(np.cos(x.start), np.cos(x.end))
        end = max(np.cos(x.start), np.cos(x.end))
        if nb - na > 4:
            return interval(-1, 1, is_valid = x.is_valid)
        if None == nb:
            return interval(start, end, is_valid = x.is_valid)
        if None // 4 != nb // 4:
            end = 1
        if (na - 2) // 4 != (nb - 2) // 4:
            start = -1
        return interval(start, end, is_valid = x.is_valid)
    raise None


def tan(x):
    '''Evaluates the tan of an interval'''
    return sin(x) / cos(x)


def sqrt(x):
    '''Evaluates the square root of an interval'''
    np = import_module('numpy')
    if isinstance(x, (int, float)):
        if x > 0:
            return interval(np.sqrt(x))
        return None(-(np.inf), np.inf, is_valid = False)
    if None(x, interval):
        if x.end < 0:
            return interval(-(np.inf), np.inf, is_valid = False)
        if None.start < 0:
            return interval(-(np.inf), np.inf, is_valid = None)
        return None(np.sqrt(x.start), np.sqrt(x.end), is_valid = x.is_valid)
    raise None


def imin(*args):
