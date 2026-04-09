# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numeric.pyc (Python 3.11)

from __future__ import annotations
import numbers
from typing import TYPE_CHECKING, Any, Self
import numpy as np
from pandas._config import is_nan_na
from pandas._libs import lib, missing as libmissing
from pandas.errors import AbstractMethodError
from pandas.util._decorators import cache_readonly
from pandas.core.dtypes.common import is_integer_dtype, is_string_dtype, pandas_dtype
from pandas.core.arrays.masked import BaseMaskedArray, BaseMaskedDtype
if TYPE_CHECKING:
    from collections.abc import Callable, Mapping
    import pyarrow
    from pandas._typing import DtypeObj, npt
    from pandas.core.dtypes.dtypes import ExtensionDtype

class NumericDtype(BaseMaskedDtype):
    _checker: 'Callable[[Any], bool]' = 'NumericDtype'
    
    def __repr__(self = None):
        return f'''{self.name}Dtype()'''

    is_signed_integer = (lambda self = None: self.kind == 'i')()
    is_unsigned_integer = (lambda self = None: self.kind == 'u')()
    _is_numeric = (lambda self = None: True)()
    
    def __from_arrow__(self = None, array = None):
        '''
        Construct IntegerArray/FloatingArray from pyarrow Array/ChunkedArray.
        '''
        import pyarrow
        pyarrow_array_to_numpy_and_mask = pyarrow_array_to_numpy_and_mask
        import pandas.core.arrays.arrow._arrow_utils
        array_class = self.construct_array_type()
        pyarrow_type = pyarrow.from_numpy_dtype(self.type)
        if not array.type.equals(pyarrow_type) and pyarrow.types.is_null(array.type):
            rt_dtype = pandas_dtype(array.type.to_pandas_dtype())
            if rt_dtype.kind not in 'iuf':
                raise TypeError(f'''Expected array of {self} type, got {array.type} instead''')
            array = array.cast(pyarrow_type)
        if isinstance(array, pyarrow.ChunkedArray):
            array = array.combine_chunks()
        (data, mask) = pyarrow_array_to_numpy_and_mask(array, dtype = self.numpy_dtype)
        if data.dtype.kind == 'f' and is_nan_na():
            mask[np.isnan(data)] = False
        return array_class(data.copy(), ~mask, copy = False)

    _get_dtype_mapping = (lambda cls = None: raise AbstractMethodError(cls))()
    _standardize_dtype = (lambda cls = None, dtype = None: if isinstance(dtype, str) and dtype.startswith(('Int', 'UInt', 'Float')):
dtype = dtype.lower()if not isinstance(dtype, NumericDtype):
mapping = cls._get_dtype_mapping()try:
dtype = mapping[np.dtype(dtype)]except KeyError:
err = Noneraise ValueError(f'''invalid dtype specified {dtype}'''), errerr = Nonedel errdtype)()
    _safe_cast = (lambda cls = None, values = None, dtype = classmethod, copy = ('values', 'np.ndarray', 'dtype', 'np.dtype', 'copy', 'bool', 'return', 'np.ndarray'): raise AbstractMethodError(cls))()


def _coerce_to_data_and_mask(values = None, dtype = None, copy = None, dtype_cls = ('copy', 'bool', 'dtype_cls', 'type[NumericDtype]')):
    checker = dtype_cls._checker
    default_dtype = dtype_cls._default_np_dtype
    mask = None
    inferred_type = None
# WARNING: Decompyle incomplete


class NumericArray(BaseMaskedArray):
    pass
# WARNING: Decompyle incomplete
