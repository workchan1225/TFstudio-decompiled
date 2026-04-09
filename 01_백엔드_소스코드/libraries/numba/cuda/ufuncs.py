# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ufuncs.pyc (Python 3.11)

'''Contains information on how to translate different ufuncs for the CUDA
target. It is a database of different ufuncs and how each of its loops maps to
a function that implements the inner kernel of that ufunc (the inner kernel
being the per-element function).

Use get_ufunc_info() to get the information related to a ufunc.
'''
import math
import numpy as np
from functools import lru_cache
from numba.core import typing

def get_ufunc_info(ufunc_key):
    return ufunc_db()[ufunc_key]

ufunc_db = (lambda : pass# WARNING: Decompyle incomplete
)()
