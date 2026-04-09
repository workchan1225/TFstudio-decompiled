# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datastructures.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Iterable, Iterator, Mapping, MutableMapping
from typing import Any, Protocol, Union
__all__ = [
    'Headers',
    'HeadersLike',
    'MultipleValuesError']

class MultipleValuesError(LookupError):
    pass
# WARNING: Decompyle incomplete


def Headers():
    '''Headers'''
    pass
# WARNING: Decompyle incomplete

Headers = <NODE:27>(Headers, 'Headers', MutableMapping[(str, str)])

class SupportsKeysAndGetItem(Protocol):
    '''
    Dict-like types with ``keys() -> str`` and ``__getitem__(key: str) -> str`` methods.

    '''
    
    def keys(self = None):
        pass

    
    def __getitem__(self = None, key = None):
        pass


HeadersLike = Union[(Headers, Mapping[(str, str)], Iterable[tuple[(str, str)]], SupportsKeysAndGetItem)]
