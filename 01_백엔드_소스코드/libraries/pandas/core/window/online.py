# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: online.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from pandas.compat._optional import import_optional_dependency

def generate_online_numba_ewma_func(nopython = None, nogil = None, parallel = None):
    '''
    Generate a numba jitted groupby ewma function specified by values
    from engine_kwargs.

    Parameters
    ----------
    nopython : bool
        nopython to be passed into numba.jit
    nogil : bool
        nogil to be passed into numba.jit
    parallel : bool
        parallel to be passed into numba.jit

    Returns
    -------
    Numba function
    '''
    pass
# WARNING: Decompyle incomplete


class EWMMeanState:
    
    def __init__(self, com = None, adjust = None, ignore_na = None, shape = ('return', 'None')):
        alpha = 1 / (1 + com)
        self.shape = shape
        self.adjust = adjust
        self.ignore_na = ignore_na
        self.new_wt = 1 if adjust else alpha
        self.old_wt_factor = 1 - alpha
        self.old_wt = np.ones(self.shape[-1])
        self.last_ewm = None

    
    def run_ewm(self, weighted_avg, deltas, min_periods, ewm_func):
        (result, old_wt) = ewm_func(weighted_avg, deltas, min_periods, self.old_wt_factor, self.new_wt, self.old_wt, self.adjust, self.ignore_na)
        self.old_wt = old_wt
        self.last_ewm = result[-1]
        return result

    
    def reset(self = None):
        self.old_wt = np.ones(self.shape[-1])
        self.last_ewm = None
