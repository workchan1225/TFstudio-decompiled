# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
A Path-like interface for zipfiles.

This codebase is shared between zipfile.Path in the stdlib
and zipp in PyPI. See
https://github.com/python/importlib_metadata/wiki/Development-Methodology
for more detail.
'''
import functools
import io
import itertools
import pathlib
import posixpath
import re
import stat
import sys
import zipfile
from _functools import save_method_args
from compat.py310 import text_encoding
from glob import Translator
__all__ = [
    'Path']

def _parents(path):
    """
    Given a path with elements separated by
    posixpath.sep, generate all parents of that path.

    >>> list(_parents('b/d'))
    ['b']
    >>> list(_parents('/b/d/'))
    ['/b']
    >>> list(_parents('b/d/f/'))
    ['b/d', 'b']
    >>> list(_parents('b'))
    []
    >>> list(_parents(''))
    []
    """
    return itertools.islice(_ancestry(path), 1, None)


def _ancestry(path):
    """
    Given a path with elements separated by
    posixpath.sep, generate all elements of that path.

    >>> list(_ancestry('b/d'))
    ['b/d', 'b']
    >>> list(_ancestry('/b/d/'))
    ['/b/d', '/b']
    >>> list(_ancestry('b/d/f/'))
    ['b/d/f', 'b/d', 'b']
    >>> list(_ancestry('b'))
    ['b']
    >>> list(_ancestry(''))
    []

    Multiple separators are treated like a single.

    >>> list(_ancestry('//b//d///f//'))
    ['//b//d///f', '//b//d', '//b']
    """
    pass
# WARNING: Decompyle incomplete

_dedupe = dict.fromkeys

def _difference(minuend, subtrahend):
    '''
    Return items in minuend not in subtrahend, retaining order
    with O(1) lookup.
    '''
    return itertools.filterfalse(set(subtrahend).__contains__, minuend)


class InitializedState:
    pass
# WARNING: Decompyle incomplete


class CompleteDirs(zipfile.ZipFile, InitializedState):
    pass
# WARNING: Decompyle incomplete


class FastLookup(CompleteDirs):
    pass
# WARNING: Decompyle incomplete


def _extract_text_encoding(encoding = (None,), *args, **kwargs):
