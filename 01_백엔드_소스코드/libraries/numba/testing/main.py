# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: main.pyc (Python 3.11)

import collections
import contextlib
import cProfile
import inspect
import gc
import multiprocessing
import os
import random
import sys
import time
import unittest
import warnings
import zlib
import traceback
from functools import lru_cache
from io import StringIO
from unittest import result, runner, signals, suite, loader, case
from loader import TestLoader
from numba.core import config
from numba.misc import memoryutils

try:
    from multiprocessing import TimeoutError
except ImportError:
    from Queue import Empty as TimeoutError


def make_tag_decorator(known_tags):
    '''
    Create a decorator allowing tests to be tagged with the *known_tags*.
    '''
    pass
# WARNING: Decompyle incomplete

_get_mtime = (lambda cls: str(os.path.getmtime(inspect.getfile(cls))))()

def cuda_sensitive_mtime(x):
    '''
    Return a key for sorting tests bases on mtime and test name. For CUDA
    tests, interleaving tests from different classes is dangerous as the CUDA
    context might get reset unexpectedly between methods of a class, so for
    CUDA tests the key prioritises the test module and class ahead of the
    mtime.
    '''
    cls = x.__class__
    key = _get_mtime(cls) + str(x)
    CUDATestCase = CUDATestCase
    import numba.cuda.testing
    if CUDATestCase in cls.mro():
        key = f'''{str(cls.__module__)!s}.{str(cls.__name__)!s} {key!s}'''
    return key


def parse_slice(useslice):
    '''Parses the argument string "useslice" as a shard index and number and
    returns a function that filters on those arguments. i.e. input
    useslice="1:3" leads to output something like `lambda x: zlib.crc32(x) % 3
    == 1`.
    '''
    pass
# WARNING: Decompyle incomplete


class TestLister(object):
    '''Simply list available tests rather than running them.'''
    
    def __init__(self, useslice):
        self.useslice = parse_slice(useslice)

    
    def run(self, test):
        result = runner.TextTestResult(sys.stderr, descriptions = True, verbosity = 1)
        self._test_list = _flatten_suite(test)
        masked_list = list(filter(self.useslice, self._test_list))
        self._test_list.sort(key = cuda_sensitive_mtime)
        for t in masked_list:
            print(t.id())
            print('%d tests found. %s selected' % (len(self._test_list), len(masked_list)))
            return result



class SerialSuite(unittest.TestSuite):
    pass
# WARNING: Decompyle incomplete


class BasicTestRunner(runner.TextTestRunner):
    pass
# WARNING: Decompyle incomplete


class NumbaTestProgram(unittest.main):
    pass
# WARNING: Decompyle incomplete

_GENERATED = ('numba.cuda.tests.cudapy.test_libdevice.TestLibdeviceCompilation', 'numba.tests.test_num_threads', 'numba.tests.test_parallel_backend', 'numba.tests.test_svml', 'numba.tests.test_ufuncs')

def _flatten_suite_inner(test):
    '''
    Workhorse for _flatten_suite
    '''
    tests = []
    if isinstance(test, (unittest.TestSuite, list, tuple)):
        for x in test:
            tests.extend(_flatten_suite_inner(x))
    tests.append(test)
    return tests


def _flatten_suite(test):
    '''
    Expand nested suite into list of test cases.
    '''
    tests = _flatten_suite_inner(test)
    generated = set()
    for t in tests:
        for g in _GENERATED:
            if g in str(t):
                generated.add(t)
        normal = set(tests) - generated
        
        def key(x):
            return (x.__module__, type(x).__name__, x._testMethodName)

        tests = sorted(normal, key = key)
        tests.extend(sorted(list(generated), key = key))
        return tests


def _choose_gitdiff_tests(tests = None, *, use_common_ancestor):
    pass
# WARNING: Decompyle incomplete


def _choose_tagged_tests(tests, tags, mode = ('include',)):
    """
    Select tests that are tagged/not tagged with at least one of the given tags.
    Set mode to 'include' to include the tests with tags, or 'exclude' to
    exclude the tests with the tags.
    """
    selected = []
    tags = set(tags)
# WARNING: Decompyle incomplete


def _choose_random_tests(tests, ratio, seed):
    '''
    Choose a given proportion of tests at random.
    '''
    rnd = random.Random()
    rnd.seed(seed)
    if isinstance(tests, unittest.TestSuite):
        tests = _flatten_suite(tests)
    tests = rnd.sample(tests, int(len(tests) * ratio))
    tests = sorted(tests, key = (lambda case: case.id()))
    return unittest.TestSuite(tests)


def _refleak_cleanup():
    func1 = sys.getallocatedblocks
    
    try:
        func2 = sys.gettotalrefcount
    except AttributeError:
        
        func2 = lambda : 42

# WARNING: Decompyle incomplete


class ReferenceLeakError(RuntimeError):
    pass


class IntPool(collections.defaultdict):
    
    def __missing__(self, key):
        return key



class RefleakTestResult(runner.TextTestResult):
    pass
# WARNING: Decompyle incomplete


class RefleakTestRunner(runner.TextTestRunner):
    resultclass = RefleakTestResult


class ParallelTestResult(runner.TextTestResult):
    '''
    A TestResult able to inject results from other results.
    '''
    
    def add_results(self, result):
        '''
        Add the results from the other *result* to this result.
        '''
        self.stream.write(result.stream.getvalue())
        self.stream.flush()
        self.failures.extend(result.failures)
        self.errors.extend(result.errors)
        self.skipped.extend(result.skipped)
        self.expectedFailures.extend(result.expectedFailures)
        self.unexpectedSuccesses.extend(result.unexpectedSuccesses)



class _MinimalResult(object):
    '''
    A minimal, picklable TestResult-alike object.
    '''
    __slots__ = ('failures', 'errors', 'skipped', 'expectedFailures', 'unexpectedSuccesses', 'stream', 'shouldStop', 'testsRun', 'test_id', 'resource_info')
    
    def fixup_case(self, case):
        '''
        Remove any unpicklable attributes from TestCase instance *case*.
        '''
        case._outcomeForDoCleanups = None

    
    def __init__(self, original_result, test_id, resource_info = (None, None)):
        for attr in self.__slots__:
            setattr(self, attr, getattr(original_result, attr, None))
            for case, _ in self.expectedFailures:
                self.fixup_case(case)
                for case, _ in self.errors:
                    self.fixup_case(case)
                    for case, _ in self.failures:
                        self.fixup_case(case)
                        self.test_id = test_id
                        self.resource_info = resource_info
                        return None



class _FakeStringIO(object):
    '''
    A trivial picklable StringIO-alike for Python 2.
    '''
    
    def __init__(self, value):
        self._value = value

    
    def getvalue(self):
        return self._value



class _MinimalRunner(object):
    '''
    A minimal picklable object able to instantiate a runner in a
    child process and run a test case with it.
    '''
    
    def __init__(self, runner_cls, runner_args):
        self.runner_cls = runner_cls
        self.runner_args = runner_args

    
    def __call__(self, test):
        kwargs = self.runner_args
        kwargs['stream'] = StringIO()
    # WARNING: Decompyle incomplete

    cleanup_object = (lambda self, test: pass# WARNING: Decompyle incomplete
)()


def _split_nonparallel_tests(test, sliced):
    '''
    Split test suite into parallel and serial tests.
    '''
    ptests = []
    stests = []
    flat = None
    
    def is_parallelizable_test_case(test):
        method_name = test._testMethodName
        method = getattr(test, method_name)
        if method.__name__ != method_name and method.__name__ == 'testFailure':
            return False
        return None(test, '_numba_parallel_test_', True)

    for t in flat:
        if is_parallelizable_test_case(t):
            ptests.append(t)
            continue
        stests.append(t)
        return (ptests, stests)

_TIMEOUT = 1200

class ParallelTestRunner(runner.TextTestRunner):
    pass
# WARNING: Decompyle incomplete
