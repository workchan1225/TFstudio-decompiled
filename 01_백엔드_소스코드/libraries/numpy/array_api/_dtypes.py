# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dtypes.pyc (Python 3.11)

import numpy as np
int8 = np.dtype('int8')
int16 = np.dtype('int16')
int32 = np.dtype('int32')
int64 = np.dtype('int64')
uint8 = np.dtype('uint8')
uint16 = np.dtype('uint16')
uint32 = np.dtype('uint32')
uint64 = np.dtype('uint64')
float32 = np.dtype('float32')
float64 = np.dtype('float64')
complex64 = np.dtype('complex64')
complex128 = np.dtype('complex128')
bool = np.dtype('bool')
_all_dtypes = (int8, int16, int32, int64, uint8, uint16, uint32, uint64, float32, float64, complex64, complex128, bool)
_boolean_dtypes = (bool,)
_real_floating_dtypes = (float32, float64)
_floating_dtypes = (float32, float64, complex64, complex128)
_complex_floating_dtypes = (complex64, complex128)
_integer_dtypes = (int8, int16, int32, int64, uint8, uint16, uint32, uint64)
_signed_integer_dtypes = (int8, int16, int32, int64)
_unsigned_integer_dtypes = (uint8, uint16, uint32, uint64)
_integer_or_boolean_dtypes = (bool, int8, int16, int32, int64, uint8, uint16, uint32, uint64)
_real_numeric_dtypes = (float32, float64, int8, int16, int32, int64, uint8, uint16, uint32, uint64)
_numeric_dtypes = (float32, float64, complex64, complex128, int8, int16, int32, int64, uint8, uint16, uint32, uint64)
_dtype_categories = {
    'all': _all_dtypes,
    'real numeric': _real_numeric_dtypes,
    'numeric': _numeric_dtypes,
    'integer': _integer_dtypes,
    'integer or boolean': _integer_or_boolean_dtypes,
    'boolean': _boolean_dtypes,
    'real floating-point': _floating_dtypes,
    'complex floating-point': _complex_floating_dtypes,
    'floating-point': _floating_dtypes }
# WARNING: Decompyle incomplete
