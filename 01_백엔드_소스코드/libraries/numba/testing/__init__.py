# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import os
import sys
import functools
import unittest
import traceback
from fnmatch import fnmatch
from os.path import join, isfile, relpath, normpath, splitext
from main import NumbaTestProgram, SerialSuite, make_tag_decorator
from numba.core import config

def load_testsuite(loader, dir):
    """Find tests in 'dir'."""
    
    try:
        suite = unittest.TestSuite()
        files = []
        for f in os.listdir(dir):
            path = join(dir, f)
            if isfile(path) and fnmatch(f, 'test_*.py'):
                files.append(f)
                continue
            if isfile(join(path, '__init__.py')):
                suite.addTests(loader.discover(path))
            for f in files:
                f = relpath(join(dir, f), loader._top_level_dir)
                f = splitext(normpath(f.replace(os.path.sep, '.')))[0]
                suite.addTests(loader.loadTestsFromName(f))
                return suite
                except Exception:
                    traceback.print_exc(file = sys.stderr)
                    sys.exit(-1)
                    return None



def run_tests(argv, defaultTest, topleveldir, xmloutput, verbosity, nomultiproc = (None, None, None, None, 1, False)):
    '''
    args
    ----
    - xmloutput [str or None]
        Path of XML output directory (optional)
    - verbosity [int]
        Verbosity level of tests output

    Returns the TestResult object after running the test *suite*.
    '''
    pass
# WARNING: Decompyle incomplete
