# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _multiprocessing_helpers.pyc (Python 3.11)

__doc__ = 'Helper module to factorize the conditional multiprocessing import logic\n\nWe use a distinct module to simplify import statements and avoid introducing\ncircular dependencies (for instance for the assert_spawning name).\n'
import os
import warnings
# WARNING: Decompyle incomplete
