# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: callconv.pyc (Python 3.11)

'''
Calling conventions for Numba-compiled functions.
'''
from collections import namedtuple
from collections.abc import Iterable
import itertools
import hashlib
from llvmlite import ir
from numba.core import types, cgutils, errors
from numba.core.base import PYOBJECT, GENERIC_POINTER
TryStatus = namedtuple('TryStatus', [
    'in_try',
    'excinfo'])
Status = namedtuple('Status', ('code', 'is_ok', 'is_none', 'is_error', 'is_stop_iteration', 'is_python_exc', 'is_user_exc', 'excinfoptr'))
int32_t = ir.IntType(32)
int64_t = ir.IntType(64)
errcode_t = int32_t

def _const_int(code):
    return ir.Constant(errcode_t, code)

RETCODE_OK = _const_int(0)
RETCODE_EXC = _const_int(-1)
RETCODE_NONE = _const_int(-2)
RETCODE_STOPIT = _const_int(-3)
FIRST_USEREXC = 1
RETCODE_USEREXC = _const_int(FIRST_USEREXC)

class BaseCallConv(object):
    
    def __init__(self, context):
        self.context = context

    
    def return_optional_value(self, builder, retty, valty, value):
        if valty == types.none:
            self.return_native_none(builder)
            return None
        if None == valty:
            optval = self.context.make_helper(builder, retty, value = value)
            validbit = cgutils.as_bool_bit(builder, optval.valid)
            builder.if_then(validbit)
            retval = self.context.get_return_value(builder, retty.type, optval.data)
            self.return_value(builder, retval)
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        self.return_native_none(builder)
        return None
        if not isinstance(valty, types.Optional):
            if valty != retty.type:
                value = self.context.cast(builder, value, fromty = valty, toty = retty.type)
            retval = self.context.get_return_value(builder, retty.type, value)
            self.return_value(builder, retval)
            return None
        raise None('returning {0} for {1}'.format(valty, retty))

    
    def return_native_none(self, builder):
        self._return_errcode_raw(builder, RETCODE_NONE)

    
    def return_exc(self, builder):
        self._return_errcode_raw(builder, RETCODE_EXC)

    
    def return_stop_iteration(self, builder):
        self._return_errcode_raw(builder, RETCODE_STOPIT)

    
    def get_return_type(self, ty):
        '''
        Get the actual type of the return argument for Numba type *ty*.
        '''
        restype = self.context.data_model_manager[ty].get_return_type()
        return restype.as_pointer()

    
    def init_call_helper(self, builder):
        '''
        Initialize and return a call helper object for the given builder.
        '''
        ch = self._make_call_helper(builder)
        builder._BaseCallConv__call_helper = ch
        return ch

    
    def _get_call_helper(self, builder):
        return builder._BaseCallConv__call_helper

    
    def unpack_exception(self, builder, pyapi, status):
        return pyapi.unserialize(status.excinfoptr)

    
    def raise_error(self, builder, pyapi, status):
