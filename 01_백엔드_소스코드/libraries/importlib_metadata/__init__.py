# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
APIs exposing metadata from third-party Python packages.

This codebase is shared between importlib.metadata in the stdlib
and importlib_metadata in PyPI. See
https://github.com/python/importlib_metadata/wiki/Development-Methodology
for more detail.
'''
from __future__ import annotations
import abc
import collections
import email
import functools
import itertools
import operator
import os
import pathlib
import posixpath
import re
import sys
import textwrap
import types
from collections.abc import Iterable, Mapping
from contextlib import suppress
from importlib import import_module
from importlib.abc import MetaPathFinder
from itertools import starmap
from typing import Any
from  import _meta
from _collections import FreezableDefaultDict, Pair
from _compat import NullFinder, install
from _functools import method_cache, noop, pass_none, passthrough
from _itertools import always_iterable, bucket, unique_everseen
from _meta import PackageMetadata, SimplePath
from _typing import md_none
from compat import py39, py311
__all__ = [
    'Distribution',
    'DistributionFinder',
    'PackageMetadata',
    'PackageNotFoundError',
    'SimplePath',
    'distribution',
    'distributions',
    'entry_points',
    'files',
    'metadata',
    'packages_distributions',
    'requires',
    'version']

class PackageNotFoundError(ModuleNotFoundError):
    '''The package was not found.'''
    
    def __str__(self = None):
        return f'''No package metadata was found for {self.name}'''

    name = (lambda self = None: (name,) = self.argsname)()


class Sectioned:
    """
    A simple entry point config parser for performance

    >>> for item in Sectioned.read(Sectioned._sample):
    ...     print(item)
    Pair(name='sec1', value='# comments ignored')
    Pair(name='sec1', value='a = 1')
    Pair(name='sec1', value='b = 2')
    Pair(name='sec2', value='a = 2')

    >>> res = Sectioned.section_pairs(Sectioned._sample)
    >>> item = next(res)
    >>> item.name
    'sec1'
    >>> item.value
    Pair(name='a', value='1')
    >>> item = next(res)
    >>> item.value
    Pair(name='b', value='2')
    >>> item = next(res)
    >>> item.name
    'sec2'
    >>> item.value
    Pair(name='a', value='2')
    >>> list(res)
    []
    """
    _sample = textwrap.dedent('\n        [sec1]\n        # comments ignored\n        a = 1\n        b = 2\n\n        [sec2]\n        a = 2\n        ').lstrip()
    section_pairs = (lambda cls, text: cls.read(text, filter_ = cls.valid)())()
    read = (lambda text, filter_ = (None,): pass# WARNING: Decompyle incomplete
)()
    valid = (lambda line = classmethod: if line:
passnot line.startswith('#'))()


class _EntryPointMatch(types.SimpleNamespace):
    extras: 'str' = '_EntryPointMatch'


class EntryPoint:
    """An entry point as defined by Python packaging conventions.

    See `the packaging docs on entry points
    <https://packaging.python.org/specifications/entry-points/>`_
    for more information.

    >>> ep = EntryPoint(
    ...     name=None, group=None, value='package.module:attr [extra1, extra2]')
    >>> ep.module
    'package.module'
    >>> ep.attr
    'attr'
    >>> ep.extras
    ['extra1', 'extra2']

    If the value package or module are not valid identifiers, a
    ValueError is raised on access.

    >>> EntryPoint(name=None, group=None, value='invalid-name').module
    Traceback (most recent call last):
    ...
    ValueError: ('Invalid object reference...invalid-name...
    >>> EntryPoint(name=None, group=None, value='invalid-name').attr
    Traceback (most recent call last):
    ...
    ValueError: ('Invalid object reference...invalid-name...
    >>> EntryPoint(name=None, group=None, value='invalid-name').extras
    Traceback (most recent call last):
    ...
    ValueError: ('Invalid object reference...invalid-name...

    The same thing happens on construction.

    >>> EntryPoint(name=None, group=None, value='invalid-name')
    Traceback (most recent call last):
    ...
    ValueError: ('Invalid object reference...invalid-name...

    """
    group: 'str' = re.compile('(?P<module>[\\w.]+)\\s*(:\\s*(?P<attr>[\\w.]+)\\s*)?((?P<extras>\\[.*\\])\\s*)?$')
    dist: 'Distribution | None' = None
    
    def __init__(self = None, name = None, value = None, group = ('name', 'str', 'value', 'str', 'group', 'str', 'return', 'None')):
        vars(self).update(name = name, value = value, group = group)
        self.module

    
    def load(self = None):
