# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dtypes.pyc (Python 3.11)

'''
Define extension dtypes.
'''
from __future__ import annotations
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import re
from typing import TYPE_CHECKING, Any, Self, cast
import warnings
import zoneinfo
import numpy as np
from pandas._config.config import get_option
from pandas._libs import lib, missing as libmissing
from pandas._libs.interval import Interval
from pandas._libs.properties import cache_readonly
from pandas._libs.tslibs import BaseOffset, NaT, NaTType, Period, Timedelta, Timestamp, timezones, to_offset, tz_compare
from pandas._libs.tslibs.dtypes import PeriodDtypeBase, abbrev_to_npy_unit
from pandas._libs.tslibs.offsets import BDay
from pandas.compat import HAS_PYARROW, PYARROW_MIN_VERSION
from pandas.errors import PerformanceWarning
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.base import ExtensionDtype, StorageExtensionDtype, register_extension_dtype
from pandas.core.dtypes.generic import ABCCategoricalIndex, ABCIndex, ABCRangeIndex
from pandas.core.dtypes.inference import is_bool, is_list_like
if HAS_PYARROW:
    import pyarrow as pa
if TYPE_CHECKING:
    from collections.abc import MutableMapping
    from datetime import tzinfo
    import pyarrow as pa
    from pandas._typing import Dtype, DtypeObj, IntervalClosedType, Ordered, Scalar, TimeUnit, npt, type_t
    from pandas import Categorical, CategoricalIndex, DatetimeIndex, Index, IntervalIndex, PeriodIndex
    from pandas.core.arrays import BaseMaskedArray, DatetimeArray, IntervalArray, NumpyExtensionArray, PeriodArray, SparseArray
    from pandas.core.arrays.arrow import ArrowExtensionArray
str_type = str

class PandasExtensionDtype(ExtensionDtype):
    kind: 'Any' = '\n    An np.dtype duck-typed class, suitable for holding a custom dtype.\n\n    THIS IS NOT A REAL NUMPY DTYPE\n    '
    str: 'str_type' = None
    num = 100
    shape: 'tuple[int, ...]' = ()
    itemsize = 8
    base: 'DtypeObj | None' = None
    isbuiltin = 0
    isnative = 0
    _cache_dtypes: 'dict[str_type, PandasExtensionDtype]' = { }
    
    def __repr__(self = None):
        '''
        Return a string representation for a particular object.
        '''
        return str(self)

    
    def __hash__(self = None):
        raise NotImplementedError('sub-classes should implement an __hash__ method')

    
    def __getstate__(self = None):
        pass
    # WARNING: Decompyle incomplete

    reset_cache = (lambda cls = None: cls._cache_dtypes = { })()


class CategoricalDtypeType(type):
    '''
    the type of CategoricalDtype, this metaclass determines subclass ability
    '''
    pass

CategoricalDtype = <NODE:12>()()
DatetimeTZDtype = <NODE:12>()()
PeriodDtype = <NODE:12>()()
IntervalDtype = <NODE:12>()()

class NumpyEADtype(ExtensionDtype):
    '''
    A Pandas ExtensionDtype for NumPy dtypes.

    This is mostly for internal compatibility, and is not especially
    useful on its own.

    Parameters
    ----------
    dtype : object
        Object to be converted to a NumPy data type object.

    See Also
    --------
    numpy.dtype
    '''
    _metadata = ('_dtype',)
    _supports_2d = False
    _can_fast_transpose = False
    
    def __init__(self = None, dtype = None):
        if isinstance(dtype, NumpyEADtype):
            dtype = dtype.numpy_dtype
        self._dtype = np.dtype(dtype)

    
    def __repr__(self = None):
        return f'''NumpyEADtype({self.name!r})'''

    numpy_dtype = (lambda self = None: self._dtype)()
    name = (lambda self = None: self._dtype.name)()
    type = (lambda self = None: self._dtype.type)()
    _is_numeric = (lambda self = None: self.kind in set('biufc'))()
    _is_boolean = (lambda self = None: self.kind == 'b')()
    construct_from_string = (lambda cls = None, string = None: try:
dtype = np.dtype(string)except TypeError:
err = Noneif not isinstance(string, str):
msg = f'''\'construct_from_string\' expects a string, got {type(string)}'''else:
msg = f'''Cannot construct a \'NumpyEADtype\' from \'{string}\''''raise TypeError(msg), errerr = Nonedel errcls(dtype))()
    
    def construct_array_type(self = None):
        '''
        Return the array type associated with this dtype.

        Returns
        -------
        type
        '''
        NumpyExtensionArray = NumpyExtensionArray
        import pandas.core.arrays
        return NumpyExtensionArray

    kind = (lambda self = None: self._dtype.kind)()
    itemsize = (lambda self = None: self._dtype.itemsize)()


class BaseMaskedDtype(ExtensionDtype):
    '''
    Base class for dtypes for BaseMaskedArray subclasses.
    '''
    _internal_fill_value: 'Scalar' = None
    _truthy_value = (lambda self: if self.kind == 'f':
1if None.kind in 'iu':
1)()
    _falsey_value = (lambda self: if self.kind == 'f':
0if None.kind in 'iu':
0)()
    na_value = (lambda self = property: libmissing.NA)()
    numpy_dtype = (lambda self = None: np.dtype(self.type))()
    kind = (lambda self = None: self.numpy_dtype.kind)()
    itemsize = (lambda self = None: self.numpy_dtype.itemsize)()
    
    def construct_array_type(self = None):
        '''
        Return the array type associated with this dtype.

        Returns
        -------
        type
        '''
        raise NotImplementedError

    from_numpy_dtype = (lambda cls = None, dtype = None: if dtype.kind == 'b':
BooleanDtype = BooleanDtypeimport pandas.core.arrays.booleanBooleanDtype()if None.kind in 'iu':
NUMPY_INT_TO_DTYPE = NUMPY_INT_TO_DTYPEimport pandas.core.arrays.integerNUMPY_INT_TO_DTYPE[dtype]if None.kind == 'f':
NUMPY_FLOAT_TO_DTYPE = NUMPY_FLOAT_TO_DTYPEimport pandas.core.arrays.floatingNUMPY_FLOAT_TO_DTYPE[dtype]raise None(dtype))()
    
    def _get_common_dtype(self = None, dtypes = None):
        find_common_type = find_common_type
        import pandas.core.dtypes.cast
        new_dtype = (lambda .0: for dtype in .0:
passcontinuedtype.numpy_dtype[dtype])(dtypes())
        if not isinstance(new_dtype, np.dtype):
            return None
        
        try:
            return type(self).from_numpy_dtype(new_dtype)
        except (KeyError, NotImplementedError):
            return None



SparseDtype = <NODE:12>()()
ArrowDtype = <NODE:12>()()
