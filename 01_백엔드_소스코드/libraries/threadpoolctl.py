# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: threadpoolctl.pyc (Python 3.11)

'''threadpoolctl

This module provides utilities to introspect native libraries that relies on
thread pools (notably BLAS and OpenMP implementations) and dynamically set the
maximal number of threads they can use.
'''
import os
import re
import sys
import ctypes
import itertools
import textwrap
from typing import final
import warnings
from ctypes.util import find_library
from abc import ABC, abstractmethod
from functools import lru_cache
from contextlib import ContextDecorator
__version__ = '3.6.0'
__all__ = [
    'threadpool_limits',
    'threadpool_info',
    'ThreadpoolController',
    'LibController',
    'register']
os.environ.setdefault('KMP_DUPLICATE_LIB_OK', 'True')
_SYSTEM_UINT = ctypes.c_uint64 if sys.maxsize > 0x100000000 else ctypes.c_uint32
_SYSTEM_UINT_HALF = ctypes.c_uint32 if sys.maxsize > 0x100000000 else ctypes.c_uint16

class _dl_phdr_info(ctypes.Structure):
    _fields_ = [
        ('dlpi_addr', _SYSTEM_UINT),
        ('dlpi_name', ctypes.c_char_p),
        ('dlpi_phdr', ctypes.c_void_p),
        ('dlpi_phnum', _SYSTEM_UINT_HALF)]


try:
    _RTLD_NOLOAD = os.RTLD_NOLOAD
except AttributeError:
    _RTLD_NOLOAD = ctypes.DEFAULT_MODE


class LibController(ABC):
    '''Abstract base class for the individual library controllers

    A library controller must expose the following class attributes:
        - user_api : str
            Usually the name of the library or generic specification the library
            implements, e.g. "blas" is a specification with different implementations.
        - internal_api : str
            Usually the name of the library or concrete implementation of some
            specification, e.g. "openblas" is an implementation of the "blas"
            specification.
        - filename_prefixes : tuple
            Possible prefixes of the shared library\'s filename that allow to
            identify the library. e.g. "libopenblas" for libopenblas.so.

    and implement the following methods: `get_num_threads`, `set_num_threads` and
    `get_version`.

    Threadpoolctl loops through all the loaded shared libraries and tries to match
    the filename of each library with the `filename_prefixes`. If a match is found, a
    controller is instantiated and a handler to the library is stored in the `dynlib`
    attribute as a `ctypes.CDLL` object. It can be used to access the necessary symbols
    of the shared library to implement the above methods.

    The following information will be exposed in the info dictionary:
      - user_api : standardized API, if any, or a copy of internal_api.
      - internal_api : implementation-specific API.
      - num_threads : the current thread limit.
      - prefix : prefix of the shared library\'s filename.
      - filepath : path to the loaded shared library.
      - version : version of the library (if available).

    In addition, each library controller may expose internal API specific entries. They
    must be set as attributes in the `set_additional_attributes` method.
    '''
    __init__ = (lambda self = final, *, filepath: self.parent = parentself.prefix = prefixself.filepath = filepathself.dynlib = ctypes.CDLL(filepath, mode = _RTLD_NOLOAD)(self._symbol_prefix, self._symbol_suffix) = self._find_affixes()self.version = self.get_version()self.set_additional_attributes())()
    
    def info(self):
        '''Return relevant info wrapped in a dict'''
        pass
    # WARNING: Decompyle incomplete

    
    def set_additional_attributes(self):
        '''Set additional attributes meant to be exposed in the info dict'''
        pass

    num_threads = (lambda self: self.get_num_threads())()
    get_num_threads = (lambda self: pass)()
    set_num_threads = (lambda self, num_threads: pass)()
    get_version = (lambda self: pass)()
    
    def _find_affixes(self):
        '''Return the affixes for the symbols of the shared library'''
        return ('', '')

    
    def _get_symbol(self, name):
        '''Return the symbol of the shared library accounding for the affixes'''
        return getattr(self.dynlib, f'''{self._symbol_prefix}{name}{self._symbol_suffix}''', None)



class OpenBLASController(LibController):
    '''Controller class for OpenBLAS'''
    user_api = 'blas'
    internal_api = 'openblas'
    filename_prefixes = ('libopenblas', 'libblas', 'libscipy_openblas')
    _symbol_prefixes = ('', 'scipy_')
    _symbol_suffixes = ('', '64_', '_64')
    check_symbols = (lambda .0: pass# WARNING: Decompyle incomplete
)(itertools.product(_symbol_prefixes, _symbol_suffixes)())
    
    def _find_affixes(self):
        for prefix, suffix in itertools.product(self._symbol_prefixes, self._symbol_suffixes):
            if hasattr(self.dynlib, f'''{prefix}openblas_get_num_threads{suffix}'''):
                
                return None, (prefix, suffix)
            return None

    
    def set_additional_attributes(self):
        self.threading_layer = self._get_threading_layer()
        self.architecture = self._get_architecture()

    
    def get_num_threads(self):
        get_num_threads_func = self._get_symbol('openblas_get_num_threads')
    # WARNING: Decompyle incomplete

    
    def set_num_threads(self, num_threads):
        set_num_threads_func = self._get_symbol('openblas_set_num_threads')
    # WARNING: Decompyle incomplete

    
    def get_version(self):
        get_version_func = self._get_symbol('openblas_get_config')
    # WARNING: Decompyle incomplete

    
    def _get_threading_layer(self):
        '''Return the threading layer of OpenBLAS'''
        get_threading_layer_func = self._get_symbol('openblas_get_parallel')
    # WARNING: Decompyle incomplete

    
    def _get_architecture(self):
        '''Return the architecture detected by OpenBLAS'''
        get_architecture_func = self._get_symbol('openblas_get_corename')
    # WARNING: Decompyle incomplete



class BLISController(LibController):
    '''Controller class for BLIS'''
    user_api = 'blas'
    internal_api = 'blis'
    filename_prefixes = ('libblis', 'libblas')
    check_symbols = ('bli_thread_get_num_threads', 'bli_thread_set_num_threads', 'bli_info_get_version_str', 'bli_info_get_enable_openmp', 'bli_info_get_enable_pthreads', 'bli_arch_query_id', 'bli_arch_string')
    
    def set_additional_attributes(self):
        self.threading_layer = self._get_threading_layer()
        self.architecture = self._get_architecture()

    
    def get_num_threads(self):
        get_func = getattr(self.dynlib, 'bli_thread_get_num_threads', (lambda : pass))
        num_threads = get_func()
        return 1 if num_threads == -1 else num_threads

    
    def set_num_threads(self, num_threads):
        set_func = getattr(self.dynlib, 'bli_thread_set_num_threads', (lambda num_threads: pass))
        return set_func(num_threads)

    
    def get_version(self):
        get_version_ = getattr(self.dynlib, 'bli_info_get_version_str', None)
    # WARNING: Decompyle incomplete

    
    def _get_threading_layer(self):
        '''Return the threading layer of BLIS'''
        if getattr(self.dynlib, 'bli_info_get_enable_openmp', (lambda : False))():
            return 'openmp'
        if getattr(self.dynlib, 'bli_info_get_enable_pthreads', (lambda : False))():
            return 'pthreads'

    
    def _get_architecture(self):
        '''Return the architecture detected by BLIS'''
        bli_arch_query_id = getattr(self.dynlib, 'bli_arch_query_id', None)
        bli_arch_string = getattr(self.dynlib, 'bli_arch_string', None)
    # WARNING: Decompyle incomplete



class FlexiBLASController(LibController):
    pass
# WARNING: Decompyle incomplete


class MKLController(LibController):
    '''Controller class for MKL'''
    user_api = 'blas'
    internal_api = 'mkl'
    filename_prefixes = ('libmkl_rt', 'mkl_rt', 'libblas')
    check_symbols = ('MKL_Get_Max_Threads', 'MKL_Set_Num_Threads', 'MKL_Get_Version_String', 'MKL_Set_Threading_Layer')
    
    def set_additional_attributes(self):
        self.threading_layer = self._get_threading_layer()

    
    def get_num_threads(self):
        get_func = getattr(self.dynlib, 'MKL_Get_Max_Threads', (lambda : pass))
        return get_func()

    
    def set_num_threads(self, num_threads):
        set_func = getattr(self.dynlib, 'MKL_Set_Num_Threads', (lambda num_threads: pass))
        return set_func(num_threads)

    
    def get_version(self):
        if not hasattr(self.dynlib, 'MKL_Get_Version_String'):
            return None
        res = None.create_string_buffer(200)
        self.dynlib.MKL_Get_Version_String(res, 200)
        version = res.value.decode('utf-8')
        group = re.search('Version ([^ ]+) ', version)
    # WARNING: Decompyle incomplete

    
    def _get_threading_layer(self):
        '''Return the threading layer of MKL'''
        set_threading_layer = getattr(self.dynlib, 'MKL_Set_Threading_Layer', (lambda layer: -1))
        layer_map = {
            0: 'intel',
            1: 'sequential',
            2: 'pgi',
            3: 'gnu',
            4: 'tbb',
            -1: 'not specified' }
        return layer_map[set_threading_layer(-1)]



class OpenMPController(LibController):
    '''Controller class for OpenMP'''
    user_api = 'openmp'
    internal_api = 'openmp'
    filename_prefixes = ('libiomp', 'libgomp', 'libomp', 'vcomp')
    check_symbols = ('omp_get_max_threads', 'omp_get_num_threads')
    
    def get_num_threads(self):
        get_func = getattr(self.dynlib, 'omp_get_max_threads', (lambda : pass))
        return get_func()

    
    def set_num_threads(self, num_threads):
        set_func = getattr(self.dynlib, 'omp_set_num_threads', (lambda num_threads: pass))
        return set_func(num_threads)

    
    def get_version(self):
        pass


_ALL_CONTROLLERS = [
    OpenBLASController,
    BLISController,
    MKLController,
    OpenMPController,
    FlexiBLASController]
_ALL_USER_APIS = set((lambda .0: pass# WARNING: Decompyle incomplete
)(_ALL_CONTROLLERS()))
_ALL_INTERNAL_APIS = _ALL_CONTROLLERS()
_ALL_PREFIXES = set((lambda .0: pass# WARNING: Decompyle incomplete
)(_ALL_CONTROLLERS()))
_ALL_BLAS_LIBRARIES = _ALL_CONTROLLERS()
_ALL_OPENMP_LIBRARIES = OpenMPController.filename_prefixes

def register(controller):
    '''Register a new controller'''
    _ALL_CONTROLLERS.append(controller)
    _ALL_USER_APIS.append(controller.user_api)
    _ALL_INTERNAL_APIS.append(controller.internal_api)
    _ALL_PREFIXES.extend(controller.filename_prefixes)


def _format_docstring(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete

_realpath = (lambda filepath: os.path.realpath(filepath))()
threadpool_info = (lambda : ThreadpoolController().info())()

class _ThreadpoolLimiter:
    '''The guts of ThreadpoolController.limit

    Refer to the docstring of ThreadpoolController.limit for more details.

    It will only act on the library controllers held by the provided `controller`.
    Using the default constructor sets the limits right away such that it can be used as
    a callable. Setting the limits can be delayed by using the `wrap` class method such
    that it can be used as a decorator.
    '''
    
    def __init__(self = None, controller = {
        'limits': None,
        'user_api': None }, *, limits, user_api):
        self._controller = controller
        (self._limits, self._user_api, self._prefixes) = self._check_params(limits, user_api)
        self._original_info = self._controller.info()
        self._set_threadpool_limits()

    
    def __enter__(self):
        return self

    
    def __exit__(self, type, value, traceback):
        self.restore_original_limits()

    wrap = (lambda cls = classmethod, controller = {
        'limits': None,
        'user_api': None }, *, limits, user_api: _ThreadpoolLimiterDecorator(controller = controller, limits = limits, user_api = user_api))()
    
    def restore_original_limits(self):
        '''Set the limits back to their original values'''
        for lib_controller, original_info in zip(self._controller.lib_controllers, self._original_info):
            lib_controller.set_num_threads(original_info['num_threads'])
            return None

    unregister = restore_original_limits
    
    def get_original_num_threads(self):
        '''Original num_threads from before calling threadpool_limits

        Return a dict `{user_api: num_threads}`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _check_params(self, limits, user_api):
        '''Suitable values for the _limits, _user_api and _prefixes attributes'''
        pass
    # WARNING: Decompyle incomplete

    
    def _set_threadpool_limits(self):
        '''Change the maximal number of threads in selected thread pools.

        Return a list with all the supported libraries that have been found
        matching `self._prefixes` and `self._user_api`.
        '''
        pass
    # WARNING: Decompyle incomplete



class _ThreadpoolLimiterDecorator(ContextDecorator, _ThreadpoolLimiter):
    '''Same as _ThreadpoolLimiter but to be used as a decorator'''
    
    def __init__(self = None, controller = {
        'limits': None,
        'user_api': None }, *, limits, user_api):
        (self._limits, self._user_api, self._prefixes) = self._check_params(limits, user_api)
        self._controller = controller

    
    def __enter__(self):
        self._original_info = self._controller.info()
        self._set_threadpool_limits()
        return self


threadpool_limits = <NODE:12>()

class ThreadpoolController:
    '''Collection of LibController objects for all loaded supported libraries

    Attributes
    ----------
    lib_controllers : list of `LibController` objects
        The list of library controllers of all loaded supported libraries.
    '''
    _system_libraries = dict()
    
    def __init__(self):
        self.lib_controllers = []
        self._load_libraries()
        self._warn_if_incompatible_openmp()

    _from_controllers = (lambda cls, lib_controllers: new_controller = cls.__new__(cls)new_controller.lib_controllers = lib_controllersnew_controller)()
    
    def info(self):
        '''Return lib_controllers info as a list of dicts'''
        return self.lib_controllers()

    
    def select(self, **kwargs):
        '''Return a ThreadpoolController containing a subset of its current
        library controllers

        It will select all libraries matching at least one pair (key, value) from kwargs
        where key is an entry of the library info dict (like "user_api", "internal_api",
        "prefix", ...) and value is the value or a list of acceptable values for that
        entry.

        For instance, `ThreadpoolController().select(internal_api=["blis", "openblas"])`
        will select all library controllers whose internal_api is either "blis" or
        "openblas".
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_params_for_sequential_blas_under_openmp(self):
        '''Return appropriate params to use for a sequential BLAS call in an OpenMP loop

        This function takes into account the unexpected behavior of OpenBLAS with the
        OpenMP threading layer.
        '''
        if self.select(internal_api = 'openblas', threading_layer = 'openmp').lib_controllers:
            return {
                'limits': None,
                'user_api': None }
        return {
            'limits': None,
            'user_api': 'blas' }

    limit = (lambda self = ', '.join(USER_APIS = (lambda .0: pass# WARNING: Decompyle incomplete
)(_ALL_USER_APIS()), BLAS_LIBS = ', '.join(_ALL_BLAS_LIBRARIES), OPENMP_LIBS = ', '.join(_ALL_OPENMP_LIBRARIES)), *, limits: _ThreadpoolLimiter(self, limits = limits, user_api = user_api))()
    wrap = (lambda self = ', '.join(USER_APIS = (lambda .0: pass# WARNING: Decompyle incomplete
)(_ALL_USER_APIS()), BLAS_LIBS = ', '.join(_ALL_BLAS_LIBRARIES), OPENMP_LIBS = ', '.join(_ALL_OPENMP_LIBRARIES)), *, limits: _ThreadpoolLimiter.wrap(self, limits = limits, user_api = user_api))()
    
    def __len__(self):
        return len(self.lib_controllers)

    
    def _load_libraries(self):
        '''Loop through loaded shared libraries and store the supported ones'''
        if sys.platform == 'darwin':
            self._find_libraries_with_dyld()
            return None
        if None.platform == 'win32':
            self._find_libraries_with_enum_process_module_ex()
            return None
        if None in sys.modules:
            self._find_libraries_pyodide()
            return None
        None._find_libraries_with_dl_iterate_phdr()

    
    def _find_libraries_with_dl_iterate_phdr(self):
        '''Loop through loaded libraries and return binders on supported ones

        This function is expected to work on POSIX system only.
        This code is adapted from code by Intel developer @anton-malakhov
        available at https://github.com/IntelPython/smp

        Copyright (c) 2017, Intel Corporation published under the BSD 3-Clause
        license
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _find_libraries_with_dyld(self):
        '''Loop through loaded libraries and return binders on supported ones

        This function is expected to work on OSX system only
        '''
        libc = self._get_libc()
        if not hasattr(libc, '_dyld_image_count'):
            warnings.warn('Could not find _dyld_image_count in the C standard library.', RuntimeWarning)
            return []
        n_dyld = None._dyld_image_count()
        libc._dyld_get_image_name.restype = ctypes.c_char_p
        for i in range(n_dyld):
            filepath = ctypes.string_at(libc._dyld_get_image_name(i))
            filepath = filepath.decode('utf-8')
            self._make_controller_from_path(filepath)
            return None

    
    def _find_libraries_with_enum_process_module_ex(self):
        '''Loop through loaded libraries and return binders on supported ones

        This function is expected to work on windows system only.
        This code is adapted from code by Philipp Hagemeister @phihag available
        at https://stackoverflow.com/questions/17474574
        '''
        DWORD = DWORD
        HMODULE = HMODULE
        MAX_PATH = MAX_PATH
        import ctypes.wintypes
        PROCESS_QUERY_INFORMATION = 1024
        PROCESS_VM_READ = 16
        LIST_LIBRARIES_ALL = 3
        ps_api = self._get_windll('Psapi')
        kernel_32 = self._get_windll('kernel32')
        h_process = kernel_32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, os.getpid())
        if not h_process:
            raise OSError(f'''Could not open PID {os.getpid()}''')
        
        try:
            buf_count = 256
            needed = DWORD()
            buf = HMODULE * buf_count()
            buf_size = ctypes.sizeof(buf)
            if not ps_api.EnumProcessModulesEx(h_process, ctypes.byref(buf), buf_size, ctypes.byref(needed), LIST_LIBRARIES_ALL):
                raise OSError('EnumProcessModulesEx failed')
            if buf_size >= needed.value:
                pass
            else:
                buf_count = needed.value // buf_size // buf_count
            count = needed.value // buf_size // buf_count
            h_modules = map(HMODULE, buf[:count])
            max_path = 10 * MAX_PATH
            buf = ctypes.create_unicode_buffer(max_path)
            n_size = DWORD()
            for h_module in h_modules:
                if not ps_api.GetModuleFileNameExW(h_process, h_module, ctypes.byref(buf), ctypes.byref(n_size)):
                    raise OSError('GetModuleFileNameEx failed')
                filepath = buf.value
                if len(filepath) == max_path:
                    warnings.warn(f'''Could not get the full path of a dynamic library (path too long). This library will be ignored and threadpoolctl might not be able to control or display information about all loaded libraries. Here\'s the truncated path: {filepath!r}''', RuntimeWarning)
                    continue
                self._make_controller_from_path(filepath)
                kernel_32.CloseHandle(h_process)
                return None
                kernel_32.CloseHandle(h_process)


    
    def _find_libraries_pyodide(self):
        '''Pyodide specific implementation for finding loaded libraries.

        Adapted from suggestion in https://github.com/joblib/threadpoolctl/pull/169#issuecomment-1946696449.

        One day, we may have a simpler solution. libc dl_iterate_phdr needs to
        be implemented in Emscripten and exposed in Pyodide, see
        https://github.com/emscripten-core/emscripten/issues/21354 for more
        details.
        '''
        
        try:
            LDSO = LDSO
            import pyodide_js._module
        except ImportError:
            warnings.warn('Unable to import LDSO from pyodide_js._module. This should never happen.')
            return None

        for filepath in LDSO.loadedLibsByName.as_object_map():
            if os.path.exists(filepath):
                self._make_controller_from_path(filepath)
            return None

    
    def _make_controller_from_path(self, filepath):
        '''Store a library controller if it is supported and selected'''
        pass
    # WARNING: Decompyle incomplete

    
    def _check_prefix(self, library_basename, filename_prefixes):
        '''Return the prefix library_basename starts with

        Return None if none matches.
        '''
        for prefix in filename_prefixes:
            if library_basename.startswith(prefix):
                
                return None, prefix
            return None

    
    def _warn_if_incompatible_openmp(self):
        '''Raise a warning if llvm-OpenMP and intel-OpenMP are both loaded'''
        prefixes = self.lib_controllers()
        msg = textwrap.dedent("\n            Found Intel OpenMP ('libiomp') and LLVM OpenMP ('libomp') loaded at\n            the same time. Both libraries are known to be incompatible and this\n            can cause random crashes or deadlocks on Linux when loaded in the\n            same Python program.\n            Using threadpoolctl may cause crashes or deadlocks. For more\n            information and possible workarounds, please see\n                https://github.com/joblib/threadpoolctl/blob/master/multiple_openmp.md\n            ")
        if 'libomp' in prefixes or 'libiomp' in prefixes:
            warnings.warn(msg, RuntimeWarning)
            return None
        return (lambda .0: [ lib_controller.prefix for lib_controller in .0 ])

    _get_libc = (lambda cls: libc = cls._system_libraries.get('libc')# WARNING: Decompyle incomplete
)()
    _get_windll = (lambda cls, dll_name: dll = cls._system_libraries.get(dll_name)# WARNING: Decompyle incomplete
)()


def _main():
    '''Commandline interface to display thread-pool information and exit.'''
    import argparse
    import importlib
    import json
    import sys
    parser = argparse.ArgumentParser(usage = 'python -m threadpoolctl -i numpy scipy.linalg xgboost', description = 'Display thread-pool information and exit.')
    parser.add_argument('-i', '--import', dest = 'modules', nargs = '*', default = (), help = 'Python modules to import before introspecting thread-pools.')
    parser.add_argument('-c', '--command', help = 'a Python statement to execute before introspecting thread-pools.')
    options = parser.parse_args(sys.argv[1:])
    for module in options.modules:
        importlib.import_module(module, package = None)
        except ImportError:
            print('WARNING: could not import', module, file = sys.stderr)
            continue
        if options.command:
            exec(options.command)
    print(json.dumps(threadpool_info(), indent = 2))

if __name__ == '__main__':
    _main()
    return None
