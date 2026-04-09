# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import re
import itertools
import textwrap
import functools

try:
    from importlib.resources import files
except ImportError:
    from pkg_resources.extern.importlib_resources import files

from pkg_resources.extern.jaraco.functools import compose, method_cache
from pkg_resources.extern.jaraco.context import ExceptionTrap

def substitution(old, new):
    '''
    Return a function that will perform a substitution on a string
    '''
    pass
# WARNING: Decompyle incomplete


def multi_substitution(*substitutions):
    """
    Take a sequence of pairs specifying substitutions, and create
    a function that performs those substitutions.

    >>> multi_substitution(('foo', 'bar'), ('bar', 'baz'))('foo')
    'baz'
    """
    substitutions = itertools.starmap(substitution, substitutions)
    substitutions = reversed(tuple(substitutions))
# WARNING: Decompyle incomplete


class FoldedCase(str):
    pass
# WARNING: Decompyle incomplete

_unicode_trap = ExceptionTrap(UnicodeDecodeError)
is_decodable = (lambda value: value.decode())()

def is_binary(value):
