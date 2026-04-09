# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: externals.pyc (Python 3.11)

'''
Register external C functions necessary for Numba code generation.
'''
import sys
from llvmlite import ir
from llvmlite.binding import binding as ll
from numba.core import utils, intrinsics
from numba import _helperlib

def _add_missing_symbol(symbol, addr):
    '''Add missing symbol into LLVM internal symtab
    '''
    if not ll.address_of_symbol(symbol):
        ll.add_symbol(symbol, addr)
        return None


def _get_msvcrt_symbol(symbol):
    '''
    Under Windows, look up a symbol inside the C runtime
    and return the raw pointer value as an integer.
    '''
    cdll = cdll
    cast = cast
    c_void_p = c_void_p
    import ctypes
    f = getattr(cdll.msvcrt, symbol)
    return cast(f, c_void_p).value


def compile_multi3(context):
    '''
    Compile the multi3() helper function used by LLVM
    for 128-bit multiplication on 32-bit platforms.
    '''
    codegen = context.codegen()
    library = codegen.create_library('multi3')
    ir_mod = library.create_ir_module('multi3')
    i64 = ir.IntType(64)
    i128 = ir.IntType(128)
    lower_mask = ir.Constant(i64, 0xFFFFFFFF)
    _32 = ir.Constant(i64, 32)
    _64 = ir.Constant(i128, 64)
    fn_type = ir.FunctionType(i128, [
        i128,
        i128])
    fn = ir.Function(ir_mod, fn_type, name = 'multi3')
    (a, b) = fn.args
    bb = fn.append_basic_block()
    builder = ir.IRBuilder(bb)
    al = builder.trunc(a, i64)
    bl = builder.trunc(b, i64)
    ah = builder.trunc(builder.ashr(a, _64), i64)
    bh = builder.trunc(builder.ashr(b, _64), i64)
    rl = builder.mul(builder.and_(al, lower_mask), builder.and_(bl, lower_mask))
    t = builder.lshr(rl, _32)
    rl = builder.and_(rl, lower_mask)
    t = builder.add(t, builder.mul(builder.lshr(al, _32), builder.and_(bl, lower_mask)))
    rl = builder.add(rl, builder.shl(t, _32))
    rh = builder.lshr(t, _32)
    t = builder.lshr(rl, _32)
    rl = builder.and_(rl, lower_mask)
    t = builder.add(t, builder.mul(builder.lshr(bl, _32), builder.and_(al, lower_mask)))
    rl = builder.add(rl, builder.shl(t, _32))
    rh = builder.add(rh, builder.lshr(t, _32))
    rh = builder.add(rh, builder.mul(builder.lshr(al, _32), builder.lshr(bl, _32)))
    rh = builder.add(rh, builder.mul(bh, al))
    rh = builder.add(rh, builder.mul(bl, ah))
    r = builder.zext(rl, i128)
    r = builder.add(r, builder.shl(builder.zext(rh, i128), _64))
    builder.ret(r)
    library.add_ir_module(ir_mod)
    library.finalize()
    return library


class _Installer(object):
    _installed = False
    
    def install(self, context):
        '''
        Install the functions into LLVM.  This only needs to be done once,
        as the mappings are persistent during the process lifetime.
        '''
        if not self._installed:
            self._do_install(context)
            self._installed = True
            return None



class _ExternalMathFunctions(_Installer):
    '''
    Map the math functions from the C runtime library into the LLVM
    execution environment.
    '''
    
    def _do_install(self, context):
        is32bit = utils.MACHINE_BITS == 32
        c_helpers = _helperlib.c_helpers
        if sys.platform.startswith('win32') and is32bit:
            ftol = _get_msvcrt_symbol('_ftol')
            _add_missing_symbol('_ftol2', ftol)
        elif sys.platform.startswith('linux') and is32bit:
            _add_missing_symbol('__fixunsdfdi', c_helpers['fptoui'])
            _add_missing_symbol('__fixunssfdi', c_helpers['fptouif'])
    # WARNING: Decompyle incomplete


c_math_functions = _ExternalMathFunctions()
