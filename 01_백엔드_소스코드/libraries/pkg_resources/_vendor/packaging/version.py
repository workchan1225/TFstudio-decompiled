# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: version.pyc (Python 3.11)

import collections
import itertools
import re
import warnings
from typing import Callable, Iterator, List, Optional, SupportsInt, Tuple, Union
from _structures import Infinity, InfinityType, NegativeInfinity, NegativeInfinityType
__all__ = [
    'parse',
    'Version',
    'LegacyVersion',
    'InvalidVersion',
    'VERSION_PATTERN']
InfiniteTypes = Union[(InfinityType, NegativeInfinityType)]
PrePostDevType = Union[(InfiniteTypes, Tuple[(str, int)])]
SubLocalType = Union[(InfiniteTypes, int, str)]
LocalType = Union[(NegativeInfinityType, Tuple[(Union[(SubLocalType, Tuple[(SubLocalType, str)], Tuple[(NegativeInfinityType, SubLocalType)])], ...)])]
CmpKey = Tuple[(int, Tuple[(int, ...)], PrePostDevType, PrePostDevType, PrePostDevType, LocalType)]
LegacyCmpKey = Tuple[(int, Tuple[(str, ...)])]
VersionComparisonMethod = Callable[([
    Union[(CmpKey, LegacyCmpKey)],
    Union[(CmpKey, LegacyCmpKey)]], bool)]
_Version = collections.namedtuple('_Version', [
    'epoch',
    'release',
    'dev',
    'pre',
    'post',
    'local'])

def parse(version = None):
    '''
    Parse the given version string and return either a :class:`Version` object
    or a :class:`LegacyVersion` object depending on if the given version is
    a valid PEP 440 version or a legacy version.
    '''
    
    try:
        return Version(version)
    except InvalidVersion:
        return 



class InvalidVersion(ValueError):
    '''
    An invalid version was found, users should refer to PEP 440.
    '''
    pass


class _BaseVersion:
    _key: Union[(CmpKey, LegacyCmpKey)] = '_BaseVersion'
    
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



class LegacyVersion(_BaseVersion):
    
    def __init__(self = None, version = None):
        self._version = str(version)
        self._key = _legacy_cmpkey(self._version)
        warnings.warn('Creating a LegacyVersion has been deprecated and will be removed in the next major release', DeprecationWarning)

    
    def __str__(self = None):
        return self._version

    
    def __repr__(self = None):
        return f'''<LegacyVersion(\'{self}\')>'''

    public = (lambda self = None: self._version)()
    base_version = (lambda self = None: self._version)()
    epoch = (lambda self = None: -1)()
    release = (lambda self = None: pass)()
    pre = (lambda self = None: pass)()
    post = (lambda self = None: pass)()
    dev = (lambda self = None: pass)()
    local = (lambda self = None: pass)()
    is_prerelease = (lambda self = None: False)()
    is_postrelease = (lambda self = None: False)()
    is_devrelease = (lambda self = None: False)()

_legacy_version_component_re = re.compile('(\\d+ | [a-z]+ | \\.| -)', re.VERBOSE)
_legacy_version_replacement_map = {
    'pre': 'c',
    'preview': 'c',
    '-': 'final-',
    'rc': 'c',
    'dev': '@' }

def _parse_version_parts(s = None):
    pass
# WARNING: Decompyle incomplete


def _legacy_cmpkey(version = None):
    epoch = -1
    parts = []
# WARNING: Decompyle incomplete

VERSION_PATTERN = '\n    v?\n    (?:\n        (?:(?P<epoch>[0-9]+)!)?                           # epoch\n        (?P<release>[0-9]+(?:\\.[0-9]+)*)                  # release segment\n        (?P<pre>                                          # pre-release\n            [-_\\.]?\n            (?P<pre_l>(a|b|c|rc|alpha|beta|pre|preview))\n            [-_\\.]?\n            (?P<pre_n>[0-9]+)?\n        )?\n        (?P<post>                                         # post release\n            (?:-(?P<post_n1>[0-9]+))\n            |\n            (?:\n                [-_\\.]?\n                (?P<post_l>post|rev|r)\n                [-_\\.]?\n                (?P<post_n2>[0-9]+)?\n            )\n        )?\n        (?P<dev>                                          # dev release\n            [-_\\.]?\n            (?P<dev_l>dev)\n            [-_\\.]?\n            (?P<dev_n>[0-9]+)?\n        )?\n    )\n    (?:\\+(?P<local>[a-z0-9]+(?:[-_\\.][a-z0-9]+)*))?       # local version\n'

class Version(_BaseVersion):
    _regex = re.compile('^\\s*' + VERSION_PATTERN + '\\s*$', re.VERBOSE | re.IGNORECASE)
    
    def __init__(self = None, version = None):
