# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: probe.pyc (Python 3.11)

from __future__ import annotations
import threading

class _HTTP2ProbeCache:
    __slots__ = ('_lock', '_cache_locks', '_cache_values')
    
    def __init__(self = None):
        self._lock = threading.Lock()
        self._cache_locks = { }
        self._cache_values = { }

    
    def acquire_and_get(self = None, host = None, port = None):
        value = None
        self._lock
        key = (host, port)
        value = self._cache_values[key]
    # WARNING: Decompyle incomplete

    
    def set_and_release(self = None, host = None, port = None, supports_http2 = ('host', 'str', 'port', 'int', 'supports_http2', 'bool | None', 'return', 'None')):
        key = (host, port)
        key_lock = self._cache_locks[key]
        key_lock
    # WARNING: Decompyle incomplete

    
    def _values(self = None):
        '''This function is for testing purposes only. Gets the current state of the probe cache'''
        self._lock
        None(None, None)
        return 
        with None:
            if not (lambda .0: pass# WARNING: Decompyle incomplete
), self._cache_values.items()():
                pass

    
    def _reset(self = None):
        '''This function is for testing purposes only. Reset the cache values'''
        self._lock
        self._cache_locks = { }
        self._cache_values = { }
        None(None, None)
        return None
        with None:
            if not None:
                pass


_HTTP2_PROBE_CACHE = _HTTP2ProbeCache()
set_and_release = _HTTP2_PROBE_CACHE.set_and_release
acquire_and_get = _HTTP2_PROBE_CACHE.acquire_and_get
_values = _HTTP2_PROBE_CACHE._values
_reset = _HTTP2_PROBE_CACHE._reset
__all__ = [
    'set_and_release',
    'acquire_and_get']
