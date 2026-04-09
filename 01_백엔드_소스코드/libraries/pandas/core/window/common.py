# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

'''Common utility functions for rolling operations'''
from __future__ import annotations
from collections import defaultdict
from typing import cast
import numpy as np
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.indexes.api import MultiIndex

def flex_binary_moment(arg1 = None, arg2 = None, f = None, pairwise = (False,)):
    pass
# WARNING: Decompyle incomplete


def zsqrt(x):
    np.errstate(all = 'ignore')
    result = np.sqrt(x)
    mask = x < 0
    None(None, None)


def prep_binary(arg1, arg2):
    X = arg1 + 0 * arg2
    Y = arg2 + 0 * arg1
    return (X, Y)
