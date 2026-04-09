# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: accessors.pyc (Python 3.11)

'''Accessors for arrow-backed data.'''
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, cast
from pandas.compat import HAS_PYARROW
from pandas.core.dtypes.common import is_list_like
if HAS_PYARROW:
    import pyarrow as pa
    from pyarrow.compute import compute as pc
    from pandas.core.dtypes.dtypes import ArrowDtype
if TYPE_CHECKING:
    from collections.abc import Iterator
    from pandas import DataFrame, Series

def ArrowAccessor():
    '''ArrowAccessor'''
    __init__ = (lambda self = None, data = None, validation_msg = abstractmethod: self._data = dataself._validation_msg = validation_msgself._validate(data))()
    _is_valid_pyarrow_dtype = (lambda self = None, pyarrow_dtype = None: pass)()
    
    def _validate(self = None, data = None):
        dtype = data.dtype
        if not HAS_PYARROW or isinstance(dtype, ArrowDtype):
            raise AttributeError(self._validation_msg.format(dtype = dtype))
        if not self._is_valid_pyarrow_dtype(dtype.pyarrow_dtype):
            raise AttributeError(self._validation_msg.format(dtype = dtype))

    _pa_array = (lambda self: self._data.array._pa_array)()

ArrowAccessor = <NODE:27>(ArrowAccessor, 'ArrowAccessor', metaclass = ABCMeta)

class ListAccessor(ArrowAccessor):
    pass
# WARNING: Decompyle incomplete


class StructAccessor(ArrowAccessor):
    pass
# WARNING: Decompyle incomplete
