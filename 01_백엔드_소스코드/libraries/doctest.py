# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: doctest.pyc (Python 3.11)

'''Module doctest -- a framework for running examples in docstrings.

In simplest use, end each module M to be tested with:

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()

Then running the module as a script will cause the examples in the
docstrings to get executed and verified:

python M.py

This won\'t display anything unless an example fails, in which case the
failing example(s) and the cause(s) of the failure(s) are printed to stdout
(why not stderr? because stderr is a lame hack <0.2 wink>), and the final
line of output is "Test failed.".

Run it with the -v switch instead:

python M.py -v

and a detailed report of all examples tried is printed to stdout, along
with assorted summaries at the end.

You can force verbose mode by passing "verbose=True" to testmod, or prohibit
it by passing "verbose=False".  In either of those cases, sys.argv is not
examined by testmod.

There are a variety of other ways to run doctests, including integration
with the unittest framework, and support for running non-Python text
files containing doctests.  There are also many ways to override parts
of doctest\'s default behaviors.  See the Library Reference Manual for
details.
'''
__docformat__ = 'reStructuredText en'
__all__ = [
    'register_optionflag',
    'DONT_ACCEPT_TRUE_FOR_1',
    'DONT_ACCEPT_BLANKLINE',
    'NORMALIZE_WHITESPACE',
    'ELLIPSIS',
    'SKIP',
    'IGNORE_EXCEPTION_DETAIL',
    'COMPARISON_FLAGS',
    'REPORT_UDIFF',
    'REPORT_CDIFF',
    'REPORT_NDIFF',
    'REPORT_ONLY_FIRST_FAILURE',
    'REPORTING_FLAGS',
    'FAIL_FAST',
    'Example',
    'DocTest',
    'DocTestParser',
    'DocTestFinder',
    'DocTestRunner',
    'OutputChecker',
    'DocTestFailure',
    'UnexpectedException',
    'DebugRunner',
    'testmod',
    'testfile',
    'run_docstring_examples',
    'DocTestSuite',
    'DocFileSuite',
    'set_unittest_reportflags',
    'script_from_examples',
    'testsource',
    'debug_src',
    'debug']
import __future__
import difflib
import inspect
import linecache
import os
import pdb
import re
import sys
import traceback
import unittest
from io import StringIO, IncrementalNewlineDecoder
from collections import namedtuple
TestResults = namedtuple('TestResults', 'failed attempted')
OPTIONFLAGS_BY_NAME = { }

def register_optionflag(name):
    return OPTIONFLAGS_BY_NAME.setdefault(name, 1 << len(OPTIONFLAGS_BY_NAME))

DONT_ACCEPT_TRUE_FOR_1 = register_optionflag('DONT_ACCEPT_TRUE_FOR_1')
DONT_ACCEPT_BLANKLINE = register_optionflag('DONT_ACCEPT_BLANKLINE')
NORMALIZE_WHITESPACE = register_optionflag('NORMALIZE_WHITESPACE')
ELLIPSIS = register_optionflag('ELLIPSIS')
SKIP = register_optionflag('SKIP')
IGNORE_EXCEPTION_DETAIL = register_optionflag('IGNORE_EXCEPTION_DETAIL')
COMPARISON_FLAGS = DONT_ACCEPT_TRUE_FOR_1 | DONT_ACCEPT_BLANKLINE | NORMALIZE_WHITESPACE | ELLIPSIS | SKIP | IGNORE_EXCEPTION_DETAIL
REPORT_UDIFF = register_optionflag('REPORT_UDIFF')
REPORT_CDIFF = register_optionflag('REPORT_CDIFF')
REPORT_NDIFF = register_optionflag('REPORT_NDIFF')
REPORT_ONLY_FIRST_FAILURE = register_optionflag('REPORT_ONLY_FIRST_FAILURE')
FAIL_FAST = register_optionflag('FAIL_FAST')
REPORTING_FLAGS = REPORT_UDIFF | REPORT_CDIFF | REPORT_NDIFF | REPORT_ONLY_FIRST_FAILURE | FAIL_FAST
BLANKLINE_MARKER = '<BLANKLINE>'
ELLIPSIS_MARKER = '...'

def _extract_future_flags(globs):
    '''
    Return the compiler-flags associated with the future features that
    have been imported into the given namespace (globs).
    '''
    flags = 0
    for fname in __future__.all_feature_names:
        feature = globs.get(fname, None)
        if feature is getattr(__future__, fname):
            flags |= feature.compiler_flag
        return flags


def _normalize_module(module, depth = (2,)):
    '''
    Return the module specified by `module`.  In particular:
      - If `module` is a module, then return module.
      - If `module` is a string, then import and return the
        module with that name.
      - If `module` is None, then return the calling module.
        The calling module is assumed to be the module of
        the stack frame at the given depth in the call stack.
    '''
    if inspect.ismodule(module):
        return module
    if None(module, str):
        return __import__(module, globals(), locals(), [
            '*'])
# WARNING: Decompyle incomplete


def _newline_convert(data):
    return IncrementalNewlineDecoder(None, True).decode(data, True)


def _load_testfile(filename, package, module_relative, encoding):
    pass
# WARNING: Decompyle incomplete


def _indent(s, indent = (4,)):
    '''
    Add the given number of space characters to the beginning of
    every non-blank line in `s`, and return the result.
    '''
    return re.sub('(?m)^(?!$)', indent * ' ', s)


def _exception_traceback(exc_info):
    '''
    Return a string containing a traceback message for the given
    exc_info tuple (as returned by sys.exc_info()).
    '''
    excout = StringIO()
    (exc_type, exc_val, exc_tb) = exc_info
    traceback.print_exception(exc_type, exc_val, exc_tb, file = excout)
    return excout.getvalue()


class _SpoofOut(StringIO):
    
    def getvalue(self):
        result = StringIO.getvalue(self)
        if not result and result.endswith('\n'):
            result += '\n'
        return result

    
    def truncate(self, size = (None,)):
        self.seek(size)
        StringIO.truncate(self)



def _ellipsis_match(want, got):
    """
    Essentially the only subtle case:
    >>> _ellipsis_match('aa...aa', 'aaa')
    False
    """
    if ELLIPSIS_MARKER not in want:
        return want == got
    ws = None.split(ELLIPSIS_MARKER)
# WARNING: Decompyle incomplete


def _comment_line(line):
    '''Return a commented form of the given line'''
    line = line.rstrip()
    if line:
        return '# ' + line


def _strip_exception_details(msg):
    end = len(msg)
    start = 0
    i = msg.find('\n')
    if i >= 0:
        end = i
    i = msg.find(':', 0, end)
    if i >= 0:
        end = i
    i = msg.rfind('.', 0, end)
    if i >= 0:
        start = i + 1
    return msg[start:end]


class _OutputRedirectingPdb(pdb.Pdb):
    '''
    A specialized version of the python debugger that redirects stdout
    to a given stream when interacting with the user.  Stdout is *not*
    redirected when traced code is executed.
    '''
    
    def __init__(self, out):
        self._OutputRedirectingPdb__out = out
        self._OutputRedirectingPdb__debugger_used = False
        pdb.Pdb.__init__(self, stdout = out, nosigint = True)
        self.use_rawinput = 1

    
    def set_trace(self, frame = (None,)):
        self._OutputRedirectingPdb__debugger_used = True
    # WARNING: Decompyle incomplete

    
    def set_continue(self):
        if self._OutputRedirectingPdb__debugger_used:
            pdb.Pdb.set_continue(self)
            return None

    
    def trace_dispatch(self, *args):
        save_stdout = sys.stdout
        sys.stdout = self._OutputRedirectingPdb__out
    # WARNING: Decompyle incomplete



def _module_relative_path(module, test_path):
    if not inspect.ismodule(module):
        raise TypeError('Expected a module: %r' % module)
    if test_path.startswith('/'):
        raise ValueError('Module-relative files may not have absolute paths')
# WARNING: Decompyle incomplete


class Example:
    """
    A single doctest example, consisting of source code and expected
    output.  `Example` defines the following attributes:

      - source: A single Python statement, always ending with a newline.
        The constructor adds a newline if needed.

      - want: The expected output from running the source code (either
        from stdout, or a traceback in case of exception).  `want` ends
        with a newline unless it's empty, in which case it's an empty
        string.  The constructor adds a newline if needed.

      - exc_msg: The exception message generated by the example, if
        the example is expected to generate an exception; or `None` if
        it is not expected to generate an exception.  This exception
        message is compared against the return value of
        `traceback.format_exception_only()`.  `exc_msg` ends with a
        newline unless it's `None`.  The constructor adds a newline
        if needed.

      - lineno: The line number within the DocTest string containing
        this Example where the Example begins.  This line number is
        zero-based, with respect to the beginning of the DocTest.

      - indent: The example's indentation in the DocTest string.
        I.e., the number of space characters that precede the
        example's first prompt.

      - options: A dictionary mapping from option flags to True or
        False, which is used to override default options for this
        example.  Any option flags not contained in this dictionary
        are left at their default value (as specified by the
        DocTestRunner's optionflags).  By default, no options are set.
    """
    
    def __init__(self, source, want, exc_msg, lineno, indent, options = (None, 0, 0, None)):
        if not source.endswith('\n'):
            source += '\n'
        if not want and want.endswith('\n'):
            want += '\n'
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
