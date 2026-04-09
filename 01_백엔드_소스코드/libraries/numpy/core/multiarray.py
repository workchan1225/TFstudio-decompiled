# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multiarray.pyc (Python 3.11)

'''
Create the numpy.core.multiarray namespace for backward compatibility. In v1.16
the multiarray and umath c-extension modules were merged into a single
_multiarray_umath extension module. So we replicate the old namespace
by importing from the extension module.

'''
import functools
from  import overrides
from  import _multiarray_umath
from _multiarray_umath import *
from _multiarray_umath import fastCopyAndTranspose, _flagdict, from_dlpack, _place, _reconstruct, _vec_string, _ARRAY_API, _monotonicity, _get_ndarray_c_version, _get_madvise_hugepage, _set_madvise_hugepage, _get_promotion_state, _set_promotion_state, _using_numpy2_behavior
__all__ = [
    '_ARRAY_API',
    'ALLOW_THREADS',
    'BUFSIZE',
    'CLIP',
    'DATETIMEUNITS',
    'ITEM_HASOBJECT',
    'ITEM_IS_POINTER',
    'LIST_PICKLE',
    'MAXDIMS',
    'MAY_SHARE_BOUNDS',
    'MAY_SHARE_EXACT',
    'NEEDS_INIT',
    'NEEDS_PYAPI',
    'RAISE',
    'USE_GETITEM',
    'USE_SETITEM',
    'WRAP',
    '_flagdict',
    'from_dlpack',
    '_place',
    '_reconstruct',
    '_vec_string',
    '_monotonicity',
    'add_docstring',
    'arange',
    'array',
    'asarray',
    'asanyarray',
    'ascontiguousarray',
    'asfortranarray',
    'bincount',
    'broadcast',
    'busday_count',
    'busday_offset',
    'busdaycalendar',
    'can_cast',
    'compare_chararrays',
    'concatenate',
    'copyto',
    'correlate',
    'correlate2',
    'count_nonzero',
    'c_einsum',
    'datetime_as_string',
    'datetime_data',
    'dot',
    'dragon4_positional',
    'dragon4_scientific',
    'dtype',
    'empty',
    'empty_like',
    'error',
    'flagsobj',
    'flatiter',
    'format_longfloat',
    'frombuffer',
    'fromfile',
    'fromiter',
    'fromstring',
    'get_handler_name',
    'get_handler_version',
    'inner',
    'interp',
    'interp_complex',
    'is_busday',
    'lexsort',
    'matmul',
    'may_share_memory',
    'min_scalar_type',
    'ndarray',
    'nditer',
    'nested_iters',
    'normalize_axis_index',
    'packbits',
    'promote_types',
    'putmask',
    'ravel_multi_index',
    'result_type',
    'scalar',
    'set_datetimeparse_function',
    'set_legacy_print_mode',
    'set_numeric_ops',
    'set_string_function',
    'set_typeDict',
    'shares_memory',
    'tracemalloc_domain',
    'typeinfo',
    'unpackbits',
    'unravel_index',
    'vdot',
    'where',
    'zeros',
    '_get_promotion_state',
    '_set_promotion_state',
    '_using_numpy2_behavior']
_reconstruct.__module__ = 'numpy.core.multiarray'
scalar.__module__ = 'numpy.core.multiarray'
from_dlpack.__module__ = 'numpy'
arange.__module__ = 'numpy'
array.__module__ = 'numpy'
asarray.__module__ = 'numpy'
asanyarray.__module__ = 'numpy'
ascontiguousarray.__module__ = 'numpy'
asfortranarray.__module__ = 'numpy'
datetime_data.__module__ = 'numpy'
empty.__module__ = 'numpy'
frombuffer.__module__ = 'numpy'
fromfile.__module__ = 'numpy'
fromiter.__module__ = 'numpy'
frompyfunc.__module__ = 'numpy'
fromstring.__module__ = 'numpy'
geterrobj.__module__ = 'numpy'
may_share_memory.__module__ = 'numpy'
nested_iters.__module__ = 'numpy'
promote_types.__module__ = 'numpy'
set_numeric_ops.__module__ = 'numpy'
seterrobj.__module__ = 'numpy'
zeros.__module__ = 'numpy'
_get_promotion_state.__module__ = 'numpy'
_set_promotion_state.__module__ = 'numpy'
_using_numpy2_behavior.__module__ = 'numpy'
array_function_from_c_func_and_dispatcher = functools.partial(overrides.array_function_from_dispatcher, module = 'numpy', docs_from_dispatcher = True, verify = False)
empty_like = (lambda prototype, dtype, order, subok, shape = (None, None, None, None): (prototype,))()
concatenate = (lambda arrays = array_function_from_c_func_and_dispatcher(_multiarray_umath.concatenate), axis = (None, None), out = {
    'dtype': None,
    'casting': None }, *, dtype, casting,
