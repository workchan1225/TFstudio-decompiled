# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: caching.pyc (Python 3.11)

from __future__ import annotations
import collections
import functools
import logging
import math
import os
import threading
from collections import OrderedDict
from collections.abc import Callable
from concurrent.futures import Future, ThreadPoolExecutor
from itertools import groupby
from operator import itemgetter
from typing import TYPE_CHECKING, Any, ClassVar, Generic, NamedTuple, TypeVar
if TYPE_CHECKING:
    import mmap
    from typing_extensions import ParamSpec
    P = ParamSpec('P')
else:
    P = TypeVar('P')
T = TypeVar('T')
logger = logging.getLogger('fsspec')
Fetcher = Callable[([
    int,
    int], bytes)]
MultiFetcher = Callable[([
    list[(int, int)]], bytes)]

class BaseCache:
    """Pass-though cache: doesn't keep anything, calls every time

    Acts as base class for other cachers

    Parameters
    ----------
    blocksize: int
        How far to read ahead in numbers of bytes
    fetcher: func
        Function of the form f(start, end) which gets bytes from remote as
        specified
    size: int
        How big this file is
    """
    name: 'ClassVar[str]' = 'none'
    
    def __init__(self = None, blocksize = None, fetcher = None, size = ('blocksize', 'int', 'fetcher', 'Fetcher', 'size', 'int', 'return', 'None')):
        self.blocksize = blocksize
        self.nblocks = 0
        self.fetcher = fetcher
        self.size = size
        self.hit_count = 0
        self.miss_count = 0
        self.total_requested_bytes = 0

    
    def _fetch(self = None, start = None, stop = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _reset_stats(self = None):
        '''Reset hit and miss counts for a more ganular report e.g. by file.'''
        self.hit_count = 0
        self.miss_count = 0
        self.total_requested_bytes = 0

    
    def _log_stats(self = None):
        '''Return a formatted string of the cache statistics.'''
        if self.hit_count == 0 and self.miss_count == 0:
            return ''
        return f'''{self.name}: {self.hit_count} hits, {self.miss_count} misses, {self.total_requested_bytes} total requested bytes'''

    
    def __repr__(self = None):
        return f'''\n        <{self.__class__.__name__}:\n            block size  :   {self.blocksize}\n            block count :   {self.nblocks}\n            file size   :   {self.size}\n            cache hits  :   {self.hit_count}\n            cache misses:   {self.miss_count}\n            total requested bytes: {self.total_requested_bytes}>\n        '''



class MMapCache(BaseCache):
    pass
# WARNING: Decompyle incomplete


class ReadAheadCache(BaseCache):
    pass
# WARNING: Decompyle incomplete


class FirstChunkCache(BaseCache):
    pass
# WARNING: Decompyle incomplete


class BlockCache(BaseCache):
    pass
# WARNING: Decompyle incomplete


class BytesCache(BaseCache):
    pass
# WARNING: Decompyle incomplete


class AllBytes(BaseCache):
    pass
# WARNING: Decompyle incomplete


class KnownPartsOfAFile(BaseCache):
    pass
# WARNING: Decompyle incomplete


def UpdatableLRU():
    '''UpdatableLRU'''
    __doc__ = '\n    Custom implementation of LRU cache that allows updating keys\n\n    Used by BackgroudBlockCache\n    '
    
    class CacheInfo(NamedTuple):
        currsize: 'int' = 'UpdatableLRU.CacheInfo'

    
    def __init__(self = None, func = None, max_size = None):
        self._cache = collections.OrderedDict()
        self._func = func
        self._max_size = max_size
        self._hits = 0
        self._misses = 0
        self._lock = threading.Lock()

    
    def __call__(self = None, *args, **kwargs):
        if kwargs:
            raise TypeError(f'''Got unexpected keyword argument {kwargs.keys()}''')
        self._lock
        if args in self._cache:
            self._cache.move_to_end(args)
            None(None, None)
            return 
        None(None, None)
    # WARNING: Decompyle incomplete

    
    def is_key_cached(self = None, *args):
        self._lock
        None(None, None)
        return 
        with None:
            if not None, args in self._cache:
                pass

    
    def add_key(self = None, result = None, *args):
        self._lock
        self._cache[args] = result
        if len(self._cache) > self._max_size:
            self._cache.popitem(last = False)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def cache_info(self = None):
        self._lock
        None(None, None)
        return 
        with None:
            if not None, self.CacheInfo(maxsize = self._max_size, currsize = len(self._cache), hits = self._hits, misses = self._misses):
                pass


UpdatableLRU = <NODE:27>(UpdatableLRU, 'UpdatableLRU', Generic[(P, T)])

class BackgroundBlockCache(BaseCache):
    pass
# WARNING: Decompyle incomplete

caches: 'dict[str | None, type[BaseCache]]' = {
    None: BaseCache }

def register_cache(cls = None, clobber = None):
    """'Register' cache implementation.

    Parameters
    ----------
    clobber: bool, optional
        If set to True (default is False) - allow to overwrite existing
        entry.

    Raises
    ------
    ValueError
    """
    name = cls.name
    if clobber and name in caches:
        raise ValueError(f'''Cache with name {name!r} is already known: {caches[name]}''')
    caches[name] = cls

for c in (BaseCache, MMapCache, BytesCache, ReadAheadCache, BlockCache, FirstChunkCache, AllBytes, KnownPartsOfAFile, BackgroundBlockCache):
    register_cache(c)
    return None
