# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dufunc.pyc (Python 3.11)

import functools
import operator
import warnings
import numpy as np
from numba import jit, typeof
from numba.core import cgutils, types, serialize, sigutils, errors
from numba.core.extending import is_jitted, overload_attribute, overload_method, register_jitable, intrinsic
from numba.core.typing import npydecl
from numba.core.typing.templates import AbstractTemplate, signature
from numba.cpython.unsafe.tuple import tuple_setitem
from numba.np.ufunc import _internal
from numba.np.ufunc.ufunc_base import UfuncBase, UfuncLowererBase
from numba.parfors import array_analysis
from numba.np.ufunc import ufuncbuilder
from numba.np import numpy_support
from typing import Callable
from llvmlite import ir
from numba.core.compiler_lock import global_compiler_lock

class UfuncAtIterator:
    
    def __init__(self, ufunc, a, a_ty, indices, indices_ty, b, b_ty = (None, None)):
        self.ufunc = ufunc
        self.a = a
        self.a_ty = a_ty
        self.indices = indices
        self.indices_ty = indices_ty
        self.b = b
        self.b_ty = b_ty

    
    def run(self, context, builder):
        self._prepare(context, builder)
        (loop_indices, _) = self.indexer.begin_loops()
        self._call_ufunc(context, builder, loop_indices)
        self.indexer.end_loops()

    
    def need_advanced_indexing(self):
        return isinstance(self.indices_ty, types.BaseTuple)

    
    def _prepare(self, context, builder):
        normalize_indices = normalize_indices
        FancyIndexer = FancyIndexer
        import numba.np.arrayobj
        indices = self.indices
        a = self.a
        indices_ty = self.indices_ty
        a_ty = self.a_ty
        zero = context.get_value_type(types.intp)(0)
    # WARNING: Decompyle incomplete

    
    def _load_val(self, context, builder, loop_indices, array, array_ty):
        load_item = load_item
        import numba.np.arrayobj
        shapes = cgutils.unpack_tuple(builder, array.shape)
        strides = cgutils.unpack_tuple(builder, array.strides)
        data = array.data
        ptr = cgutils.get_item_pointer2(context, builder, data, shapes, strides, array_ty.layout, loop_indices)
        val = load_item(context, builder, array_ty, ptr)
        return (ptr, val)

    
    def _load_flat(self, context, builder, indices, array, array_ty):
        idx = builder.load(indices)
        sig = array_ty.dtype(array_ty, types.intp)
        impl = context.get_function(operator.getitem, sig)
        val = impl(builder, (array, idx))
        one = context.get_value_type(types.intp)(1)
        idx = builder.add(idx, one)
        builder.store(idx, indices)
        return (None, val)

    
    def _store_val(self, context, builder, array, array_ty, ptr, val):
        store_item = store_item
        import numba.np.arrayobj
        fromty = self.cres.signature.return_type
        toty = array_ty.dtype
        val = context.cast(builder, val, fromty, toty)
        store_item(context, builder, array_ty, val, ptr)

    
    def _compile_ufunc(self, context, builder):
        ufunc = self.ufunc.key[0]
    # WARNING: Decompyle incomplete

    
    def _call_ufunc(self, context, builder, loop_indices):
        cres = self.cres
        a_ty = self.a_ty
        a = self.a
        (ptr, val) = self._load_val(context, builder, loop_indices, a, a_ty)
    # WARNING: Decompyle incomplete



def make_dufunc_kernel(_dufunc):
    pass
# WARNING: Decompyle incomplete


class DUFuncLowerer(UfuncLowererBase):
    pass
# WARNING: Decompyle incomplete


class DUFunc(UfuncBase, _internal._DUFunc, serialize.ReduceMixin):
    pass
# WARNING: Decompyle incomplete

array_analysis.MAP_TYPES.append(DUFunc)
