# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: runtime.pyc (Python 3.11)

'''
CUDA Runtime wrapper.

This provides a very minimal set of bindings, since the Runtime API is not
really used in Numba except for querying the Runtime version.
'''
import ctypes
import functools
import sys
from numba.core import config
from numba.cuda.cudadrv.driver import ERROR_MAP, make_logger
from numba.cuda.cudadrv.error import CudaSupportError, CudaRuntimeError
from numba.cuda.cudadrv.libs import open_cudalib
from numba.cuda.cudadrv.rtapi import API_PROTOTYPES
from numba.cuda.cudadrv import enums

class CudaRuntimeAPIError(CudaRuntimeError):
    pass
# WARNING: Decompyle incomplete


class Runtime:
    '''
    Runtime object that lazily binds runtime API functions.
    '''
    
    def __init__(self):
        self.is_initialized = False

    
    def _initialize(self):
        global _logger
        _logger = make_logger()
        if config.DISABLE_CUDA:
            msg = 'CUDA is disabled due to setting NUMBA_DISABLE_CUDA=1 in the environment, or because CUDA is unsupported on 32-bit systems.'
            raise CudaSupportError(msg)
        self.lib = open_cudalib('cudart')
        self.is_initialized = True

    
    def __getattr__(self, fname):
        
        try:
            proto = API_PROTOTYPES[fname]
        except KeyError:
            raise AttributeError(fname)

        restype = proto[0]
        argtypes = proto[1:]
        if not self.is_initialized:
            self._initialize()
        libfn = self._find_api(fname)
        libfn.restype = restype
        libfn.argtypes = argtypes
        safe_call = self._wrap_api_call(fname, libfn)
        setattr(self, fname, safe_call)
        return safe_call

    
    def _wrap_api_call(self, fname, libfn):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_error(self, fname, retcode):
        if retcode != enums.CUDA_SUCCESS:
            errname = ERROR_MAP.get(retcode, 'cudaErrorUnknown')
            msg = f'''Call to {fname!s} results in {errname!s}'''
            _logger.error(msg)
            raise CudaRuntimeAPIError(retcode, msg)

    
    def _find_api(self, fname):
        pass
    # WARNING: Decompyle incomplete

    
    def get_version(self):
        '''
        Returns the CUDA Runtime version as a tuple (major, minor).
        '''
        rtver = ctypes.c_int()
        self.cudaRuntimeGetVersion(ctypes.byref(rtver))
        major = rtver.value // 1000
        minor = (rtver.value - major * 1000) // 10
        return (major, minor)

    
    def is_supported_version(self):
        '''
        Returns True if the CUDA Runtime is a supported version.
        '''
        return self.get_version() in self.supported_versions

    supported_versions = (lambda self: if sys.platform not in ('linux', 'win32') or config.MACHINE_BITS != 64:
())()

runtime = Runtime()

def get_version():
    '''
    Return the runtime version as a tuple of (major, minor)
    '''
    return runtime.get_version()
