# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: appengine_memcache.pyc (Python 3.11)

'''App Engine memcache based cache for the discovery document.'''
import logging
from google.appengine.api import memcache
from  import base
from discovery_cache import DISCOVERY_DOC_MAX_AGE
LOGGER = logging.getLogger(__name__)
NAMESPACE = 'google-api-client'

class Cache(base.Cache):
    '''A cache with app engine memcache API.'''
    
    def __init__(self, max_age):
        '''Constructor.

        Args:
          max_age: Cache expiration in seconds.
        '''
        self._max_age = max_age

    
    def get(self, url):
        
        try:
            return memcache.get(url, namespace = NAMESPACE)
        except Exception:
            e = None
            LOGGER.warning(e, exc_info = True)
            e = None
            del e
            return None
            e = None
            del e


    
    def set(self, url, content):
        
        try:
            memcache.set(url, content, time = int(self._max_age), namespace = NAMESPACE)
            return None
        except Exception:
            e = None
            LOGGER.warning(e, exc_info = True)
            e = None
            del e
            return None
            e = None
            del e



cache = Cache(max_age = DISCOVERY_DOC_MAX_AGE)
