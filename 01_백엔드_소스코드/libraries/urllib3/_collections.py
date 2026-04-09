# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _collections.pyc (Python 3.11)

from __future__ import annotations
import typing
from collections import OrderedDict
from enum import Enum, auto
from threading import RLock
if typing.TYPE_CHECKING:
    from typing import Protocol
    from typing_extensions import Self
    
    class HasGettableStringKeys(Protocol):
        
        def keys(self = None):
            pass

        
        def __getitem__(self = None, key = None):
            pass


__all__ = [
    'RecentlyUsedContainer',
    'HTTPHeaderDict']
_KT = typing.TypeVar('_KT')
_VT = typing.TypeVar('_VT')
_DT = typing.TypeVar('_DT')
ValidHTTPHeaderSource = typing.Union[('HTTPHeaderDict', typing.Mapping[(str, str)], typing.Iterable[tuple[(str, str)]], 'HasGettableStringKeys')]

class _Sentinel(Enum):
    not_passed = auto()


def ensure_can_construct_http_header_dict(potential = None):
    if isinstance(potential, HTTPHeaderDict):
        return potential
    if None(potential, typing.Mapping):
        return typing.cast(typing.Mapping[(str, str)], potential)
    if None(potential, typing.Iterable):
        return typing.cast(typing.Iterable[tuple[(str, str)]], potential)
    if None(potential, 'keys') and hasattr(potential, '__getitem__'):
        return typing.cast('HasGettableStringKeys', potential)


def RecentlyUsedContainer():
    '''RecentlyUsedContainer'''
    pass
# WARNING: Decompyle incomplete

RecentlyUsedContainer = <NODE:27>(RecentlyUsedContainer, 'RecentlyUsedContainer', typing.Generic[(_KT, _VT)], typing.MutableMapping[(_KT, _VT)])

def HTTPHeaderDictItemView():
    '''HTTPHeaderDictItemView'''
    _headers: 'HTTPHeaderDict' = '\n    HTTPHeaderDict is unusual for a Mapping[str, str] in that it has two modes of\n    address.\n\n    If we directly try to get an item with a particular name, we will get a string\n    back that is the concatenated version of all the values:\n\n    >>> d[\'X-Header-Name\']\n    \'Value1, Value2, Value3\'\n\n    However, if we iterate over an HTTPHeaderDict\'s items, we will optionally combine\n    these values based on whether combine=True was called when building up the dictionary\n\n    >>> d = HTTPHeaderDict({"A": "1", "B": "foo"})\n    >>> d.add("A", "2", combine=True)\n    >>> d.add("B", "bar")\n    >>> list(d.items())\n    [\n        (\'A\', \'1, 2\'),\n        (\'B\', \'foo\'),\n        (\'B\', \'bar\'),\n    ]\n\n    This class conforms to the interface required by the MutableMapping ABC while\n    also giving us the nonstandard iteration behavior we want; items with duplicate\n    keys, ordered by time of first insertion.\n    '
    
    def __init__(self = None, headers = None):
        self._headers = headers

    
    def __len__(self = None):
        return len(list(self._headers.iteritems()))

    
    def __iter__(self = None):
        return self._headers.iteritems()

    
    def __contains__(self = None, item = None):
