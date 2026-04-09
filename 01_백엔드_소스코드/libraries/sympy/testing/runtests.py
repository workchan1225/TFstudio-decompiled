# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: runtests.pyc (Python 3.11)

"""
This is our testing framework.

Goals:

* it should be compatible with py.test and operate very similarly
  (or identically)
* does not require any external dependencies
* preferably all the functionality should be in this file only
* no magic, just import the test file and execute the test functions, that's it
* portable

"""
import os
import sys
import platform
import inspect
import traceback
import pdb
import re
import linecache
import time
from fnmatch import fnmatch
from timeit import default_timer as clock
import doctest as pdoctest
from doctest import DocTestFinder, DocTestRunner
import random
import subprocess
import shutil
import signal
import stat
import tempfile
import warnings
from contextlib import contextmanager
from inspect import unwrap
from sympy.core.cache import clear_cache
from sympy.external import import_module
from sympy.external.gmpy import GROUND_TYPES
IS_WINDOWS = os.name == 'nt'
ON_CI = os.getenv('CI', None)
SPLIT_DENSITY = [
    0.0059,
    0.0027,
    0.0068,
    0.0011,
    0.0006,
    0.0058,
    0.0047,
    0.0046,
    0.004,
    0.0257,
    0.0017,
    0.0026,
    0.004,
    0.0032,
    0.0016,
    0.0015,
    0.0004,
    0.0011,
    0.0016,
    0.0014,
    0.0077,
    0.0137,
    0.0217,
    0.0074,
    0.0043,
    0.0067,
    0.0236,
    0.0004,
    0.1189,
    0.0142,
    0.0234,
    0.0003,
    0.0003,
    0.0047,
    0.0006,
    0.0013,
    0.0004,
    0.0008,
    0.0007,
    0.0006,
    0.0139,
    0.0013,
    0.0007,
    0.0051,
    0.002,
    0.0004,
    0.0005,
    0.0213,
    0.0048,
    0.0016,
    0.0012,
    0.0014,
    0.0024,
    0.0015,
    0.0004,
    0.0005,
    0.0007,
    0.011,
    0.0062,
    0.0015,
    0.0021,
    0.0049,
    0.0006,
    0.0006,
    0.0011,
    0.0006,
    0.0019,
    0.003,
    0.0044,
    0.0054,
    0.0057,
    0.0049,
    0.0016,
    0.0006,
    0.0009,
    0.0006,
    0.0012,
    0.0006,
    0.0149,
    0.0532,
    0.0076,
    0.0041,
    0.0024,
    0.0135,
    0.0081,
    0.2209,
    0.0459,
    0.0438,
    0.0488,
    0.0137,
    0.002,
    0.0003,
    0.0008,
    0.0039,
    0.0024,
    0.0005,
    0.0004,
    0.003,
    0.056,
    0.0026]
SPLIT_DENSITY_SLOW = [
    0.0086,
    0.0004,
    0.0568,
    0.0003,
    0.0032,
    0.0005,
    0.0004,
    0.0013,
    0.0016,
    0.0648,
    0.0198,
    0.1285,
    0.098,
    0.0005,
    0.0064,
    0.0003,
    0.0004,
    0.0026,
    0.0007,
    0.0051,
    0.0089,
    0.0024,
    0.0033,
    0.0057,
    0.0005,
    0.0003,
    0.001,
    0.0045,
    0.0091,
    0.0006,
    0.0005,
    0.0321,
    0.0059,
    0.1105,
    0.216,
    0.1489,
    0.0004,
    0.0003,
    0.0006,
    0.0483]

class Skipped(Exception):
    pass


class TimeOutError(Exception):
    pass


class DependencyError(Exception):
    pass


def _indent(s, indent = (4,)):
    '''
    Add the given number of space characters to the beginning of
    every non-blank line in ``s``, and return the result.
    If the string ``s`` is Unicode, it is encoded using the stdout
    encoding and the ``backslashreplace`` error handler.
    '''
    return re.sub('(?m)^(?!$)', indent * ' ', s)

pdoctest._indent = _indent

def _report_failure(self, out, test, example, got):
    '''
    Report that the given example failed.
    '''
    s = self._checker.output_difference(example, got, self.optionflags)
    s = s.encode('raw_unicode_escape').decode('utf8', 'ignore')
    out(self._failure_header(test, example) + s)

if IS_WINDOWS:
    DocTestRunner.report_failure = _report_failure

def convert_to_native_paths(lst):
    """
    Converts a list of '/' separated paths into a list of
    native (os.sep separated) paths and converts to lowercase
    if the system is case insensitive.
    """
    newlst = []
# WARNING: Decompyle incomplete


def get_sympy_dir():
    '''
    Returns the root SymPy directory and set the global value
    indicating whether the system is case sensitive or not.
    '''
    this_file = os.path.abspath(__file__)
    sympy_dir = os.path.join(os.path.dirname(this_file), '..', '..')
    sympy_dir = os.path.normpath(sympy_dir)
    return os.path.normcase(sympy_dir)


def setup_pprint(disable_line_wrap = (True,)):
    init_printing = init_printing
    import sympy.interactive.printing
    pprint_use_unicode = pprint_use_unicode
    import sympy.printing.pretty.pretty
    
    printing
    from sympy.printing.pretty import stringpict
    import sympy.interactive.printing, interactive
    interactive_printing.NO_GLOBAL = True
    use_unicode_prev = pprint_use_unicode(False)
    wrap_line_prev = stringpict._GLOBAL_WRAP_LINE
    if disable_line_wrap:
        stringpict._GLOBAL_WRAP_LINE = False
    init_printing(pretty_print = False)
    return (use_unicode_prev, wrap_line_prev)

raise_on_deprecated = (lambda : pass# WARNING: Decompyle incomplete
)()

def run_in_subprocess_with_hash_randomization(function, function_args, function_kwargs, command, module, force = ((), None, sys.executable, 'sympy.testing.runtests', False)):
    '''
    Run a function in a Python subprocess with hash randomization enabled.

    If hash randomization is not supported by the version of Python given, it
    returns False.  Otherwise, it returns the exit value of the command.  The
    function is passed to sys.exit(), so the return value of the function will
    be the return value.

    The environment variable PYTHONHASHSEED is used to seed Python\'s hash
    randomization.  If it is set, this function will return False, because
    starting a new subprocess is unnecessary in that case.  If it is not set,
    one is set at random, and the tests are run.  Note that if this
    environment variable is set when Python starts, hash randomization is
    automatically enabled.  To force a subprocess to be created even if
    PYTHONHASHSEED is set, pass ``force=True``.  This flag will not force a
    subprocess in Python versions that do not support hash randomization (see
    below), because those versions of Python do not support the ``-R`` flag.

    ``function`` should be a string name of a function that is importable from
    the module ``module``, like "_test".  The default for ``module`` is
    "sympy.testing.runtests".  ``function_args`` and ``function_kwargs``
    should be a repr-able tuple and dict, respectively.  The default Python
    command is sys.executable, which is the currently running Python command.

    This function is necessary because the seed for hash randomization must be
    set by the environment variable before Python starts.  Hence, in order to
    use a predetermined seed for tests, we must start Python in a separate
    subprocess.

    Hash randomization was added in the minor Python versions 2.6.8, 2.7.3,
    3.1.5, and 3.2.3, and is enabled by default in all Python versions after
    and including 3.3.0.

    Examples
    ========

    >>> from sympy.testing.runtests import (
    ... run_in_subprocess_with_hash_randomization)
    >>> # run the core tests in verbose mode
    >>> run_in_subprocess_with_hash_randomization("_test",
    ... function_args=("core",),
    ... function_kwargs={\'verbose\': True}) # doctest: +SKIP
    # Will return 0 if sys.executable supports hash randomization and tests
    # pass, 1 if they fail, and False if it does not support hash
    # randomization.

    '''
    cwd = get_sympy_dir()
    p = subprocess.Popen([
        command,
        '-RV'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, cwd = cwd)
    p.communicate()
    if p.returncode != 0:
        return False
    hash_seed = None.getenv('PYTHONHASHSEED')
    if not hash_seed:
        os.environ['PYTHONHASHSEED'] = str(random.randrange(0x100000000))
    elif not force:
        return False
# WARNING: Decompyle incomplete


def run_all_tests(test_args, test_kwargs, doctest_args, doctest_kwargs, examples_args, examples_kwargs = ((), None, (), None, (), None)):
    '''
    Run all tests.

    Right now, this runs the regular tests (bin/test), the doctests
    (bin/doctest), and the examples (examples/all.py).

    This is what ``setup.py test`` uses.

    You can pass arguments and keyword arguments to the test functions that
    support them (for now, test,  doctest, and the examples). See the
    docstrings of those functions for a description of the available options.

    For example, to run the solvers tests with colors turned off:

    >>> from sympy.testing.runtests import run_all_tests
    >>> run_all_tests(test_args=("solvers",),
    ... test_kwargs={"colors:False"}) # doctest: +SKIP

    '''
    tests_successful = True
# WARNING: Decompyle incomplete


def test(*, subprocess, rerun, *paths, **kwargs):
    '''
    Run tests in the specified test_*.py files.

    Tests in a particular test_*.py file are run if any of the given strings
    in ``paths`` matches a part of the test file\'s path. If ``paths=[]``,
    tests in all test_*.py files are run.

    Notes:

    - If sort=False, tests are run in random order (not default).
    - Paths can be entered in native system format or in unix,
      forward-slash format.
    - Files that are on the blacklist can be tested by providing
      their path; they are only excluded if no paths are given.

    **Explanation of test results**

    ======  ===============================================================
    Output  Meaning
    ======  ===============================================================
    .       passed
    F       failed
    X       XPassed (expected to fail but passed)
    f       XFAILed (expected to fail and indeed failed)
    s       skipped
    w       slow
    T       timeout (e.g., when ``--timeout`` is used)
    K       KeyboardInterrupt (when running the slow tests with ``--slow``,
            you can interrupt one of them without killing the test runner)
    ======  ===============================================================


    Colors have no additional meaning and are used just to facilitate
    interpreting the output.

    Examples
    ========

    >>> import sympy

    Run all tests:

    >>> sympy.test()    # doctest: +SKIP

    Run one file:

    >>> sympy.test("sympy/core/tests/test_basic.py")    # doctest: +SKIP
    >>> sympy.test("_basic")    # doctest: +SKIP

    Run all tests in sympy/functions/ and some particular file:

    >>> sympy.test("sympy/core/tests/test_basic.py",
    ...        "sympy/functions")    # doctest: +SKIP

    Run all tests in sympy/core and sympy/utilities:

    >>> sympy.test("/core", "/util")    # doctest: +SKIP

    Run specific test from a file:

    >>> sympy.test("sympy/core/tests/test_basic.py",
    ...        kw="test_equality")    # doctest: +SKIP

    Run specific test from any file:

    >>> sympy.test(kw="subs")    # doctest: +SKIP

    Run the tests with verbose mode on:

    >>> sympy.test(verbose=True)    # doctest: +SKIP

    Do not sort the test output:

    >>> sympy.test(sort=False)    # doctest: +SKIP

    Turn on post-mortem pdb:

    >>> sympy.test(pdb=True)    # doctest: +SKIP

    Turn off colors:

    >>> sympy.test(colors=False)    # doctest: +SKIP

    Force colors, even when the output is not to a terminal (this is useful,
    e.g., if you are piping to ``less -r`` and you still want colors)

    >>> sympy.test(force_colors=False)    # doctest: +SKIP

    The traceback verboseness can be set to "short" or "no" (default is
    "short")

    >>> sympy.test(tb=\'no\')    # doctest: +SKIP

    The ``split`` option can be passed to split the test run into parts. The
    split currently only splits the test files, though this may change in the
    future. ``split`` should be a string of the form \'a/b\', which will run
    part ``a`` of ``b``. For instance, to run the first half of the test suite:

    >>> sympy.test(split=\'1/2\')  # doctest: +SKIP

    The ``time_balance`` option can be passed in conjunction with ``split``.
    If ``time_balance=True`` (the default for ``sympy.test``), SymPy will attempt
    to split the tests such that each split takes equal time.  This heuristic
    for balancing is based on pre-recorded test data.

    >>> sympy.test(split=\'1/2\', time_balance=True)  # doctest: +SKIP

    You can disable running the tests in a separate subprocess using
    ``subprocess=False``.  This is done to support seeding hash randomization,
    which is enabled by default in the Python versions where it is supported.
    If subprocess=False, hash randomization is enabled/disabled according to
    whether it has been enabled or not in the calling Python process.
    However, even if it is enabled, the seed cannot be printed unless it is
    called from a new Python process.

    Hash randomization was added in the minor Python versions 2.6.8, 2.7.3,
    3.1.5, and 3.2.3, and is enabled by default in all Python versions after
    and including 3.3.0.

    If hash randomization is not supported ``subprocess=False`` is used
    automatically.

    >>> sympy.test(subprocess=False)     # doctest: +SKIP

    To set the hash randomization seed, set the environment variable
    ``PYTHONHASHSEED`` before running the tests.  This can be done from within
    Python using

    >>> import os
    >>> os.environ[\'PYTHONHASHSEED\'] = \'42\' # doctest: +SKIP

    Or from the command line using

    $ PYTHONHASHSEED=42 ./bin/test

    If the seed is not set, a random seed will be chosen.

    Note that to reproduce the same hash values, you must use both the same seed
    as well as the same architecture (32-bit vs. 64-bit).

    '''
    pass
# WARNING: Decompyle incomplete


def _test(*, verbose, tb, kw, pdb, colors, force_colors, sort, seed, timeout, fail_on_timeout, slow, enhance_asserts, split, time_balance, blacklist, fast_threshold, slow_threshold, *paths):
    '''
    Internal function that actually runs the tests.

    All keyword arguments from ``test()`` are passed to this function except for
    ``subprocess``.

    Returns 0 if tests passed and 1 if they failed.  See the docstring of
    ``test()`` for more information.
    '''
    pass
# WARNING: Decompyle incomplete


def doctest(*, subprocess, rerun, *paths, **kwargs):
    '''
    Runs doctests in all \\*.py files in the SymPy directory which match
    any of the given strings in ``paths`` or all tests if paths=[].

    Notes:

    - Paths can be entered in native system format or in unix,
      forward-slash format.
    - Files that are on the blacklist can be tested by providing
      their path; they are only excluded if no paths are given.

    Examples
    ========

    >>> import sympy

    Run all tests:

    >>> sympy.doctest() # doctest: +SKIP

    Run one file:

    >>> sympy.doctest("sympy/core/basic.py") # doctest: +SKIP
    >>> sympy.doctest("polynomial.rst") # doctest: +SKIP

    Run all tests in sympy/functions/ and some particular file:

    >>> sympy.doctest("/functions", "basic.py") # doctest: +SKIP

    Run any file having polynomial in its name, doc/src/modules/polynomial.rst,
    sympy/functions/special/polynomials.py, and sympy/polys/polynomial.py:

    >>> sympy.doctest("polynomial") # doctest: +SKIP

    The ``split`` option can be passed to split the test run into parts. The
    split currently only splits the test files, though this may change in the
    future. ``split`` should be a string of the form \'a/b\', which will run
    part ``a`` of ``b``. Note that the regular doctests and the Sphinx
    doctests are split independently. For instance, to run the first half of
    the test suite:

    >>> sympy.doctest(split=\'1/2\')  # doctest: +SKIP

    The ``subprocess`` and ``verbose`` options are the same as with the function
    ``test()`` (see the docstring of that function for more information) except
    that ``verbose`` may also be set equal to ``2`` in order to print
    individual doctest lines, as they are being tested.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_doctest_blacklist():
    '''Get the default blacklist for the doctests'''
    blacklist = []
    blacklist.extend([
        'doc/src/modules/plotting.rst',
        'doc/src/modules/physics/mechanics/autolev_parser.rst',
        'sympy/codegen/array_utils.py',
        'sympy/core/compatibility.py',
        'sympy/core/trace.py',
        'sympy/galgebra.py',
        'sympy/parsing/autolev/_antlr/autolevlexer.py',
        'sympy/parsing/autolev/_antlr/autolevlistener.py',
        'sympy/parsing/autolev/_antlr/autolevparser.py',
        'sympy/parsing/latex/_antlr/latexlexer.py',
        'sympy/parsing/latex/_antlr/latexparser.py',
        'sympy/plotting/pygletplot/__init__.py',
        'sympy/plotting/pygletplot/plot.py',
        'sympy/printing/ccode.py',
        'sympy/printing/cxxcode.py',
        'sympy/printing/fcode.py',
        'sympy/testing/randtest.py',
        'sympy/this.py'])
    num = 12
# WARNING: Decompyle incomplete


def _doctest(*paths, **kwargs):
    '''
    Internal function that actually runs the doctests.

    All keyword arguments from ``doctest()`` are passed to this function
    except for ``subprocess``.

    Returns 0 if tests passed and 1 if they failed.  See the docstrings of
    ``doctest()`` and ``test()`` for more information.
    '''
    pass
# WARNING: Decompyle incomplete

sp = re.compile('([0-9]+)/([1-9][0-9]*)')

def split_list(l, split, density = (None,)):
    """
    Splits a list into part a of b

    split should be a string of the form 'a/b'. For instance, '1/3' would give
    the split one of three.

    If the length of the list is not divisible by the number of splits, the
    last split will have more items.

    `density` may be specified as a list.  If specified,
    tests will be balanced so that each split has as equal-as-possible
    amount of mass according to `density`.

    >>> from sympy.testing.runtests import split_list
    >>> a = list(range(10))
    >>> split_list(a, '1/3')
    [0, 1, 2]
    >>> split_list(a, '2/3')
    [3, 4, 5]
    >>> split_list(a, '3/3')
    [6, 7, 8, 9]
    """
    pass
# WARNING: Decompyle incomplete

from collections import namedtuple
SymPyTestResults = namedtuple('SymPyTestResults', 'failed attempted')

def sympytestfile(filename, module_relative, name, package, globs, verbose, report, optionflags, extraglobs, raise_on_error, parser, encoding = (True, None, None, None, None, True, 0, None, False, pdoctest.DocTestParser(), None)):
    '''
    Test examples in the given file.  Return (#failures, #tests).

    Optional keyword arg ``module_relative`` specifies how filenames
    should be interpreted:

    - If ``module_relative`` is True (the default), then ``filename``
      specifies a module-relative path.  By default, this path is
      relative to the calling module\'s directory; but if the
      ``package`` argument is specified, then it is relative to that
      package.  To ensure os-independence, ``filename`` should use
      "/" characters to separate path segments, and should not
      be an absolute path (i.e., it may not begin with "/").

    - If ``module_relative`` is False, then ``filename`` specifies an
      os-specific path.  The path may be absolute or relative (to
      the current working directory).

    Optional keyword arg ``name`` gives the name of the test; by default
    use the file\'s basename.

    Optional keyword argument ``package`` is a Python package or the
    name of a Python package whose directory should be used as the
    base directory for a module relative filename.  If no package is
    specified, then the calling module\'s directory is used as the base
    directory for module relative filenames.  It is an error to
    specify ``package`` if ``module_relative`` is False.

    Optional keyword arg ``globs`` gives a dict to be used as the globals
    when executing examples; by default, use {}.  A copy of this dict
    is actually used for each docstring, so that each docstring\'s
    examples start with a clean slate.

    Optional keyword arg ``extraglobs`` gives a dictionary that should be
    merged into the globals that are used to execute examples.  By
    default, no extra globals are used.

    Optional keyword arg ``verbose`` prints lots of stuff if true, prints
    only failures if false; by default, it\'s true iff "-v" is in sys.argv.

    Optional keyword arg ``report`` prints a summary at the end when true,
    else prints nothing at the end.  In verbose mode, the summary is
    detailed, else very brief (in fact, empty if all tests passed).

    Optional keyword arg ``optionflags`` or\'s together module constants,
    and defaults to 0.  Possible values (see the docs for details):

    - DONT_ACCEPT_TRUE_FOR_1
    - DONT_ACCEPT_BLANKLINE
    - NORMALIZE_WHITESPACE
    - ELLIPSIS
    - SKIP
    - IGNORE_EXCEPTION_DETAIL
    - REPORT_UDIFF
    - REPORT_CDIFF
    - REPORT_NDIFF
    - REPORT_ONLY_FIRST_FAILURE

    Optional keyword arg ``raise_on_error`` raises an exception on the
    first unexpected exception or failure. This allows failures to be
    post-mortem debugged.

    Optional keyword arg ``parser`` specifies a DocTestParser (or
    subclass) that should be used to extract tests from the files.

    Optional keyword arg ``encoding`` specifies an encoding that should
    be used to convert the file to unicode.

    Advanced tomfoolery:  testmod runs methods of a local instance of
    class doctest.Tester, then merges the results into (or creates)
    global Tester instance doctest.master.  Methods of doctest.master
    can be called directly too, if you want to do something unusual.
    Passing report=0 to testmod is especially useful then, to delay
    displaying a summary.  Invoke doctest.master.summarize(verbose)
    when you\'re done fiddling.
    '''
    if not package and module_relative:
        raise ValueError('Package may only be specified for module-relative paths.')
    (text, filename) = pdoctest._load_testfile(filename, package, module_relative, encoding)
# WARNING: Decompyle incomplete


class SymPyTests:
    
    def __init__(self, reporter, kw, post_mortem, seed, fast_threshold, slow_threshold = ('', False, None, None, None)):
        self._post_mortem = post_mortem
        self._kw = kw
        self._count = 0
        self._root_dir = get_sympy_dir()
        self._reporter = reporter
        self._reporter.root_dir(self._root_dir)
        self._testfiles = []
    # WARNING: Decompyle incomplete

    
    def test(self, sort, timeout, slow, enhance_asserts, fail_on_timeout = (False, False, False, False, False)):
        '''
        Runs the tests returning True if all tests pass, otherwise False.

        If sort=False run tests in random order.
        '''
        if sort:
            self._testfiles.sort()
        elif slow:
            pass
        else:
            random.seed(self._seed)
            random.shuffle(self._testfiles)
        self._reporter.start(self._seed)
        for f in self._testfiles:
            self.test_file(f, sort, timeout, slow, enhance_asserts, fail_on_timeout)
            except KeyboardInterrupt:
                print(' interrupted by user')
                self._reporter.finish()
                raise 
            return self._reporter.finish()

    
    def _enhance_asserts(self, source):
        pass
    # WARNING: Decompyle incomplete

    
    def test_file(self, filename, sort, timeout, slow, enhance_asserts, fail_on_timeout = (True, False, False, False, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def _timeout(self, function, timeout, fail_on_timeout):
        pass
    # WARNING: Decompyle incomplete

    
    def matches(self, x):
        '''
        Does the keyword expression self._kw match "x"? Returns True/False.

        Always returns True if self._kw is "".
        '''
        if not self._kw:
            return True
        for kw in None._kw:
            if x.__name__.lower().find(kw.lower()) != -1:
                return True
            return False

    
    def get_test_files(self, dir, pat = ('test_*.py',)):
        '''
        Returns the list of test_*.py (default) files at or below directory
        ``dir`` relative to the SymPy home directory.
        '''
        pass
    # WARNING: Decompyle incomplete



class SymPyDocTests:
    
    def __init__(self, reporter, normal):
        self._count = 0
        self._root_dir = get_sympy_dir()
        self._reporter = reporter
        self._reporter.root_dir(self._root_dir)
        self._normal = normal
        self._testfiles = []

    
    def test(self):
        '''
        Runs the tests and returns True if all tests pass, otherwise False.
        '''
        self._reporter.start()
        for f in self._testfiles:
            self.test_file(f)
            except KeyboardInterrupt:
                print(' interrupted by user')
                self._reporter.finish()
                raise 
            return self._reporter.finish()

    
    def test_file(self, filename):
        clear_cache()
        StringIO = StringIO
        import io
        
        printing
        from sympy.printing.pretty.pretty import pprint_use_unicode
        import sympy.interactive.printing, interactive
        stringpict = stringpict
        import sympy.printing.pretty
        rel_name = filename[len(self._root_dir) + 1:]
        (dirname, file) = os.path.split(filename)
        module = rel_name.replace(os.sep, '.')[:-3]
        if rel_name.startswith('examples'):
            sys.path.insert(0, dirname)
            module = file[:-3]
        
        try:
            module = pdoctest._normalize_module(module)
            tests = SymPyDocTestFinder().find(module)
            
            try:
                pass
            except (SystemExit, KeyboardInterrupt):
                raise 

            except ImportError:
                self._reporter.import_error(filename, sys.exc_info())
                
                try:
                    if rel_name.startswith('examples'):
                        del sys.path[0]
                        return None
                    return None
                    
                    try:
                        if rel_name.startswith('examples'):
                            del sys.path[0]
                        elif rel_name.startswith('examples'):
                            del sys.path[0]



        tests = tests()
        tests.sort(key = (lambda x: -(x.lineno)))
        if not tests:
            return None
        (lambda .0: pass# WARNING: Decompyle incomplete
)._reporter.entering_filename(filename, len(tests))
    # WARNING: Decompyle incomplete

    
    def get_test_files(self, dir, pat, init_only = ('*.py', True)):
        '''
        Returns the list of \\*.py files (default) from which docstrings
        will be tested which are at or below directory ``dir``. By default,
        only those that have an __init__.py in their parent directory
        and do not start with ``test_`` will be included.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _check_dependencies(self, executables, modules, disable_viewers, python_version, ground_types = ((), (), (), (3, 5), None)):
        '''
        Checks if the dependencies for the test are installed.

        Raises ``DependencyError`` it at least one dependency is not installed.
        '''
        pass
    # WARNING: Decompyle incomplete



class SymPyDocTestFinder(DocTestFinder):
    """
    A class used to extract the DocTests that are relevant to a given
    object, from its docstring and the docstrings of its contained
    objects.  Doctests can currently be extracted from the following
    object types: modules, functions, classes, methods, staticmethods,
    classmethods, and properties.

    Modified from doctest's version to look harder for code that
    appears comes from a different module. For example, the @vectorize
    decorator makes it look like functions come from multidimensional.py
    even though their code exists elsewhere.
    """
    
    def _find(self, tests, obj, name, module, source_lines, globs, seen):
        '''
        Find tests for the given object and any contained objects, and
        add them to ``tests``.
        '''
        if self._verbose:
            print('Finding tests in %s' % name)
        if id(obj) in seen:
            return None
        seen[id(obj)] = None
        if inspect.isclass(obj) and obj.__module__.split('.')[0] != 'sympy':
            return None
        test = None._get_test(obj, name, module, globs, source_lines)
    # WARNING: Decompyle incomplete

    
    def _get_test(self, obj, name, module, globs, source_lines):
        '''
        Return a DocTest for the given object, if it defines a docstring;
        otherwise, return None.
        '''
        lineno = None
    # WARNING: Decompyle incomplete



class SymPyDocTestRunner(DocTestRunner):
    '''
    A class used to run DocTest test cases, and accumulate statistics.
    The ``run`` method is used to process a single DocTest case.  It
    returns a tuple ``(f, t)``, where ``t`` is the number of test cases
    tried, and ``f`` is the number of test cases that failed.

    Modified from the doctest version to not reset the sys.displayhook (see
    issue 5140).

    See the docstring of the original DocTestRunner for more information.
    '''
    
    def run(self, test, compileflags, out, clear_globs = (None, None, True)):
        '''
        Run the examples in ``test``, and display the results using the
        writer function ``out``.

        The examples are run in the namespace ``test.globs``.  If
        ``clear_globs`` is true (the default), then this namespace will
        be cleared after the test runs, to help with garbage
        collection.  If you would like to examine the namespace after
        the test completes, then use ``clear_globs=False``.

        ``compileflags`` gives the set of flags that should be used by
        the Python compiler when running the examples.  If not
        specified, then it will default to the set of future-import
        flags that apply to ``globs``.

        The output of each example is checked using
        ``SymPyDocTestRunner.check_output``, and the results are
        formatted by the ``SymPyDocTestRunner.report_*`` methods.
        '''
        self.test = test
    # WARNING: Decompyle incomplete


monkeypatched_methods = [
    'patched_linecache_getlines',
    'run',
    'record_outcome']
for method in monkeypatched_methods:
    oldname = '_DocTestRunner__' + method
    newname = '_SymPyDocTestRunner__' + method
    setattr(SymPyDocTestRunner, newname, getattr(DocTestRunner, oldname))
    
    class SymPyOutputChecker(pdoctest.OutputChecker):
        '''
    Compared to the OutputChecker from the stdlib our OutputChecker class
    supports numerical comparison of floats occurring in the output of the
    doctest examples
    '''
        
        def __init__(self):
            got_floats = '(\\d+\\.\\d*|\\.\\d+)'
            want_floats = got_floats + '(\\.{3})?'
            front_sep = '\\s|\\+|\\-|\\*|,'
            back_sep = front_sep + '|j|e'
            fbeg = f'''^{got_floats!s}(?={back_sep!s}|$)'''
            fmidend = f'''(?<={front_sep!s}){got_floats!s}(?={back_sep!s}|$)'''
            self.num_got_rgx = re.compile(f'''({fbeg!s}|{fmidend!s})''')
            fbeg = f'''^{want_floats!s}(?={back_sep!s}|$)'''
            fmidend = f'''(?<={front_sep!s}){want_floats!s}(?={back_sep!s}|$)'''
            self.num_want_rgx = re.compile(f'''({fbeg!s}|{fmidend!s})''')

        
        def check_output(self, want, got, optionflags):
