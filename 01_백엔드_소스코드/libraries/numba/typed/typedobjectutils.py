# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typedobjectutils.pyc (Python 3.11)

''' Common compiler level utilities for typed dict and list. '''
import operator
import warnings
from llvmlite import ir
from numba.core import types, cgutils
from numba.core import typing
from numba.core.registry import cpu_target
from numba.core.typeconv import Conversion
from numba.core.extending import intrinsic
from numba.core.errors import TypingError, NumbaTypeSafetyWarning, NumbaTypeError

def _as_bytes(builder, ptr):
    '''Helper to do (void*)ptr
    '''
    return builder.bitcast(ptr, cgutils.voidptr_t)

_cast = (lambda typingctx, val, typ: 
def codegen(context, builder, signature, args):
(val, typ) = argscontext.nrt.incref(builder, signature.return_type, val)valcasted = typ.instance_type_sentry_safe_cast(val, casted)sig = casted(casted, typ)(sig, codegen))()

def _sentry_safe_cast(fromty, toty):
    '''Check and raise TypingError if *fromty* cannot be safely cast to *toty*
    '''
    pass
# WARNING: Decompyle incomplete


def _sentry_safe_cast_default(default, valty):
    '''Similar to _sentry_safe_cast but handle default value.
    '''
    pass
# WARNING: Decompyle incomplete

_nonoptional = (lambda typingctx, val: if not isinstance(val, types.Optional):
raise NumbaTypeError('expected an optional')
def codegen(context, builder, sig, args):
context.nrt.incref(builder, sig.return_type, args[0])args[0]casted = val.typesig = casted(casted)(sig, codegen))()

def _container_get_data(context, builder, container_ty, c):
    '''Helper to get the C list pointer in a numba containers.
    '''
    ctor = cgutils.create_struct_proxy(container_ty)
    conatainer_struct = ctor(context, builder, value = c)
    return conatainer_struct.data


def _container_get_meminfo(context, builder, container_ty, c):
    '''Helper to get the meminfo for a container
    '''
    ctor = cgutils.create_struct_proxy(container_ty)
    conatainer_struct = ctor(context, builder, value = c)
    return conatainer_struct.meminfo


def _get_incref_decref(context, module, datamodel, container_element_type):
    pass
# WARNING: Decompyle incomplete


def _get_equal(context, module, datamodel, container_element_type):
    pass
# WARNING: Decompyle incomplete
