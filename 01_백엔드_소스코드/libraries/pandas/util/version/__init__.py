# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable
import itertools
import re
from typing import Any, NamedTuple, SupportsInt, TypeAlias
__all__ = [
    'VERSION_PATTERN',
    'InvalidVersion',
    'Version',
    'parse']

class InfinityType:
    
    def __repr__(self = None):
        return 'Infinity'

    
    def __hash__(self = None):
        return hash(repr(self))

    
    def __lt__(self = None, other = None):
        return False

    
    def __le__(self = None, other = None):
        return False

    
    def __eq__(self = None, other = None):
        return isinstance(other, type(self))

    
    def __gt__(self = None, other = None):
        return True

    
    def __ge__(self = None, other = None):
        return True

    
    def __neg__(self = None):
        return NegativeInfinity


Infinity = InfinityType()

class NegativeInfinityType:
    
    def __repr__(self = None):
        return '-Infinity'

    
    def __hash__(self = None):
        return hash(repr(self))

    
    def __lt__(self = None, other = None):
        return True

    
    def __le__(self = None, other = None):
        return True

    
    def __eq__(self = None, other = None):
        return isinstance(other, type(self))

    
    def __gt__(self = None, other = None):
        return False

    
    def __ge__(self = None, other = None):
        return False

    
    def __neg__(self = None):
        return Infinity


NegativeInfinity = NegativeInfinityType()
LocalType: 'TypeAlias' = tuple[(int | str, ...)]
CmpPrePostDevType: 'TypeAlias' = InfinityType | NegativeInfinityType | tuple[(str, int)]
CmpLocalType: 'TypeAlias' = NegativeInfinityType | tuple[(tuple[(int, str)] | tuple[(NegativeInfinityType, int | str)], ...)]
CmpKey: 'TypeAlias' = tuple[(int, tuple[(int, ...)], CmpPrePostDevType, CmpPrePostDevType, CmpPrePostDevType, CmpLocalType)]
VersionComparisonMethod: 'TypeAlias' = Callable[([
    CmpKey,
    CmpKey], bool)]

class _Version(NamedTuple):
    local: 'LocalType | None' = '_Version'


def parse(version = None):
    return Version(version)


class InvalidVersion(ValueError):
    '''
    An invalid version was found, users should refer to PEP 440.

    The ``InvalidVersion`` exception is raised when a version string is
    improperly formatted. Pandas uses this exception to ensure that all
    version strings are PEP 440 compliant.

    See Also
    --------
    util.version.Version : Class for handling and parsing version strings.

    Examples
    --------
    >>> pd.util.version.Version("1.")
    Traceback (most recent call last):
    InvalidVersion: Invalid version: \'1.\'
    '''
    __module__ = 'pandas.errors'


class _BaseVersion:
    _key: 'tuple[Any, ...]' = '_BaseVersion'
    
    def __hash__(self = None):
        return hash(self._key)

    
    def __lt__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key < other._key

    
    def __le__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key <= other._key

    
    def __eq__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key == other._key

    
    def __ge__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key >= other._key

    
    def __gt__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key > other._key

    
    def __ne__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key != other._key


_VERSION_PATTERN = '\n    v?\n    (?:\n        (?:(?P<epoch>[0-9]+)!)?                           # epoch\n        (?P<release>[0-9]+(?:\\.[0-9]+)*)                  # release segment\n        (?P<pre>                                          # pre-release\n            [-_\\.]?\n            (?P<pre_l>alpha|a|beta|b|preview|pre|c|rc)\n            [-_\\.]?\n            (?P<pre_n>[0-9]+)?\n        )?\n        (?P<post>                                         # post release\n            (?:-(?P<post_n1>[0-9]+))\n            |\n            (?:\n                [-_\\.]?\n                (?P<post_l>post|rev|r)\n                [-_\\.]?\n                (?P<post_n2>[0-9]+)?\n            )\n        )?\n        (?P<dev>                                          # dev release\n            [-_\\.]?\n            (?P<dev_l>dev)\n            [-_\\.]?\n            (?P<dev_n>[0-9]+)?\n        )?\n    )\n    (?:\\+(?P<local>[a-z0-9]+(?:[-_\\.][a-z0-9]+)*))?       # local version\n'
VERSION_PATTERN = _VERSION_PATTERN

class Version(_BaseVersion):
    _key: 'CmpKey' = re.compile('^\\s*' + VERSION_PATTERN + '\\s*$', re.VERBOSE | re.IGNORECASE)
    
    def __init__(self = None, version = None):
