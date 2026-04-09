# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: py313.pyc (Python 3.11)

import functools
import sys

def identity(x):
    return x


def apply(transform):
    pass
# WARNING: Decompyle incomplete


def compose(*funcs):
    
    def compose_two(f1, f2):
        pass
    # WARNING: Decompyle incomplete

    return functools.reduce(compose_two, funcs)


def replace(pattern):
    """
    >>> replace(r'foo\\z')
    'foo\\\\Z'
    """
    return pattern[:-2] + pattern[-2:].replace('\\z', '\\Z')

legacy_end_marker = apply(replace) if sys.version_info < (3, 14) else identity
