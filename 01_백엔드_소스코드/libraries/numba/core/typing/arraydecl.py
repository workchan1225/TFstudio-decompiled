# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arraydecl.pyc (Python 3.11)

import numpy as np
import operator
from collections import namedtuple
from numba.core import types, utils
from numba.core.typing.templates import AttributeTemplate, AbstractTemplate, infer, infer_global, infer_getattr, signature, bound_function
from numba.core.typing import collections
from numba.core.errors import TypingError, RequireLiteralValue, NumbaTypeError, NumbaNotImplementedError, NumbaAssertionError, NumbaKeyError, NumbaIndexError, NumbaValueError
from numba.core.cgutils import is_nonelike
numpy_version = tuple(map(int, np.__version__.split('.')[:2]))
Indexing = namedtuple('Indexing', ('index', 'result', 'advanced'))

def get_array_index_type(ary, idx):
    '''
    Returns None or a tuple-3 for the types of the input array, index, and
    resulting type of ``array[index]``.

    Note: This is shared logic for ndarray getitem and setitem.
    '''
    pass
# WARNING: Decompyle incomplete

GetItemBuffer = <NODE:12>()
SetItemBuffer = <NODE:12>()

def normalize_shape(shape):
    if isinstance(shape, types.UniTuple):
        if isinstance(shape.dtype, types.Integer):
            dimtype = types.intp if shape.dtype.signed else types.uintp
            return types.UniTuple(dimtype, len(shape))
        return None
    if None(shape, types.Tuple) or shape.count == 0:
        return types.UniTuple(types.intp, 0)
    return None

ArrayAttribute = <NODE:12>()
DTypeAttr = <NODE:12>()
StaticGetItemArray = <NODE:12>()
RecordAttribute = <NODE:12>()
StaticGetItemRecord = <NODE:12>()
StaticGetItemLiteralRecord = <NODE:12>()
StaticSetItemRecord = <NODE:12>()
StaticSetItemLiteralRecord = <NODE:12>()
ArrayCTypesAttribute = <NODE:12>()
ArrayFlagsAttribute = <NODE:12>()
NestedArrayAttribute = <NODE:12>()

def _expand_integer(ty):
    '''
    If *ty* is an integer, expand it to a machine int (like Numpy).
    '''
    if isinstance(ty, types.Integer):
        if ty.signed:
            return max(types.intp, ty)
        return None(types.uintp, ty)
    if None(ty, types.Boolean):
        return types.intp


def generic_homog(self, args, kws):
    if args:
        raise NumbaAssertionError('args not supported')
    if kws:
        raise NumbaAssertionError('kws not supported')
    return signature(self.this.dtype, recvr = self.this)


def generic_expand(self, args, kws):
    pass
# WARNING: Decompyle incomplete


def sum_expand(self, args, kws):
    '''
    sum can be called with or without an axis parameter, and with or without
    a dtype parameter
    '''
    pysig = None
    if 'axis' in kws and 'dtype' not in kws:
        
        def sum_stub(axis):
            pass

        pysig = utils.pysignature(sum_stub)
        args = list(args) + [
            kws['axis']]
    elif 'dtype' in kws and 'axis' not in kws:
        
        def sum_stub(dtype):
            pass

        pysig = utils.pysignature(sum_stub)
        args = list(args) + [
            kws['dtype']]
    elif 'dtype' in kws and 'axis' in kws:
        
        def sum_stub(axis, dtype):
            pass

        pysig = utils.pysignature(sum_stub)
        args = list(args) + [
            kws['axis'],
            kws['dtype']]
    args_len = len(args)
# WARNING: Decompyle incomplete


def generic_expand_cumulative(self, args, kws):
    if args:
        raise NumbaAssertionError('args unsupported')
    if kws:
        raise NumbaAssertionError('kwargs unsupported')
# WARNING: Decompyle incomplete


def generic_hetero_real(self, args, kws):
    pass
# WARNING: Decompyle incomplete


def generic_hetero_always_real(self, args, kws):
    pass
# WARNING: Decompyle incomplete


def generic_index(self, args, kws):
    pass
# WARNING: Decompyle incomplete


def install_array_method(name, generic, prefer_literal = (True,)):
    pass
# WARNING: Decompyle incomplete

install_array_method('sum', sum_expand, prefer_literal = True)
CmpOpEqArray = <NODE:12>()
