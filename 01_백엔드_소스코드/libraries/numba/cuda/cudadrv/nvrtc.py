# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nvrtc.pyc (Python 3.11)

from ctypes import byref, c_char, c_char_p, c_int, c_size_t, c_void_p, POINTER
from enum import IntEnum
from numba.core import config
from numba.cuda.cudadrv.error import NvrtcError, NvrtcCompilationError, NvrtcSupportError
import functools
import os
import threading
import warnings
nvrtc_program = c_void_p
nvrtc_result = c_int

class NvrtcResult(IntEnum):
    NVRTC_SUCCESS = 0
    NVRTC_ERROR_OUT_OF_MEMORY = 1
    NVRTC_ERROR_PROGRAM_CREATION_FAILURE = 2
    NVRTC_ERROR_INVALID_INPUT = 3
    NVRTC_ERROR_INVALID_PROGRAM = 4
    NVRTC_ERROR_INVALID_OPTION = 5
    NVRTC_ERROR_COMPILATION = 6
    NVRTC_ERROR_BUILTIN_OPERATION_FAILURE = 7
    NVRTC_ERROR_NO_NAME_EXPRESSIONS_AFTER_COMPILATION = 8
    NVRTC_ERROR_NO_LOWERED_NAMES_BEFORE_COMPILATION = 9
    NVRTC_ERROR_NAME_EXPRESSION_NOT_VALID = 10
    NVRTC_ERROR_INTERNAL_ERROR = 11

_nvrtc_lock = threading.Lock()

class NvrtcProgram:
    '''
    A class for managing the lifetime of nvrtcProgram instances. Instances of
    the class own an nvrtcProgram; when an instance is deleted, the underlying
    nvrtcProgram is destroyed using the appropriate NVRTC API.
    '''
    
    def __init__(self, nvrtc, handle):
        self._nvrtc = nvrtc
        self._handle = handle

    handle = (lambda self: self._handle)()
    
    def __del__(self):
        if self._handle:
            self._nvrtc.destroy_program(self)
            return None



class NVRTC:
    '''
    Provides a Pythonic interface to the NVRTC APIs, abstracting away the C API
    calls.

    The sole instance of this class is a process-wide singleton, similar to the
    NVVM interface. Initialization is protected by a lock and uses the standard
    (for Numba) open_cudalib function to load the NVRTC library.
    '''
    _PROTOTYPES = {
        'nvrtcVersion': (nvrtc_result, POINTER(c_int), POINTER(c_int)),
        'nvrtcCreateProgram': (nvrtc_result, nvrtc_program, c_char_p, c_char_p, c_int, POINTER(c_char_p), POINTER(c_char_p)),
        'nvrtcDestroyProgram': (nvrtc_result, POINTER(nvrtc_program)),
        'nvrtcCompileProgram': (nvrtc_result, nvrtc_program, c_int, POINTER(c_char_p)),
        'nvrtcGetPTXSize': (nvrtc_result, nvrtc_program, POINTER(c_size_t)),
        'nvrtcGetPTX': (nvrtc_result, nvrtc_program, c_char_p),
        'nvrtcGetCUBINSize': (nvrtc_result, nvrtc_program, POINTER(c_size_t)),
        'nvrtcGetCUBIN': (nvrtc_result, nvrtc_program, c_char_p),
        'nvrtcGetProgramLogSize': (nvrtc_result, nvrtc_program, POINTER(c_size_t)),
        'nvrtcGetProgramLog': (nvrtc_result, nvrtc_program, c_char_p) }
    __INSTANCE = None
    
    def __new__(cls):
        _nvrtc_lock
    # WARNING: Decompyle incomplete

    
    def get_version(self):
        '''
        Get the NVRTC version as a tuple (major, minor).
        '''
        major = c_int()
        minor = c_int()
        self.nvrtcVersion(byref(major), byref(minor))
        return (major.value, minor.value)

    
    def create_program(self, src, name):
        '''
        Create an NVRTC program with managed lifetime.
        '''
        if isinstance(src, str):
            src = src.encode()
        if isinstance(name, str):
            name = name.encode()
        handle = nvrtc_program()
        self.nvrtcCreateProgram(byref(handle), src, name, 0, None, None)
        return NvrtcProgram(self, handle)

    
    def compile_program(self, program, options):
        '''
        Compile an NVRTC program. Compilation may fail due to a user error in
        the source; this function returns ``True`` if there is a compilation
        error and ``False`` on success.
        '''
        encoded_options = options()
        option_pointers = encoded_options()
        c_options_type = c_char_p * len(options)
    # WARNING: Decompyle incomplete

    
    def destroy_program(self, program):
        '''
        Destroy an NVRTC program.
        '''
        self.nvrtcDestroyProgram(byref(program.handle))

    
    def get_compile_log(self, program):
        '''
        Get the compile log as a Python string.
        '''
        log_size = c_size_t()
        self.nvrtcGetProgramLogSize(program.handle, byref(log_size))
        log = c_char * log_size.value()
        self.nvrtcGetProgramLog(program.handle, log)
        return log.value.decode()

    
    def get_ptx(self, program):
        '''
        Get the compiled PTX as a Python string.
        '''
        ptx_size = c_size_t()
        self.nvrtcGetPTXSize(program.handle, byref(ptx_size))
        ptx = c_char * ptx_size.value()
        self.nvrtcGetPTX(program.handle, ptx)
        return ptx.value.decode()



def compile(src, name, cc):
    '''
    Compile a CUDA C/C++ source to PTX for a given compute capability.

    :param src: The source code to compile
    :type src: str
    :param name: The filename of the source (for information only)
    :type name: str
    :param cc: A tuple ``(major, minor)`` of the compute capability
    :type cc: tuple
    :return: The compiled PTX and compilation log
    :rtype: tuple
    '''
    nvrtc = NVRTC()
    program = nvrtc.create_program(src, name)
    (major, minor) = cc
    arch = f'''--gpu-architecture=compute_{major}{minor}'''
    include = f'''-I{config.CUDA_INCLUDE_PATH}'''
    cudadrv_path = os.path.dirname(os.path.abspath(__file__))
    numba_cuda_path = os.path.dirname(cudadrv_path)
    numba_include = f'''-I{numba_cuda_path}'''
    options = [
        arch,
        include,
        numba_include,
        '-rdc',
        'true']
    compile_error = nvrtc.compile_program(program, options)
    log = nvrtc.get_compile_log(program)
    if compile_error:
        msg = f'''NVRTC Compilation failure whilst compiling {name}:\n\n{log}'''
        raise NvrtcError(msg)
    if log:
        msg = f'''NVRTC log messages whilst compiling {name}:\n\n{log}'''
        warnings.warn(msg)
    ptx = nvrtc.get_ptx(program)
    return (ptx, log)
