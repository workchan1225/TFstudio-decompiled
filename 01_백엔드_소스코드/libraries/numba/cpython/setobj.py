# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: setobj.pyc (Python 3.11)

'''
Support for native homogeneous sets.
'''
import collections
import contextlib
import math
import operator
from functools import cached_property
from llvmlite import ir
from numba.core import types, typing, cgutils
from numba.core.imputils import lower_builtin, lower_cast, iternext_impl, impl_ret_borrowed, impl_ret_new_ref, impl_ret_untracked, for_iter, call_len, RefType
from numba.misc import quicksort
from numba.cpython import slicing
from numba.core.errors import NumbaValueError, TypingError
from numba.core.extending import overload, overload_method, intrinsic

def get_payload_struct(context, builder, set_type, ptr):
    '''
    Given a set value and type, get its payload structure (as a
    reference, so that mutations are seen by all).
    '''
    payload_type = types.SetPayload(set_type)
    ptrty = context.get_data_type(payload_type).as_pointer()
    payload = builder.bitcast(ptr, ptrty)
    return context.make_data_helper(builder, payload_type, ref = payload)


def get_entry_size(context, set_type):
    '''
    Return the entry size for the given set type.
    '''
    llty = context.get_data_type(types.SetEntry(set_type))
    return context.get_abi_sizeof(llty)

EMPTY = -1
DELETED = -2
FALLBACK = -43
MINSIZE = 16
LINEAR_PROBES = 3
DEBUG_ALLOCS = False

def get_hash_value(context, builder, typ, value):
    '''
    Compute the hash of the given value.
    '''
    typingctx = context.typing_context
    fnty = typingctx.resolve_value_type(hash)
    sig = fnty.get_call_type(typingctx, (typ,), { })
    fn = context.get_function(fnty, sig)
    h = fn(builder, (value,))
    is_ok = is_hash_used(context, builder, h)
    fallback = ir.Constant(h.type, FALLBACK)
    return builder.select(is_ok, h, fallback)

_get_hash_value_intrinsic = (lambda typingctx, value: pass# WARNING: Decompyle incomplete
)()

def is_hash_empty(context, builder, h):
    '''
    Whether the hash value denotes an empty entry.
    '''
    empty = ir.Constant(h.type, EMPTY)
    return builder.icmp_unsigned('==', h, empty)


def is_hash_deleted(context, builder, h):
    '''
    Whether the hash value denotes a deleted entry.
    '''
    deleted = ir.Constant(h.type, DELETED)
    return builder.icmp_unsigned('==', h, deleted)


def is_hash_used(context, builder, h):
    '''
    Whether the hash value denotes an active entry.
    '''
    deleted = ir.Constant(h.type, DELETED)
    return builder.icmp_unsigned('<', h, deleted)


def check_all_set(*args):
    pass
# WARNING: Decompyle incomplete

SetLoop = collections.namedtuple('SetLoop', ('index', 'entry', 'do_break'))

class _SetPayload(object):
    
    def __init__(self, context, builder, set_type, ptr):
        payload = get_payload_struct(context, builder, set_type, ptr)
        self._context = context
        self._builder = builder
        self._ty = set_type
        self._payload = payload
        self._entries = payload._get_ptr_by_name('entries')
        self._ptr = ptr

    mask = (lambda self: self._payload.mask)()
    mask = (lambda self, value: self._payload.mask = value)()
    used = (lambda self: self._payload.used)()
    used = (lambda self, value: self._payload.used = value)()
    fill = (lambda self: self._payload.fill)()
    fill = (lambda self, value: self._payload.fill = value)()
    finger = (lambda self: self._payload.finger)()
    finger = (lambda self, value: self._payload.finger = value)()
    dirty = (lambda self: self._payload.dirty)()
    dirty = (lambda self, value: self._payload.dirty = value)()
    entries = (lambda self: self._entries)()
    ptr = (lambda self: self._ptr)()
    
    def get_entry(self, idx):
        '''
        Get entry number *idx*.
        '''
        entry_ptr = cgutils.gep(self._builder, self._entries, idx)
        entry = self._context.make_data_helper(self._builder, types.SetEntry(self._ty), ref = entry_ptr)
        return entry

    
    def _lookup(self, item, h, for_insert = (False,)):
        '''
        Lookup the *item* with the given hash values in the entries.

        Return a (found, entry index) tuple:
        - If found is true, <entry index> points to the entry containing
          the item.
        - If found is false, <entry index> points to the empty entry that
          the item can be written to (only if *for_insert* is true)
        '''
        pass
    # WARNING: Decompyle incomplete

    _iterate = (lambda self, start = (None,): pass# WARNING: Decompyle incomplete
)()
    _next_entry = (lambda self: pass# WARNING: Decompyle incomplete
)()


class SetInstance(object):
    
    def __init__(self, context, builder, set_type, set_val):
        self._context = context
        self._builder = builder
        self._ty = set_type
        self._entrysize = get_entry_size(context, set_type)
        self._set = context.make_helper(builder, set_type, set_val)

    dtype = (lambda self: self._ty.dtype)()
    payload = (lambda self: context = self._contextbuilder = self._builderptr = self._context.nrt.meminfo_data(builder, self.meminfo)_SetPayload(context, builder, self._ty, ptr))()
    value = (lambda self: self._set._getvalue())()
    meminfo = (lambda self: self._set.meminfo)()
    parent = (lambda self: self._set.parent)()
    parent = (lambda self, value: self._set.parent = value)()
    
    def get_size(self):
        '''
        Return the number of elements in the size.
        '''
        return self.payload.used

    
    def set_dirty(self, val):
        if self._ty.reflected:
            self.payload.dirty = cgutils.true_bit if val else cgutils.false_bit
            return None

    
    def _add_entry(self, payload, entry, item, h, do_resize = (True,)):
        context = self._context
        builder = self._builder
        old_hash = entry.hash
        entry.hash = h
        self.incref_value(item)
        entry.key = item
        used = payload.used
        one = ir.Constant(used.type, 1)
        used = builder.add(used, one)
        payload.used = builder.add(used, one)
        builder.if_then(is_hash_empty(context, builder, old_hash), likely = True)
        payload.fill = builder.add(payload.fill, one)
        None(None, None)

    
    def _add_key(self, payload, item, h, do_resize, do_incref = (True, True)):
        context = self._context
        builder = self._builder
        (found, i) = payload._lookup(item, h, for_insert = True)
        not_found = builder.not_(found)
        builder.if_then(not_found)
        entry = payload.get_entry(i)
        old_hash = entry.hash
        entry.hash = h
        if do_incref:
            self.incref_value(item)
        entry.key = item
        used = payload.used
        one = ir.Constant(used.type, 1)
        used = builder.add(used, one)
        payload.used = builder.add(used, one)
        builder.if_then(is_hash_empty(context, builder, old_hash), likely = True)
        payload.fill = builder.add(payload.fill, one)
        None(None, None)

    
    def _remove_entry(self, payload, entry, do_resize, do_decref = (True, True)):
        entry.hash = ir.Constant(entry.hash.type, DELETED)
        if do_decref:
            self.decref_value(entry.key)
        used = payload.used
        one = ir.Constant(used.type, 1)
        used = self._builder.sub(used, one)
        payload.used = self._builder.sub(used, one)
        if do_resize:
            self.downsize(used)
        self.set_dirty(True)

    
    def _remove_key(self, payload, item, h, do_resize = (True,)):
        context = self._context
        builder = self._builder
        (found, i) = payload._lookup(item, h)
        builder.if_then(found)
        entry = payload.get_entry(i)
        self._remove_entry(payload, entry, do_resize)
        None(None, None)

    
    def add(self, item, do_resize = (True,)):
        context = self._context
        builder = self._builder
        payload = self.payload
        h = get_hash_value(context, builder, self._ty.dtype, item)
        self._add_key(payload, item, h, do_resize)

    
    def add_pyapi(self, pyapi, item, do_resize = (True,)):
        '''A version of .add for use inside functions following Python calling
        convention.
        '''
        context = self._context
        builder = self._builder
        payload = self.payload
        h = self._pyapi_get_hash_value(pyapi, context, builder, item)
        self._add_key(payload, item, h, do_resize)

    
    def _pyapi_get_hash_value(self, pyapi, context, builder, item):
        '''Python API compatible version of `get_hash_value()`.
        '''
        argtypes = [
            self._ty.dtype]
        resty = types.intp
        
        def wrapper(val):
            return _get_hash_value_intrinsic(val)

        args = [
            item]
    # WARNING: Decompyle incomplete

    
    def contains(self, item):
        context = self._context
        builder = self._builder
        payload = self.payload
        h = get_hash_value(context, builder, self._ty.dtype, item)
        (found, i) = payload._lookup(item, h)
        return found

    
    def discard(self, item):
        context = self._context
        builder = self._builder
        payload = self.payload
        h = get_hash_value(context, builder, self._ty.dtype, item)
        found = self._remove_key(payload, item, h)
        return found

    
    def pop(self):
        context = self._context
        builder = self._builder
        lty = context.get_value_type(self._ty.dtype)
        key = cgutils.alloca_once(builder, lty)
        payload = self.payload
        entry = payload._next_entry()
        builder.store(entry.key, key)
        self._remove_entry(payload, entry, do_decref = False)
        None(None, None)

    
    def clear(self):
        context = self._context
        builder = self._builder
        intp_t = context.get_value_type(types.intp)
        minsize = ir.Constant(intp_t, MINSIZE)
        self._replace_payload(minsize)
        self.set_dirty(True)

    
    def copy(self):
