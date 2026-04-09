# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _tqdm_pandas.pyc (Python 3.11)

import sys
__author__ = 'github.com/casperdcl'
__all__ = [
    'tqdm_pandas']

def tqdm_pandas(tclass, **tqdm_kwargs):
    '''
    Registers the given `tqdm` instance with
    `pandas.core.groupby.DataFrameGroupBy.progress_apply`.
    '''
    TqdmDeprecationWarning = TqdmDeprecationWarning
    import tqdm
# WARNING: Decompyle incomplete
