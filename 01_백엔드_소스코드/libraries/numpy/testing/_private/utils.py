# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

'''
Utility function to facilitate testing.

'''
import os
import sys
import platform
import re
import gc
import operator
import warnings
from functools import partial, wraps
import shutil
import contextlib
from tempfile import mkdtemp, mkstemp
from unittest.case import SkipTest
from warnings import WarningMessage
import pprint
import sysconfig
import numpy as np
from numpy.core import intp, float32, empty, arange, array_repr, ndarray, isnat, array
from numpy import isfinite, isnan, isinf
import numpy.linalg._umath_linalg as numpy
from io import StringIO
__all__ = [
    'assert_equal',
    'assert_almost_equal',
    'assert_approx_equal',
    'assert_array_equal',
    'assert_array_less',
    'assert_string_equal',
    'assert_array_almost_equal',
    'assert_raises',
    'build_err_msg',
    'decorate_methods',
    'jiffies',
    'memusage',
    'print_assert_equal',
    'rundocs',
    'runstring',
    'verbose',
    'measure',
    'assert_',
    'assert_array_almost_equal_nulp',
    'assert_raises_regex',
    'assert_array_max_ulp',
    'assert_warns',
    'assert_no_warnings',
    'assert_allclose',
    'IgnoreException',
    'clear_and_catch_warnings',
    'SkipTest',
    'KnownFailureException',
    'temppath',
    'tempdir',
    'IS_PYPY',
    'HAS_REFCOUNT',
    'IS_WASM',
    'suppress_warnings',
    'assert_array_compare',
    'assert_no_gc_cycles',
    'break_cycles',
    'HAS_LAPACK64',
    'IS_PYSTON',
    '_OLD_PROMOTION',
    'IS_MUSL',
    '_SUPPORTS_SVE']

class KnownFailureException(Exception):
    '''Raise this exception to mark a test as a known failing test.'''
    pass

KnownFailureTest = KnownFailureException
verbose = 0
IS_WASM = platform.machine() in ('wasm32', 'wasm64')
IS_PYPY = sys.implementation.name == 'pypy'
IS_PYSTON = hasattr(sys, 'pyston_version_info')
if getattr(sys, 'getrefcount', None) is not None:
    HAS_REFCOUNT = not IS_PYSTON
    HAS_LAPACK64 = numpy.linalg._umath_linalg._ilp64
    
    _OLD_PROMOTION = lambda : np._get_promotion_state() == 'legacy'
    IS_MUSL = False
    if not sysconfig.get_config_var('HOST_GNU_TYPE'):
        _v = ''
        if 'musl' in _v:
            IS_MUSL = True

def assert_(val, msg = ('',)):
    '''
    Assert that works in release mode.
    Accepts callable msg to allow deferring evaluation until failure.

    The Python built-in ``assert`` does not work when executing code in
    optimized mode (the ``-O`` flag) - no byte-code is generated for it.

    For documentation on usage, refer to the Python documentation.

    '''
    __tracebackhide__ = True
    if not val:
        
        try:
            smsg = msg()
        except TypeError:
            smsg = msg

        raise AssertionError(smsg)

if os.name == 'nt':
    
    def GetPerformanceAttributes(object, counter, instance, inum, format, machine = (None, -1, None, None)):
        import win32pdh
    # WARNING: Decompyle incomplete

    
    def memusage(processName, instance = ('python', 0)):
        import win32pdh
        return GetPerformanceAttributes('Process', 'Virtual Bytes', processName, instance, win32pdh.PDH_FMT_LONG, None)

elif sys.platform[:5] == 'linux':
    
    def memusage(_proc_pid_stat = (f'''/proc/{os.getpid()}/stat''',)):
        '''
        Return virtual memory size in bytes of the running python.

        '''
        
        try:
            f = open(_proc_pid_stat)
            l = f.readline().split(' ')
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            return int(l[22])
                        except Exception:
                            return None





else:
    
    def memusage():
        '''
        Return memory usage of running python. [Not implemented]

        '''
        raise NotImplementedError


def build_err_msg(arrays, err_msg, header, verbose, names, precision = ('Items are not equal:', True, ('ACTUAL', 'DESIRED'), 8)):
    msg = [
        '\n' + header]
    if err_msg:
        if err_msg.find('\n') == -1 and len(err_msg) < 79 - len(header):
            msg = [
                msg[0] + ' ' + err_msg]
        else:
            msg.append(err_msg)
    if verbose:
        for i, a in enumerate(arrays):
            if isinstance(a, ndarray):
                r_func = partial(array_repr, precision = precision)
            else:
                r_func = repr
            r = r_func(a)
        except Exception:
            exc = None
            r = f'''[repr failed for <{type(a).__name__}>: {exc}]'''
            exc = None
            del exc
        except:
            exc = None
            del exc
        if r.count('\n') > 3:
            r = '\n'.join(r.splitlines()[:3])
            r += '...'
        msg.append(f''' {names[i]}: {r}''')
        continue
    return '\n'.join(msg)


def assert_equal(actual, desired, err_msg, verbose = ('', True)):
    '''
    Raises an AssertionError if two objects are not equal.

    Given two objects (scalars, lists, tuples, dictionaries or numpy arrays),
    check that all elements of these objects are equal. An exception is raised
    at the first conflicting values.

    When one of `actual` and `desired` is a scalar and the other is array_like,
    the function checks that each element of the array_like object is equal to
    the scalar.

    This function handles NaN comparisons as if NaN was a "normal" number.
    That is, AssertionError is not raised if both objects have NaNs in the same
    positions.  This is in contrast to the IEEE standard on NaNs, which says
    that NaN compared to anything must return False.

    Parameters
    ----------
    actual : array_like
        The object to check.
    desired : array_like
        The expected object.
    err_msg : str, optional
        The error message to be printed in case of failure.
    verbose : bool, optional
        If True, the conflicting values are appended to the error message.

    Raises
    ------
    AssertionError
        If actual and desired are not equal.

    Examples
    --------
    >>> np.testing.assert_equal([4,5], [4,6])
    Traceback (most recent call last):
        ...
    AssertionError:
    Items are not equal:
    item=1
     ACTUAL: 5
     DESIRED: 6

    The following comparison does not raise an exception.  There are NaNs
    in the inputs, but they are in the same positions.

    >>> np.testing.assert_equal(np.array([1.0, 2.0, np.nan]), [1, 2, np.nan])

    '''
    __tracebackhide__ = True
    if isinstance(desired, dict):
        if not isinstance(actual, dict):
            raise AssertionError(repr(type(actual)))
        assert_equal(len(actual), len(desired), err_msg, verbose)
        for k, i in desired.items():
            if k not in actual:
                raise AssertionError(repr(k))
            assert_equal(actual[k], desired[k], f'''key={k!r}\n{err_msg}''', verbose)
            return None
            if isinstance(desired, (list, tuple)) and isinstance(actual, (list, tuple)):
                assert_equal(len(actual), len(desired), err_msg, verbose)
                for k in range(len(desired)):
                    assert_equal(actual[k], desired[k], f'''item={k!r}\n{err_msg}''', verbose)
                    return None
                    ndarray = ndarray
                    isscalar = isscalar
                    signbit = signbit
                    import numpy.core
                    iscomplexobj = iscomplexobj
                    real = real
                    imag = imag
                    import numpy.lib
                    if isinstance(actual, ndarray) or isinstance(desired, ndarray):
                        return assert_array_equal(actual, desired, err_msg, verbose)
                    msg = None([
                        actual,
                        desired], err_msg, verbose = verbose)
                    
                    try:
                        if not iscomplexobj(actual):
                            usecomplex = iscomplexobj(desired)
                        else:
                            except (ValueError, TypeError):
                                usecomplex = False
                            if usecomplex:
                                if iscomplexobj(actual):
                                    actualr = real(actual)
                                    actuali = imag(actual)
                                else:
                                    actualr = actual
                                    actuali = 0
                                if iscomplexobj(desired):
                                    desiredr = real(desired)
                                    desiredi = imag(desired)
                                else:
                                    desiredr = desired
                                    desiredi = 0
                                
                                try:
                                    assert_equal(actualr, desiredr)
                                    assert_equal(actuali, desiredi)
                                except AssertionError:
                                    raise AssertionError(msg)

                                if isscalar(desired) != isscalar(actual):
                                    raise AssertionError(msg)
                                
                                try:
                                    isdesnat = isnat(desired)
                                    isactnat = isnat(actual)
                                    dtypes_match = np.asarray(desired).dtype.type == np.asarray(actual).dtype.type
                                    if isdesnat and isactnat:
                                        if dtypes_match:
                                            return None
                                        raise None(msg)
                                except (TypeError, ValueError, NotImplementedError):
                                    pass

                                
                                try:
                                    isdesnan = isnan(desired)
                                    isactnan = isnan(actual)
                                    if isdesnan and isactnan:
                                        return None
                                    array_actual = iscomplexobj(actual).asarray(actual)
                                    array_desired = np.asarray(desired)
                                    if array_actual.dtype.char in 'Mm' or array_desired.dtype.char in 'Mm':
                                        raise NotImplementedError('cannot compare to a scalar with a different type')
                                    if not desired == 0 and actual == 0 and signbit(desired) == signbit(actual):
                                        raise AssertionError(msg)
                                except (TypeError, ValueError, NotImplementedError):
                                    pass

                                
                                try:
                                    if not desired == actual:
                                        raise AssertionError(msg)
                                    return None
                                except (DeprecationWarning, FutureWarning):
                                    e = None
                                    if 'elementwise == comparison' in e.args[0]:
                                        raise AssertionError(msg)
                                    raise 
                                    e = None
                                    del e




def print_assert_equal(test_string, actual, desired):
    """
    Test if two objects are equal, and print an error message if test fails.

    The test is performed with ``actual == desired``.

    Parameters
    ----------
    test_string : str
        The message supplied to AssertionError.
    actual : object
        The object to test for equality against `desired`.
    desired : object
        The expected result.

    Examples
    --------
    >>> np.testing.print_assert_equal('Test XYZ of func xyz', [0, 1], [0, 1])
    >>> np.testing.print_assert_equal('Test XYZ of func xyz', [0, 1], [0, 2])
    Traceback (most recent call last):
    ...
    AssertionError: Test XYZ of func xyz failed
    ACTUAL:
    [0, 1]
    DESIRED:
    [0, 2]

    """
    __tracebackhide__ = True
    import pprint
    if not actual == desired:
        msg = StringIO()
        msg.write(test_string)
        msg.write(' failed\nACTUAL: \n')
        pprint.pprint(actual, msg)
        msg.write('DESIRED: \n')
        pprint.pprint(desired, msg)
        raise AssertionError(msg.getvalue())

assert_almost_equal = (lambda actual, desired, decimal, err_msg, verbose = (7, '', True): pass# WARNING: Decompyle incomplete
)()
assert_approx_equal = (lambda actual, desired, significant, err_msg, verbose = (7, '', True):
