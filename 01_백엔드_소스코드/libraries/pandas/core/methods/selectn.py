# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: selectn.pyc (Python 3.11)

'''
Implementation of nlargest and nsmallest.
'''
from __future__ import annotations
from collections.abc import Hashable, Sequence
from typing import TYPE_CHECKING, Generic, Literal, cast, final
import numpy as np
from pandas._libs import algos as libalgos
from pandas.core.dtypes.common import is_bool_dtype, is_complex_dtype, is_integer_dtype, is_list_like, is_numeric_dtype, needs_i8_conversion
from pandas.core.dtypes.dtypes import BaseMaskedDtype
from pandas.core.indexes.api import default_index
if TYPE_CHECKING:
    from pandas._typing import DtypeObj, IndexLabel, NDFrameT
    from pandas import DataFrame, Index, Series
else:
    from pandas._typing import T
    NDFrameT = T
    DataFrame = T
    Series = T

def SelectN():
    '''SelectN'''
    
    def __init__(self = None, obj = None, n = None, keep = ('obj', 'NDFrameT', 'n', 'int', 'keep', "Literal['first', 'last', 'all']", 'return', 'None')):
        self.obj = obj
        self.n = n
        self.keep = keep
        if self.keep not in ('first', 'last', 'all'):
            raise ValueError('keep must be either "first", "last" or "all"')

    
    def compute(self = None, method = None):
        raise NotImplementedError

    nlargest = (lambda self = None: self.compute('nlargest'))()
    nsmallest = (lambda self = None: self.compute('nsmallest'))()
    is_valid_dtype_n_method = (lambda dtype = None: if is_numeric_dtype(dtype):
not is_complex_dtype(dtype)None(dtype))()()

SelectN = <NODE:27>(SelectN, 'SelectN', Generic[NDFrameT])

def SelectNSeries():
    '''SelectNSeries'''
    __doc__ = "\n    Implement n largest/smallest for Series\n\n    Parameters\n    ----------\n    obj : Series\n    n : int\n    keep : {'first', 'last'}, default 'first'\n\n    Returns\n    -------\n    nordered : Series\n    "
    
    def compute(self = None, method = None):
        concat = concat
        import pandas.core.reshape.concat
        n = self.n
        dtype = self.obj.dtype
        if not self.is_valid_dtype_n_method(dtype):
            raise TypeError(f'''Cannot use method \'{method}\' with dtype {dtype}''')
        if n <= 0:
            return self.obj[[]]
        original_index = None.obj.index
        default_index = self.obj.reset_index(drop = True)
        if n >= len(default_index):
            ascending = method == 'nsmallest'
            result = default_index.sort_values(ascending = ascending, kind = 'stable').head(n)
            result.index = original_index.take(result.index)
            return result
        dropped = default_index.dropna()
        nan_index = default_index.drop(dropped.index)
        new_dtype = dropped.dtype
        arr = dropped._values
        if needs_i8_conversion(arr.dtype):
            arr = arr.view('i8')
        elif isinstance(arr.dtype, BaseMaskedDtype):
            arr = arr._data
        else:
            arr = np.asarray(arr)
        if arr.dtype.kind == 'b':
            arr = arr.view(np.uint8)
        if method == 'nlargest':
            arr = -arr
            if is_integer_dtype(new_dtype):
                arr -= 1
            elif is_bool_dtype(new_dtype):
                arr = 1 - -arr
        if self.keep == 'last':
            arr = arr[::-1]
        nbase = n
        narr = len(arr)
        n = min(n, narr)
        if len(arr) > 0:
            kth_val = libalgos.kth_smallest(arr.copy(order = 'C'), n - 1)
        else:
            kth_val = np.nan
        (ns,) = np.nonzero(arr <= kth_val)
        inds = ns[arr[ns].argsort(kind = 'stable')]
        if self.keep != 'all':
            inds = inds[:n]
            findex = nbase
        elif  < len(inds), nbase or len(inds), nbase <= len(nan_index) + len(inds):
            pass
        
        len(inds) = len(nan_index) + len(inds)


SelectNSeries = <NODE:27>(SelectNSeries, 'SelectNSeries', SelectN[Series])

def SelectNFrame():
    '''SelectNFrame'''
    pass
# WARNING: Decompyle incomplete

SelectNFrame = <NODE:27>(SelectNFrame, 'SelectNFrame', SelectN[DataFrame])
