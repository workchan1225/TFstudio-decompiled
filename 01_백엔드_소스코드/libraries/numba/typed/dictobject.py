# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dictobject.pyc (Python 3.11)

'''
Compiler-side implementation of the dictionary.
'''
import ctypes
import operator
from enum import IntEnum
from llvmlite import ir
from numba import _helperlib
from numba.core.extending import overload, overload_method, overload_attribute, intrinsic, register_model, models, lower_builtin, lower_cast, make_attribute_wrapper
from numba.core.imputils import iternext_impl, impl_ret_untracked
from numba.core import types, cgutils
from numba.core.types import DictType, DictItemsIterableType, DictKeysIterableType, DictValuesIterableType, DictIteratorType, Type
from numba.core.imputils import impl_ret_borrowed, RefType
from numba.core.errors import TypingError, LoweringError, NumbaTypeError
from numba.core import typing
from numba.typed.typedobjectutils import _as_bytes, _cast, _nonoptional, _sentry_safe_cast_default, _get_incref_decref, _get_equal, _container_get_data
ll_dict_type = cgutils.voidptr_t
ll_dictiter_type = cgutils.voidptr_t
ll_voidptr_type = cgutils.voidptr_t
ll_status = cgutils.int32_t
ll_ssize_t = cgutils.intp_t
ll_hash = ll_ssize_t
ll_bytes = cgutils.voidptr_t
_meminfo_dictptr = types.MemInfoPointer(types.voidptr)

class DKIX(IntEnum):
    '''Special return value of dict lookup.
    '''
    EMPTY = -1


class Status(IntEnum):
    '''Status code for other dict operations.
    '''
    OK = 0
    OK_REPLACED = 1
    ERR_NO_MEMORY = -1
    ERR_DICT_MUTATED = -2
    ERR_ITER_EXHAUSTED = -3
    ERR_DICT_EMPTY = -4
    ERR_CMP_FAILED = -5


def new_dict(key, value, n_keys = (0,)):
    '''Construct a new dict with enough space for *n_keys* without a resize.

    Parameters
    ----------
    key, value : TypeRef
        Key type and value type of the new dict.
    n_keys : int, default 0
        The number of keys to insert without needing a resize.
        A value of 0 creates a dict with minimum size.
    '''
    return dict()

DictModel = <NODE:12>()
DictIterModel = <NODE:12>()()()()
make_attribute_wrapper(DictItemsIterableType, 'parent', '_parent')
make_attribute_wrapper(DictKeysIterableType, 'parent', '_parent')
make_attribute_wrapper(DictValuesIterableType, 'parent', '_parent')

def _raise_if_error(context, builder, status, msg):
    '''Raise an internal error depending on the value of *status*
    '''
    ok_status = status.type(int(Status.OK))
    builder.if_then(builder.icmp_signed('!=', status, ok_status))
    context.call_conv.return_user_exc(builder, RuntimeError, (msg,))
    None(None, None)
    return None
    with None:
        if not None:
            pass

_as_meminfo = (lambda typingctx, dctobj: if not isinstance(dctobj, types.DictType):
raise TypingError('expected *dctobj* to be a DictType')
def codegen(context, builder, sig, args):
(td,) = sig.args(d,) = argscontext.nrt.incref(builder, td, d)ctor = cgutils.create_struct_proxy(td)dstruct = ctor(context, builder, value = d)dstruct.meminfosig = _meminfo_dictptr(dctobj)(sig, codegen))()
_from_meminfo = (lambda typingctx, mi, dicttyperef: pass# WARNING: Decompyle incomplete
)()

def _call_dict_free(context, builder, ptr):
    '''Call numba_dict_free(ptr)
    '''
    fnty = ir.FunctionType(ir.VoidType(), [
        ll_dict_type])
    free = cgutils.get_or_insert_function(builder.module, fnty, 'numba_dict_free')
    builder.call(free, [
        ptr])


def _imp_dtor(context, module):
    '''Define the dtor for dictionary
    '''
    llvoidptr = context.get_value_type(types.voidptr)
    llsize = context.get_value_type(types.uintp)
    fnty = ir.FunctionType(ir.VoidType(), [
        llvoidptr,
        llsize,
        llvoidptr])
    fname = '_numba_dict_dtor'
    fn = cgutils.get_or_insert_function(module, fnty, fname)
    if fn.is_declaration:
        fn.linkage = 'linkonce_odr'
        builder = ir.IRBuilder(fn.append_basic_block())
        dp = builder.bitcast(fn.args[0], ll_dict_type.as_pointer())
        d = builder.load(dp)
        _call_dict_free(context, builder, d)
        builder.ret_void()
    return fn

_dict_new_sized = (lambda typingctx, n_keys, keyty, valty: pass# WARNING: Decompyle incomplete
)()
_dict_set_method_table = (lambda typingctx, dp, keyty, valty: pass# WARNING: Decompyle incomplete
)()
_dict_insert = (lambda typingctx, d, key, hashval, val: resty = types.int32sig = resty(d, d.key_type, types.intp, d.value_type)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ll_status, [
ll_dict_type,
ll_bytes,
ll_hash,
ll_bytes,
ll_bytes])(d, key, hashval, val) = args(td, tkey, thashval, tval) = sig.argsfn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_dict_insert')dm_key = context.data_model_manager[tkey]dm_val = context.data_model_manager[tval]data_key = dm_key.as_data(builder, key)data_val = dm_val.as_data(builder, val)ptr_key = cgutils.alloca_once_value(builder, data_key)cgutils.memset_padding(builder, ptr_key)ptr_val = cgutils.alloca_once_value(builder, data_val)ptr_oldval = cgutils.alloca_once(builder, data_val.type)dp = _container_get_data(context, builder, td, d)status = builder.call(fn, [
dp,
_as_bytes(builder, ptr_key),
hashval,
_as_bytes(builder, ptr_val),
_as_bytes(builder, ptr_oldval)])status(sig, codegen))()
_dict_length = (lambda typingctx, d: resty = types.intpsig = resty(d)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ll_ssize_t, [
ll_dict_type])fn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_dict_length')(d,) = args(td,) = sig.argsdp = _container_get_data(context, builder, td, d)n = builder.call(fn, [
dp])n(sig, codegen))()
_dict_dump = (lambda typingctx, d: resty = types.voidsig = resty(d)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ir.VoidType(), [
ll_dict_type])(td,) = sig.args(d,) = argsdp = _container_get_data(context, builder, td, d)fn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_dict_dump')builder.call(fn, [
dp])(sig, codegen))()
_dict_lookup = (lambda typingctx, d, key, hashval: pass# WARNING: Decompyle incomplete
)()
_dict_popitem = (lambda typingctx, d: pass# WARNING: Decompyle incomplete
)()
_dict_delitem = (lambda typingctx, d, hk, ix: resty = types.int32sig = resty(d, hk, types.intp)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ll_status, [
ll_dict_type,
ll_hash,
ll_ssize_t])(d, hk, ix) = args(td, thk, tix) = sig.argsfn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_dict_delitem')dp = _container_get_data(context, builder, td, d)status = builder.call(fn, [
dp,
hk,
ix])status(sig, codegen))()

def _iterator_codegen(resty):
    '''The common codegen for iterator intrinsics.

    Populates the iterator struct and increfs.
    '''
    pass
# WARNING: Decompyle incomplete

_dict_items = (lambda typingctx, d: resty = types.DictItemsIterableType(d)sig = resty(d)codegen = _iterator_codegen(resty)(sig, codegen))()
_dict_keys = (lambda typingctx, d: resty = types.DictKeysIterableType(d)sig = resty(d)codegen = _iterator_codegen(resty)(sig, codegen))()
_dict_values = (lambda typingctx, d: resty = types.DictValuesIterableType(d)sig = resty(d)codegen = _iterator_codegen(resty)(sig, codegen))()
_make_dict = (lambda typingctx, keyty, valty, ptr: pass# WARNING: Decompyle incomplete
)()
impl_new_dict = (lambda key, value, n_keys = (0,): pass# WARNING: Decompyle incomplete
)()
impl_len = (lambda d:
