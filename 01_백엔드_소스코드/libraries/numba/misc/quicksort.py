# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: quicksort.pyc (Python 3.11)

import collections
import numpy as np
from numba.core import types, config
QuicksortImplementation = collections.namedtuple('QuicksortImplementation', ('compile', 'partition', 'partition3', 'insertion_sort', 'run_quicksort'))
Partition = collections.namedtuple('Partition', ('start', 'stop'))
SMALL_QUICKSORT = 15
MAX_STACK = 100

def make_quicksort_impl(wrap, lt, is_argsort, is_list, is_np_array = (None, False, False, False)):
    pass
# WARNING: Decompyle incomplete


def make_py_quicksort(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def make_jit_quicksort(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete
