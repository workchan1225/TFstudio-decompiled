# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Expose top-level symbols that are safe for import *
'''
import platform
import re
import sys
import warnings

def _ensure_critical_deps():
    """
    Make sure the Python, NumPy and SciPy present are supported versions.
    This has to be done _before_ importing anything from Numba such that
    incompatible versions can be reported to the user. If this occurs _after_
    importing things from Numba and there's an issue in e.g. a Numba c-ext, a
    SystemError might have occurred which prevents reporting the likely cause of
    the problem (incompatible versions of critical dependencies).
    """
    
    def extract_version(mod):
        return tuple(map(int, mod.__version__.split('.')[:2]))

    PYVERSION = sys.version_info[:2]
    if PYVERSION < (3, 10):
        msg = f'''Numba needs Python 3.10 or greater. Got Python {PYVERSION[0]}.{PYVERSION[1]}.'''
        raise ImportError(msg)
    import numpy as np
    numpy_version = extract_version(np)
    if numpy_version < (1, 22):
        msg = f'''Numba needs NumPy 1.22 or greater. Got NumPy {numpy_version[0]}.{numpy_version[1]}.'''
        raise ImportError(msg)
    if numpy_version > (2, 3):
        msg = f'''Numba needs NumPy 2.3 or less. Got NumPy {numpy_version[0]}.{numpy_version[1]}.'''
        raise ImportError(msg)
    
    try:
        import scipy
        sp_version = extract_version(scipy)
        if sp_version < (1, 0):
            msg = f'''Numba requires SciPy version 1.0 or greater. Got SciPy {scipy.__version__}.'''
            raise ImportError(msg)
        return None
    except ImportError:
        return None


_ensure_critical_deps()
from _version import get_versions
from numba.misc.init_utils import generate_version_info
__version__ = get_versions()['version']
version_info = generate_version_info(__version__)
del get_versions
del generate_version_info
from numba.core import config
from numba.core import types, errors
from numba.misc.special import typeof, prange, pndindex, gdb, gdb_breakpoint, gdb_init, literally, literal_unroll
from numba.core.errors import *

types
from numba.core.types import *
from numba.core.decorators import cfunc, jit, njit, stencil, jit_module
jit = jit
njit = njit
stencil = stencil
jit_module = jit_module
import numba.core.types, core
from numba.np.ufunc import vectorize, guvectorize, threading_layer, get_num_threads, set_num_threads, set_parallel_chunksize, get_parallel_chunksize, get_thread_id
from numba.np.numpy_support import carray, farray, from_dtype
from numba import experimental
import numba.core.withcontexts as numba
from numba.core.withcontexts import objmode_context as objmode
from numba.core.withcontexts import parallel_chunksize
import numba.core.target_extension as numba
import numba.typed as numba

def test(argv, **kwds):
    runtests = _runtests
    import numba.testing
# WARNING: Decompyle incomplete

__all__ = '\n    cfunc\n    from_dtype\n    guvectorize\n    jit\n    experimental\n    njit\n    stencil\n    jit_module\n    typeof\n    prange\n    gdb\n    gdb_breakpoint\n    gdb_init\n    vectorize\n    objmode\n    literal_unroll\n    get_num_threads\n    set_num_threads\n    set_parallel_chunksize\n    get_parallel_chunksize\n    parallel_chunksize\n    '.split() + types.__all__ + errors.__all__
_min_llvmlite_version = (0, 46, 0)
_min_llvm_version = (14, 0, 0)

def _ensure_llvm():
    '''
    Make sure llvmlite is operational.
    '''
    import warnings
    import llvmlite
    regex = re.compile('(\\d+)\\.(\\d+).(\\d+)')
    m = regex.match(llvmlite.__version__)
    if m:
        ver = tuple(map(int, m.groups()))
        if ver < _min_llvmlite_version:
            msg = 'Numba requires at least version %d.%d.%d of llvmlite.\nInstalled version is %s.\nPlease update llvmlite.' % (_min_llvmlite_version + (llvmlite.__version__,))
            raise ImportError(msg)
    else:
        warnings.warn('llvmlite version format not recognized!')
    llvm_version_info = llvm_version_info
    check_jit_execution = check_jit_execution
    import llvmlite.binding
    if llvm_version_info < _min_llvm_version:
        msg = 'Numba requires at least version %d.%d.%d of LLVM.\nInstalled llvmlite is built against version %d.%d.%d.\nPlease update llvmlite.' % (_min_llvm_version + llvm_version_info)
        raise ImportError(msg)
    check_jit_execution()


def _try_enable_svml():
    '''
    Tries to enable SVML if configuration permits use and the library is found.
    '''
    if not config.DISABLE_INTEL_SVML:
        
        try:
            if sys.platform.startswith('linux'):
                llvmlite.binding.load_library_permanently('libsvml.so')
            elif sys.platform.startswith('darwin'):
                llvmlite.binding.load_library_permanently('libsvml.dylib')
            elif sys.platform.startswith('win'):
                llvmlite.binding.load_library_permanently('svml_dispmd')
            else:
                return False
            
            try:
                if not getattr(llvmlite.binding.targets, 'has_svml')():
                    return False
            except AttributeError:
                if platform.machine() == 'x86_64' and config.DEBUG:
                    msg = 'SVML was found but llvmlite >= 0.23.2 is needed to support it.'
                    warnings.warn(msg)
                    
                    try:
                        return False
                        
                        try:
                            llvmlite.binding.set_option('SVML', '-vector-library=SVML')
                            return True
                        except:
                            if platform.machine() == 'x86_64' and config.DEBUG:
                                warnings.warn('SVML was not found/could not be loaded.')

                        return False




_ensure_llvm()
import llvmlite
config.USING_SVML = _try_enable_svml()
