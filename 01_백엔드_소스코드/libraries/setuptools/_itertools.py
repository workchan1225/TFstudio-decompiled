# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _itertools.pyc (Python 3.11)

from setuptools.extern.more_itertools import consume

def ensure_unique(iterable, key = ((lambda x: x),)):
    """
    Wrap an iterable to raise a ValueError if non-unique values are encountered.

    >>> list(ensure_unique('abc'))
    ['a', 'b', 'c']
    >>> consume(ensure_unique('abca'))
    Traceback (most recent call last):
    ...
    ValueError: Duplicate element 'a' encountered.
    """
    pass
# WARNING: Decompyle incomplete
