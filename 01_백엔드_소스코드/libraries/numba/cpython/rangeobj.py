# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rangeobj.pyc (Python 3.11)

__doc__ = '\nImplementation of the range object for fixed-size integers.\n'
import operator
from numba import prange
from numba.core import types, cgutils, errors, config
from numba.core.imputils import lower_builtin, lower_cast, iterator_impl, impl_ret_untracked
from numba.core.typing import signature
from numba.core.extending import intrinsic, overload, overload_attribute, register_jitable
from numba.parfors.parfor import internal_prange

def make_range_iterator(typ):
    '''
    Return the Structure representation of the given *typ* (an
    instance of types.RangeIteratorType).
    '''
    return cgutils.create_struct_proxy(typ)


def make_range_impl(int_type, range_state_type, range_iter_type):
    pass
# WARNING: Decompyle incomplete

if config.USE_LEGACY_TYPE_SYSTEM:
    range_impl_map = {
        types.uint64: (types.unsigned_range_state64_type, types.unsigned_range_iter64_type),
        types.int64: (types.range_state64_type, types.range_iter64_type),
        types.int32: (types.range_state32_type, types.range_iter32_type) }
else:
    range_impl_map = {
        types.py_int: (types.range_state_type, types.range_iter_type) }
# WARNING: Decompyle incomplete
