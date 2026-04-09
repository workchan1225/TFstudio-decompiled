# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: integer.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any, ClassVar
import numpy as np
from pandas.util._decorators import set_module
from pandas.core.dtypes.base import register_extension_dtype
from pandas.core.dtypes.common import is_integer_dtype
from pandas.core.arrays.numeric import NumericArray, NumericDtype
if TYPE_CHECKING:
    from collections.abc import Callable

class IntegerDtype(NumericDtype):
    '''
    An ExtensionDtype to hold a single size & kind of integer dtype.

    These specific implementations are subclasses of the non-public
    IntegerDtype. For example, we have Int8Dtype to represent signed int 8s.

    The attributes name & type are set when these subclasses are created.
    '''
    _internal_fill_value = 1
    _default_np_dtype = np.dtype(np.int64)
    _checker: 'Callable[[Any], bool]' = is_integer_dtype
    
    def construct_array_type(self = None):
        '''
        Return the array type associated with this dtype.

        Returns
        -------
        type
        '''
        return IntegerArray

    _get_dtype_mapping = (lambda cls = None: NUMPY_INT_TO_DTYPE)()
    _safe_cast = (lambda cls = None, values = None, dtype = classmethod, copy = ('values', 'np.ndarray', 'dtype', 'np.dtype', 'copy', 'bool', 'return', 'np.ndarray'): try:
values.astype(dtype, casting = 'safe', copy = copy)except TypeError:
err = Nonecasted = values.astype(dtype, copy = copy)if (casted == values).all():
del errNoneraise None(f'''cannot safely cast non-equivalent {values.dtype} to {np.dtype(dtype)}'''), errNone = Nonedel err)()

IntegerArray = <NODE:12>()
_dtype_docstring = '\nAn ExtensionDtype for {dtype} integer data.\n\nUses :attr:`pandas.NA` as its missing value, rather than :attr:`numpy.nan`.\n\nAttributes\n----------\nNone\n\nMethods\n-------\nNone\n\nSee Also\n--------\nInt8Dtype : 8-bit nullable integer type.\nInt16Dtype : 16-bit nullable integer type.\nInt32Dtype : 32-bit nullable integer type.\nInt64Dtype : 64-bit nullable integer type.\n\nExamples\n--------\nFor Int8Dtype:\n\n>>> ser = pd.Series([2, pd.NA], dtype=pd.Int8Dtype())\n>>> ser.dtype\nInt8Dtype()\n\nFor Int16Dtype:\n\n>>> ser = pd.Series([2, pd.NA], dtype=pd.Int16Dtype())\n>>> ser.dtype\nInt16Dtype()\n\nFor Int32Dtype:\n\n>>> ser = pd.Series([2, pd.NA], dtype=pd.Int32Dtype())\n>>> ser.dtype\nInt32Dtype()\n\nFor Int64Dtype:\n\n>>> ser = pd.Series([2, pd.NA], dtype=pd.Int64Dtype())\n>>> ser.dtype\nInt64Dtype()\n\nFor UInt8Dtype:\n\n>>> ser = pd.Series([2, pd.NA], dtype=pd.UInt8Dtype())\n>>> ser.dtype\nUInt8Dtype()\n\nFor UInt16Dtype:\n\n>>> ser = pd.Series([2, pd.NA], dtype=pd.UInt16Dtype())\n>>> ser.dtype\nUInt16Dtype()\n\nFor UInt32Dtype:\n\n>>> ser = pd.Series([2, pd.NA], dtype=pd.UInt32Dtype())\n>>> ser.dtype\nUInt32Dtype()\n\nFor UInt64Dtype:\n\n>>> ser = pd.Series([2, pd.NA], dtype=pd.UInt64Dtype())\n>>> ser.dtype\nUInt64Dtype()\n'
Int8Dtype = <NODE:12>()()
Int16Dtype = <NODE:12>()()
Int32Dtype = <NODE:12>()()
Int64Dtype = <NODE:12>()()
UInt8Dtype = <NODE:12>()()
UInt16Dtype = <NODE:12>()()
UInt32Dtype = <NODE:12>()()
UInt64Dtype = <NODE:12>()()
NUMPY_INT_TO_DTYPE: 'dict[np.dtype, IntegerDtype]' = {
    np.dtype(np.uint64): UInt64Dtype(),
    np.dtype(np.uint32): UInt32Dtype(),
    np.dtype(np.uint16): UInt16Dtype(),
    np.dtype(np.uint8): UInt8Dtype(),
    np.dtype(np.int64): Int64Dtype(),
    np.dtype(np.int32): Int32Dtype(),
    np.dtype(np.int16): Int16Dtype(),
    np.dtype(np.int8): Int8Dtype() }
