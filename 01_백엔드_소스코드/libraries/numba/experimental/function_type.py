# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function_type.pyc (Python 3.11)

'''Provides Numba type, FunctionType, that makes functions as
instances of a first-class function type.
'''
from functools import partial
from numba.extending import typeof_impl
from numba.extending import models, register_model
from numba.extending import unbox, NativeValue, box
from numba.core.imputils import lower_constant, lower_cast
from numba.core.ccallback import CFunc
from numba.core import cgutils
from llvmlite import ir
from numba.core import types, errors
from numba.core.types import FunctionType, UndefinedFunctionType, FunctionPrototype, WrapperAddressProtocol
from numba.core.dispatcher import Dispatcher
typeof_function_type = (lambda val, c: if isinstance(val, CFunc):
sig = val._sigelif isinstance(val, WrapperAddressProtocol):
sig = val.signature()else:
raise NotImplementedError(f'''function type from {type(val).__name__}''')FunctionType(sig))()()
FunctionProtoModel = <NODE:12>()
FunctionModel = <NODE:12>()()
lower_constant_dispatcher = (lambda context, builder, typ, pyval: context.add_dynamic_addr(builder, id(pyval), info = type(pyval).__name__))()
lower_constant_function_type = (lambda context, builder, typ, pyval: typ = typ.get_precise()if isinstance(pyval, CFunc):
addr = pyval._wrapper_addresssfunc = cgutils.create_struct_proxy(typ)(context, builder)sfunc.c_addr = context.add_dynamic_addr(builder, addr, info = str(typ))sfunc.py_addr = context.add_dynamic_addr(builder, id(pyval), info = type(pyval).__name__)sfunc._getvalue()if None(pyval, Dispatcher):
sfunc = cgutils.create_struct_proxy(typ)(context, builder)sfunc.py_addr = context.add_dynamic_addr(builder, id(pyval), info = type(pyval).__name__)sfunc._getvalue()# WARNING: Decompyle incomplete
)()

def _get_wrapper_address(func, sig):
    '''Return the address of a compiled cfunc wrapper function of `func`.

    Warning: The compiled function must be compatible with the given
    signature `sig`. If it is not, then result of calling the compiled
    function is undefined. The compatibility is ensured when passing
    in a first-class function to a Numba njit compiled function either
    as an argument or via namespace scoping.

    Parameters
    ----------
    func : object
      A Numba cfunc or jit decoreated function or an object that
      implements the wrapper address protocol (see note below).
    sig : Signature
      The expected function signature.

    Returns
    -------
    addr : int
      An address in memory (pointer value) of the compiled function
      corresponding to the specified signature.

    Note: wrapper address protocol
    ------------------------------

    An object implements the wrapper address protocol iff the object
    provides a callable attribute named __wrapper_address__ that takes
    a Signature instance as the argument, and returns an integer
    representing the address or pointer value of a compiled function
    for the given signature.

    '''
    if not sig.is_precise():
        addr = -1
    elif hasattr(func, '__wrapper_address__'):
        addr = func.__wrapper_address__()
# WARNING: Decompyle incomplete


def _get_jit_address(func, sig):
    '''Similar to ``_get_wrapper_address()`` but get the `.jit_addr` instead.
    '''
    if isinstance(func, Dispatcher):
        cres = func.get_compile_result(sig)
        jit_name = cres.fndesc.llvm_func_name
        addr = cres.library.get_pointer_to_function(jit_name)
    else:
        addr = 0
    if not isinstance(addr, int):
        raise TypeError(f'''jit address must be integer, got {type(addr)} instance''')
    return addr


def _lower_get_address(context, builder, func, sig, failure_mode, *, function_name):
    '''Low-level call to <function_name>(func, sig).

    When calling this function, GIL must be acquired.
    '''
    pyapi = context.get_python_api(builder)
    modname = context.insert_const_string(builder.module, __name__)
    numba_mod = pyapi.import_module(modname)
    numba_func = pyapi.object_getattr_string(numba_mod, function_name)
    pyapi.decref(numba_mod)
    sig_obj = pyapi.unserialize(pyapi.serialize_object(sig))
    addr = pyapi.call_function_objargs(numba_func, (func, sig_obj))
    if failure_mode != 'ignore':
        builder.if_then(cgutils.is_null(builder, addr), likely = False)
        if failure_mode == 'return_exc':
            context.call_conv.return_exc(builder)
        elif failure_mode == 'return_null':
            builder.ret(pyapi.get_null_object())
        else:
            raise NotImplementedError(failure_mode)
        None(None, None)
    else:
        with None:
            if not None:
                pass
    return addr

lower_get_wrapper_address = partial(_lower_get_address, function_name = '_get_wrapper_address')
lower_get_jit_address = partial(_lower_get_address, function_name = '_get_jit_address')
unbox_function_type = (lambda typ, obj, c: typ = typ.get_precise()sfunc = cgutils.create_struct_proxy(typ)(c.context, c.builder)addr = lower_get_wrapper_address(c.context, c.builder, obj, typ.signature, failure_mode = 'return_null')sfunc.c_addr = c.pyapi.long_as_voidptr(addr)c.pyapi.decref(addr)llty = c.context.get_value_type(types.voidptr)sfunc.py_addr = c.builder.ptrtoint(obj, llty)addr = lower_get_jit_address(c.context, c.builder, obj, typ.signature, failure_mode = 'return_null')sfunc.jit_addr = c.pyapi.long_as_voidptr(addr)c.pyapi.decref(addr)NativeValue(sfunc._getvalue()))()
box_function_type = (lambda typ, val, c: typ = typ.get_precise()sfunc = cgutils.create_struct_proxy(typ)(c.context, c.builder, value = val)pyaddr_ptr = cgutils.alloca_once(c.builder, c.pyapi.pyobj)raw_ptr = c.builder.inttoptr(sfunc.py_addr, c.pyapi.pyobj)c.builder.if_then(cgutils.is_null(c.builder, raw_ptr), likely = False)cstr = f'''first-class function {typ} parent object not set'''c.pyapi.err_set_string('PyExc_MemoryError', cstr)c.builder.ret(c.pyapi.get_null_object())None(None, None))()
lower_cast_function_type_to_function_type = (lambda context, builder, fromty, toty, val: val)()
lower_cast_dispatcher_to_function_type = (lambda context, builder, fromty, toty, val: toty = toty.get_precise()sig = toty.signaturedispatcher = fromty.dispatcherllvoidptr = context.get_value_type(types.voidptr)sfunc = cgutils.create_struct_proxy(toty)(context, builder)sfunc.py_addr = builder.ptrtoint(val, llvoidptr)try:
cres = dispatcher.get_compile_result(sig)except errors.NumbaError:
cres = None# WARNING: Decompyle incomplete
)()
