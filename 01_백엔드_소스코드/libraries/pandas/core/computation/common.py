# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from __future__ import annotations
from functools import reduce
import numpy as np
from pandas._config import get_option

def ensure_decoded(s = None):
    '''
    If we have bytes, decode them to unicode.
    '''
    if isinstance(s, (np.bytes_, bytes)):
        s = s.decode(get_option('display.encoding'))
    return s


def result_type_many(*arrays_and_dtypes):
    '''
    Wrapper around numpy.result_type which overcomes the NPY_MAXARGS (32)
    argument limit.
    '''
    pass
# WARNING: Decompyle incomplete
