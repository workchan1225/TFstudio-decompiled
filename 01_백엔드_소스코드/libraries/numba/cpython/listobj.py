# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: listobj.pyc (Python 3.11)

'''
Support for native homogeneous lists.
'''
import math
import operator
from functools import cached_property
from llvmlite import ir
from numba.core import types, typing, errors, cgutils, config
from numba.core.imputils import lower_builtin, lower_cast, iternext_impl, impl_ret_borrowed, impl_ret_new_ref, impl_ret_untracked, RefType
from numba.core.extending import overload_method, overload
from numba.misc import quicksort
from numba.cpython import slicing
from numba import literal_unroll

def get_list_payload(context, builder, list_type, value):
    '''
    Given a list value and type, get its payload structure (as a
    reference, so that mutations are seen by all).
    '''
    payload_type = types.ListPayload(list_type)
    payload = context.nrt.meminfo_data(builder, value.meminfo)
    ptrty = context.get_data_type(payload_type).as_pointer()
    payload = builder.bitcast(payload, ptrty)
    return context.make_data_helper(builder, payload_type, ref = payload)


def get_itemsize(context, list_type):
    '''
    Return the item size for the given list type.
    '''
    llty = context.get_data_type(list_type.dtype)
    return context.get_abi_sizeof(llty)


class _ListPayloadMixin(object):
    size = (lambda self: self._payload.size)()
    size = (lambda self, value: self._payload.size = value)()
    dirty = (lambda self: self._payload.dirty)()
    data = (lambda self: self._payload._get_ptr_by_name('data'))()
    
    def _gep(self, idx):
        return cgutils.gep(self._builder, self.data, idx)

    
    def getitem(self, idx):
        ptr = self._gep(idx)
        data_item = self._builder.load(ptr)
        return self._datamodel.from_data(self._builder, data_item)

    
    def fix_index(self, idx):
        '''
        Fix negative indices by adding the size to them.  Positive
        indices are left untouched.
        '''
        is_negative = self._builder.icmp_signed('<', idx, ir.Constant(idx.type, 0))
        wrapped_index = self._builder.add(idx, self.size)
        return self._builder.select(is_negative, wrapped_index, idx)

    
    def is_out_of_bounds(self, idx):
        '''
        Return whether the index is out of bounds.
        '''
        underflow = self._builder.icmp_signed('<', idx, ir.Constant(idx.type, 0))
        overflow = self._builder.icmp_signed('>=', idx, self.size)
        return self._builder.or_(underflow, overflow)

    
    def clamp_index(self, idx):
