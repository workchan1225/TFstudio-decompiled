# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cgutils.pyc (Python 3.11)

'''
Generic helpers for LLVM code generation.
'''
import collections
from contextlib import contextmanager, ExitStack
import functools
from llvmlite import ir
from numba.core import utils, types, config, debuginfo
import numba.core.datamodel as numba
bool_t = ir.IntType(1)
int8_t = ir.IntType(8)
int32_t = ir.IntType(32)
intp_t = ir.IntType(utils.MACHINE_BITS)
voidptr_t = int8_t.as_pointer()
true_bit = bool_t(1)
false_bit = bool_t(0)
true_byte = int8_t(1)
false_byte = int8_t(0)

def as_bool_bit(builder, value):
    return builder.icmp_unsigned('!=', value, value.type(0))


def make_anonymous_struct(builder, values, struct_type = (None,)):
    '''
    Create an anonymous struct containing the given LLVM *values*.
    '''
    pass
# WARNING: Decompyle incomplete


def make_bytearray(buf):
    '''
    Make a byte array constant from *buf*.
    '''
    b = bytearray(buf)
    n = len(b)
    return ir.Constant(ir.ArrayType(ir.IntType(8), n), b)

_struct_proxy_cache = { }

def create_struct_proxy(fe_type, kind = ('value',)):
    '''
    Returns a specialized StructProxy subclass for the given fe_type.
    '''
    cache_key = (fe_type, kind)
    res = _struct_proxy_cache.get(cache_key)
# WARNING: Decompyle incomplete


def copy_struct(dst, src, repl = (None,)):
    '''
    Copy structure from *src* to *dst* with replacement from *repl*.
    '''
    pass
# WARNING: Decompyle incomplete


class _StructProxy(object):
    pass
# WARNING: Decompyle incomplete


class ValueStructProxy(_StructProxy):
    '''
    Create a StructProxy suitable for accessing regular values
    (e.g. LLVM values or alloca slots).
    '''
    
    def _get_be_type(self, datamodel):
        return datamodel.get_value_type()

    
    def _cast_member_to_value(self, index, val):
        return val

    
    def _cast_member_from_value(self, index, val):
        return val



class DataStructProxy(_StructProxy):
    '''
    Create a StructProxy suitable for accessing data persisted in memory.
    '''
    
    def _get_be_type(self, datamodel):
        return datamodel.get_data_type()

    
    def _cast_member_to_value(self, index, val):
        model = self._datamodel.get_model(index)
        return model.from_data(self._builder, val)

    
    def _cast_member_from_value(self, index, val):
        model = self._datamodel.get_model(index)
        return model.as_data(self._builder, val)



class Structure(object):
    pass
# WARNING: Decompyle incomplete


def alloca_once(builder, ty, size, name, zfill = (None, '', False)):
    '''Allocate stack memory at the entry block of the current function
    pointed by ``builder`` with llvm type ``ty``.  The optional ``size`` arg
    set the number of element to allocate.  The default is 1.  The optional
    ``name`` arg set the symbol name inside the llvm IR for debugging.
    If ``zfill`` is set, fill the memory with zeros at the current
    use-site location.  Note that the memory is always zero-filled after the
    ``alloca`` at init-site (the entry block).
    '''
    if isinstance(size, int):
        size = ir.Constant(intp_t, size)
    debuginfo.suspend_emission(builder)
    builder.goto_entry_block()
    ptr = builder.alloca(ty, size = size, name = name)
    builder.store(ty(None), ptr)
    None(None, None)


def sizeof(builder, ptr_type):
    '''Compute sizeof using GEP
    '''
    null = ptr_type(None)
    offset = null.gep([
        int32_t(1)])
    return builder.ptrtoint(offset, intp_t)


def alloca_once_value(builder, value, name, zfill = ('', False)):
    '''
    Like alloca_once(), but passing a *value* instead of a type.  The
    type is inferred and the allocated slot is also initialized with the
    given value.
    '''
    storage = alloca_once(builder, value.type, zfill = zfill)
    builder.store(value, storage)
    return storage


def insert_pure_function(module, fnty, name):
    '''
    Insert a pure function (in the functional programming sense) in the
    given module.
    '''
    fn = get_or_insert_function(module, fnty, name)
    fn.attributes.add('readonly')
    fn.attributes.add('nounwind')
    return fn


def get_or_insert_function(module, fnty, name):
    """
    Get the function named *name* with type *fnty* from *module*, or insert it
    if it doesn't exist.
    """
    fn = module.globals.get(name, None)
# WARNING: Decompyle incomplete


def get_or_insert_named_metadata(module, name):
    
    try:
        return module.get_named_metadata(name)
    except KeyError:
        return 



def add_global_variable(module, ty, name, addrspace = (0,)):
    unique_name = module.get_unique_name(name)
    return ir.GlobalVariable(module, ty, unique_name, addrspace)


def terminate(builder, bbend):
    bb = builder.basic_block
# WARNING: Decompyle incomplete


def get_null_value(ltype):
    return ltype(None)


def is_null(builder, val):
    null = get_null_value(val.type)
    return builder.icmp_unsigned('==', null, val)


def is_not_null(builder, val):
    null = get_null_value(val.type)
    return builder.icmp_unsigned('!=', null, val)


def if_unlikely(builder, pred):
    return builder.if_then(pred, likely = False)


def if_likely(builder, pred):
    return builder.if_then(pred, likely = True)


def ifnot(builder, pred):
    return builder.if_then(builder.not_(pred))


def increment_index(builder, val):
    '''
    Increment an index *val*.
    '''
    one = val.type(1)
    return builder.add(val, one, flags = [
        'nsw'])

Loop = collections.namedtuple('Loop', ('index', 'do_break'))
for_range = (lambda builder, count, start, intp = (None, None): pass# WARNING: Decompyle incomplete
)()
for_range_slice = (lambda builder, start, stop, step, intp, inc = (None, True): pass# WARNING: Decompyle incomplete
)()
for_range_slice_generic = (lambda builder, start, stop, step: pass# WARNING: Decompyle incomplete
)()
loop_nest = (lambda builder, shape, intp, order = ('C',): pass# WARNING: Decompyle incomplete
)()
_loop_nest = (lambda builder, shape, intp: pass# WARNING: Decompyle incomplete
)()

def pack_array(builder, values, ty = (None,)):
    """
    Pack a sequence of values in a LLVM array.  *ty* should be given
    if the array may be empty, in which case the type can't be inferred
    from the values.
    """
    n = len(values)
# WARNING: Decompyle incomplete


def pack_struct(builder, values):
    '''
    Pack a sequence of values into a LLVM struct.
    '''
    structty = (lambda .0: [ v.type for v in .0 ])(values())
    st = structty(ir.Undefined)
    for i, v in enumerate(values):
        st = builder.insert_value(st, v, i)
        return st


def unpack_tuple(builder, tup, count = (None,)):
    '''
    Unpack an array or structure of values, return a Python tuple.
    '''
    pass
# WARNING: Decompyle incomplete


def get_item_pointer(context, builder, aryty, ary, inds, wraparound, boundscheck = (False, False)):
    shapes = unpack_tuple(builder, ary.shape, count = aryty.ndim)
    strides = unpack_tuple(builder, ary.strides, count = aryty.ndim)
    return get_item_pointer2(context, builder, data = ary.data, shape = shapes, strides = strides, layout = aryty.layout, inds = inds, wraparound = wraparound, boundscheck = boundscheck)


def do_boundscheck(context, builder, ind, dimlen, axis = (None,)):
    pass
# WARNING: Decompyle incomplete


def get_item_pointer2(context, builder, data, shape, strides, layout, inds, wraparound, boundscheck = (False, False)):
    pass
# WARNING: Decompyle incomplete


def _scalar_pred_against_zero(builder, value, fpred, icond):
    nullval = value.type(0)
    if isinstance(value.type, (ir.FloatType, ir.DoubleType)):
        isnull = fpred(value, nullval)
    elif isinstance(value.type, ir.IntType):
        isnull = builder.icmp_signed(icond, value, nullval)
    else:
        raise TypeError(f'''unexpected value type {value.type!s}''')
    return isnull


def is_scalar_zero(builder, value):
    '''
    Return a predicate representing whether *value* is equal to zero.
    '''
    return _scalar_pred_against_zero(builder, value, functools.partial(builder.fcmp_ordered, '=='), '==')


def is_not_scalar_zero(builder, value):
    '''
    Return a predicate representing whether a *value* is not equal to zero.
    (not exactly "not is_scalar_zero" because of nans)
    '''
    return _scalar_pred_against_zero(builder, value, functools.partial(builder.fcmp_unordered, '!='), '!=')


def is_scalar_zero_or_nan(builder, value):
    '''
    Return a predicate representing whether *value* is equal to either zero
    or NaN.
    '''
    return _scalar_pred_against_zero(builder, value, functools.partial(builder.fcmp_unordered, '=='), '==')

is_true = is_not_scalar_zero
is_false = is_scalar_zero

def is_scalar_neg(builder, value):
    '''
    Is *value* negative?  Assumes *value* is signed.
    '''
    return _scalar_pred_against_zero(builder, value, functools.partial(builder.fcmp_ordered, '<'), '<')

early_exit_if = (lambda builder = contextmanager, stack = contextmanager, cond = contextmanager: pass# WARNING: Decompyle incomplete
)()

def early_exit_if_null(builder, stack, obj):
    '''
    A convenience wrapper for :func:`early_exit_if`, for the common case where
    the CPython API indicates an error by returning ``NULL``.
    '''
    return early_exit_if(builder, stack, is_null(builder, obj))


def guard_null(context, builder, value, exc_tuple):
    '''
    Guard against *value* being null or zero.
    *exc_tuple* should be a (exception type, arguments...) tuple.
    '''
    builder.if_then(is_scalar_zero(builder, value), likely = False)
    exc = exc_tuple[0]
    if not exc_tuple[1:]:
        exc_args = None
        context.call_conv.return_user_exc(builder, exc, exc_args)
        None(None, None)
        return None
    with None:
        if not exc_tuple[1:]:
            pass


def guard_memory_error(context, builder, pointer, msg = (None,)):
    '''
    Guard against *pointer* being NULL (and raise a MemoryError).
    '''
    pass
# WARNING: Decompyle incomplete

if_zero = (lambda builder, value, likely = (False,): pass# WARNING: Decompyle incomplete
)()
guard_zero = guard_null

def is_pointer(ltyp):
    '''
    Whether the LLVM type *typ* is a struct type.
    '''
    return isinstance(ltyp, ir.PointerType)


def get_record_member(builder, record, offset, typ):
    pval = gep_inbounds(builder, record, 0, offset)
# WARNING: Decompyle incomplete


def is_neg_int(builder, val):
    return builder.icmp_signed('<', val, val.type(0))


def gep_inbounds(builder, ptr, *inds, **kws):
    '''
    Same as *gep*, but add the `inbounds` keyword.
    '''
    pass
# WARNING: Decompyle incomplete


def gep(builder, ptr, *inds, **kws):
    '''
    Emit a getelementptr instruction for the given pointer and indices.
    The indices can be LLVM values or Python int constants.
    '''
    name = kws.pop('name', '')
    inbounds = kws.pop('inbounds', False)
# WARNING: Decompyle incomplete


def pointer_add(builder, ptr, offset, return_type = (None,)):
