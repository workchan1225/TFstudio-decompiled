# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import gc
from os.path import dirname, join
import multiprocessing
import sys
import time
import unittest
import warnings
from unittest.suite import TestSuite
from numba.testing import load_testsuite

try:
    import faulthandler
    
    try:
        faulthandler.enable()
    except Exception:
        e = None
        msg = 'Failed to enable faulthandler due to:\n{err}'
        warnings.warn(msg.format(err = e))
        e = None
        del e
    except ImportError:
        faulthandler = None

    
    def load_tests(loader, tests, pattern):
        suite = TestSuite()
        suite.addTests(load_testsuite(loader, dirname(__file__)))
        cuda_dir = join(dirname(dirname(__file__)), 'cuda/tests')
        suite.addTests(loader.discover(cuda_dir))
        return suite

    return None
