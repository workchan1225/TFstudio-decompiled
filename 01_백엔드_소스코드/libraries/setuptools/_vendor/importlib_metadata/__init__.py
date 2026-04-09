# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import os
import re
import abc
import csv
import sys
from  import zipp
import email
import pathlib
import operator
import textwrap
import warnings
import functools
import itertools
import posixpath
import collections
from  import _adapters, _meta
from _collections import FreezableDefaultDict, Pair
from _compat import NullFinder, install, pypy_partial
from _functools import method_cache, pass_none
from _itertools import always_iterable, unique_everseen
from _meta import PackageMetadata, SimplePath
from contextlib import suppress
from importlib import import_module
from importlib.abc import MetaPathFinder
from itertools import starmap
from typing import List, Mapping, Optional, Union
__all__ = [
    'Distribution',
    'DistributionFinder',
    'PackageMetadata',
    'PackageNotFoundError',
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
    
    def __str__(self):
        return f'''No package metadata was found for {self.name}'''

    name = (lambda self: (name,) = self.argsname)()


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
    valid = (lambda line: if line:
passnot line.startswith('#'))()


class DeprecatedTuple:
    """
    Provide subscript item access for backward compatibility.

    >>> recwarn = getfixture('recwarn')
    >>> ep = EntryPoint(name='name', value='value', group='group')
    >>> ep[:]
    ('name', 'value', 'group')
    >>> ep[0]
    'name'
    >>> len(recwarn)
    1
    """
    _warn = functools.partial(warnings.warn, 'EntryPoint tuple interface is deprecated. Access members by name.', DeprecationWarning, stacklevel = pypy_partial(2))
    
    def __getitem__(self, item):
        self._warn()
        return self._key()[item]



class EntryPoint(DeprecatedTuple):
    '''An entry point as defined by Python packaging conventions.

    See `the packaging docs on entry points
    <https://packaging.python.org/specifications/entry-points/>`_
    for more information.
    '''
    pattern = re.compile('(?P<module>[\\w.]+)\\s*(:\\s*(?P<attr>[\\w.]+)\\s*)?((?P<extras>\\[.*\\])\\s*)?$')
    dist: Optional['Distribution'] = None
    
    def __init__(self, name, value, group):
        vars(self).update(name = name, value = value, group = group)

    
    def load(self):
