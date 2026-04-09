# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: version.pyc (Python 3.11)

'''
.. testsetup::

    from packaging.version import parse, Version
'''
from __future__ import annotations
import itertools
import re
from typing import Any, Callable, NamedTuple, SupportsInt, Tuple, Union
from _structures import Infinity, InfinityType, NegativeInfinity, NegativeInfinityType
__all__ = [
    'VERSION_PATTERN',
    'InvalidVersion',
    'Version',
    'parse']
LocalType = Tuple[(Union[(int, str)], ...)]
CmpPrePostDevType = Union[(InfinityType, NegativeInfinityType, Tuple[(str, int)])]
CmpLocalType = Union[(NegativeInfinityType, Tuple[(Union[(Tuple[(int, str)], Tuple[(NegativeInfinityType, Union[(int, str)])])], ...)])]
CmpKey = Tuple[(int, Tuple[(int, ...)], CmpPrePostDevType, CmpPrePostDevType, CmpPrePostDevType, CmpLocalType)]
VersionComparisonMethod = Callable[([
    CmpKey,
    CmpKey], bool)]

class _Version(NamedTuple):
    local: 'LocalType | None' = '_Version'


def parse(version = None):
    """Parse the given version string.

    >>> parse('1.0.dev1')
    <Version('1.0.dev1')>

    :param version: The version string to parse.
    :raises InvalidVersion: When the version string is not a valid version.
    """
    return Version(version)


class InvalidVersion(ValueError):
    '''Raised when a version string is not a valid version.

    >>> Version("invalid")
    Traceback (most recent call last):
        ...
    packaging.version.InvalidVersion: Invalid version: \'invalid\'
    '''
    pass


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
    '''This class abstracts handling of a project\'s versions.

    A :class:`Version` instance is comparison aware and can be compared and
    sorted using the standard Python interfaces.

    >>> v1 = Version("1.0a5")
    >>> v2 = Version("1.0")
    >>> v1
    <Version(\'1.0a5\')>
    >>> v2
    <Version(\'1.0\')>
    >>> v1 < v2
    True
    >>> v1 == v2
    False
    >>> v1 > v2
    False
    >>> v1 >= v2
    False
    >>> v1 <= v2
    True
    '''
    _key: 'CmpKey' = re.compile('^\\s*' + VERSION_PATTERN + '\\s*$', re.VERBOSE | re.IGNORECASE)
    
    def __init__(self = None, version = None):
