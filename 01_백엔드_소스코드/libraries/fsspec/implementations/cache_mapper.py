# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cache_mapper.pyc (Python 3.11)

from __future__ import annotations
import abc
import hashlib
from fsspec.implementations.local import make_path_posix

class AbstractCacheMapper(abc.ABC):
    '''Abstract super-class for mappers from remote URLs to local cached
    basenames.
    '''
    __call__ = (lambda self = None, path = None: pass)()
    
    def __eq__(self = None, other = None):
        return isinstance(other, type(self))

    
    def __hash__(self = None):
        return hash(type(self))



class BasenameCacheMapper(AbstractCacheMapper):
    pass
# WARNING: Decompyle incomplete


class HashCacheMapper(AbstractCacheMapper):
    '''Cache mapper that uses a hash of the remote URL.'''
    
    def __call__(self = None, path = None):
        return hashlib.sha256(path.encode()).hexdigest()



def create_cache_mapper(same_names = None):
    '''Factory method to create cache mapper for backward compatibility with
    ``CachingFileSystem`` constructor using ``same_names`` kwarg.
    '''
    if same_names:
        return BasenameCacheMapper()
    return None()
