# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: npyimpl.pyc (Python 3.11)

'''
Implementation of functions in the Numpy package.
'''
import math
import sys
import itertools
from collections import namedtuple
from llvmlite.ir import ir
import numpy as np
import operator
from numba.np import arrayobj, ufunc_db, numpy_support
from numba.np.ufunc.sigparse import parse_signature
from numba.core.imputils import Registry, impl_ret_new_ref, force_error_model, impl_ret_borrowed
from numba.core import typing, types, utils, cgutils, callconv, config
from numba.np.numpy_support import ufunc_find_matching_loop, select_array_wrapper, from_dtype, _ufunc_loop_sig
from numba.np.arrayobj import _getitem_array_generic
from numba.core.typing import npydecl
from numba.core.extending import overload, intrinsic
from numba.core import errors
registry = Registry('npyimpl')

class _ScalarIndexingHelper(object):
    
    def update_indices(self, loop_indices, name):
        pass

    
    def as_values(self):
        pass



class _ScalarHelper(object):
    '''Helper class to handle scalar arguments (and result).
    Note that store_data is only used when generating code for
    a scalar ufunc and to write the output value.

    For loading, the value is directly used without having any
    kind of indexing nor memory backing it up. This is the use
    for input arguments.

    For storing, a variable is created in the stack where the
    value will be written.

    Note that it is not supported (as it is unneeded for our
    current use-cases) reading back a stored value. This class
    will always "load" the original value it got at its creation.
    '''
    
    def __init__(self, ctxt, bld, val, ty):
        self.context = ctxt
        self.builder = bld
        self.val = val
        self.base_type = ty
        intpty = ctxt.get_value_type(types.intp)
        self.shape = [
            ir.Constant(intpty, 1)]
        lty = ctxt.get_data_type(ty) if ty != types.boolean else ir.IntType(1)
        self._ptr = cgutils.alloca_once(bld, lty)

    
    def create_iter_indices(self):
        return _ScalarIndexingHelper()

    
    def load_data(self, indices):
        return self.val

    
    def store_data(self, indices, val):
        self.builder.store(val, self._ptr)

    return_val = (lambda self: self.builder.load(self._ptr))()


def _ArrayIndexingHelper():
    '''_ArrayIndexingHelper'''
    
    def update_indices(self, loop_indices, name):
        bld = self.array.builder
        intpty = self.array.context.get_value_type(types.intp)
        ONE = ir.Constant(ir.IntType(intpty.width), 1)
        indices = loop_indices[len(loop_indices) - len(self.indices):]
        for src, dst, dim in zip(indices, self.indices, self.array.shape):
            cond = bld.icmp_unsigned('>', dim, ONE)
            bld.if_then(cond)
            bld.store(src, dst)
            None(None, None)
        with None:
            if not None:
                pass
        continue

    
    def as_values(self):
        '''
        The indexing helper is built using alloca for each value, so it
        actually contains pointers to the actual indices to load. Note
        that update_indices assumes the same. This method returns the
        indices as values
        '''
        pass
    # WARNING: Decompyle incomplete


_ArrayIndexingHelper = <NODE:27>(_ArrayIndexingHelper, '_ArrayIndexingHelper', namedtuple('_ArrayIndexingHelper', ('array', 'indices')))

def _ArrayHelper():
    '''_ArrayHelper'''
    __doc__ = 'Helper class to handle array arguments/result.\n    It provides methods to generate code loading/storing specific\n    items as well as support code for handling indices.\n    '
    
    def create_iter_indices(self):
        intpty = self.context.get_value_type(types.intp)
        ZERO = ir.Constant(ir.IntType(intpty.width), 0)
        indices = []
        for i in range(self.ndim):
            x = cgutils.alloca_once(self.builder, ir.IntType(intpty.width))
            self.builder.store(ZERO, x)
            indices.append(x)
            return _ArrayIndexingHelper(self, indices)

    
    def _load_effective_address(self, indices):
        return cgutils.get_item_pointer2(self.context, self.builder, data = self.data, shape = self.shape, strides = self.strides, layout = self.layout, inds = indices)

    
    def load_data(self, indices):
        model = self.context.data_model_manager[self.base_type]
        ptr = self._load_effective_address(indices)
        return model.load_from_data_pointer(self.builder, ptr)

    
    def store_data(self, indices, value):
        ctx = self.context
        bld = self.builder
        store_value = ctx.get_value_as_data(bld, self.base_type, value)
    # WARNING: Decompyle incomplete


_ArrayHelper = <NODE:27>(_ArrayHelper, '_ArrayHelper', namedtuple('_ArrayHelper', ('context', 'builder', 'shape', 'strides', 'data', 'layout', 'base_type', 'ndim', 'return_val')))

def _ArrayGUHelper():
    '''_ArrayGUHelper'''
    __doc__ = 'Helper class to handle array arguments/result.\n    It provides methods to generate code loading/storing specific\n    items as well as support code for handling indices.\n\n    Contrary to _ArrayHelper, this class can create a view to a subarray\n    '
    
    def create_iter_indices(self):
        intpty = self.context.get_value_type(types.intp)
        ZERO = ir.Constant(ir.IntType(intpty.width), 0)
        indices = []
        for i in range(self.ndim - self.inner_arr_ty.ndim):
            x = cgutils.alloca_once(self.builder, ir.IntType(intpty.width))
            self.builder.store(ZERO, x)
            indices.append(x)
            return _ArrayIndexingHelper(self, indices)

    
    def _load_effective_address(self, indices):
        context = self.context
        builder = self.builder
        arr_ty = types.Array(self.base_type, self.ndim, self.layout)
        arr = context.make_array(arr_ty)(context, builder, self.data)
        return cgutils.get_item_pointer2(context, builder, data = arr.data, shape = self.shape, strides = self.strides, layout = self.layout, inds = indices)

    
    def load_data(self, indices):
        builder = self.builder
        context = self.context
        if self.inner_arr_ty.ndim == 0 and self.is_input_arg:
            model = context.data_model_manager[self.base_type]
            ptr = self._load_effective_address(indices)
            return model.load_from_data_pointer(builder, ptr)
        if not None.inner_arr_ty.ndim == 0 and self.is_input_arg:
            intpty = context.get_value_type(types.intp)
            one = intpty(1)
            fromty = types.Array(self.base_type, self.ndim, self.layout)
            toty = types.Array(self.base_type, 1, self.layout)
            itemsize = intpty(arrayobj.get_itemsize(context, fromty))
            arr_from = self.context.make_array(fromty)(context, builder, self.data)
            arr_to = self.context.make_array(toty)(context, builder)
            arrayobj.populate_array(arr_to, data = self._load_effective_address(indices), shape = cgutils.pack_array(builder, [
                one]), strides = cgutils.pack_array(builder, [
                itemsize]), itemsize = arr_from.itemsize, meminfo = arr_from.meminfo, parent = arr_from.parent)
            return arr_to._getvalue()
        index_types = (None.int64,) * (self.ndim - self.inner_arr_ty.ndim)
        arrty = types.Array(self.base_type, self.ndim, self.layout)
        arr = self.context.make_array(arrty)(context, builder, self.data)
        res = _getitem_array_generic(context, builder, self.inner_arr_ty, arrty, arr, index_types, indices)
        return res

    
    def guard_shape(self, loopshape):
        pass
    # WARNING: Decompyle incomplete

    
    def guard_match_core_dims(self = None, other = None, ndims = None):
        pass
    # WARNING: Decompyle incomplete


_ArrayGUHelper = <NODE:27>(_ArrayGUHelper, '_ArrayGUHelper', namedtuple('_ArrayHelper', ('context', 'builder', 'shape', 'strides', 'data', 'layout', 'base_type', 'ndim', 'inner_arr_ty', 'is_input_arg')))

def _prepare_argument(ctxt, bld, inp, tyinp, where = ('input operand',)):
    '''returns an instance of the appropriate Helper (either
    _ScalarHelper or _ArrayHelper) class to handle the argument.
    using the polymorphic interface of the Helper classes, scalar
    and array cases can be handled with the same code'''
    if isinstance(tyinp, types.Optional):
        oty = tyinp
        tyinp = tyinp.type
        inp = ctxt.cast(bld, inp, oty, tyinp)
    if isinstance(tyinp, types.ArrayCompatible):
        ary = ctxt.make_array(tyinp)(ctxt, bld, inp)
        shape = cgutils.unpack_tuple(bld, ary.shape, tyinp.ndim)
        strides = cgutils.unpack_tuple(bld, ary.strides, tyinp.ndim)
        return _ArrayHelper(ctxt, bld, shape, strides, ary.data, tyinp.layout, tyinp.dtype, tyinp.ndim, inp)
    if None.unliteral(tyinp) in types.number_domain | {
        types.boolean} or isinstance(tyinp, types.scalars._NPDatetimeBase):
        return _ScalarHelper(ctxt, bld, inp, tyinp)
    raise None('unsupported type for {0}: {1}'.format(where, str(tyinp)))


def _broadcast_onto(src_ndim, src_shape, dest_ndim, dest_shape):
    '''Low-level utility function used in calculating a shape for
    an implicit output array.  This function assumes that the
    destination shape is an LLVM pointer to a C-style array that was
    already initialized to a size of one along all axes.

    Returns an integer value:
    >= 1  :  Succeeded.  Return value should equal the number of dimensions in
             the destination shape.
    0     :  Failed to broadcast because source shape is larger than the
             destination shape (this case should be weeded out at type
             checking).
    < 0   :  Failed to broadcast onto destination axis, at axis number ==
             -(return_value + 1).
    '''
    if src_ndim > dest_ndim:
        return 0
    src_index = None
    dest_index = dest_ndim - src_ndim
# WARNING: Decompyle incomplete


def _build_array(context, builder, array_ty, input_types, inputs):
    '''Utility function to handle allocation of an implicit output array
    given the target context, builder, output array type, and a list of
    _ArrayHelper instances.
    '''
    pass
# WARNING: Decompyle incomplete


def _unpack_output_types(ufunc, sig):
    if ufunc.nout == 1:
        return [
            sig.return_type]
    return None(sig.return_type)


def _unpack_output_values(ufunc, builder, values):
    if ufunc.nout == 1:
        return [
            values]
    return None.unpack_tuple(builder, values)


def _pack_output_values(ufunc, context, builder, typ, values):
    if ufunc.nout == 1:
        return values[0]
    return None.make_tuple(builder, typ, values)


def numpy_ufunc_kernel(context, builder, sig, args, ufunc, kernel_class):
    pass
# WARNING: Decompyle incomplete


def numpy_gufunc_kernel(context, builder, sig, args, ufunc, kernel_class):
    arguments = []
    expected_ndims = kernel_class.dufunc.expected_ndims()
    expected_ndims = expected_ndims[0] + expected_ndims[1]
    is_input = [
        True] * ufunc.nin + [
        False] * ufunc.nout
    for arg, ty, exp_ndim, is_inp in zip(args, sig.args, expected_ndims, is_input):
        if isinstance(ty, types.ArrayCompatible):
            arr = context.make_array(ty)(context, builder, arg)
            shape = cgutils.unpack_tuple(builder, arr.shape, ty.ndim)
            strides = cgutils.unpack_tuple(builder, arr.strides, ty.ndim)
            inner_arr_ty = ty.copy(ndim = exp_ndim)
            ndim = ty.ndim
            layout = ty.layout
            base_type = ty.dtype
            array_helper = _ArrayGUHelper(context, builder, shape, strides, arg, layout, base_type, ndim, inner_arr_ty, is_inp)
            arguments.append(array_helper)
            continue
        scalar_helper = _ScalarHelper(context, builder, arg, ty)
        arguments.append(scalar_helper)
        kernel = kernel_class(context, builder, sig)
        layouts = arguments()
        num_c_layout = (lambda .0: pass# WARNING: Decompyle incomplete
)(layouts())
        num_f_layout = (lambda .0: pass# WARNING: Decompyle incomplete
)(layouts())
    outputs = arguments[ufunc.nin:]
    intpty = context.get_value_type(types.intp)
    indices = arguments()
    loopshape_ndim = outputs[0].ndim - outputs[0].inner_arr_ty.ndim
    loopshape = outputs[0].shape[:loopshape_ndim]
    _sig = parse_signature(ufunc.gufunc_builder.signature)
# WARNING: Decompyle incomplete


class _Kernel(object):
    
    def __init__(self, context, builder, outer_sig):
        self.context = context
        self.builder = builder
        self.outer_sig = outer_sig

    
    def cast(self, val, fromty, toty):
        '''Numpy uses cast semantics that are different from standard Python
        (for example, it does allow casting from complex to float).

        This method acts as a patch to context.cast so that it allows
        complex to real/int casts.

        '''
        if not isinstance(fromty, types.Complex) and isinstance(toty, types.Complex):
            newty = fromty.underlying_float
            attr = self.context.get_getattr(fromty, 'real')
            val = attr(self.context, self.builder, fromty, val, 'real')
            fromty = newty
        return self.context.cast(self.builder, val, fromty, toty)

    
    def generate(self, *args):
        pass
    # WARNING: Decompyle incomplete



def _ufunc_db_function(ufunc):
    """Use the ufunc loop type information to select the code generation
    function from the table provided by the dict_of_kernels. The dict
    of kernels maps the loop identifier to a function with the
    following signature: (context, builder, signature, args).

    The loop type information has the form 'AB->C'. The letters to the
    left of '->' are the input types (specified as NumPy letter
    types).  The letters to the right of '->' are the output
    types. There must be 'ufunc.nin' letters to the left of '->', and
    'ufunc.nout' letters to the right.

    For example, a binary float loop resulting in a float, will have
    the following signature: 'ff->f'.

    A given ufunc implements many loops. The list of loops implemented
    for a given ufunc can be accessed using the 'types' attribute in
    the ufunc object. The NumPy machinery selects the first loop that
    fits a given calling signature (in our case, what we call the
    outer_sig). This logic is mimicked by 'ufunc_find_matching_loop'.
    """
    pass
# WARNING: Decompyle incomplete


def register_ufunc_kernel(ufunc, kernel, lower):
    pass
# WARNING: Decompyle incomplete


def register_unary_operator_kernel(operator, ufunc, kernel, lower, inplace = (False,)):
    pass
# WARNING: Decompyle incomplete


def register_binary_operator_kernel(op, ufunc, kernel, lower, inplace = (False,)):
    pass
# WARNING: Decompyle incomplete

array_positive_impl = (lambda context, builder, sig, args: 
class _UnaryPositiveKernel(_Kernel):

def generate(self, *args):
(val,) = argsvalnumpy_ufunc_kernel(context, builder, sig, args, np.positive, _UnaryPositiveKernel))()

def register_ufuncs(ufuncs, lower):
    kernels = { }
    for ufunc in ufuncs:
        db_func = _ufunc_db_function(ufunc)
        kernels[ufunc] = register_ufunc_kernel(ufunc, db_func, lower)
        for _op_map in (npydecl.NumpyRulesUnaryArrayOperator._op_map, npydecl.NumpyRulesArrayOperator._op_map):
            for operator, ufunc_name in _op_map.items():
                ufunc = getattr(np, ufunc_name)
                kernel = kernels[ufunc]
                if ufunc.nin == 1:
                    register_unary_operator_kernel(operator, ufunc, kernel, lower)
                    continue
                if ufunc.nin == 2:
                    register_binary_operator_kernel(operator, ufunc, kernel, lower)
                    continue
                raise RuntimeError("There shouldn't be any non-unary or binary operators")
                for _op_map in (npydecl.NumpyRulesInplaceArrayOperator._op_map,):
                    for operator, ufunc_name in _op_map.items():
                        ufunc = getattr(np, ufunc_name)
                        kernel = kernels[ufunc]
                        if ufunc.nin == 1:
                            register_unary_operator_kernel(operator, ufunc, kernel, lower, inplace = True)
                            continue
                        if ufunc.nin == 2:
                            register_binary_operator_kernel(operator, ufunc, kernel, lower, inplace = True)
                            continue
                        raise RuntimeError("There shouldn't be any non-unary or binary operators")
                        return None

register_ufuncs(ufunc_db.get_ufuncs(), registry.lower)
_make_dtype_object = (lambda typingctx, desc: pass# WARNING: Decompyle incomplete
)()
numpy_dtype = (lambda desc: if isinstance(desc, (types.Literal, types.functions.NumberClass)):

def imp(desc):
_make_dtype_object(desc)impraise None.NumbaTypeError('unknown dtype descriptor: {}'.format(desc)))()
