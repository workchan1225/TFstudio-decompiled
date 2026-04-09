# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ccallback.pyc (Python 3.11)

'''
Implementation of compiled C callbacks (@cfunc).
'''
import ctypes
from functools import cached_property
from numba.core import compiler, registry
from numba.core.caching import NullCache, FunctionCache
from numba.core.dispatcher import _FunctionCompiler
from numba.core.typing import signature
from numba.core.typing.ctypes_utils import to_ctypes
from numba.core.compiler_lock import global_compiler_lock

class _CFuncCompiler(_FunctionCompiler):
    
    def _customize_flags(self, flags):
        flags.no_cpython_wrapper = True
        flags.no_cfunc_wrapper = False
        flags.no_compile = True
        flags.enable_pyobject = False
        if flags.force_pyobject:
            raise NotImplementedError('object mode not allowed in C callbacks')
        return flags



class CFunc(object):
    '''
    A compiled C callback, as created by the @cfunc decorator.
    '''
    _targetdescr = registry.cpu_target
    
    def __init__(self, pyfunc, sig, locals, options, pipeline_class = (compiler.Compiler,)):
        (args, return_type) = sig
    # WARNING: Decompyle incomplete

    
    def enable_caching(self):
        self._cache = FunctionCache(self._pyfunc)

    compile = (lambda self: cres = self._cache.load_overload(self._sig, self._targetdescr.target_context)# WARNING: Decompyle incomplete
)()
    
    def _compile_uncached(self):
        sig = self._sig
        return self._compiler.compile(sig.args, sig.return_type)

    native_name = (lambda self: self._wrapper_name)()
    address = (lambda self: self._wrapper_address)()
    cffi = (lambda self: import cffiffi = cffi.FFI()ffi.cast('void *', self.address))()
    ctypes = (lambda self: ctypes_args = self._sig.args()ctypes_restype = to_ctypes(self._sig.return_type)# WARNING: Decompyle incomplete
)()
    
    def inspect_llvm(self):
        '''
        Return the LLVM IR of the C callback definition.
        '''
        return self._library.get_llvm_str()

    cache_hits = (lambda self: self._cache_hits)()
    
    def __repr__(self):
        return f'''<Numba C callback {self.__qualname__!r}>'''

    
    def __call__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete
