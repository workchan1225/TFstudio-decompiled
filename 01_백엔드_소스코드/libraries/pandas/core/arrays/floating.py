# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: floating.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any, ClassVar
import numpy as np
from pandas.util._decorators import set_module
from pandas.core.dtypes.base import register_extension_dtype
from pandas.core.dtypes.common import is_float_dtype
from pandas.core.arrays.numeric import NumericArray, NumericDtype
if TYPE_CHECKING:
    from collections.abc import Callable

class FloatingDtype(NumericDtype):
    '''
    An ExtensionDtype to hold a single size of floating dtype.

    These specific implementations are subclasses of the non-public
    FloatingDtype. For example we have Float32Dtype to represent float32.

    The attributes name & type are set when these subclasses are created.
    '''
    _internal_fill_value = np.nan
    _default_np_dtype = np.dtype(np.float64)
    _checker: 'Callable[[Any], bool]' = is_float_dtype
    
    def construct_array_type(self = None):
        '''
        Return the array type associated with this dtype.

        Returns
        -------
        type
        '''
        return FloatingArray

    _get_dtype_mapping = (lambda cls = None: NUMPY_FLOAT_TO_DTYPE)()
    _safe_cast = (lambda cls = None, values = None, dtype = classmethod, copy = ('values', 'np.ndarray', 'dtype', 'np.dtype', 'copy', 'bool', 'return', 'np.ndarray'): values.astype(dtype, copy = copy))()

FloatingArray = <NODE:12>()
_dtype_docstring = '\nAn ExtensionDtype for {dtype} data.\n\nThis dtype uses ``pd.NA`` as missing value indicator.\n\nAttributes\n----------\nNone\n\nMethods\n-------\nNone\n\nSee Also\n--------\nCategoricalDtype : Type for categorical data with the categories and orderedness.\nIntegerDtype : An ExtensionDtype to hold a single size & kind of integer dtype.\nStringDtype : An ExtensionDtype for string data.\n\nExamples\n--------\nFor Float32Dtype:\n\n>>> ser = pd.Series([2.25, pd.NA], dtype=pd.Float32Dtype())\n>>> ser.dtype\nFloat32Dtype()\n\nFor Float64Dtype:\n\n>>> ser = pd.Series([2.25, pd.NA], dtype=pd.Float64Dtype())\n>>> ser.dtype\nFloat64Dtype()\n'
Float32Dtype = <NODE:12>()()
Float64Dtype = <NODE:12>()()
NUMPY_FLOAT_TO_DTYPE: 'dict[np.dtype, FloatingDtype]' = {
    np.dtype(np.float64): Float64Dtype(),
    np.dtype(np.float32): Float32Dtype() }
