# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: listobject.pyc (Python 3.11)

'''
Compiler-side implementation of the Numba  typed-list.
'''
import operator
from enum import IntEnum
from llvmlite import ir
from numba.core.extending import overload, overload_method, overload_attribute, register_jitable, intrinsic, register_model, models, lower_builtin
from numba.core.imputils import iternext_impl
from numba.core import types, cgutils, config
from numba.core.types import ListType, ListTypeIterableType, ListTypeIteratorType, Type, NoneType
from numba.core.imputils import impl_ret_borrowed, RefType
from numba.core.errors import TypingError, NumbaTypeError
from numba.core import typing
from numba.typed.typedobjectutils import _as_bytes, _cast, _nonoptional, _get_incref_decref, _container_get_data, _container_get_meminfo
from numba.cpython import listobj
ll_list_type = cgutils.voidptr_t
ll_listiter_type = cgutils.voidptr_t
ll_voidptr_type = cgutils.voidptr_t
ll_status = cgutils.int32_t
ll_ssize_t = cgutils.intp_t
ll_bytes = cgutils.voidptr_t
_meminfo_listptr = types.MemInfoPointer(types.voidptr)
if config.USE_LEGACY_TYPE_SYSTEM:
    INDEXTY = types.intp
    index_types = types.integer_domain
else:
    INDEXTY = types.py_int
    index_types = types.py_integer_domain
DEFAULT_ALLOCATED = 0
ListModel = <NODE:12>()
ListIterModel = <NODE:12>()()

class ListStatus(IntEnum):
    '''Status code for other list operations.
    '''
    LIST_OK = (0,)
    LIST_ERR_INDEX = -1
    LIST_ERR_NO_MEMORY = -2
    LIST_ERR_MUTATED = -3
    LIST_ERR_ITER_EXHAUSTED = -4
    LIST_ERR_IMMUTABLE = -5


class ErrorHandler(object):
    '''ErrorHandler for calling codegen functions from this file.

    Stores the state needed to raise an exception from nopython mode.
    '''
    
    def __init__(self, context):
        self.context = context

    
    def __call__(self, builder, status, msg):
        ok_status = status.type(int(ListStatus.LIST_OK))
        builder.if_then(builder.icmp_signed('!=', status, ok_status), likely = True)
        self.context.call_conv.return_user_exc(builder, RuntimeError, (msg,))
        None(None, None)
        return None
        with None:
            if not None:
                pass



def _check_for_none_typed(lst, method):
    if isinstance(lst.dtype, NoneType):
        raise TypingError("method support for List[None] is limited, not supported: '{}'.".format(method))

_as_meminfo = (lambda typingctx, lstobj: if not isinstance(lstobj, types.ListType):
raise TypingError('expected *lstobj* to be a ListType')
def codegen(context, builder, sig, args):
(tl,) = sig.args(l,) = argscontext.nrt.incref(builder, tl, l)ctor = cgutils.create_struct_proxy(tl)lstruct = ctor(context, builder, value = l)lstruct.meminfosig = _meminfo_listptr(lstobj)(sig, codegen))()
_from_meminfo = (lambda typingctx, mi, listtyperef: pass# WARNING: Decompyle incomplete
)()

def _list_codegen_set_method_table(context, builder, lp, itemty):
    vtablety = ir.LiteralStructType([
        ll_voidptr_type,
        ll_voidptr_type])
    setmethod_fnty = ir.FunctionType(ir.VoidType(), [
        ll_list_type,
        vtablety.as_pointer()])
    setmethod_fn = cgutils.get_or_insert_function(builder.module, setmethod_fnty, 'numba_list_set_method_table')
    vtable = cgutils.alloca_once(builder, vtablety, zfill = True)
    item_incref_ptr = cgutils.gep_inbounds(builder, vtable, 0, 0)
    item_decref_ptr = cgutils.gep_inbounds(builder, vtable, 0, 1)
    dm_item = context.data_model_manager[itemty]
    if dm_item.contains_nrt_meminfo():
        (item_incref, item_decref) = _get_incref_decref(context, builder.module, dm_item, 'list')
        builder.store(builder.bitcast(item_incref, item_incref_ptr.type.pointee), item_incref_ptr)
        builder.store(builder.bitcast(item_decref, item_decref_ptr.type.pointee), item_decref_ptr)
    builder.call(setmethod_fn, [
        lp,
        vtable])

_list_set_method_table = (lambda typingctx, lp, itemty: pass# WARNING: Decompyle incomplete
)()
list_is = (lambda context, builder, sig, args: a_meminfo = _container_get_meminfo(context, builder, sig.args[0], args[0])b_meminfo = _container_get_meminfo(context, builder, sig.args[1], args[1])ma = builder.ptrtoint(a_meminfo, cgutils.intp_t)mb = builder.ptrtoint(b_meminfo, cgutils.intp_t)builder.icmp_signed('==', ma, mb))()

def _call_list_free(context, builder, ptr):
    '''Call numba_list_free(ptr)
    '''
    fnty = ir.FunctionType(ir.VoidType(), [
        ll_list_type])
    free = cgutils.get_or_insert_function(builder.module, fnty, 'numba_list_free')
    builder.call(free, [
        ptr])


def _imp_dtor(context, module):
    '''Define the dtor for list
    '''
    llvoidptr = context.get_value_type(types.voidptr)
    llsize = context.get_value_type(types.uintp)
    fnty = ir.FunctionType(ir.VoidType(), [
        llvoidptr,
        llsize,
        llvoidptr])
    fname = '_numba_list_dtor'
    fn = cgutils.get_or_insert_function(module, fnty, fname)
    if fn.is_declaration:
        fn.linkage = 'linkonce_odr'
        builder = ir.IRBuilder(fn.append_basic_block())
        lp = builder.bitcast(fn.args[0], ll_list_type.as_pointer())
        l = builder.load(lp)
        _call_list_free(context, builder, l)
        builder.ret_void()
    return fn


def new_list(item, allocated = (DEFAULT_ALLOCATED,)):
    '''Construct a new list. (Not implemented in the interpreter yet)

    Parameters
    ----------
    item: TypeRef
        Item type of the new list.
    allocated: int
        number of items to pre-allocate

    '''
    return list()


def _add_meminfo(context, builder, lstruct):
    alloc_size = context.get_abi_sizeof(context.get_value_type(types.voidptr))
    dtor = _imp_dtor(context, builder.module)
    meminfo = context.nrt.meminfo_alloc_dtor(builder, context.get_constant(types.uintp, alloc_size), dtor)
    data_pointer = context.nrt.meminfo_data(builder, meminfo)
    data_pointer = builder.bitcast(data_pointer, ll_list_type.as_pointer())
    builder.store(lstruct.data, data_pointer)
    lstruct.meminfo = meminfo

_make_list = (lambda typingctx, itemty, ptr: pass# WARNING: Decompyle incomplete
)()

def _list_new_codegen(context, builder, itemty, new_size, error_handler):
    fnty = ir.FunctionType(ll_status, [
        ll_list_type.as_pointer(),
        ll_ssize_t,
        ll_ssize_t])
    fn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_list_new')
    ll_item = context.get_data_type(itemty)
    sz_item = context.get_abi_sizeof(ll_item)
    reflp = cgutils.alloca_once(builder, ll_list_type, zfill = True)
    status = builder.call(fn, [
        reflp,
        ll_ssize_t(sz_item),
        new_size])
    msg = 'Failed to allocate list'
    error_handler(builder, status, msg)
    lp = builder.load(reflp)
    return lp

_list_new = (lambda typingctx, itemty, allocated: pass# WARNING: Decompyle incomplete
)()
impl_new_list = (lambda item, allocated = (DEFAULT_ALLOCATED,): pass# WARNING: Decompyle incomplete
)()
impl_len = (lambda l: if isinstance(l, types.ListType):

def impl(l):
_list_length(l)impl)()
_list_length = (lambda typingctx, l: sig = types.intp(l)
def codegen(context, builder, sig, args):
(tl,) = sig.args(l,) = argsfnty = ir.FunctionType(ll_ssize_t, [
ll_list_type])fname = 'numba_list_size_address'fn = cgutils.get_or_insert_function(builder.module, fnty, fname)fn.attributes.add('alwaysinline')fn.attributes.add('readonly')fn.attributes.add('nounwind')lp = _container_get_data(context, builder, tl, l)len_addr = builder.call(fn, [
lp])ptr = builder.inttoptr(len_addr, cgutils.intp_t.as_pointer())builder.load(ptr)(sig, codegen))()
impl_allocated = (lambda l: if isinstance(l, types.ListType):

def impl(l):
_list_allocated(l)impl)()
_list_allocated = (lambda typingctx, l: resty = types.intpsig = resty(l)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ll_ssize_t, [
ll_list_type])fn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_list_allocated')(l,) = args(tl,) = sig.argslp = _container_get_data(context, builder, tl, l)n = builder.call(fn, [
lp])n(sig, codegen))()
impl_is_mutable = (lambda l: if isinstance(l, types.ListType):

def impl(l):
bool(_list_is_mutable(l))impl)()
_list_is_mutable = (lambda typingctx, l: resty = types.int32sig = resty(l)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ll_status, [
ll_list_type])fn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_list_is_mutable')(l,) = args(tl,) = sig.argslp = _container_get_data(context, builder, tl, l)n = builder.call(fn, [
lp])n(sig, codegen))()
impl_make_mutable = (lambda l: if isinstance(l, types.ListType):

def impl(l):
_list_set_is_mutable(l, 1)impl)()
impl_make_immutable = (lambda l: if isinstance(l, types.ListType):

def impl(l):
_list_set_is_mutable(l, 0)impl)()
_list_set_is_mutable = (lambda typingctx, l, is_mutable: resty = types.voidsig = resty(l, is_mutable)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ir.VoidType(), [
ll_list_type,
cgutils.intp_t])fn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_list_set_is_mutable')(l, i) = args(tl, ti) = sig.argslp = _container_get_data(context, builder, tl, l)builder.call(fn, [
lp,
i])(sig, codegen))()
_list_append = (lambda typingctx, l, item: resty = types.int32sig = resty(l, l.item_type)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ll_status, [
ll_list_type,
ll_bytes])(l, item) = args(tl, titem) = sig.argsfn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_list_append')dm_item = context.data_model_manager[titem]data_item = dm_item.as_data(builder, item)ptr_item = cgutils.alloca_once_value(builder, data_item)lp = _container_get_data(context, builder, tl, l)status = builder.call(fn, [
lp,
_as_bytes(builder, ptr_item)])status(sig, codegen))()
impl_append = (lambda l, item: pass# WARNING: Decompyle incomplete
)()
fix_index = (lambda tyctx, list_ty, index_ty: sig = types.intp(list_ty, index_ty)
def codegen(context, builder, sig, args):
(list_ty, index_ty) = sig.args(ll_list, ll_idx) = argsis_negative = builder.icmp_signed('<', ll_idx, ir.Constant(ll_idx.type, 0))(fast_len_sig, length_fn) = _list_length._defn(context.typing_context, list_ty)length = length_fn(context, builder, fast_len_sig, (ll_list,))st = 'sext' if ll_idx.type.width < length.type.width else 'trunc'op = getattr(builder, st)fixedup_idx = op(ll_idx, length.type)wrapped_index = builder.add(fixedup_idx, length)builder.select(is_negative, wrapped_index, fixedup_idx)(sig, codegen))()
handle_index = (lambda l, index: index = fix_index(l, index)if index < 0 or index >= len(l):
raise IndexError('list index out of range')index)()
handle_slice = (lambda l, s: if len(l) == 0:
range(0)(ll, sa, so, se) = (None(l), s.start, s.stop, s.step)if se > 0:
start = max(ll + sa, 0) if s.start < 0 else min(ll, sa)stop = max(ll + so, 0) if so < 0 else min(ll, so)elif se < 0:
start = max(ll + sa, -1) if s.start < 0 else min(ll - 1, sa)stop = max(ll + so, -1) if so < 0 else min(ll, so)else:
raise ValueError('slice step cannot be zero')range(start, stop, s.step))()

def _gen_getitem(borrowed):
    pass
# WARNING: Decompyle incomplete

_list_getitem = _gen_getitem(False)
_list_getitem_borrowed = _gen_getitem(True)
impl_getitem = (lambda l, index: pass# WARNING: Decompyle incomplete
)()
_list_setitem = (lambda typingctx, l, index, item: resty = types.int32sig = resty(l, index, item)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ll_status, [
ll_list_type,
ll_ssize_t,
ll_bytes])(l, index, item) = args(tl, tindex, titem) = sig.argsfn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_list_setitem')dm_item = context.data_model_manager[titem]data_item = dm_item.as_data(builder, item)ptr_item = cgutils.alloca_once_value(builder, data_item)lp = _container_get_data(context, builder, tl, l)status = builder.call(fn, [
lp,
index,
_as_bytes(builder, ptr_item)])status(sig, codegen))()
impl_setitem = (lambda l, index, item: pass# WARNING: Decompyle incomplete
)()
impl_pop = (lambda l, index = (-1,): pass# WARNING: Decompyle incomplete
)()
_list_delitem = (lambda typingctx, l, index: resty = types.int32sig = resty(l, index)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ll_status, [
ll_list_type,
ll_ssize_t])(tl, tindex) = sig.args(l, index) = argsfn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_list_delitem')lp = _container_get_data(context, builder, tl, l)status = builder.call(fn, [
lp,
index])status(sig, codegen))()
_list_delete_slice = (lambda typingctx, l, start, stop, step: resty = types.int32sig = resty(l, start, stop, step)
def codegen(context, builder, sig, args):
fnty = ir.FunctionType(ll_status, [
ll_list_type,
ll_ssize_t,
ll_ssize_t,
ll_ssize_t])(l, start, stop, step) = args(tl, tstart, tstop, tstep) = sig.argsfn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_list_delete_slice')lp = _container_get_data(context, builder, tl, l)status = builder.call(fn, [
lp,
start,
stop,
step])status(sig, codegen))()
impl_delitem = (lambda l, index: if not isinstance(l, types.ListType):
NoneNone(l, 'delitem')if index in index_types:

def integer_impl(l, index):
cindex = _cast(handle_index(l, index), INDEXTY)status = _list_delitem(l, cindex)if status == ListStatus.LIST_OK:
Noneif None == ListStatus.LIST_ERR_IMMUTABLE:
raise ValueError('list is immutable')raise AssertionError('internal list error during delitem')integer_implif None(index, types.SliceType):

def slice_impl(l, index):
slice_range = handle_slice(l, index)status = _list_delete_slice(l, slice_range.start, slice_range.stop, slice_range.step)if status == ListStatus.LIST_ERR_MUTATED:
raise ValueError('list is immutable')slice_implraise None('list indices must be integers or slices'))()
impl_contains = (lambda l, item: pass# WARNING: Decompyle incomplete
)()
impl_count = (lambda l, item: pass# WARNING: Decompyle incomplete
)()
impl_extend = (lambda l, iterable: pass# WARNING: Decompyle incomplete
)()
impl_insert = (lambda l, index, item: if not isinstance(l, types.ListType):
NoneNone(l, 'insert')if isinstance(item, NoneType):
raise TypingError('method support for List[None] is limited')if index in index_types:

def impl(l, index, item):
if index >= len(l) or len(l) == 0:
l.append(item)Noneif None < 0:
index = max(len(l) + index, 0)l.append(l[0])i = len(l) - 1# WARNING: Decompyle incomplete
if l.is_precise():
impll = None.refine(item)itemty = l.item_typesig = typing.signature(types.void, l, INDEXTY, itemty)(sig, impl)raise None('list insert indices must be integers'))()
impl_remove = (lambda l, item: pass# WARNING: Decompyle incomplete
)()
impl_clear = (lambda l:
