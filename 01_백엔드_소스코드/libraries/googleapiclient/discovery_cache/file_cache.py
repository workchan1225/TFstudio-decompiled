# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_cache.pyc (Python 3.11)

'''File based cache for the discovery document.

The cache is stored in a single file so that multiple processes can
share the same cache. It locks the file whenever accessing to the
file. When the cache content is corrupted, it will be initialized with
an empty cache.
'''
from __future__ import division
import datetime
import json
import logging
import os
import tempfile

try:
    from oauth2client.contrib.locked_file import LockedFile
except ImportError:
    from oauth2client.locked_file import LockedFile
except ImportError:
    raise ImportError('file_cache is unavailable when using oauth2client >= 4.0.0 or google-auth')

from  import base
from discovery_cache import DISCOVERY_DOC_MAX_AGE
LOGGER = logging.getLogger(__name__)
FILENAME = 'google-api-python-client-discovery-doc.cache'
EPOCH = datetime.datetime(1970, 1, 1)

def _to_timestamp(date):
    
    try:
        return (date - EPOCH).total_seconds()
    except AttributeError:
        delta = date - EPOCH
        return 



def _read_or_initialize_cache(f):
    f.file_handle().seek(0)
    
    try:
        cache = json.load(f.file_handle())
    except Exception:
        cache = { }
        f.file_handle().truncate(0)
        f.file_handle().seek(0)
        json.dump(cache, f.file_handle())

    return cache


class Cache(base.Cache):
    '''A file based cache for the discovery documents.'''
    
    def __init__(self, max_age):
        '''Constructor.

        Args:
          max_age: Cache expiration in seconds.
        '''
        self._max_age = max_age
        self._file = os.path.join(tempfile.gettempdir(), FILENAME)
        f = LockedFile(self._file, 'a+', 'r')
        
        try:
            f.open_and_lock()
            if f.is_locked():
                _read_or_initialize_cache(f)
                
                try:
                    pass
                except Exception:
                    e = None
                    LOGGER.warning(e, exc_info = True)
                    
                    try:
                        e = None
                        del e
                    e = None
                    del e
                    try:
                        f.unlock_and_close()
                        return None
                    except:
                        f.unlock_and_close()




    
    def get(self, url):
        f = LockedFile(self._file, 'r+', 'r')
        
        try:
            f.open_and_lock()
            if f.is_locked():
                cache = _read_or_initialize_cache(f)
                if url in cache:
                    (content, t) = cache.get(url, (None, 0))
                    if _to_timestamp(datetime.datetime.now()) < t + self._max_age:
                        f.unlock_and_close()
                        return content
                    f.unlock_and_close()
                    return None
                None.debug('Could not obtain a lock for the cache file.')
                f.unlock_and_close()
                return None
            except Exception:
                e = None
                LOGGER.warning(e, exc_info = True)
                
                try:
                    e = None
                    del e
                e = None
                del e
                try:
                    f.unlock_and_close()
                    return None
                except:
                    f.unlock_and_close()



    
    def set(self, url, content):
        f = LockedFile(self._file, 'r+', 'r')
        
        try:
            f.open_and_lock()
            if f.is_locked():
                cache = _read_or_initialize_cache(f)
                cache[url] = (content, _to_timestamp(datetime.datetime.now()))
                for _, timestamp in list(cache.items()):
                    if _to_timestamp(datetime.datetime.now()) >= timestamp + self._max_age:
                        del cache[k]
                    f.file_handle().truncate(0)
                    f.file_handle().seek(0)
                    json.dump(cache, f.file_handle())
            LOGGER.debug('Could not obtain a lock for the cache file.')
            
            try:
                pass
            except Exception:
                e = None
                LOGGER.warning(e, exc_info = True)
                
                try:
                    e = None
                    del e
                e = None
                del e
                try:
                    f.unlock_and_close()
                    return None
                except:
                    f.unlock_and_close()





cache = Cache(max_age = DISCOVERY_DOC_MAX_AGE)
