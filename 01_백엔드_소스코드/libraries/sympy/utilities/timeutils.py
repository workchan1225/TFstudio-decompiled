# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: timeutils.pyc (Python 3.11)

"""Simple tools for timing functions' execution, when IPython is not available. """
import timeit
import math
_scales = [
    1,
    1000,
    1e+06,
    1e+09]
_units = [
    's',
    'ms',
    'μs',
    'ns']

def timed(func, setup, limit = ('pass', None)):
    '''Adaptively measure execution time of a function. '''
    timer = timeit.Timer(func, setup = setup)
    (repeat, number) = (3, 1)
# WARNING: Decompyle incomplete


def __do_timings():
    import os
    res = os.getenv('SYMPY_TIMINGS', '')
    res = res.split(',')()
    return set(res)

_do_timings = __do_timings()
_timestack = None

def _print_timestack(stack, level = (1,)):
    print('-' * level, '%.2f %s%s' % (stack[2], stack[0], stack[3]))
    for s in stack[1]:
        _print_timestack(s, level + 1)
        return None


def timethis(name):
    pass
# WARNING: Decompyle incomplete
