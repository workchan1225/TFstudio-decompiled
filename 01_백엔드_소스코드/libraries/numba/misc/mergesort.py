# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mergesort.pyc (Python 3.11)

'''
The same algorithm as translated from numpy.
See numpy/core/src/npysort/mergesort.c.src.
The high-level numba code is adding a little overhead comparing to
the pure-C implementation in numpy.
'''
import numpy as np
from collections import namedtuple
SMALL_MERGESORT = 20
MergesortImplementation = namedtuple('MergesortImplementation', [
    'run_mergesort'])

def make_mergesort_impl(wrap, lt, is_argsort = (None, False)):
    pass
# WARNING: Decompyle incomplete


def make_jit_mergesort(*args, **kwargs):
    njit = njit
    import numba
# WARNING: Decompyle incomplete
