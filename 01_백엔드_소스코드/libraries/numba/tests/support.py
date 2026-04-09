# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: support.pyc (Python 3.11)

'''
Assorted utilities for use in tests.
'''
import cmath
import contextlib
from collections import defaultdict
import enum
import gc
import math
import platform
import os
import signal
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import io
import ctypes
import multiprocessing as mp
import warnings
import traceback
from contextlib import contextmanager
import uuid
import importlib
import types as pytypes
from functools import cached_property
import numpy as np
from numba import testing, types
from numba.core import errors, typing, utils, config, cpu
from numba.core.typing import cffi_utils
from numba.core.compiler import compile_extra, Flags, DEFAULT_FLAGS, CompilerBase, DefaultPassBuilder
from numba.core.typed_passes import IRLegalization
from numba.core.untyped_passes import PreserveIR
import unittest
from numba.core.runtime import rtsys
from numba.np import numpy_support
from numba.core.runtime import _nrt_python as _nrt
from numba.core.extending import overload_method, typeof_impl, register_model, unbox, NativeValue, models
from numba.core.datamodel.models import OpaqueModel

try:
    import scipy
except ImportError:
    scipy = None


try:
    import coverage
    coverage.process_startup()
except ImportError:
    pass

enable_pyobj_flags = Flags()
enable_pyobj_flags.enable_pyobject = True
force_pyobj_flags = Flags()
force_pyobj_flags.force_pyobject = True
no_pyobj_flags = Flags()
nrt_flags = Flags()
nrt_flags.nrt = True
tag = testing.make_tag_decorator([
    'important',
    'long_running',
    'always_test'])
always_test = tag('always_test')
_32bit = sys.maxsize <= 0x100000000
is_parfors_unsupported = _32bit
skip_parfors_unsupported = unittest.skipIf(is_parfors_unsupported, 'parfors not supported')
skip_unless_py10_or_later = unittest.skipUnless(utils.PYVERSION >= (3, 10), 'needs Python 3.10 or later')
skip_unless_py10 = unittest.skipUnless(utils.PYVERSION == (3, 10), 'needs Python 3.10')
skip_unless_py312 = unittest.skipUnless(utils.PYVERSION == (3, 12), 'needs Python 3.12')
if utils.PYVERSION >= (3, 13):
    skip_if_py313plus_on_windows = unittest.skipIf(sys.platform.startswith('win'), 'Not supported on Python 3.13+ on Windows')
    skip_if_py314 = unittest.skipIf(utils.PYVERSION == (3, 14), 'Test unstable on 3.14')
    if sys.platform.startswith('linux'):
        skip_if_linux_aarch64 = unittest.skipIf(platform.machine() == 'aarch64', 'Not supported on Linux aarch64')
        skip_if_32bit = unittest.skipIf(_32bit, 'Not supported on 32 bit')
        IS_NUMPY_2 = numpy_support.numpy_version >= (2, 0)
        skip_if_numpy_2 = unittest.skipIf(IS_NUMPY_2, 'Not supported on numpy 2.0+')
        REDUCED_TESTING = bool(int(os.environ.get('_NUMBA_REDUCED_TESTING', 0)))
        skip_if_reduced_testing = unittest.skipIf(REDUCED_TESTING, 'Skipped for reduced testing')
        _free_threading = not getattr(sys, '_is_gil_enabled', (lambda : True))()
        skip_if_freethreading = unittest.skipIf(_free_threading, 'Skipped [NOT APPLICABLE] if using a free-threading build and free-threading is enabled.')
        
        def expected_failure_py311(fn):
            if utils.PYVERSION == (3, 11):
                return unittest.expectedFailure(fn)

        
        def expected_failure_py312(fn):
            if utils.PYVERSION == (3, 12):
                return unittest.expectedFailure(fn)

        
        def expected_failure_py313(fn):
            if utils.PYVERSION == (3, 13):
                return unittest.expectedFailure(fn)

        
        def expected_failure_py314(fn):
            if utils.PYVERSION == (3, 14):
                return unittest.expectedFailure(fn)

        
        def expected_failure_np2(fn):
            if numpy_support.numpy_version == (2, 0):
                return unittest.expectedFailure(fn)

        _msg = 'SciPy needed for test'
        skip_unless_scipy = unittest.skipIf(scipy is None, _msg)
        skip_unless_cffi = unittest.skipUnless(cffi_utils.SUPPORTED, 'requires cffi')
        _lnx_reason = 'linux only test'
        linux_only = unittest.skipIf(not sys.platform.startswith('linux'), _lnx_reason)
        _win_reason = 'Windows-only test'
        windows_only = unittest.skipIf(not sys.platform.startswith('win'), _win_reason)
        _is_armv7l = platform.machine() == 'armv7l'
        disabled_test = unittest.skipIf(True, 'Test disabled')
        skip_ppc64le_issue4563 = unittest.skipIf(platform.machine() == 'ppc64le', "Hits: 'Parameter area must exist to pass an argument in memory'")
        has_typeguard = bool(os.environ.get('NUMBA_USE_TYPEGUARD', 0))
        skip_unless_typeguard = unittest.skipUnless(has_typeguard, 'Typeguard is not enabled')
        skip_if_typeguard = unittest.skipIf(has_typeguard, 'Broken if Typeguard is enabled')
        skip_ppc64le_issue6465 = unittest.skipIf(platform.machine() == 'ppc64le', "Hits: 'mismatch in size of parameter area' in LowerCall_64SVR4")
        skip_ppc64le_invalid_ctr_loop = unittest.skipIf(platform.machine() == 'ppc64le', 'Invalid PPC CTR loop')
        _uname = platform.uname()
        IS_MACOS = _uname.system == 'Darwin'
        skip_macos_fenv_errors = unittest.skipIf(IS_MACOS, 'fenv.h-like functionality unreliable on macOS')
        if IS_MACOS:
            IS_MACOS_ARM64 = _uname.machine == 'arm64'
            
            try:
                import scipy.linalg.cython_lapack as scipy
                has_lapack = True
            except ImportError:
                has_lapack = False

            needs_lapack = unittest.skipUnless(has_lapack, 'LAPACK needs SciPy 1.0+')
            
            try:
                import scipy.linalg.cython_blas as scipy
                has_blas = True
            except ImportError:
                unittest.skipIf
                has_blas = False

            needs_blas = unittest.skipUnless(has_blas, 'BLAS needs SciPy 1.0+')
            _exec_cond = os.environ.get('SUBPROC_TEST', None) == '1'
            needs_subprocess = unittest.skipUnless(_exec_cond, 'needs subprocess harness')
            
            try:
                import setuptools
                has_setuptools = True
            except (ImportError, OSError):
                unittest.skipIf
                has_setuptools = False

            needs_setuptools = unittest.skipUnless(has_setuptools, 'Test needs setuptools')
            
            def ignore_internal_warnings():
                '''Use in testing within a ` warnings.catch_warnings` block to filter out
    warnings that are unrelated/internally generated by Numba.
    '''
                warnings.filterwarnings('ignore', module = 'typeguard')
                warnings.filterwarnings(action = 'ignore', message = '.*TBB_INTERFACE_VERSION.*', category = errors.NumbaWarning, module = 'numba\\.np\\.ufunc\\.parallel.*')

            
            class TestCase(unittest.TestCase):
                longMessage = True
                random = (lambda self: np.random.RandomState(42))()
                
                def reset_module_warnings(self, module):
                    '''
        Reset the warnings registry of a module.  This can be necessary
        as the warnings module is buggy in that regard.
        See http://bugs.python.org/issue4180
        '''
                    if isinstance(module, str):
                        module = sys.modules[module]
                    
                    try:
                        del module.__warningregistry__
                        return None
                    except AttributeError:
                        return None


                assertTypingError = (lambda self: pass# WARNING: Decompyle incomplete
)()
                assertRefCount = (lambda self: pass# WARNING: Decompyle incomplete
)()
                
                def assertRefCountEqual(self, *objects):
                    gc.collect()
                    rc = objects()
                    rc_0 = rc[0]
                    for i in range(len(objects))[1:]:
                        rc_i = rc[i]
                        if rc_0 != rc_i:
                            self.fail(f'''Refcount for objects does not match. #0({rc_0}) != #{i}({rc_i}) does not match.''')
                        return None

                assertNoNRTLeak = (lambda self: pass# WARNING: Decompyle incomplete
)()
                _bool_types = (bool, np.bool_)
                _exact_typesets = [
                    _bool_types,
                    (int,),
                    (str,),
                    (np.integer,),
                    (bytes, np.bytes_)]
                _approx_typesets = [
                    (float,),
                    (complex,),
                    np.inexact]
                _sequence_typesets = [
                    (tuple, list)]
                _float_types = (float, np.floating)
                _complex_types = (complex, np.complexfloating)
                
                def _detect_family(self, numeric_object):
                    '''
        This function returns a string description of the type family
        that the object in question belongs to.  Possible return values
        are: "exact", "complex", "approximate", "sequence", and "unknown"
        '''
                    if isinstance(numeric_object, np.ndarray):
                        return 'ndarray'
                    if None(numeric_object, enum.Enum):
                        return 'enum'
                    for tp in None._sequence_typesets:
                        if isinstance(numeric_object, tp):
                            return 'sequence'
                        for tp in self._exact_typesets:
                            if isinstance(numeric_object, tp):
                                return 'exact'
                            for tp in self._complex_types:
                                if isinstance(numeric_object, tp):
                                    return 'complex'
                                for tp in self._approx_typesets:
                                    if isinstance(numeric_object, tp):
                                        return 'approximate'
                                    return 'unknown'

                
                def _fix_dtype(self, dtype):
                    '''
        Fix the given *dtype* for comparison.
        '''
                    if sys.platform == 'win32' and sys.maxsize > 0x100000000 and dtype == np.dtype('int32'):
                        return np.dtype('int64')

                
                def _fix_strides(self, arr):
                    '''
        Return the strides of the given array, fixed for comparison.
        Strides for 0- or 1-sized dimensions are ignored.
        '''
                    pass
                # WARNING: Decompyle incomplete

                
                def assertStridesEqual(self, first, second):
                    '''
        Test that two arrays have the same shape and strides.
        '''
                    self.assertEqual(first.shape, second.shape, 'shapes differ')
                    self.assertEqual(first.itemsize, second.itemsize, 'itemsizes differ')
                    self.assertEqual(self._fix_strides(first), self._fix_strides(second), 'strides differ')

                
                def assertPreciseEqual(self, first, second, prec, ulps, msg, ignore_sign_on_zero, abs_tol = ('exact', 1, None, False, None)):
                    '''
        Versatile equality testing function with more built-in checks than
        standard assertEqual().

        For arrays, test that layout, dtype, shape are identical, and
        recursively call assertPreciseEqual() on the contents.

        For other sequences, recursively call assertPreciseEqual() on
        the contents.

        For scalars, test that two scalars or have similar types and are
        equal up to a computed precision.
        If the scalars are instances of exact types or if *prec* is
        \'exact\', they are compared exactly.
        If the scalars are instances of inexact types (float, complex)
        and *prec* is not \'exact\', then the number of significant bits
        is computed according to the value of *prec*: 53 bits if *prec*
        is \'double\', 24 bits if *prec* is single.  This number of bits
        can be lowered by raising the *ulps* value.
        ignore_sign_on_zero can be set to True if zeros are to be considered
        equal regardless of their sign bit.
        abs_tol if this is set to a float value its value is used in the
        following. If, however, this is set to the string "eps" then machine
        precision of the type(first) is used in the following instead. This
        kwarg is used to check if the absolute difference in value between first
        and second is less than the value set, if so the numbers being compared
        are considered equal. (This is to handle small numbers typically of
        magnitude less than machine precision).

        Any value of *prec* other than \'exact\', \'single\' or \'double\'
        will raise an error.
        '''
                    
                    try:
                        self._assertPreciseEqual(first, second, prec, ulps, msg, ignore_sign_on_zero, abs_tol)
                        return None
                    except AssertionError:
                        exc = None
                        failure_msg = str(exc)
                        exc = None
                        del exc
                    except:
                        exc = None
                        del exc

                    self.fail(f'''when comparing {first!s} and {second!s}: {failure_msg!s}''')

                
                def _assertPreciseEqual(self, first, second, prec, ulps, msg, ignore_sign_on_zero, abs_tol = ('exact', 1, None, False, None)):
                    '''Recursive workhorse for assertPreciseEqual().'''
                    pass
                # WARNING: Decompyle incomplete

                
                def subprocess_test_runner(self, test_module, test_class, test_name, envvars, timeout, flags, _subproc_test_env = (None, None, None, 60, None, '1')):
                    '''
        Runs named unit test(s) as specified in the arguments as:
        test_module.test_class.test_name. test_module must always be supplied
        and if no further refinement is made with test_class and test_name then
        all tests in the module will be run. The tests will be run in a
        subprocess with environment variables specified in `envvars`.
        If given, envvars must be a map of form:
            environment variable name (str) -> value (str)
        If given, flags must be a map of form:
            flag including the `-` (str) -> value (str)
        It is most convenient to use this method in conjunction with
        @needs_subprocess as the decorator will cause the decorated test to be
        skipped unless the `SUBPROC_TEST` environment variable is set to
        the same value of ``_subproc_test_env``
        (this special environment variable is set by this method such that the
        specified test(s) will not be skipped in the subprocess).


        Following execution in the subprocess this method will check the test(s)
        executed without error. The timeout kwarg can be used to allow more time
        for longer running tests, it defaults to 60 seconds.
        '''
                    themod = self.__module__
                    thecls = type(self).__name__
                    parts = (test_module, test_class, test_name)
                    fully_qualified_test = (lambda .0: pass# WARNING: Decompyle incomplete
)(parts())
                    flags_args = []
                # WARNING: Decompyle incomplete

                
                def run_test_in_subprocess(maybefunc, timeout, envvars = (None, 60, None)):
                    """Runs the decorated test in a subprocess via invoking numba's test
        runner. kwargs timeout and envvars are passed through to
        subprocess_test_runner."""
                    pass
                # WARNING: Decompyle incomplete

                
                def make_dummy_type(self):
                    '''Use to generate a dummy type unique to this test. Returns a python
        Dummy class and a corresponding Numba type DummyType.'''
                    pass
                # WARNING: Decompyle incomplete

                
                def skip_if_no_external_compiler(self):
                    '''
        Call this to ensure the test is skipped if no suitable external compiler
        is found. This is a method on the TestCase opposed to a stand-alone
        decorator so as to make it "lazy" via runtime evaluation opposed to
        running at test-discovery time.
        '''
                    external_compiler_works = external_compiler_works
                    import numba.pycc.platform
                    if not external_compiler_works():
                        self.skipTest('No suitable external compiler was found.')
                        return None


            
            class SerialMixin(object):
                '''Mixin to mark test for serial execution.
    '''
                _numba_parallel_test_ = False

            override_config = (lambda name, value: pass# WARNING: Decompyle incomplete
)()
            override_env_config = (lambda name, value: pass# WARNING: Decompyle incomplete
)()
            
            def compile_function(name, code, globs):
                '''
    Given a *code* string, compile it with globals *globs* and return
    the function named *name*.
    '''
                co = compile(code.rstrip(), '<string>', 'single')
                ns = { }
                eval(co, globs, ns)
                return ns[name]

            _trashcan_dir = 'numba-tests'
_trashcan_timeout = 86400

def _create_trashcan_dir():
    
    try:
        os.mkdir(_trashcan_dir)
        return None
    except FileExistsError:
        return None



def _purge_trashcan_dir():
    freshness_threshold = time.time() - _trashcan_timeout
    for fn in sorted(os.listdir(_trashcan_dir)):
        fn = os.path.join(_trashcan_dir, fn)
        st = os.stat(fn)
        if st.st_mtime < freshness_threshold:
            shutil.rmtree(fn, ignore_errors = True)
        except OSError:
            e = None
            e = None
            del e
            continue
            e = None
            del e
        return None


def _create_trashcan_subdir(prefix):
    _purge_trashcan_dir()
    path = tempfile.mkdtemp(prefix = prefix + '-', dir = _trashcan_dir)
    return path


def temp_directory(prefix):
    """
    Create a temporary directory with the given *prefix* that will survive
    at least as long as this process invocation.  The temporary directory
    will be eventually deleted when it becomes stale enough.

    This is necessary because a DLL file can't be deleted while in use
    under Windows.

    An interesting side-effect is to be able to inspect the test files
    shortly after a test suite run.
    """
    _create_trashcan_dir()
    return _create_trashcan_subdir(prefix)


def import_dynamic(modname):
    """
    Import and return a module of the given name.  Care is taken to
    avoid issues due to Python's internal directory caching.
    """
    import importlib
    importlib.invalidate_caches()
    __import__(modname)
    return sys.modules[modname]

captured_output = (lambda stream_name: pass# WARNING: Decompyle incomplete
)()

def captured_stdout():
    '''Capture the output of sys.stdout:

       with captured_stdout() as stdout:
           print("hello")
       self.assertEqual(stdout.getvalue(), "hello
")
    '''
    return captured_output('stdout')


def captured_stderr():
    '''Capture the output of sys.stderr:

       with captured_stderr() as stderr:
           print("hello", file=sys.stderr)
       self.assertEqual(stderr.getvalue(), "hello
")
    '''
    return captured_output('stderr')

capture_cache_log = (lambda : pass# WARNING: Decompyle incomplete
)()

class EnableNRTStatsMixin(object):
    '''Mixin to enable the NRT statistics counters.'''
    
    def setUp(self):
        _nrt.memsys_enable_stats()

    
    def tearDown(self):
        _nrt.memsys_disable_stats()



class MemoryLeak(object):
    __enable_leak_check = True
    
    def memory_leak_setup(self):
        gc.collect()
        self._MemoryLeak__init_stats = rtsys.get_allocation_stats()

    
    def memory_leak_teardown(self):
        if self.__enable_leak_check:
            self.assert_no_memory_leak()
            return None

    
    def assert_no_memory_leak(self):
        old = self._MemoryLeak__init_stats
        new = rtsys.get_allocation_stats()
        total_alloc = new.alloc - old.alloc
        total_free = new.free - old.free
        total_mi_alloc = new.mi_alloc - old.mi_alloc
        total_mi_free = new.mi_free - old.mi_free
        self.assertEqual(total_alloc, total_free)
        self.assertEqual(total_mi_alloc, total_mi_free)

    
    def disable_leak_check(self):
        self.__enable_leak_check = False



class MemoryLeakMixin(MemoryLeak, EnableNRTStatsMixin):
    pass
# WARNING: Decompyle incomplete

forbid_codegen = (lambda : pass# WARNING: Decompyle incomplete
)()
redirect_fd = (lambda fd: pass# WARNING: Decompyle incomplete
)()

def redirect_c_stdout():
    '''Redirect C stdout
    '''
    fd = sys.__stdout__.fileno()
    return redirect_fd(fd)


def redirect_c_stderr():
    '''Redirect C stderr
    '''
    fd = sys.__stderr__.fileno()
    return redirect_fd(fd)


def run_in_new_process_caching(func, cache_dir_prefix, verbose = (__name__, True)):
    """Spawn a new process to run `func` with a temporary cache directory.

    The childprocess's stdout and stderr will be captured and redirected to
    the current process's stdout and stderr.

    Returns
    -------
    ret : dict
        exitcode: 0 for success. 1 for exception-raised.
        stdout: str
        stderr: str
    """
    cache_dir = temp_directory(cache_dir_prefix)
    return run_in_new_process_in_cache_dir(func, cache_dir, verbose = verbose)


def run_in_new_process_in_cache_dir(func, cache_dir, verbose = (True,)):
    """Spawn a new process to run `func` with a temporary cache directory.

    The childprocess's stdout and stderr will be captured and redirected to
    the current process's stdout and stderr.

    Similar to ``run_in_new_process_caching()`` but the ``cache_dir`` is a
    directory path instead of a name prefix for the directory path.

    Returns
    -------
    ret : dict
        exitcode: 0 for success. 1 for exception-raised.
        stdout: str
        stderr: str
    """
    ctx = mp.get_context('spawn')
    qout = ctx.Queue()
    override_env_config('NUMBA_CACHE_DIR', cache_dir)
    proc = ctx.Process(target = _remote_runner, args = [
        func,
        qout])
    proc.start()
    proc.join()
    stdout = qout.get_nowait()
    stderr = qout.get_nowait()
    if verbose and stdout.strip():
        print()
        print('STDOUT'.center(80, '-'))
        print(stdout)
    if verbose and stderr.strip():
        print(file = sys.stderr)
        print('STDERR'.center(80, '-'), file = sys.stderr)
        print(stderr, file = sys.stderr)
    None(None, None)


def _remote_runner(fn, qout):
    '''Used by `run_in_new_process_caching()`
    '''
    stderr = captured_stderr()
    stdout = captured_stdout()
    fn()
    exitcode = 0


class CheckWarningsMixin(object):
    check_warnings = (lambda self, messages, category = (RuntimeWarning,): pass# WARNING: Decompyle incomplete
)()


def _format_jit_options(**jit_options):
    if not jit_options:
        return ''
    out = None
    for key, value in jit_options.items():
        if isinstance(value, str):
            value = '"{}"'.format(value)
        out.append('{}={}'.format(key, value))
        return ', '.join(out)

create_temp_module = (lambda source_lines: pass# WARNING: Decompyle incomplete
)()

def run_in_subprocess(code, flags, env, timeout = (None, None, 30)):
    """Run a snippet of Python code in a subprocess with flags, if any are
    given. 'env' is passed to subprocess.Popen(). 'timeout' is passed to
    popen.communicate().

    Returns the stdout and stderr of the subprocess after its termination.
    """
    pass
# WARNING: Decompyle incomplete


def strace(work, syscalls, timeout = (10,)):
    '''Runs strace whilst executing the function work() in the current process,
    captures the listed syscalls (list of strings). Takes an optional timeout in
    seconds, default is 10, if this is exceeded the process will be sent a
    SIGKILL. Returns a list of lines that are output by strace.
    '''
    pass
# WARNING: Decompyle incomplete


def strace_supported():
