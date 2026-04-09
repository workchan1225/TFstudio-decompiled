# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pickle_compat.pyc (Python 3.11)

'''
Pickle compatibility to pandas version 1.0
'''
from __future__ import annotations
import contextlib
import io
import pickle
from typing import TYPE_CHECKING, Any
import numpy as np
from pandas._libs.arrays import NDArrayBacked
from pandas._libs.tslibs import BaseOffset
from pandas.core.arrays import DatetimeArray, PeriodArray, TimedeltaArray
from pandas.core.internals import BlockManager
if TYPE_CHECKING:
    from collections.abc import Generator
_class_locations_map = {
    ('pandas.core.internals.blocks', 'new_block'): ('pandas._libs.internals', '_unpickle_block'),
    ('pandas._libs.tslibs.nattype', '__nat_unpickle'): ('pandas._libs.tslibs.nattype', '_nat_unpickle'),
    ('pandas.core.indexes.numeric', 'Int64Index'): ('pandas.core.indexes.base', 'Index'),
    ('pandas.core.indexes.numeric', 'UInt64Index'): ('pandas.core.indexes.base', 'Index'),
    ('pandas.core.indexes.numeric', 'Float64Index'): ('pandas.core.indexes.base', 'Index'),
    ('pandas.core.arrays.sparse.dtype', 'SparseDtype'): ('pandas.core.dtypes.dtypes', 'SparseDtype') }

class Unpickler(pickle._Unpickler):
    pass
# WARNING: Decompyle incomplete


def loads(bytes_object = None, *, fix_imports, encoding, errors):
    '''
    Analogous to pickle._loads.
    '''
    fd = io.BytesIO(bytes_object)
    return Unpickler(fd, fix_imports = fix_imports, encoding = encoding, errors = errors).load()

patch_pickle = (lambda : pass# WARNING: Decompyle incomplete
)()
