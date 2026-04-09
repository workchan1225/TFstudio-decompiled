# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dircache.pyc (Python 3.11)

import time
from collections.abc import MutableMapping
from functools import lru_cache

class DirCache(MutableMapping):
    '''
    Caching of directory listings, in a structure like::

        {"path0": [
            {"name": "path0/file0",
             "size": 123,
             "type": "file",
             ...
            },
            {"name": "path0/file1",
            },
            ...
            ],
         "path1": [...]
        }

    Parameters to this class control listing expiry or indeed turn
    caching off
    '''
    
    def __init__(self, use_listings_cache, listings_expiry_time, max_paths = (True, None, None), **kwargs):
        """

        Parameters
        ----------
        use_listings_cache: bool
            If False, this cache never returns items, but always reports KeyError,
            and setting items has no effect
        listings_expiry_time: int or float (optional)
            Time in seconds that a listing is considered valid. If None,
            listings do not expire.
        max_paths: int (optional)
            The number of most recent listings that are considered valid; 'recent'
            refers to when the entry was set.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, item):
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self):
        self._cache.clear()

    
    def __len__(self):
        return len(self._cache)

    
    def __contains__(self, item):
        
        try:
            self[item]
            return True
        except KeyError:
            return False


    
    def __setitem__(self, key, value):
        if not self.use_listings_cache:
            return None
        if None.max_paths:
            self._q(key)
        self._cache[key] = value
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, key):
        del self._cache[key]

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __reduce__(self):
        return (DirCache, (self.use_listings_cache, self.listings_expiry_time, self.max_paths))
