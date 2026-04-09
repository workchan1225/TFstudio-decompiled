# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: streaming.pyc (Python 3.11)

import io
import os
from pyasn1 import error
from pyasn1.type import univ

class CachingStreamWrapper(io.IOBase):
    '''Wrapper around non-seekable streams.

    Note that the implementation is tied to the decoder,
    not checking for dangerous arguments for the sake
    of performance.

    The read bytes are kept in an internal cache until
    setting _markedPosition which may reset the cache.
    '''
    
    def __init__(self, raw):
        self._raw = raw
        self._cache = io.BytesIO()
        self._markedPosition = 0

    
    def peek(self, n):
        result = self.read(n)
        self._cache.seek(-len(result), os.SEEK_CUR)
        return result

    
    def seekable(self):
        return True

    
    def seek(self, n, whence = (-1, os.SEEK_SET)):
        return self._cache.seek(n, whence)

    
    def read(self, n = (-1,)):
