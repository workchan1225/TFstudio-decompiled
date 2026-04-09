# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arrayobj.pyc (Python 3.11)

'''
Implementation of operations on Array objects and objects supporting
the buffer protocol.
'''
import functools
import math
import operator
import textwrap
from llvmlite import ir
from llvmlite.ir import Constant
import numpy as np
from numba import pndindex, literal_unroll
from numba.core import types, typing, errors, cgutils, extending, config
from numba.np.numpy_support import as_dtype, from_dtype, carray, farray, is_contiguous, is_fortran, check_is_integer, type_is_scalar, lt_complex, lt_floats
from numba.np.numpy_support import type_can_asarray, is_nonelike, numpy_version
from numba.core.imputils import lower_builtin, lower_getattr, lower_getattr_generic, lower_setattr_generic, lower_cast, lower_constant, iternext_impl, impl_ret_borrowed, impl_ret_new_ref, impl_ret_untracked, RefType
from numba.core.typing import signature
from numba.core.types import StringLiteral
from numba.core.extending import register_jitable, overload, overload_method, intrinsic, overload_attribute
from numba.misc import quicksort, mergesort
from numba.cpython import slicing
from numba.cpython.charseq import _make_constant_bytes, bytes_type
from numba.cpython.unsafe.tuple import tuple_setitem, build_full_slice_tuple
from numba.core.extending import overload_classmethod
from numba.core.typing.npydecl import parse_dtype as ty_parse_dtype, parse_shape as ty_parse_shape, _parse_nested_sequence, _sequence_of_arrays, _choose_concatenation_layout

def set_range_metadata(builder, load, lower_bound, upper_bound):
    '''
    Set the "range" metadata on a load instruction.
    Note the interval is in the form [lower_bound, upper_bound).
    '''
    range_operands = [
        Constant(load.type, lower_bound),
        Constant(load.type, upper_bound)]
    md = builder.module.add_metadata(range_operands)
    load.set_metadata('range', md)


def mark_positive(builder, load):
    '''
    Mark the result of a load instruction as positive (or zero).
    '''
    upper_bound = (1 << load.type.width - 1) - 1
    set_range_metadata(builder, load, 0, upper_bound)


def make_array(array_type):
    '''
    Return the Structure representation of the given *array_type*
    (an instance of types.ArrayCompatible).

    Note this does not call __array_wrap__ in case a new array structure
    is being created (rather than populated).
    '''
    pass
# WARNING: Decompyle incomplete


def get_itemsize(context, array_type):
    '''
    Return the item size for the given array or buffer type.
    '''
    llty = context.get_data_type(array_type.dtype)
    return context.get_abi_sizeof(llty)


def load_item(context, builder, arrayty, ptr):
    '''
    Load the item at the given array pointer.
    '''
    align = None if arrayty.aligned else 1
    return context.unpack_value(builder, arrayty.dtype, ptr, align = align)


def store_item(context, builder, arrayty, val, ptr):
    '''
    Store the item at the given array pointer.
    '''
    align = None if arrayty.aligned else 1
    return context.pack_value(builder, arrayty.dtype, val, ptr, align = align)


def fix_integer_index(context, builder, idxty, idx, size):
    """
    Fix the integer index' type and value for the given dimension size.
    """
    if idxty.signed:
        ind = context.cast(builder, idx, idxty, types.intp)
        ind = slicing.fix_index(builder, ind, size)
    else:
        ind = context.cast(builder, idx, idxty, types.uintp)
    return ind


def normalize_index(context, builder, idxty, idx):
    '''
    Normalize the index type and value.  0-d arrays are converted to scalars.
    '''
    pass
# WARNING: Decompyle incomplete


def normalize_indices(context, builder, index_types, indices):
    '''
    Same as normalize_index(), but operating on sequences of
    index types and values.
    '''
    pass
# WARNING: Decompyle incomplete


def populate_array(array, data, shape, strides, itemsize, meminfo, parent = (None,)):
    '''
    Helper function for populating array structures.
    This avoids forgetting to set fields.

    *shape* and *strides* can be Python tuples or LLVM arrays.
    '''
    context = array._context
    builder = array._builder
    datamodel = array._datamodel
    standard_array = types.Array(types.float64, 1, 'C')
    standard_array_type_datamodel = context.data_model_manager[standard_array]
    required_fields = set(standard_array_type_datamodel._fields)
    datamodel_fields = set(datamodel._fields)
    if required_fields & datamodel_fields != required_fields:
        missing = required_fields - datamodel_fields
        msg = f'''The datamodel for type {array._fe_type} is missing field{'s' if len(missing) > 1 else ''} {missing}.'''
        raise ValueError(msg)
# WARNING: Decompyle incomplete


def update_array_info(aryty, array):
    '''
    Update some auxiliary information in *array* after some of its fields
    were changed.  `itemsize` and `nitems` are updated.
    '''
    context = array._context
    builder = array._builder
    nitems = context.get_constant(types.intp, 1)
    unpacked_shape = cgutils.unpack_tuple(builder, array.shape, aryty.ndim)
    for axlen in unpacked_shape:
        nitems = builder.mul(nitems, axlen, flags = [
            'nsw'])
        array.nitems = nitems
        array.itemsize = context.get_constant(types.intp, get_itemsize(context, aryty))
        return None


def normalize_axis(func_name, arg_name, ndim, axis):
    '''Constrain axis values to valid positive values.'''
    raise NotImplementedError()

normalize_axis_overloads = (lambda func_name, arg_name, ndim, axis: pass# WARNING: Decompyle incomplete
)()
getiter_array = (lambda context, builder, sig, args: (arrayty,) = sig.args(array,) = argsiterobj = context.make_helper(builder, sig.return_type)zero = context.get_constant(types.intp, 0)indexptr = cgutils.alloca_once_value(builder, zero)iterobj.index = indexptriterobj.array = arrayif context.enable_nrt:
context.nrt.incref(builder, arrayty, array)res = iterobj._getvalue()out = impl_ret_new_ref(context, builder, sig.return_type, res)out)()

def _getitem_array_single_int(context, builder, return_type, aryty, ary, idx):
    ''' Evaluate `ary[idx]`, where idx is a single int. '''
    shapes = cgutils.unpack_tuple(builder, ary.shape, count = aryty.ndim)
    strides = cgutils.unpack_tuple(builder, ary.strides, count = aryty.ndim)
    offset = builder.mul(strides[0], idx)
    dataptr = cgutils.pointer_add(builder, ary.data, offset)
    view_shapes = shapes[1:]
    view_strides = strides[1:]
    if isinstance(return_type, types.Buffer):
        retary = make_view(context, builder, aryty, ary, return_type, dataptr, view_shapes, view_strides)
        return retary._getvalue()
# WARNING: Decompyle incomplete

iternext_array = (lambda context, builder, sig, args, result: (iterty,) = sig.args(iter,) = argsarrayty = iterty.array_typeiterobj = context.make_helper(builder, iterty, value = iter)ary = make_array(arrayty)(context, builder, value = iterobj.array)(nitems,) = cgutils.unpack_tuple(builder, ary.shape, count = 1)index = builder.load(iterobj.index)is_valid = builder.icmp_signed('<', index, nitems)result.set_valid(is_valid)builder.if_then(is_valid)value = _getitem_array_single_int(context, builder, iterty.yield_type, arrayty, ary, index)result.yield_(value)nindex = cgutils.increment_index(builder, index)builder.store(nindex, iterobj.index)None(None, None)Nonewith None:
if not None:
pass)()()

def basic_indexing(context, builder, aryty, ary, index_types, indices, boundscheck = (None,)):
    '''
    Perform basic indexing on the given array.
    A (data pointer, shapes, strides) tuple is returned describing
    the corresponding view.
    '''
    zero = context.get_constant(types.intp, 0)
    one = context.get_constant(types.intp, 1)
    shapes = cgutils.unpack_tuple(builder, ary.shape, aryty.ndim)
    strides = cgutils.unpack_tuple(builder, ary.strides, aryty.ndim)
    output_indices = []
    output_shapes = []
    output_strides = []
    num_newaxes = (lambda .0: pass# WARNING: Decompyle incomplete
)(index_types())
    ax = 0
# WARNING: Decompyle incomplete


def make_view(context, builder, aryty, ary, return_type, data, shapes, strides):
    '''
    Build a view over the given array with the given parameters.
    '''
    retary = make_array(return_type)(context, builder)
    populate_array(retary, data = data, shape = shapes, strides = strides, itemsize = ary.itemsize, meminfo = ary.meminfo, parent = ary.parent)
    return retary


def _getitem_array_generic(context, builder, return_type, aryty, ary, index_types, indices):
    '''
    Return the result of indexing *ary* with the given *indices*,
    returning either a scalar or a view.
    '''
    (dataptr, view_shapes, view_strides) = basic_indexing(context, builder, aryty, ary, index_types, indices, boundscheck = context.enable_boundscheck)
    if isinstance(return_type, types.Buffer):
        retary = make_view(context, builder, aryty, ary, return_type, dataptr, view_shapes, view_strides)
        return retary._getvalue()
# WARNING: Decompyle incomplete

getitem_arraynd_intp = (lambda context, builder, sig, args: (aryty, idxty) = sig.args(ary, idx) = args# WARNING: Decompyle incomplete
)()()
getitem_array_tuple = (lambda context, builder, sig, args: (aryty, tupty) = sig.args(ary, tup) = argsary = make_array(aryty)(context, builder, ary)index_types = tupty.typesindices = cgutils.unpack_tuple(builder, tup, count = len(tupty))(index_types, indices) = normalize_indices(context, builder, index_types, indices)if (lambda .0: pass# WARNING: Decompyle incomplete
)(index_types()):
        return fancy_getitem(context, builder, sig, args, aryty, ary, index_types, indices)
    res = any(context, builder, sig.return_type, aryty, ary, index_types, indices)
    return impl_ret_borrowed(context, builder, sig.return_type, res)
)()
setitem_array = (lambda context, builder, sig, args: (aryty, idxty, valty) = sig.args(ary, idx, val) = argsif isinstance(idxty, types.BaseTuple):
index_types = idxty.typesindices = cgutils.unpack_tuple(builder, idx, count = len(idxty))else:
index_types = (idxty,)indices = (idx,)ary = make_array(aryty)(context, builder, ary)(index_types, indices) = normalize_indices(context, builder, index_types, indices)try:
(dataptr, shapes, strides) = basic_indexing(context, builder, aryty, ary, index_types, indices, boundscheck = context.enable_boundscheck)use_fancy_indexing = bool(shapes)except NotImplementedError:
use_fancy_indexing = Trueif use_fancy_indexing:
fancy_setslice(context, builder, sig, args, index_types, indices)val = None.cast(builder, val, valty, aryty.dtype)store_item(context, builder, aryty, val, dataptr))()
array_len = (lambda context, builder, sig, args: (aryty,) = sig.args(ary,) = argsarystty = make_array(aryty)ary = arystty(context, builder, ary)shapeary = ary.shaperes = builder.extract_value(shapeary, 0)impl_ret_untracked(context, builder, sig.return_type, res))()
array_item = (lambda context, builder, sig, args: (aryty,) = sig.args(ary,) = argsary = make_array(aryty)(context, builder, ary)nitems = ary.nitemsbuilder.if_then(builder.icmp_signed('!=', nitems, nitems.type(1)), likely = False)msg = 'item(): can only convert an array of size 1 to a Python scalar'context.call_conv.return_user_exc(builder, ValueError, (msg,))None(None, None))()
if numpy_version < (2, 0):
    array_itemset = (lambda context, builder, sig, args: (aryty, valty) = sig.args(ary, val) = args# WARNING: Decompyle incomplete
)()

class Indexer(object):
    '''
    Generic indexer interface, for generating indices over a fancy indexed
    array on a single dimension.
    '''
    
    def prepare(self):
        '''
        Prepare the indexer by initializing any required variables, basic
        blocks...
        '''
        raise NotImplementedError

    
    def get_size(self):
        """
        Return this dimension's size as an integer.
        """
        raise NotImplementedError

    
    def get_shape(self):
        """
        Return this dimension's shape as a tuple.
        """
        raise NotImplementedError

    
    def get_index_bounds(self):
        '''
        Return a half-open [lower, upper) range of indices this dimension
        is guaranteed not to step out of.
        '''
        raise NotImplementedError

    
    def loop_head(self):
        '''
        Start indexation loop.  Return a (index, count) tuple.
        *index* is an integer LLVM value representing the index over this
        dimension.
        *count* is either an integer LLVM value representing the current
        iteration count, or None if this dimension should be omitted from
        the indexation result.
        '''
        raise NotImplementedError

    
    def loop_tail(self):
        '''
        Finish indexation loop.
        '''
        raise NotImplementedError



class EntireIndexer(Indexer):
    '''
    Compute indices along an entire array dimension.
    '''
    
    def __init__(self, context, builder, aryty, ary, dim):
        self.context = context
        self.builder = builder
        self.aryty = aryty
        self.ary = ary
        self.dim = dim
        self.ll_intp = self.context.get_value_type(types.intp)

    
    def prepare(self):
        builder = self.builder
        self.size = builder.extract_value(self.ary.shape, self.dim)
        self.index = cgutils.alloca_once(builder, self.ll_intp)
        self.bb_start = builder.append_basic_block()
        self.bb_end = builder.append_basic_block()

    
    def get_size(self):
        return self.size

    
    def get_shape(self):
        return (self.size,)

    
    def get_index_bounds(self):
        return (self.ll_intp(0), self.size)

    
    def loop_head(self):
        builder = self.builder
        self.builder.store(Constant(self.ll_intp, 0), self.index)
        builder.branch(self.bb_start)
        builder.position_at_end(self.bb_start)
        cur_index = builder.load(self.index)
        builder.if_then(builder.icmp_signed('>=', cur_index, self.size), likely = False)
        builder.branch(self.bb_end)
        None(None, None)

    
    def loop_tail(self):
        builder = self.builder
        next_index = cgutils.increment_index(builder, builder.load(self.index))
        builder.store(next_index, self.index)
        builder.branch(self.bb_start)
        builder.position_at_end(self.bb_end)



class IntegerIndexer(Indexer):
    '''
    Compute indices from a single integer.
    '''
    
    def __init__(self, context, builder, idx):
        self.context = context
        self.builder = builder
        self.idx = idx
        self.ll_intp = self.context.get_value_type(types.intp)

    
    def prepare(self):
        pass

    
    def get_size(self):
        return Constant(self.ll_intp, 1)

    
    def get_shape(self):
        return ()

    
    def get_index_bounds(self):
        return (self.idx, self.builder.add(self.idx, self.get_size()))

    
    def loop_head(self):
        return (self.idx, None)

    
    def loop_tail(self):
        pass



class IntegerArrayIndexer(Indexer):
    '''
    Compute indices from an array of integer indices.
    '''
    
    def __init__(self, context, builder, idxty, idxary, size):
        self.context = context
        self.builder = builder
        self.idxty = idxty
        self.idxary = idxary
        self.size = size
    # WARNING: Decompyle incomplete

    
    def prepare(self):
        builder = self.builder
        self.idx_size = cgutils.unpack_tuple(builder, self.idxary.shape)[0]
        self.idx_index = cgutils.alloca_once(builder, self.ll_intp)
        self.bb_start = builder.append_basic_block()
        self.bb_end = builder.append_basic_block()

    
    def get_size(self):
        return self.idx_size

    
    def get_shape(self):
        return (self.idx_size,)

    
    def get_index_bounds(self):
        return (self.ll_intp(0), self.size)

    
    def loop_head(self):
        builder = self.builder
        self.builder.store(Constant(self.ll_intp, 0), self.idx_index)
        builder.branch(self.bb_start)
        builder.position_at_end(self.bb_start)
        cur_index = builder.load(self.idx_index)
        builder.if_then(builder.icmp_signed('>=', cur_index, self.idx_size), likely = False)
        builder.branch(self.bb_end)
        None(None, None)

    
    def loop_tail(self):
        builder = self.builder
        next_index = cgutils.increment_index(builder, builder.load(self.idx_index))
        builder.store(next_index, self.idx_index)
        builder.branch(self.bb_start)
        builder.position_at_end(self.bb_end)



class BooleanArrayIndexer(Indexer):
    '''
    Compute indices from an array of boolean predicates.
    '''
    
    def __init__(self, context, builder, idxty, idxary):
        self.context = context
        self.builder = builder
        self.idxty = idxty
        self.idxary = idxary
    # WARNING: Decompyle incomplete

    
    def prepare(self):
        builder = self.builder
        self.size = cgutils.unpack_tuple(builder, self.idxary.shape)[0]
        self.idx_index = cgutils.alloca_once(builder, self.ll_intp)
        self.count = cgutils.alloca_once(builder, self.ll_intp)
        self.bb_start = builder.append_basic_block()
        self.bb_tail = builder.append_basic_block()
        self.bb_end = builder.append_basic_block()

    
    def get_size(self):
        builder = self.builder
        count = cgutils.alloca_once_value(builder, self.zero)
        loop = cgutils.for_range(builder, self.size)
        c = builder.load(count)
        pred = _getitem_array_single_int(self.context, builder, self.idxty.dtype, self.idxty, self.idxary, loop.index)
        c = builder.add(c, builder.zext(pred, c.type))
        builder.store(c, count)
        None(None, None)

    
    def get_shape(self):
        return (self.get_size(),)

    
    def get_index_bounds(self):
        return (self.ll_intp(0), self.size)

    
    def loop_head(self):
